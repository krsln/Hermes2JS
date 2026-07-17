from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(Ret, Reg8)
# Example: <Ret>: <Reg8: 1>
class Ret(OpcodeHandler):
    """Return a value from the current function."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if match:
            reg = int(match.group(1))
            value = self._get_register_value(analysis, reg)
            return_stmt = f"return {value};"
        else:
            return_stmt = "return;"

        variable = JSVariable(handler, entry.address, '', return_stmt)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _get_register_value(self, analysis: HermesAnalysis, reg: int) -> str:
        var = self.GetVariableByReg(analysis, reg)
        return var.value if var and var.value is not None else f'undefined_r{reg}'
