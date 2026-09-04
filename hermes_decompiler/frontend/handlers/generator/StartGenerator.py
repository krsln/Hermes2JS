import re

from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers.OpcodeHandler import OpcodeHandler, OpcodeContext, ArgsPattern
from hermes_decompiler.ir.expressions import RawExpression


# (total size 0)
# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    ARGUMENTS = ArgsPattern(re.compile(r'^(?:<>)?$'), "<>")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        # No JS-observable effect of its own; kept as a bare comment
        # marker via RawExpression, same as before.
        expression = RawExpression(source="// StartGenerator")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
