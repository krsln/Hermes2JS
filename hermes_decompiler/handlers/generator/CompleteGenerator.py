import re

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext
from hermes_decompiler.ir.expressions import RawExpression


# (total size 0)
# DEFINE_OPCODE_0(CompleteGenerator)
# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Set the generator status to complete, but do not return."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        expression = RawExpression(source="// CompleteGenerator")

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result
