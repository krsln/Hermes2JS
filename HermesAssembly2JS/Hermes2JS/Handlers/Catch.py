import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# /// Catch an exception (the first instruction in an exception handler).
# /// } catch(Arg1) {
# DEFINE_OPCODE_1(Catch, Reg8)
# Example: <Catch>: <Reg8: 1>
class Catch(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: expecting "Reg8: X"
        match = re.match(r'^Reg8:\s*(\d+)$', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 argument")

        # Extract destination register
        dest_reg = int(match.group(1))

        # Create JSVariable for the caught exception
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'caughtException')
        analysis.AddResult(entry, variable)

        # Optionally, mark the start of a catch block in analysis
        # analysis.MarkCatchBlock(entry.address, dest_reg)
        print("MarkCatchBlock", entry.address, dest_reg)

        return OpcodeResult(entry, variable)