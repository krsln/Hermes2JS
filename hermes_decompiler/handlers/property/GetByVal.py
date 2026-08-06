from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    """Get property by dynamic value: obj[key]"""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry, "Expected Reg8, Reg8, Reg8 arguments")

        dest_reg, base_reg, prop_reg = map(int, match.groups())

        receiver = self.get_register_expression(ctx.analysis, base_reg)
        index = self.get_register_expression(ctx.analysis, prop_reg)

        expression = MemberExpression(receiver=receiver, member=index, computed=True)

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result

# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetByValWithReceiver, Reg8, Reg8, Reg8, Reg8)
