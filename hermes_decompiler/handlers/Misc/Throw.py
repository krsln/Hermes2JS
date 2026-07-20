from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.Enums import FlowType
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    """Throw an exception."""
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        value_reg = int(match.group(1))
        reg_var = self.get_register_variable(analysis, value_reg)
        reg_value = reg_var.value if reg_var and reg_var.value is not None else 'undefined'

        throw_stmt = f"throw {reg_value}"
        variable = JSVariable(handler, entry.address, f'r{value_reg}', throw_stmt)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable, flow=FlowType.THROW)
