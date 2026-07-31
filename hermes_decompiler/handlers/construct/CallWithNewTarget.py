from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    CallExpression,
    Identifier,
    MemberExpression,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, Reg8, UInt8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTarget, Reg8, Reg8, Reg8, UInt8)
# Example: <CallWithNewTarget>: <Reg8: 0, Reg8: 2, Reg8: 3, UInt8: 2>
class CallWithNewTarget(OpcodeHandler):
    """Call a function with an explicit `new.target`, e.g. super(...) plumbing."""

    _PATTERN = sequence(REG, REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected Reg8, Reg8, Reg8, UInt8 arguments"
            )

        dest_reg, func_reg, new_target_reg, num_args = map(int, match.groups())

        callee = self.get_register_expression(analysis, func_reg)
        new_target = self.get_register_expression(analysis, new_target_reg)

        arg_regs = list(range(func_reg - num_args, func_reg))
        arguments = ArrayExpression(elements=tuple(Identifier(name=f"r{r}") for r in arg_regs))

        call_callee = MemberExpression(
            receiver=Identifier(name="Reflect"),
            member=Identifier(name="construct"),
            computed=False,
        )

        expression = CallExpression(
            callee=call_callee,
            arguments=(callee, arguments, new_target),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(CallWithNewTargetLong, Reg8, Reg8, Reg8, Reg8)
class CallWithNewTargetLong(CallWithNewTarget):
    _PATTERN = sequence(REG, REG, REG, REG)
