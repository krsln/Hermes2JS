from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(GetClosureEnvironment, Reg8, Reg8)
# Example: <GetClosureEnvironment>: <Reg8: 3, Reg8: 2>
class GetClosureEnvironment(OpcodeHandler):
    """Fetch the environment/scope captured by an explicit closure register."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG), "Reg8, Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, closure_reg = map(int, match.groups())

        closure = self.get_register_expression(ctx.analysis, closure_reg)

        expression = CallExpression(
            callee=Identifier(name="__getClosureEnvironment__"),
            arguments=(closure,),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
