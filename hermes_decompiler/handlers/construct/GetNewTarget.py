from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression, Identifier


# Reg8 (total size 1)
# DEFINE_OPCODE_1(GetNewTarget, Reg8)
# Example: <GetNewTarget>: <Reg8: 4>
class GetNewTarget(OpcodeHandler):
    """Arg1 = new.target"""

    _PATTERN = sequence(REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        expression = MemberExpression(receiver=Identifier(name="new"), member=Identifier(name="target"), computed=False)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
