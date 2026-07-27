import re

from hermes_decompiler.handlers import OpcodeHandler
from hermes_decompiler.ir.expressions import RawExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        if not self._PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        # No JS-observable effect of its own; kept as a bare comment
        # marker via RawExpression, same as before.
        expression = RawExpression(source="// StartGenerator")

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
