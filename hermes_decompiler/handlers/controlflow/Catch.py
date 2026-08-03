from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.handlers import OpcodeHandler, REG, sequence
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis

logger = get_logger(__name__)


# Reg8 (total size 1)
# DEFINE_OPCODE_1(Catch, Reg8)
# Example: <Catch>: <Reg8: 12>
class Catch(OpcodeHandler):
    """Marks the start of a catch block, binding the caught exception value
    to the destination register."""

    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected a single Reg8 argument")

        dest_reg = int(match.group(1))

        expression = Identifier(name="caughtException")

        logger.debug("Catch block starts at %d -> r%d", entry.address, dest_reg)
        # TODO: if/when `analysis` grows structured exception-handler-range
        # tracking (e.g. an `analysis.MarkCatchBlock(...)` API), record it
        # here instead of only logging — replaces the earlier print()/stub.

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
