from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    CallExpression,
    Identifier,
    MemberExpression,
)


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTarget, Reg8, Reg8, Reg8, UInt8)
# Example: <CallWithNewTarget>: <Reg8: 0, Reg8: 2, Reg8: 3, UInt8: 2>
class CallWithNewTarget(OpcodeHandler):
    """Call a function with an explicit `new.target`, e.g. super(...) plumbing."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, UINT8), "Reg8, Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, func_reg, new_target_reg, num_args = map(int, match.groups())

        callee = self.get_register_expression(ctx.analysis, func_reg)
        new_target = self.get_register_expression(ctx.analysis, new_target_reg)

        arg_regs = list(range(func_reg - num_args, func_reg))
        arguments = ArrayExpression(elements=tuple(Identifier(name=f"r{r}") for r in arg_regs))

        call_callee = MemberExpression(
            obj=Identifier(name="Reflect"),
            prop=Identifier(name="construct"),
            computed=False,
        )

        expression = CallExpression(
            callee=call_callee,
            arguments=(callee, arguments, new_target),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTargetLong, Reg8, Reg8, Reg8, Reg8)
class CallWithNewTargetLong(CallWithNewTarget):
    _PATTERN = sequence(REG, REG, REG, REG)
    ARGUMENTS = ArgsPattern(sequence(REG, REG, REG, REG), "Reg8, Reg8, Reg8, Reg8")
