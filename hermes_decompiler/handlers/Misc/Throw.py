from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# /// Throw an exception.
# /// throw Arg1;
# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    """Throw an exception."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse the Reg8 argument (e.g., "Reg8: 2")
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        reg = int(match.group(1))
        value = self._get_register_value(analysis, reg)

        throw_stmt = f"throw {value}"
        variable = JSVariable(handler, entry.address, f'r{reg}', throw_stmt)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _get_register_value(self, analysis: HermesAnalysis, reg: int) -> str:
        var = self.GetVariableByReg(analysis.results, reg)
        return var.value if var and var.value is not None else 'undefined'
