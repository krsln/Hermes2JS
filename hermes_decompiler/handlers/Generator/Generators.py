import re

from hermes_decompiler.ir.Values import CommentValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, ADDR, sequence

# Pre-compiled patterns
START_GENERATOR_PATTERN = re.compile(r'^(?:<>)?$')


# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        value = CommentValue(value=f"// StartGenerator")
        variable = JSVariable(handler, entry.address, "", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    """Resume a suspended generator."""
    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # value = f"await yield"
        value = CommentValue(f"await yield /* ResumeGenerator -> r{dest_reg} */")
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Mark the generator as completed."""

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        if not START_GENERATOR_PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        value = CommentValue(value=f"// CompleteGenerator")
        variable = JSVariable(handler, entry.address, "", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <SaveGenerator>: <Addr8: 4>  # Address: 00000095
class SaveGenerator(OpcodeHandler):
    """Save generator state and yield."""
    _PATTERN = sequence(ADDR)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        offset = int(match.group(1))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        # value = f'yield label_{target};  // SaveGenerator: suspend and jump to {target}'
        # value = CommentValue(value=f'yield label_{target}; // SaveGenerator: suspend and jump to {target}')
        value = CommentValue(f"yield label_{target};")
        variable = JSVariable(handler, entry.address, "", value)
        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)
