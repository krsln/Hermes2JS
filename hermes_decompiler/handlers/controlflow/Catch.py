from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.ir.expressions import Identifier

logger = get_logger(__name__)


# Reg8 (total size 1)
# DEFINE_OPCODE_1(Catch, Reg8)
# Example: <Catch>: <Reg8: 12>
class Catch(OpcodeHandler):
    """Marks the start of a catch block, binding the caught exception value
    to the destination register."""

    ARGUMENTS = ArgsPattern(sequence(REG), "Reg8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg = int(match.group(1))

        expression = Identifier(name="caughtException")

        logger.debug("Catch block starts at %d -> r%d", ctx.entry.address, dest_reg)
        # TODO: if/when `analysis` grows structured exception-handler-range
        # tracking (e.g. an `analysis.MarkCatchBlock(...)` API), record it
        # here instead of only logging — replaces the earlier print()/stub.

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
