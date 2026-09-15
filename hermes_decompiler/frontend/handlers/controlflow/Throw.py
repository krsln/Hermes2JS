from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, STRING_ID
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import CallExpression, Identifier, StringLiteral
from hermes_decompiler.ir.statements import ExpressionStatement, ThrowStatement
from hermes_decompiler.ir.terminators import TerminatorThrow


# Reg8 (total size 1)
# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    """Throw an exception."""

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        value_reg = int(match.group(1))

        # NOTE (fix): same reasoning as Ret.py - kept symbolic here
        # rather than inlined via `get_register_expression`, which has
        # no control-flow awareness during this single linear,
        # address-order scan and can silently substitute a
        # conditionally-written value as if it always executes. A
        # later region pass (`ReturnValueResolutionPass`) folds it
        # back in only once real dominance information is available.
        expression = self.get_register_reference(ctx.analysis, value_reg)
        terminator = TerminatorThrow(value=expression)

        # NOTE (fix): same reasoning as Ret.py - `Throw` terminators are
        # never consumed by a structurer, so without an explicit
        # `statement` attached here the `throw ...;` line silently
        # disappears from the output (this is what was happening in the
        # generated `catch` blocks).
        statement = ThrowStatement(argument=expression)

        result = OpcodeResult(
            ctx.entry, value=expression, statement=statement, terminator=terminator, dest_reg=None
        )
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ThrowIfEmpty, Reg8, Reg8)
# Example:
class ThrowIfEmpty(OpcodeHandler):
    """
    If Arg2 is Empty, throw ReferenceError, otherwise move it into Arg1.

    Confirmed via the hermes-dec version catalog (hbc81-99): `Arg1, Arg2 =
    Reg8, Reg8`, same dest-first convention as `Mov` - used for `let`/
    `const` TDZ reads. The check itself needs no surface syntax: real JS
    already throws a ReferenceError on TDZ access on its own, so this is
    decompiled as the plain pass-through it is at the JS level (`Arg1 =
    Arg2`), same as `Mov`.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_expression(ctx.analysis, src_reg)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# UInt32 (string_id) (total size 4)
# DEFINE_OPCODE_1(ThrowIfHasRestrictedGlobalProperty, UInt32)
# Example:
class ThrowIfHasRestrictedGlobalProperty(OpcodeHandler):
    """
    Throw a SyntaxError if globalThis already has a restricted global
    property with the given name (e.g., a top-level `let`/`const`/`class`
    colliding with an existing non-configurable global).

    No destination register - this is a pure compile-time-style guard
    with no JS-visible value of its own, same shape as its neighbor in
    Hermes's own opcode list, `DeclareGlobalVar` (also a bare
    `UInt32 string_id`, also no destination). Like
    `ThrowIfThisInitialized` below, it has no direct surface-syntax
    equivalent, so it's kept traceable as an inert pseudo-call statement
    rather than silently dropped.
    """

    ARGUMENTS = ArgsPattern(sequence(STRING_ID), "UInt32 (string_id)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        string_id = int(match.group(1))
        prop_name = ctx.entry.identifier_name or f"string_{string_id}"

        expression = CallExpression(
            callee=Identifier(name="__throwIfHasRestrictedGlobalProperty__"),
            arguments=(StringLiteral(value=prop_name),),
        )
        statement = ExpressionStatement(expression=expression)

        result = OpcodeResult(ctx.entry, value=expression, statement=statement, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(ThrowIfUndefined, Reg8, Reg8)
# Example:
class ThrowIfUndefined(OpcodeHandler):
    """
    If Arg2 is `undefined`, throw ReferenceError, otherwise move it into
    Arg1.

    Same `Reg8, Reg8` dest-first shape as `ThrowIfEmpty` (confirmed via
    the hermes-dec version catalog, hbc98-99) and the same reasoning
    applies: the check is implicit in real JS semantics, so this
    decompiles as the plain pass-through `Arg1 = Arg2`.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, src_reg = map(int, match.groups())

        expression = self.get_register_expression(ctx.analysis, src_reg)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ThrowIfUndefinedInst, Reg8)
# Example:
class ThrowIfUndefinedInst(OpcodeHandler):
    """
    Throw if the given register contains an undefined instance.

    Single in-place register (hbc59-81, per the hermes-dec version
    catalog) - the historical predecessor of the two-register
    `ThrowIfEmpty`/`ThrowIfUndefined`, checking and passing through the
    same register rather than a separate dest/src pair. Re-affirms the
    register's own current value (rather than leaving it undefined here)
    so a version bump is recorded and downstream reads still resolve
    correctly.
    """

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        reg = int(match.group(1))

        expression = self.get_register_expression(ctx.analysis, reg)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=reg)
        ctx.analysis.add_result(result)

        return result


# Reg8 (total size 1)
# DEFINE_OPCODE_1(ThrowIfThisInitialized, Reg8)
# Example:
class ThrowIfThisInitialized(OpcodeHandler):
    """
    Throw if 'this' has already been initialized.

    Used by derived-class constructor initialization checks (introduced
    alongside class-field support, hbc98-99 per the hermes-dec version
    catalog) to guard against `super()` being invoked more than once.
    """

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match
        this_reg = int(match.group(1))

        this_value = self.get_register_expression(ctx.analysis, this_reg)

        # No JS-visible expression on the success path; modeled as an
        # inert pseudo-call so it's still traceable in output rather
        # than silently discarded, consistent with the
        # getParentEnvironment()-style convention used for other
        # no-surface-syntax opcodes.
        expression = CallExpression(
            callee=Identifier(name="__throwIfThisInitialized__"),
            arguments=(this_value,),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
