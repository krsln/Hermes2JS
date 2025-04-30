import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# CreateEnvironment
# CreateInnerEnvironment
# LoadFromEnvironment
# LoadFromEnvironmentL
# StoreNPToEnvironment
# StoreNPToEnvironmentL
# StoreToEnvironment
# StoreToEnvironmentL

# /// Create a new environment, to store values captured by closures.
# DEFINE_OPCODE_1(CreateEnvironment, Reg8)
# Example: <CreateEnvironment>: <Reg8: 1>
class CreateEnvironment(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Match: "Reg8: x"
        match = re.match(r'^Reg8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(entry, "Expected single Reg8 argument")

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"// Create new environment")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Get an environment (scope) from N levels up the stack.
# /// 0 is the current environment, 1 is the caller's environment, etc.
# DEFINE_OPCODE_2(GetEnvironment, Reg8, UInt8)
# Example: <GetEnvironment>: <Reg8: 1, UInt8: 4>
class GetEnvironment(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # This matches "Reg8: x, UInt8: y" with optional whitespace
        match = re.match(r'^Reg8:\s*(\d+),\s*UInt8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(entry, "Expected Reg8 and UInt8 arguments")

        dest_reg, env_index = [int(x) for x in match.groups()]

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"getEnvironment({env_index});")
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
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'^Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*UInt8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(entry, "Expected two Reg8 and one UInt8 arguments")

        dest_reg, env_reg, index = [int(x) for x in match.groups()]
        env_value = self.GetValueByReg(analysis.results, env_reg)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{env_value}[{index}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class LoadFromEnvironmentL(LoadFromEnvironment):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


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
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return self._handle_store_env(analysis, entry)

    def _handle_store_env(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__
        args = entry.args.strip()

        # Try to match both UInt8 and UInt16 formats
        match = re.match(r'^Reg8:\s*(\d+),\s*UInt(?:8|16):\s*(\d+),\s*Reg8:\s*(\d+)$', args)
        if not match:
            return self.InvalidArgs(entry, "Expected Reg8, UInt(8|16), Reg8 format")

        env_reg, index, value_reg = [int(x) for x in match.groups()]

        comment = f"{handler}: env=r{env_reg}, slot={index}, value=r{value_reg}"
        variable = JSVariable(handler, entry.address, f'r{env_reg}', f'setEnvSlot({index}, r{value_reg})  // {comment}')
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class StoreToEnvironmentL(StoreToEnvironment): pass


class StoreNPToEnvironment(StoreToEnvironment): pass


class StoreNPToEnvironmentL(StoreToEnvironment): pass
