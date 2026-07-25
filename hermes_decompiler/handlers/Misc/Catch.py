from hermes_decompiler.Logger import get_logger
from hermes_decompiler.ir import Identifier
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence

logger = get_logger(__name__)


# DEFINE_OPCODE_1(Catch, Reg8)
# Example: <Catch>: <Reg8: 1>
class Catch(OpcodeHandler):
    """Marks the start of a catch block, binding the caught exception value
    to the destination register."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected a single Reg8 argument")

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", Identifier(name="caughtException"))
        analysis.add_result(entry, variable)

        logger.debug("Catch block starts at %d -> r%d", entry.address, dest_reg)
        # TODO: if/when `analysis` grows structured exception-handler-range
        # tracking (e.g. an `analysis.MarkCatchBlock(...)` API), record it
        # here instead of only logging — replaces the earlier print()/stub.

        return OpcodeResult(entry, variable)