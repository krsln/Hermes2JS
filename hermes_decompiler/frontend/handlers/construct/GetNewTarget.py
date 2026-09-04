from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression, Identifier


# Reg8 (total size 1)
# DEFINE_OPCODE_1(GetNewTarget, Reg8)
# Example: <GetNewTarget>: <Reg8: 4>
class GetNewTarget(OpcodeHandler):
    """Arg1 = new.target"""

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        expression = MemberExpression(obj=Identifier(name="new"), prop=Identifier(name="target"), computed=False)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
