import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


# /// Throw an exception.
# /// throw Arg1;
# DEFINE_OPCODE_1(Throw, Reg8)
# Example: <Throw>: <Reg8: 2>
class Throw(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse the Reg8 argument (e.g., "Reg8: 2")
        match = re.match(r'Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        # Retrieve the value from the register
        value_var = self.GetVariableByReg(analysis.results, dest_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        # Create a JSVariable representing the throw operation
        throw_value = f'throw {value}'
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', throw_value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
