import re

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


# Start the generator by jumping to the next instruction to begin.
# Restore the stack frame if this generator has previously been suspended.
# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if entry.args.strip() not in ('<>', ''):
            return self.InvalidArgs(entry)

        variable = JSVariable(handler, entry.address, "",
                              f"// StartGenerator: prepare generator context and jump to next instruction")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Resume generator by performing one of the following user-requested actions:
# - next(val): Set Arg1 to val, Arg2 to false, run next instruction
# - return(val): Set Arg1 to val, Arg2 to true, run next instruction
# - throw(val): Throw val as an error
# Arg1 is the result provided by the user.
# Arg2 is a boolean which is true if the user requested a return().
# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse args: expect format 'Reg8: dest, Reg8: flag'
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # Generate JavaScript: e.g., 'r0 = await yield;'
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"await yield")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Set the generator status to complete, but do not return.
# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if entry.args.strip() not in ('<>', ''):
            return self.InvalidArgs(entry)

        variable = JSVariable(handler, entry.address, "", f"// CompleteGenerator: No output needed")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Save the provided value, yield, and signal the VM to restart execution at the provided target.
# Example: <SaveGenerator>: <Addr8: 4>  # Address: 00000095
class SaveGenerator(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = re.match(r'Addr8:\s*(\d+)', entry.args.strip())

        if not match:
            return self.InvalidArgs(entry)

        addr = int(match.group(1))
        label = f"label_{addr}"
        analysis.gotoList.append(addr)  # TODO: ??

        variable = JSVariable(handler, entry.address, "",
                              f'yield {label};  // SaveGenerator: suspend and jump to {addr}')
        analysis.AddResult(entry, variable, goto=addr)

        return OpcodeResult(entry, variable, goto=addr)
