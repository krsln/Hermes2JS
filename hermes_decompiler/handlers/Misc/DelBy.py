from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, STRING_ID, sequence
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.expressions import UnaryExpression, MemberExpression, Identifier
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# DEFINE_OPCODE_4(DelById, Reg8, Reg8, UInt8, UInt16)
# OPERAND_STRING_ID(DelById, 4)
# Example: <DelById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 158>  # String: 'cache' (Identifier)
class DelById(OpcodeHandler):
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8, string_id arguments")

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        prop_name = entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_value(analysis, obj_reg)

        expression = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(
                receiver=obj,
                member=Identifier(name=prop_name),
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = map(int, match.groups())

        obj = self.get_register_value(analysis, obj_reg)
        prop = self.get_register_value(analysis, prop_reg)

        expression = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(
                receiver=obj,
                member=prop,
                computed=True,
            ),
        )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
