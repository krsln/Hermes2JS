import re

from hermes2js.models.HermesAnalysis import HermesAnalysis
from hermes2js.models.OpcodeResult import OpcodeResult
from hermes2js.models.JSVariable import JSVariable
from hermes2js.models.OpcodeEntry import OpcodeEntry
from hermes2js.models.OpcodeHandler import OpcodeHandler


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
