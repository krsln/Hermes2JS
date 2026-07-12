import re

from conversion.hermes2js.models.HermesAnalysis import HermesAnalysis
from conversion.hermes2js.models.OpcodeResult import OpcodeResult
from conversion.hermes2js.models.JSVariable import JSVariable
from conversion.hermes2js.models.OpcodeEntry import OpcodeEntry
from conversion.hermes2js.models.OpcodeHandler import OpcodeHandler


class SelectObject(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, obj, selector = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"r{obj}[r{selector}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
