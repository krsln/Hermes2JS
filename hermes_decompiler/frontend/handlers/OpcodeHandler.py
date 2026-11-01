from __future__ import annotations

import dataclasses
import re
from abc import ABC, abstractmethod

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import (
    Expression, Identifier, RawExpression, ObjectExpression,
    ArrayExpression, Literal, CallExpression, MemberExpression, ThisPlaceholder, BinaryExpression, NewExpression,
    UndefinedLiteral,
)
from .OpcodeTypes import OpcodeContext, ArgsPattern, OperandMode

logger = get_logger(__name__)


class OpcodeHandler(ABC):
    """
    Abstract base class for handling Hermes bytecode opcodes.

    Subclasses implement `handle()` to turn one disassembled opcode
    (`OpcodeContext`) into an `OpcodeResult`. Every concrete subclass is
    auto-registered under its own class name via `__init_subclass__`
    (opt out with `_abstract = True`), so `OpcodeDispatcher` can look
    handlers up by opcode name through `get_handler()` without a
    separate manual registry.

    Subclasses declare their expected operand syntax via the
    `ARGUMENTS` class attribute (one `ArgsPattern`, or a tuple of
    alternatives) and use `match_arguments()` to parse `ctx.entry.args`
    against it, falling back to `build_invalid_args_result()` on a
    mismatch. The `resolve_*` `classmethods` below are the shared,
    single-source-of-truth logic for turning a register operand into
    an IR `Expression` (inlining vs. symbolic reference, loop-safety
    guards, etc.) - handlers should use these rather than reading
    register state directly.
    """

    ARGUMENTS: ArgsPattern | tuple[ArgsPattern, ...] = ()

    registry: dict[str, "OpcodeHandler"] = {}

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
    def get_handler(cls, opcode: str) -> "OpcodeHandler | None":
        return cls.registry.get(opcode)

    def match_arguments(self, ctx: OpcodeContext) -> re.Match[str] | OpcodeResult:
        patterns = self.ARGUMENTS
        if not isinstance(patterns, tuple):
            patterns = (patterns,)

        args = ctx.entry.args.strip()

        for item in patterns:
            match = item.regex.fullmatch(args)
            if match:
                return match

        return self.build_invalid_args_result(ctx.analysis, ctx.entry, self.expected_arguments_message(patterns))

    @classmethod
    def expected_arguments_message(cls, patterns: tuple[ArgsPattern, ...]) -> str:
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
    def resolve_operand(cls, analysis: HermesAnalysis, reg: int, mode: "OperandMode") -> Expression:
        """
        Resolve a register operand according to `mode`. Single dispatch
        point shared by `BaseUnaryOperator` and `BaseBinaryOperator` (and
        any future handler), so the EXPRESSION-vs.-REFERENCE choice lives
        in one place instead of being reimplemented per subclass.
        """

        if mode is OperandMode.REFERENCE:
            return cls.get_register_reference(analysis, reg)

        return cls.get_register_expression(analysis, reg)

    @staticmethod
    def _restore_folded_constants(analysis: HermesAnalysis, state) -> None:
        """A join read names the register, so every write that can reach it must print. A
        constant an earlier test consumed (`r4 = undefined` folded into `undefined === r8`) is
        in no fold's way any more and nothing else prints it (98/9611 `dt`: `r3.size = r4` on
        the path where `r4` is `undefined`). The write ran in the bytecode, so printing it is
        faithful; `DeadUndefinedStorePass` removes an `undefined` store nothing reads."""
        for earlier in analysis.history.get(state.definition.name, ())[:state.version]:
            if isinstance(earlier.value, UndefinedLiteral) and earlier.definition.definition_used:
                earlier.materialize()

    @classmethod
    def get_register_reference(cls, analysis: HermesAnalysis, reg: int, materialize: bool = True) -> Identifier:
        """Always symbolic - never inlines the defining expression.

        Exception: a register whose only definition so far is a
        function parameter (LoadParam/LoadParamLong) keeps that
        parameter's name instead of a synthetic r{reg}. A parameter
        name is the register's stable identity for the entire
        function - not a computed expression being substituted in -
        so returning it here doesn't inline anything; it just avoids
        two different call sites (e.g., a MemberExpression's receiver
        built via resolve_get_by_argument, and this `this`-register
        reference used to structurally compare against it) disagreeing
        about what to call the exact same untouched parameter register.
        """

        state = analysis.get_register_state(reg)

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        state.mark_read()

        value = state.value
        if (
                state.handler in ("LoadParam", "LoadParamLong")
                and isinstance(value, Identifier)
                and not analysis.is_rewritten_in_loop(reg)
        ):
            return value

        # `materialize=False` is for callers that only *compare* against the
        # reference, or whose own pass decides how the register is folded
        # (Call's `this` check, Ret) - pinning there would resurrect
        # definitions that were folded on purpose.
        if materialize:
            state.materialize()

        return Identifier(name=f"r{reg}")

    @classmethod
    def get_register_expression(
            cls, analysis: HermesAnalysis, reg: int, *, keep_placeholder: bool = False
    ) -> Expression:
        """
        Return the current expression assigned to a register.

        Identity-sensitive expressions are kept symbolic to preserve
        aliasing semantics.

        Loop-safety: if the register's definition and this read both fall
        inside the same detected loop body (`analysis.loop_ranges`), the
        stored expression is NOT inlined - it's returned as a bare `rN`
        reference instead, same as `get_register_reference()`. Without
        this, a register redefined every iteration (directly, or via a
        `Mov` aliasing one that is) would have a single iteration's
        snapshot baked into every use inside the loop body - see
        `Binary.AddN`/`Binary.SubN`'s `LHS_MODE = REFERENCE` for the
        original, manually-special-cased instance of this same hazard.
        This check generalizes that fix to every opcode automatically,
        instead of requiring each new affected opcode to opt in by hand.
        """

        state = analysis.get_register_state(reg)

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        value = state.value
        if value is None:
            logger.error("Register r%d has no value (handler=%s)", reg, state.handler)
            return Identifier(name=f"r{reg}")

        if isinstance(value, (ObjectExpression, ArrayExpression, CallExpression)):
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # A `new` evaluated by a read inside a loop its definition is outside of would build a
        # fresh object on every iteration (96/1163 `new Array(r5)[r0] = arguments[r0]`): the
        # register keeps the one object, like the `ObjectExpression`/`CallExpression` above.
        # An earlier read of the same object has to keep the register too, or the loop's read
        # would print a second `new` (96/15130 `tag`): the scratch pass knows the definition prints.
        if isinstance(value, NewExpression) and (
                analysis.read_enters_loop(state)
                or (state.definition.name, state.definition.address) in analysis.printed_definitions
        ):
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # The `this` object a `new`/`super` allocates is ONE object with an
        # identity, not an expression: inlined into every reader it printed as
        # `CreateThisForNew(r8)._cursor = 0; CreateThisForNew(r8)._size = 0`,
        # which reads as several objects. Only the opcodes that consume it
        # (the `new`/`super` call, `Mov` carrying it to its window slot) take
        # the placeholder itself; everything else reads the register.
        if isinstance(value, ThisPlaceholder) and not keep_placeholder:
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # Join guard: the register's latest definition ran on one path of a join of three
        # or more (`r1 = p; if (c) { r1 = q; if (d) r1 = p }; r6 = r1`): the read sees a
        # merge no single value stands for. Inlined `p` was wrong whenever `c && !d`
        # (96/4775 `interpolate`: `r6 = param1` for `r6 = r1`). A binary expression is no
        # different (96/1801 `getComponentNameFromType`: the `ForwardRef(...)` string built
        # on one arm was inlined into `r1 = r3` on every other arm). Other shapes keep
        # inlining: a member read is left to the ternary fold, which names the register
        # itself afterwards (`tests/test_default_parameter_merge.py`), and a constant or
        # an environment value would leave a read of a register that prints nowhere
        # (`reject.call(r0, ...)`, 96/2999).
        if isinstance(value, (Identifier, BinaryExpression)) and analysis.is_nested_join_value(state):
            # Like the branch test (`JmpTrue`): the arm's own write is left for a fold or
            # for `UnfoldedMergeRepairPass`, which prints it when no fold took it.
            state.mark_read()
            cls._restore_folded_constants(analysis, state)
            return Identifier(name=f"r{reg}")

        # Try-boundary guard: a read that can throw stays where the `try` put it, so the
        # reader outside the range reads the register (98/13768 `typeof p.aborted`).
        if analysis.crosses_try_boundary(state) and any(isinstance(node, MemberExpression) for node in value.walk()):
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # Stale-value guard: the value refers to a register that was
        # redefined after it was built (or to its own destination, as in
        # `r3 = r3.a`), so inlining it here would silently rebind that
        # `rN` to the NEW definition. Keep this read symbolic instead.
        if not analysis.may_inline(state):
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # Loop-safety guard excludes MemberExpression (property-lookup
        # chains, e.g. `console.log`): re-fetched fresh every iteration
        # in typical Hermes output, but landing on the exact same value
        # each time - not itself an accumulator. Guarding it caused real
        # regressions (`console.log(...)` rendering as a nonsensical
        # `r6.call(r7, ...)`) without preventing any known bug.
        #
        # It also excludes non-register-alias Identifiers (fixed
        # protocol/magic symbols, e.g. `__resumeIsReturn` -
        # see `_is_register_alias`): guarding those broke
        # `GeneratorStateMachineRegionPass`'s exact-name pattern match,
        # regressing a clean `yield expr;` back into raw suspend/resume
        # boilerplate.
        #
        # Every other value shape stays guarded: Literal (e.g., a loop
        # counter's pre-loop `r5 = 0`), a register-alias Identifier
        # (e.g. `r6 = Mov(r4)`), and BinaryExpression (e.g. `r8 =
        # r2-2`) are exactly the shapes a loop-carried accumulator's
        # value can take depending on which iteration of the single
        # linear scan last defined it. This is still an approximation
        # (a MemberExpression with a loop-dependent computed key could
        # in principle be unsafe too), but matches the confirmed bug
        # shapes while leaving the known-safe patterns alone.
        # A parameter's own name is exempt above only while nothing rewrites its register inside the loop
        # that holds the read (96/4846 `binarySubdivide`: `Mov r11, r15` ends the body, `Sub r0, r10, r11` starts it).
        if (
                (
                        not isinstance(value, MemberExpression)
                        and (
                                not (isinstance(value, Identifier) and not cls._is_register_alias(value))
                                or (state.handler in ("LoadParam", "LoadParamLong")
                                    and analysis.is_rewritten_in_loop(reg))
                        )
                )
                # A member read defined before the loop and rewritten inside it
                or (isinstance(value, MemberExpression)
                    and analysis.is_rewritten_in_loop(reg, state.definition.address))
        ) and \
                analysis.is_unsafe_loop_register(reg, state.definition.address):
            state.mark_read()
            state.materialize()
            return Identifier(name=f"r{reg}")

        # if it has been read at least once before
        if state.reads > 0:
            state.mark_read()

            # The defining statement is printed (an earlier read used the
            # bare `rN`), so `rN` already holds the value: re-inlining the
            # expression here would evaluate it a SECOND time - a second
            # `new Set(...)` (a different object), a second property fetch
            # (different if it is a getter or the object changed in
            # between: `if (r3 !== undefined) { r5 = r2.timeout }` for
            # `Mov r5, r3`). Only literals / plain identifiers stay
            # duplicated: free and safe.
            if state.definition.definition_pinned and not isinstance(value, (Literal, Identifier)):
                return Identifier(name=f"r{reg}")

            # A second read of a `new` object: it is pinned now, and the scratch pass tells the
            # first read of the real pass to keep the register too (96/4138 `createSearchParams`:
            # three reads of one `URLSearchParams` printed as three `new`s).
            if isinstance(value, NewExpression):
                state.materialize()
                return Identifier(name=f"r{reg}")

            return dataclasses.replace(value)

        state.mark_read()
        state.mark_used()
        return value

    @classmethod
    def resolve_get_by_argument(cls, analysis, reg: int) -> Expression:
        state = analysis.get_register_state(reg)

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        # _GET_BY_ARGUMENT_INLINE_OPCODES
        if analysis.may_inline(state) and state.handler in frozenset({
            "GetGlobalObject",
            "TryGetById",
            "LoadParam",
            "LoadParamLong",
            "Catch",
        }):
            if isinstance(state.value, MemberExpression):
                state.mark_read()
                state.mark_used()

                return state.value
            elif isinstance(state.value, Identifier):
                state.mark_read()
                state.mark_used()

                return state.value

            logger.warning(
                "resolve_get_by_argument | Cannot inline get-by-argument value: handler=%s value=%r",
                state.handler, state.value
            )

        state.mark_read()
        state.materialize()
        return Identifier(name=f"r{reg}")

    @classmethod
    def resolve_call_argument(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        state = analysis.get_register_state(reg)

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        value = state.value
        # _CALL_ARGUMENT_INLINE_OPCODES
        if analysis.may_inline(state) and state.handler in frozenset({
            "CreateClosure",
            "GetById",
            "GetByIdShort",
            "LoadConstUInt8",
            "LoadConstString",
            "LoadParam",
            "Catch",
        }):
            if isinstance(value, Literal):
                state.mark_read()
                state.mark_used()

                return value
            elif isinstance(value, Identifier):
                state.mark_read()
                state.mark_used()

                return value
            elif isinstance(value, MemberExpression):
                state.mark_read()
                state.mark_used()

                return value

            logger.warning(
                "resolve_call_argument | Cannot inline get-by-argument value: handler=%s value=%r",
                state.handler, state.value
            )

        # Not one of the safely-inlineable shapes above (e.g., the
        # value came from a Call/CallBuiltin/Construct result, a
        # binary op, etc.) - this is returned as a bare symbolic
        # register reference, NOT an inlined substitution of the
        # actual expression. Marking it "used" here (as the
        # inlineable branches above correctly do) would tell the
        # printer the defining statement was folded into this call
        # site and can be skipped - but it wasn't folded in, so that
        # previously suppressed the defining assignment entirely,
        # leaving this bare reference dangling with no definition
        # printed at all (see e.g. `console.log(scores.get("bob"))`,
        # which silently dropped the `.get()` call and printed a
        # stale/undefined `r0` instead). Only mark_read() here, so
        # the defining statement still gets printed - matching how
        # get_register_expression() already treats CallExpression/
        # ObjectExpression/ArrayExpression values (kept symbolic,
        # never marked used).
        state.mark_read()
        state.materialize()
        return Identifier(name=f"r{reg}")

    @classmethod
    def resolve_condition_argument(cls, analysis: HermesAnalysis, reg: int) -> Expression:
        state = analysis.get_register_state(reg)

        if state is None:
            return Identifier(name=f"r{reg}_undefined")

        # Const-load literals: always safe to inline, regardless of
        # mode - a genuine LoadConstX opcode produces one immutable
        # value that can never be redefined by a loop iteration between
        # its own occurrences (each const-load is itself the
        # definition being read).
        value = state.value
        # _CONDITION_ARGUMENT_INLINE_OPCODES
        if analysis.may_inline(state) and state.handler in frozenset({
            "LoadParam",
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
            "Catch",
        }):
            if isinstance(value, Literal):
                state.mark_read()
                state.mark_used()

                return value
            elif isinstance(value, Identifier):
                state.mark_read()
                state.mark_used()

                return value

            logger.warning(
                "resolve_condition_argument | Cannot inline get-by-argument value: handler=%s value=%r",
                state.handler, state.value
            )

        state.mark_read()
        state.materialize()
        return Identifier(name=f"r{reg}")

    @classmethod
    def _is_register_alias(cls, value: Expression) -> bool:
        """
        True only for an Identifier that names a *register* (`r0`, `r12`,
        ...) - i.e., a value produced by aliasing/copying another register
        (typically a `Mov`), which is exactly the shape the loop-safety
        guard in `get_register_expression` needs to catch.

        Deliberately excludes Identifiers that name a fixed protocol/magic
        symbol instead of a register - e.g., ResumeGenerator's
        `Identifier(name="__resumeIsReturn")`. Such a symbol never varies
        across loop iterations (it isn't loop-carried state at all - it's
        a constant marker), and later passes (e.g.
        `GeneratorStateMachineRegionPass._is_resume_guard`) pattern-match
        on the EXACT string `"__resumeIsReturn"` to recognize the
        suspend/resume machinery. Guarding it here would replace that name
        with a symbolic `rN` and silently break that later fold - it did,
        in practice (see the regression this comment is guarding against:
        a loop-body yield rendering as raw goto/ResumeGenerator boilerplate
        instead of a clean `yield expr;`).
        """
        _REGISTER_ALIAS_RE = re.compile(r"r\d+$")

        return isinstance(value, Identifier) and bool(_REGISTER_ALIAS_RE.fullmatch(value.name))
