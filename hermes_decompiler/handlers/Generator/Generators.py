import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, FUNCTION_ID, ADDR, sequence

# Pre-compiled patterns
START_GENERATOR_PATTERN = re.compile(r'^(?:<>)?$')


# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.InvalidArgs(analysis, entry)

        variable = JSVariable(handler, entry.address, "",
                              f"// StartGenerator: prepare generator context and jump to next instruction")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    """Resume a suspended generator."""
    _PATTERN = sequence(REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # Generate JavaScript: e.g., 'r0 = await yield;'
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"await yield")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Mark generator as completed."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.InvalidArgs(analysis, entry)

        variable = JSVariable(handler, entry.address, "", f"// CompleteGenerator: No output needed")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <SaveGenerator>: <Addr8: 4>  # Address: 00000095
class SaveGenerator(OpcodeHandler):
    """Save generator state and yield."""
    _PATTERN = sequence(ADDR)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        addr = int(match.group(1))
        label = f"label_{addr}"
        analysis.gotoList.append(addr)  # TODO: ??

        variable = JSVariable(handler, entry.address, "",
                              f'yield {label};  // SaveGenerator: suspend and jump to {addr}')
        analysis.AddResult(entry, variable, goto=addr)

        return OpcodeResult(entry, variable, goto=addr)
