from hermes_decompiler.ir.Expressions import UnaryExpression, MemberExpression
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.Values import IdentifierValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence


# DEFINE_OPCODE_4(DelById, Reg8, Reg8, UInt8, UInt16)
# OPERAND_STRING_ID(DelById, 4)
# Example: <DelById>: <Reg8: 2, Reg8: 1, UInt8: 0, string_id: 158>  # String: 'cache' (Identifier)
class DelById(OpcodeHandler):
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8, UInt8, string_id arguments")

        dest_reg, obj_reg, _cache, string_id = map(int, match.groups())

        prop_name = entry.identifier_name or f"string_{string_id}"
        obj = self.get_register_value(analysis, obj_reg)

        value = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(
                object=obj,
                property=IdentifierValue(prop_name),
            ),
        )

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    """delete obj[prop]"""
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = map(int, match.groups())

        obj = self.get_register_value(analysis, obj_reg)
        prop = self.get_register_value(analysis, prop_reg)

        value = UnaryExpression(
            operator=UnaryOperator.DELETE,
            operand=MemberExpression(
                object=obj,
                property=prop,
                computed=True,
            ),
        )

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
