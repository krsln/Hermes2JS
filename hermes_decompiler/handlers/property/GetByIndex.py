from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG, UINT8
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetByIndex, Reg8, Reg8, UInt8)
# Example: <GetByIndex>: <Reg8: 4, Reg8: 1, UInt8: 0>
class GetByIndex(OpcodeHandler):
    """Get property by small integer index: obj[N] (N is an immediate UInt8)."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, obj_reg, index = map(int, match.groups())

        receiver = self.get_register_expression(ctx.analysis, obj_reg)
        member = NumericLiteral(value=index)

        expression = MemberExpression(receiver=receiver, member=member, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
