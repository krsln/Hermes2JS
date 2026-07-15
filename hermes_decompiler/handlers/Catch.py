from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, sequence


# /// Catch an exception (the first instruction in an exception handler).
# /// } catch(Arg1) {
# DEFINE_OPCODE_1(Catch, Reg8)
# Example: <Catch>: <Reg8: 1>
class Catch(OpcodeHandler):
    """Marks the start of a catch block, binding the caught exception value
    to the destination register."""
    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: expecting "Reg8: X"
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected a single Reg8 argument")

        # Extract destination register
        dest_reg = int(match.group(1))

        # Create JSVariable for the caught exception
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', 'caughtException')
        analysis.AddResult(entry, variable)

        logger.debug(f"{handler}: catch block starts at address {entry.address}, binds r{dest_reg}")
        # TODO: if/when `analysis` grows structured exception-handler-range
        # tracking (e.g. an `analysis.MarkCatchBlock(...)` API), record it
        # here instead of only logging — replaces the earlier print()/stub.

        return OpcodeResult(entry, variable)
