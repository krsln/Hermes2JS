from __future__ import annotations

import dataclasses
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Optional

from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.ir.expressions import (
    Expression, Identifier, RawExpression, ObjectExpression,
    ArrayExpression, Literal,
)
from hermes_decompiler.runtime import HermesAnalysis

logger = get_logger(__name__)


@dataclass(slots=True)
class OpcodeContext:
    analysis: HermesAnalysis
    entry: OpcodeEntry
    entries: list[OpcodeEntry]
    index: int


@dataclass(frozen=True, slots=True)
class ArgsPattern:
    regex: re.Pattern[str]
    desc: str


# Types whose IDENTITY matters (mutation-sensitive) - inlining a second
# reference to the same literal object/array expression would make two
# independent-looking `{}`/`[]` in the output secretly alias the same
# runtime object. Always kept symbolic (`rN`), regardless of which
# resolver is used.
_IDENTITY_SENSITIVE_TYPES = (ObjectExpression, ArrayExpression)

# Opcodes whose produced value, though not a Literal, is still safe to
# inline even in "symbolic" resolution mode: the value is bound EXACTLY
# ONCE per scope entry and never redefined afterward within that scope
# (unlike Mov/Inc/Add/GetById, which can sit inside a loop and be
# re-evaluated on every iteration - see get_register_symbolic's own
# docstring for why those must stay symbolic). `Catch` is the first
# case: `caughtException` is bound once at catch-block entry and never
# reassigned for the rest of that block.
_SAFE_IDENTIFIER_INLINE_OPCODES = frozenset({"Catch"})

_CONST_LOAD_OPCODES = frozenset({
    "LoadConstZero",
    "LoadConstUInt8",
    "LoadConstInt",
    "LoadConstDouble",
    "LoadConstString",
    "LoadConstNull",
    "LoadConstUndefined",
    "LoadConstTrue",
    "LoadConstFalse",
    "LoadConstBigInt",
})


