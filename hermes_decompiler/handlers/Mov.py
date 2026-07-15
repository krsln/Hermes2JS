import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


class Mov(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest, src = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest}', f"r{src}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
