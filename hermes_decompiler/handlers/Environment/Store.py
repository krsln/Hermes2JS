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


class StoreToEnvironment(EnvironmentAccess):
    """
    Store a value into a lexical environment.

        env[slot] = value
    """

    _PATTERN = sequence(REG, UINT8, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        env_reg, slot, value_reg = map(int, match.groups())
        env = self.ResolveEnvironment(analysis, env_reg)
        value = self.ResolveValue(analysis, value_reg)
        expression = f"{self.FormatSlot(env, slot)} = {value};"

        variable = JSVariable(self.__class__.__name__, entry.address, "", expression)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class StoreToEnvironmentL(StoreToEnvironment):
    _PATTERN = sequence(REG, UINT16, REG, )


class StoreNPToEnvironment(StoreToEnvironment):
    """
    Non-pointer variant.

    Semantically identical during decompilation.
    """
    pass


class StoreNPToEnvironmentL(StoreToEnvironmentL):
    """
    Long non-pointer variant.
    """
    pass
