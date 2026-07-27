from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence, UINT32
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(GetByIndex, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(GetByIndexLong, Reg8, Reg8, UInt32)
class GetByIndex(OpcodeHandler):
    """Get property by immediate numeric index: obj[index]"""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, obj_reg, index = map(int, match.groups())

        receiver = self.get_register_value(analysis, obj_reg)

        expression = MemberExpression(
            receiver=receiver,
            member=NumericLiteral(value=index),
            computed=True,
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class GetByIndexLong(GetByIndex):
    _PATTERN = sequence(REG, REG, UINT32)