from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, sequence, UINT32
from hermes_decompiler.ir.expressions import MemberExpression, NumericLiteral
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_3(GetByIndex, Reg8, Reg8, UInt8)
# Confirmed from hermes-dec opcode table (not in the version of
# BytecodeList.def checked, appears in newer bytecode versions ~97-99):
#
#   "Get a property by value, for the special case where the property is a
#    numeric literal that is a uint8_t integer. Arg1 = Arg2[Arg3]"
#
# So unlike GetByVal (index comes from a register) the index here is
# an immediate UInt8 baked into the bytecode -- i.e. obj[3] where 3 is
# small enough to fit in a byte. Rendered the same way GetByVal is,
# just with a numeric literal instead of a register-derived expression.
class GetByIndex(OpcodeHandler):
    """Get property by small integer index: obj[N] (N is an immediate UInt8)."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8 arguments")

        dest_reg, obj_reg, index = map(int, match.groups())

        receiver = self.get_register_value(analysis, obj_reg)
        member = NumericLiteral(value=index)

        expression = MemberExpression(receiver=receiver, member=member, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


class GetByIndexLong(GetByIndex):
    _PATTERN = sequence(REG, REG, UINT32)
