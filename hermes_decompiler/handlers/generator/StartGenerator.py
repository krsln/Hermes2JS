import re

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers.OpcodeHandler import OpcodeHandler, OpcodeContext
from hermes_decompiler.ir.expressions import RawExpression


# (total size 0)
# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        # No JS-observable effect of its own; kept as a bare comment
        # marker via RawExpression, same as before.
        expression = RawExpression(source="// StartGenerator")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
