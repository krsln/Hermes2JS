from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import CallExpression, Identifier


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(<GetClosureEnvironment, Reg8>, Reg8)
# Example: <GetClosureEnvironment>: <Reg8: 3, Reg8: 2>
class GetClosureEnvironment(OpcodeHandler):
    """Fetch the environment/scope captured by an explicit closure register."""

    _PATTERN = sequence(REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, Reg8 arguments")

        dest_reg, closure_reg = map(int, match.groups())

        closure = self.get_register_expression(ctx.analysis, closure_reg)

        expression = CallExpression(
            callee=Identifier(name="__getClosureEnvironment__"),
            arguments=(closure,),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
