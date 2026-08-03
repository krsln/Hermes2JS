from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG
from hermes_decompiler.ir.expressions import MemberExpression
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(GetByVal, Reg8, Reg8, Reg8)
# Example: <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 0>
class GetByVal(OpcodeHandler):
    """Get property by dynamic value: obj[key]"""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, Reg8 arguments")

        dest_reg, base_reg, prop_reg = map(int, match.groups())

        receiver = self.get_register_expression(analysis, base_reg)
        index = self.get_register_expression(analysis, prop_reg)

        expression = MemberExpression(receiver=receiver, member=index, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result

# Reg8, Reg8, Reg8, Reg8 (total size 4)
# DEFINE_OPCODE_4(GetByValWithReceiver, Reg8, Reg8, Reg8, Reg8)
