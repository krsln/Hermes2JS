from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import CallExpression, Identifier, NumericLiteral


# Reg8, UInt8 (total size 2)
# DEFINE_OPCODE_2(GetParentEnvironment, Reg8, UInt8)
# Example: <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
class GetParentEnvironment(OpcodeHandler):
    """Fetch an environment N levels up the *enclosing* scope chain."""

    ARGUMENTS = ArgsPattern(sequence(REG, UINT8), "Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, levels = map(int, match.groups())

        expression = CallExpression(
            callee=Identifier(name="getParentEnvironment"),
            arguments=(NumericLiteral(value=levels),),
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
