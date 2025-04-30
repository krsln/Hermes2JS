import re

from Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from Hermes2JS.Models.OpcodeResult import OpcodeResult
from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Models.OpcodeHandler import OpcodeHandler


class SelectObject(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg, obj, selector = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"r{obj}[r{selector}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
