from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# DEFINE_OPCODE_1(LoadThisNS, Reg8)
# Example: <LoadThisNS>: <Reg8: 4>
class LoadThisNS(OpcodeHandler):
    """Load and coerce `this` value."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'this')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
