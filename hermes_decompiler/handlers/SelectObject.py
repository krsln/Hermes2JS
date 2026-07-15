import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, sequence

SELECT_PATTERN = sequence(REG, REG, REG)


class SelectObject(OpcodeHandler):
    """Select property by dynamic key: obj[key]"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = SELECT_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest_reg}',
            f"r{obj_reg}[r{selector_reg}]"
        )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
