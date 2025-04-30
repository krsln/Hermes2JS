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
