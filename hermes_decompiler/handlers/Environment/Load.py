from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import (
    REG,
    UINT8,
    UINT16,
    sequence,
)

from .Base import EnvironmentAccess


class LoadFromEnvironment(EnvironmentAccess):
    """
    Load a value from a lexical environment.

        dst = env[slot]
    """

    _PATTERN = sequence(REG, REG, UINT8, )

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, env_reg, slot = map(int, match.groups())
        env = self.ResolveEnvironment(analysis, env_reg)
        expression = self.FormatSlot(env, slot)

        variable = JSVariable(self.__class__.__name__, entry.address, f"r{dest_reg}", expression)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadFromEnvironmentL(LoadFromEnvironment):
    _PATTERN = sequence(REG, REG, UINT16)
