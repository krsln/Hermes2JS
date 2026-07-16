from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    sequence,
)

from .Base import EnvironmentAccess


class GetEnvironment(EnvironmentAccess):
    """
    Resolve an environment from the lexical scope chain.

    level = 0  -> current environment
    level = 1  -> parent environment
    level = 2  -> grandparent
    ...
    """

    _PATTERN = sequence(REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, level = map(int, match.groups())

        variable = JSVariable(self.__class__.__name__, entry.address, f"r{dest_reg}", f"getEnvironment({level})")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
