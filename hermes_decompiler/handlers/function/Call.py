

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier, MemberExpression


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(Call, Reg8, Reg8, UInt8)
# Example: <Call>: <Reg8: 4, Reg8: 9, UInt8: 6>
class Call(OpcodeHandler):
    """
    Runtime argument count variant.

    Hermes layout:

        [arg1][arg2]...[argN][callee]

    Example:

        Call r4, r9, 6

    means

        r4 = r9(r3, r4, r5, r6, r7, r8)
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, func_reg, num_args = map(int, match.groups())

        highest = max(
            int(r[1:])
            for r in ctx.analysis.registers
        )

        if highest + 1 < num_args:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        # Arguments occupy the contiguous register range
        # [function - argCount, function). First argument is at the
        # lowest register index.
        arg_regs = range(highest, highest - num_args, -1)
        # arg_regs = list(range(func_reg - num_args, func_reg))

        # NOTE: kept as bare register references (not resolved via
        # get_register_value), same as the original - the argument slots
        # here are a contiguous stack range that doesn't necessarily
        # correspond to individually tracked register assignments.
        arguments = tuple(
            self.get_register_reference(ctx.analysis, r)
            for r in arg_regs
        )

        callee = self.get_register_expression(ctx.analysis, func_reg)
        expression = CallExpression(callee=callee, arguments=arguments)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(Call1, Reg8, Reg8, Reg8)
# Example: <Call1>: <Reg8: 1, Reg8: 1, Reg8: 2>
class Call1(OpcodeHandler):
    """
    Call a function with one arg (`Call1`), and shared base
    implementation for the rest of the fixed-arg-count Call family
    (`Call2`, `Call3`, `Call4`). A real opcode is used as the shared base
    (rather than a separate non-opcode `CallX` class) - see `Add` in
    `handlers/arithmetic/Binary.py` for the rationale.

    Hermes CallN opcodes mirror `Function.prototype.call` semantics:
    the FIRST argument register is always the `this` context, not a
    regular positional argument - `CallN dst, callee, thisArg, arg1,
    arg2, ...`. For the extremely common `obj.method(...)` shape, the
    compiler puts `obj` itself into the `thisArg` slot (the same value
    already sitting in a preceding `GetById`'s receiver), so rendering
    it a second time as an explicit argument duplicates the receiver
    expression and produces `obj.method(obj)` instead of `obj.method()`.

    We special-case the common pattern: if `callee` is a
    `MemberExpression` whose `.receiver` is structurally identical to
    the resolved `thisArg` value, the call is a plain method call and
    `thisArg` is dropped entirely (it's already implicit in
    `obj.method(...)`). Otherwise `this` isn't the callee's own
    receiver (e.g. `fn.call(otherThis, ...)`, or a bare function call
    where `thisArg` is `undefined`/unrelated) and must be preserved
    explicitly via `.call(thisArg, ...)` to keep semantics correct.
    """

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG), "Reg8, Reg8, Reg8 (dest, callee, thisArg)")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, func_reg, this_reg, *rest_arg_regs = map(int, match.groups())

        callee = self.get_register_expression(ctx.analysis, func_reg)

        if isinstance(callee, MemberExpression) and isinstance(callee.obj, Identifier):
            this_value = self.get_register_reference(ctx.analysis, this_reg)
        else:
            this_value = self.get_register_expression(ctx.analysis, this_reg)

        real_arguments = tuple(
            self.resolve_call_argument(ctx.analysis, reg)
            for reg in rest_arg_regs
        )

        if isinstance(callee, MemberExpression) and callee.obj.structurally_equal(this_value):
            # Plain `obj.method(...)` - `this` is already implicit.
            expression = CallExpression(callee=callee, arguments=real_arguments)
        else:
            # `this` doesn't match the callee's own receiver (or callee
            # isn't a member access at all) - preserve it explicitly.
            call_callee = MemberExpression(obj=callee, prop=Identifier(name="call"), computed=False)
            expression = CallExpression(callee=call_callee, arguments=(this_value, *real_arguments))

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(Call2, Reg8, Reg8, Reg8, Reg8)
class Call2(Call1):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8")


# Reg8, Reg8, Reg8, Reg8, Reg8 (total size 5)
# DEFINE_OPCODE_5(Call3, Reg8, Reg8, Reg8, Reg8, Reg8)
class Call3(Call1):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8, Reg8")


# Reg8, Reg8, Reg8, Reg8, Reg8, Reg8 (total size 6)
# DEFINE_OPCODE_6(Call4, Reg8, Reg8, Reg8, Reg8, Reg8, Reg8)
class Call4(Call1):
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG, REG, REG), "Reg8 × 6")
