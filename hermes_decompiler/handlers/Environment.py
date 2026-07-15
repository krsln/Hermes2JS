import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, UINT8, UINT16, sequence


# /// Create a new environment to store values captured by closures.
# DEFINE_OPCODE_1(CreateEnvironment, Reg8)
# Example: <CreateEnvironment>: <Reg8: 1>
class CreateEnvironment(OpcodeHandler):
    """Create a new lexical environment for closures."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', "createEnvironment()")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Get an environment (scope) from N levels up the stack.
# /// 0 is the current environment, 1 is the caller's environment, etc.
# DEFINE_OPCODE_2(GetEnvironment, Reg8, UInt8)
# Example: <GetEnvironment>: <Reg8: 1, UInt8: 4>
class GetEnvironment(OpcodeHandler):
    """Get environment from N levels up the scope chain."""
    _PATTERN = sequence(REG, UINT8)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, UInt8 arguments")

        dest_reg, env_level = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"getEnvironment({env_level})")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


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

        env_value = self.GetValueByReg(analysis.results, env_reg) or f"r{env_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{env_value}[{slot}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadFromEnvironmentL(LoadFromEnvironment):
    """Long index variant."""
    _PATTERN = sequence(REG, REG, UINT16)
    pass


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
