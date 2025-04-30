import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# Call a constructor, with semantics identical to Call.
# Arg1 is the destination of the return value.
# Arg2 is the closure to invoke.
# Arg3 is the number of arguments, assumed to be found in reverse order
#      from the end of the current frame. The first argument 'this'
#      is assumed to be created with CreateThis.
# DEFINE_OPCODE_3(Construct, Reg8, Reg8, UInt8)
# DEFINE_RET_TARGET(Construct)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest, func, new_target = map(int, match.groups())

        variable = JSVariable(handler, entry.address, f'r{dest}', f"createThis(r{func}, r{new_target});")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Create a closure.
# /// Arg1 is the register in which to store the closure.
# /// Arg2 is the current environment as loaded by GetEnvironment 0.
# /// Arg3 is index in the function table.
# DEFINE_OPCODE_3(CreateClosure, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(CreateClosureLongIndex, Reg8, Reg8, UInt32)
# OPERAND_FUNCTION_ID(CreateClosure, 3)
# OPERAND_FUNCTION_ID(CreateClosureLongIndex, 3)
# Example: <CreateClosure>: <Reg8: 3, Reg8: 1, function_id: 11944>  # Function: [#11944  of 37 bytes]: 1 params @ offset 0x0021917e
# Example: <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 11947>  # Function: [#11947 fetchMovies of 29 bytes]: 2 params @ offset 0x00150430
class CreateClosure(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*function_id:\s*(\d+)', entry.args.strip())
        if not match:
            return self.InvalidArgs(entry)

        dest, env, func_id = map(int, match.groups())

        # Look up the function name from metadataList
        func_name = analysis.functionTable.get(str(func_id), f"function_{func_id}")

        variable = JSVariable(handler, entry.address, f'r{dest}', f"// Closure {func_name} with env r{env}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
