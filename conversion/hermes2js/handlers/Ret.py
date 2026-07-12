import re

from conversion.hermes2js.models.HermesAnalysis import HermesAnalysis
from conversion.hermes2js.models.OpcodeResult import OpcodeResult
from conversion.hermes2js.models.JSVariable import JSVariable
from conversion.hermes2js.models.OpcodeEntry import OpcodeEntry
from conversion.hermes2js.models.OpcodeHandler import OpcodeHandler

# /// Return a value from the current function.
# /// return Arg1;
# DEFINE_OPCODE_1(Ret, Reg8)
# Example: <Ret>: <Reg8: 1>
class Ret(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        """Handle <Ret> opcode, returning the value from the specified register or performing the return action."""
        handler = self.__class__.__name__

        # Check if the line contains specific return arguments.
        arg_match = re.match(r'Reg8:\s*(\d+)', entry.args.strip())
        if arg_match:
            obj_reg = int(arg_match.group(1))  # Get the register

            obj_val = self.GetValueByReg(analysis.results, obj_reg)
            # print(obj_reg, obj_val)

            variable = JSVariable(handler, entry.address, '', f"return {obj_val};")
            analysis.AddResult(entry, variable)

            return OpcodeResult(entry, variable)  # Return the value in that register
        else:
            variable = JSVariable(handler, entry.address, '', f"return;")  # If no arguments, just return with no value
            analysis.AddResult(entry, variable)

            return OpcodeResult(entry, variable)
