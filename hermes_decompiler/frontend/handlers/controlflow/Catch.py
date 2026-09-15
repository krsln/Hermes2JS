from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG
from hermes_decompiler.frontend.opcode import OpcodeResult
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
        # Note: structured exception-handler-range tracking already exists
        # and doesn't need to be added here. It comes from the bytecode's
        # own exception-handler table (FunctionMetadataParser.parse_exception_handlers
        # -> MetadataStage -> CFG.from_results), which CFGBuilder resolves
        # into `cfg.exception_handlers` and try_structurer consumes directly.
        # This per-instruction debug log is just IR-emission-time diagnostics
        # for this one Catch opcode (which register got the caught value) -
        # unrelated to that range-based analysis.

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result
