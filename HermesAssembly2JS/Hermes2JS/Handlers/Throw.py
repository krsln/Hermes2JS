import json
import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


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
            return self.InvalidArgs(entry)

        dest_reg = int(match.group(1))

        # Retrieve the value from the register
        value_var = self.GetVariableByReg(analysis.results, dest_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        # Create a JSVariable representing the throw operation
        throw_value = f'throw {value}'
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', throw_value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
