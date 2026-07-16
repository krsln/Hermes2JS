from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT16, sequence


# /// Load a value from an environment.
# /// Arg1 is the destination.
# /// Arg2 is the environment (as fetched by GetEnvironment).
# /// Arg3 is the environment index slot number.
# DEFINE_OPCODE_3(LoadFromEnvironment, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(LoadFromEnvironmentL, Reg8, Reg8, UInt16)
# Example: <LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 16>
class LoadFromEnvironment(OpcodeHandler):
    """Load value from environment slot."""
    _PATTERN = sequence(REG, REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8, UInt8")

        dest_reg, env_reg, slot = map(int, match.groups())

        env_value = self.GetValueByReg(analysis, env_reg) or f"r{env_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{env_value}[{slot}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadFromEnvironmentL(LoadFromEnvironment):
    """Long index variant."""
    _PATTERN = sequence(REG, REG, UINT16)
    pass
