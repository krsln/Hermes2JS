from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
class PutByVal(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        obj_reg, key_reg, value_reg = map(int, match.groups())

        obj_val = self.get_register_value(analysis, obj_reg) or f"r{obj_reg}"
        key_val = self.get_register_value(analysis, key_reg) or f"r{key_reg}"
        value_val = self.get_register_value(analysis, value_reg) or f"r{value_reg}"

        statement = f"{obj_val}[{key_val}] = {value_val}"
        variable = JSVariable(handler, entry.address, "", statement)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