class OpcodeHandler(ABC):
    """
    Abstract base class for handling Hermes bytecode opcodes.
    (class docstring unchanged - see original)
    """

    ARGUMENTS: ArgsPattern | tuple[ArgsPattern, ...] = ()

    registry: Dict[str, "OpcodeHandler"] = {}

    # Set to True on a class (not inherited implicitly - see
    # `__init_subclass__` below) to opt it out of registration. Only
    # meant for genuine non-opcode helper/mixin classes.
    _abstract: bool = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.__name__ == "OpcodeHandler":
            return

        # Only a class's OWN `_abstract = True` opts it out - it must not
        # be inherited, or a real opcode subclassing an abstract base
        # would silently stay unregistered too.
        if cls.__dict__.get("_abstract", False):
            return

        OpcodeHandler.registry[cls.__name__] = cls()

    @abstractmethod
    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        """
        Process a Hermes bytecode opcode and produce the corresponding
        `OpcodeResult`.
        """
        ...

    @classmethod
    def get_handler(cls, opcode: str) -> Optional["OpcodeHandler"]:
        return cls.registry.get(opcode)

    def match_arguments(self, ctx: OpcodeContext) -> re.Match[str] | OpcodeResult:
        patterns = self.ARGUMENTS
        if not isinstance(patterns, tuple):
            patterns = (patterns,)

        args = ctx.entry.args.strip()

        for item in patterns:
            match = item.regex.match(args)
            if match:
                return match

        return self.build_invalid_args_result(ctx.analysis, ctx.entry, self.expected_arguments_message())

    def expected_arguments_message(self) -> str:
        patterns = self.ARGUMENTS
        if isinstance(patterns, ArgsPattern):
            patterns = (patterns,)

        descriptions = [p.desc for p in patterns]
        if len(descriptions) == 1:
            return f"Expected arguments: {descriptions[0]}"

        return "Expected one of: " + "; ".join(descriptions)

    @classmethod
    def build_invalid_args_result(cls, analysis, entry, error_detail="Invalid arguments") -> OpcodeResult:
        logger.warning(
            "Invalid arguments for opcode '%s' at address %d: %s (args=%r)",
            entry.opcode, entry.address, error_detail, entry.args,
        )

        error_msg = f"// Error: {cls.__name__} at address {entry.address}: {error_detail}: {entry.args}"
        result = OpcodeResult(entry, value=RawExpression(source=error_msg))
        analysis.add_result(result)

        return result

    @classmethod
    def build_exception_result(cls, analysis, entry, error: str) -> OpcodeResult:
        logger.error("%s failed while processing opcode '%s' at address %d: %s",
                     cls.__name__, entry.opcode, entry.address, error)

        result = OpcodeResult(entry, value=RawExpression(source=error))
        analysis.add_result(result)

        return result

    # -----------------------------------------------------------------
    # Register resolution
    # -----------------------------------------------------------------
    #
    # Three resolvers, in increasing order of how much they're willing
    # to inline:
    #
    #   get_register_reference   - NEVER inlines. Always `rN`. Use when
    #                               the slot is a raw stack/register
    #                               range with no reliable per-register
    #                               tracking (e.g. Call's variadic
    #                               argument window).
    #
    #   get_register_symbolic    - inlines ONLY a `Literal` produced by
    #                               a genuine const-load opcode
    #                               (LoadConstZero/UInt8/String/...).
    #                               Every other definition (Mov, Inc,
    #                               Add, GetById, a prior Call result,
    #                               a parameter, ...) stays symbolic.
    #                               This is the SAFE default for any
    #                               register whose value might be
    #                               loop-carried (i.e. could still
    #                               change on a later iteration/read
    #                               relative to where the source
    #                               *textually* appears): a `Mov r6,
    #                               r5` sitting once at the top of a
    #                               loop body must never be frozen into
    #                               whatever `r5` happened to equal the
    #                               first time this single-pass
    #                               left-to-right analysis walked past
    #                               it - see the forTest console.log(0)
    #                               regression this fixed. Use for:
    #                               branch/loop conditions, call
    #                               arguments, anything read potentially
    #                               more than once relative to its
    #                               definition's real (dynamic) lifetime.
    #
    #   get_register_expression  - inlines almost anything (Mov, Inc,
    #                               GetById/MemberExpression chains,
    #                               CallExpression, BinaryExpression,
    #                               ...), EXCEPT identity-sensitive
    #                               Object/Array literals. This is what
    #                               keeps common chains like
    #                               `globalThis.console.log` readable
    #                               instead of printing as bare `rN`
    #                               everywhere. Only safe to use where
    #                               the caller can be sure the register
    #                               is read essentially once, at its
    #                               one true definition site (e.g. the
    #                               callee/receiver of a call
    #                               immediately following its
    #                               TryGetById/GetByIdShort) - NOT for
    #                               anything that could be re-entered
    #                               by a loop back-edge before the read.
    #
    # When in doubt, prefer get_register_symbolic - a spurious `rN` in
    # the output is a readability regression; a wrongly-inlined stale
    # value is a correctness regression. See Call1/Call2/Call3/Call4
    # in Call.py for a concrete example of choosing the safe one for
    # call arguments.

    @classmethod
    def get_register_reference(cls, analysis: HermesAnalysis, reg: int) -> Identifier:
        """Always symbolic - never inlines the defining expression."""

        state = analysis.registers.get(f"r{reg}")

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        if state is not None:
            state.reads += 1

        return Identifier(name=f"r{reg}")

    @classmethod
    def get_register_symbolic(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Inline only if the definition is a `Literal` from a genuine
        const-load opcode; everything else (including Mov/Inc copies
        of another register) stays symbolic. See class-level comment
        above for the rationale - this is the resolver to reach for
        by default whenever a stale/loop-carried value would be a
        correctness bug, not just a cosmetic one.
        """
        return cls._resolve_register(analysis, reg, inline_non_literal=False)

    @classmethod
    def get_register_expression(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Inline the register's current defining expression, of (almost)
        any kind - see class-level comment above for exactly when this
        is/isn't safe to use.
        """
        return cls._resolve_register(analysis, reg, inline_non_literal=True)

    @classmethod
    def _resolve_register(cls, analysis: HermesAnalysis, reg: int, *, inline_non_literal: bool) -> Expression:

        state = analysis.registers.get(f"r{reg}")

        if state is None or state.definition is None:
            return Identifier(name=f"r{reg}_undefined")

        definition = state.definition
        value = definition.value
        opcode = definition.handler

        # Const-load literals: always safe to inline, regardless of
        # mode - a genuine LoadConstX opcode produces one immutable
        # value that can never be redefined by a loop iteration between
        # its own occurrences (each const-load is itself the
        # definition being read).
        if opcode in _CONST_LOAD_OPCODES and isinstance(value, Literal):
            state.reads += 1
            definition.definition_used = True

            if state.reads > 1:
                return dataclasses.replace(value)

            return value

        # Catch (and any future single-bind-per-scope opcode): safe to
        # inline even in symbolic mode - see _SAFE_IDENTIFIER_INLINE_OPCODES
        # docstring above.
        if opcode in _SAFE_IDENTIFIER_INLINE_OPCODES and isinstance(value, Identifier):
            state.reads += 1
            definition.definition_used = True
            return value

        if not inline_non_literal:
            # Symbolic mode (get_register_symbolic /
            # get_register_for_condition): Mov/Inc/Add/GetById/Call/
            # param/... never inlined, might be loop-carried.
            state.reads += 1
            definition.definition_used = True
            return Identifier(name=f"r{reg}")

        state_value = state.value
        # Expression mode (get_register_expression): inline anything
        # except identity-sensitive Object/Array literals.
        if not isinstance(state_value, Expression):
            return Identifier(name=f"r{reg}")

        state.reads += 1

        if isinstance(state.value, _IDENTITY_SENSITIVE_TYPES):
            return Identifier(name=f"r{reg}")

        if state.reads > 1:
            state_value = dataclasses.replace(state_value)

        definition.definition_used = True
        return state_value
