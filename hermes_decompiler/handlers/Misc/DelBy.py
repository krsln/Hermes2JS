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

        prop_name = self.resolve_property_name(analysis, entry, string_id)
        if prop_name is None:
            error = f'/* Error: string_id {string_id} not found in stringTable */ undefined'
            return self.build_exception_result(analysis, entry, error)

        obj_val = self.get_register_value(analysis, obj_reg)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}.{prop_name}")
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

        obj_val = self.get_register_value(analysis, obj_reg)
        prop_val = self.get_register_value(analysis, prop_reg)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}[{prop_val}]")
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
