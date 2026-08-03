from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetByIndex, Reg8, Reg8, UInt8)
# Example: <GetByIndex>: <Reg8: 4, Reg8: 1, UInt8: 0>
class GetByIndex(OpcodeHandler):
    """Get property by small integer index: obj[N] (N is an immediate UInt8)."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, obj_reg, index = map(int, match.groups())

        receiver = self.get_register_expression(analysis, obj_reg)
        member = NumericLiteral(value=index)

        expression = MemberExpression(receiver=receiver, member=member, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
