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

# Get an environment (scope) from N levels up the stack.
# 0 is the current environment, 1 is the caller's environment, etc.
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


# Load a value from an environment.
# Arg1 is the destination.
# Arg2 is the environment (as fetched by GetEnvironment).
# Arg3 is the environment index slot number.
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
