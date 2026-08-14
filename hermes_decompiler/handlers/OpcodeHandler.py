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
    def get_register_expression(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Return the current expression assigned to a register.

        This exposes the actual IR node currently stored in the register
        (ObjectExpression, Literal, BinaryExpression, CallExpression, etc.)
        and should only be used by optimization or analysis passes that need
        the defining expression.

        If the register has never been defined, fall back to its symbolic
        identifier.
        """

        state = analysis.registers.get(f"r{reg}")

        if state is None or state.definition is None:
            return Identifier(name=f"r{reg}_undefined")

        state_value = state.value
        if isinstance(state_value, Expression):
            state.reads += 1

            if isinstance(state.value, _IDENTITY_SENSITIVE_TYPES):
                return Identifier(name=f"r{reg}")

            if state.reads > 1:
                state_value = dataclasses.replace(state_value)

            state.definition.definition_used = True
            return state_value

        return Identifier(name=f"r{reg}")

    @classmethod
    def get_register_for_condition(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        """
        Jump/branch condition operands.

        Inline ONLY when this register was defined by a const-load opcode.
        That preserves switch case labels (r1 = 0; if (r1 === disc)) while
        keeping Mov/Inc/phi-carried values symbolic for loops.
        """
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

        # Symbolic mode (get_register_symbolic /
        # get_register_for_condition): Mov/Inc/Add/GetById/Call/
        # param/... never inlined, might be loop-carried.
        state.reads += 1
        definition.definition_used = True
        return Identifier(name=f"r{reg}")
