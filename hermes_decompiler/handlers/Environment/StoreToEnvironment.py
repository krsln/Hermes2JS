import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


# /// Store a value in an environment.
# /// StoreNPToEnvironment[L] store a non-pointer value in an environment
# /// Arg1 is the environment (as fetched by GetEnvironment).
# /// Arg2 is the environment index slot number.
# /// Arg3 is the value.
# DEFINE_OPCODE_3(StoreToEnvironment, Reg8, UInt8, Reg8)
# DEFINE_OPCODE_3(StoreToEnvironmentL, Reg8, UInt16, Reg8)
# DEFINE_OPCODE_3(StoreNPToEnvironment, Reg8, UInt8, Reg8)
# DEFINE_OPCODE_3(StoreNPToEnvironmentL, Reg8, UInt16, Reg8)
# Example:  <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 3>
class StoreToEnvironment(OpcodeHandler):
    """Store value into environment slot."""
    _PATTERN = re.compile(
        r'^Reg8:\s*(\d+),\s*UInt(?:8|16):\s*(\d+),\s*Reg8:\s*(\d+)$'
    )

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, UInt(8|16), Reg8")

        env_reg, slot, value_reg = map(int, match.groups())

        value = self.GetValueByReg(analysis.results, value_reg) or f"r{value_reg}"

        comment = f"{handler}: env=r{env_reg}, slot={slot}, value=r{value_reg}"
        variable = JSVariable(handler, entry.address, f"r{env_reg}", f"setEnvSlot({slot}, {value})  /*{comment}*/")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Aliases for different variants
class StoreToEnvironmentL(StoreToEnvironment): pass


class StoreNPToEnvironment(StoreToEnvironment): pass


class StoreNPToEnvironmentL(StoreToEnvironment): pass
