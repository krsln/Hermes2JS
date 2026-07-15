import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


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
