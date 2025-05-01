import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# Get the global object (the object in which global variables are stored).
# DEFINE_OPCODE_1(GetGlobalObject, Reg8)
# Example: <GetGlobalObject>: <Reg8: 2>
class GetGlobalObject(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        """Handle <GetGlobalObject> opcode, tracking the global object register."""
        handler = self.__class__.__name__

        arg_match = re.match(r'Reg8:\s*(\d+)', entry.args.strip())

        if not arg_match:
            return self.InvalidArgs(analysis, entry)

        global_reg = int(arg_match.group(1))
        analysis.globalObjects = global_reg

        variable = JSVariable(handler, entry.address, f'r{global_reg}', f"this")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
