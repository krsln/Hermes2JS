import re

from hermes2js.models.HermesAnalysis import HermesAnalysis
from hermes2js.models.OpcodeResult import OpcodeResult
from hermes2js.models.JSVariable import JSVariable
from hermes2js.models.OpcodeEntry import OpcodeEntry
from hermes2js.models.OpcodeHandler import OpcodeHandler

# /// Create an actual 'arguments' array, if get-by-index and length isn't enough.
# /// Arg1 is the lazy loaded register, which afterwards will contain a proper
# ///      object that can be used by non-*Arguments* opcodes like Return.
# DEFINE_OPCODE_1(ReifyArguments, Reg8)
# Example: <ReifyArguments>: <Reg8: 0>
class ReifyArguments(OpcodeHandler):

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: expecting "Reg8: X"
        match = re.match(r'^Reg8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        # Extract destination register
        dest_reg = int(match.group(1))

        # Create JSVariable for the arguments object
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'arguments')
        analysis.AddResult(entry, variable)

        # Optionally, mark the creation of the argument object in analysis.
        # analysis.MarkArgumentsObject(entry.address, dest_reg)
        print("MarkArgumentsObject", entry.address, dest_reg)

        return OpcodeResult(entry, variable)
