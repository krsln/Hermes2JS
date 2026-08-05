import re

from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler
from hermes_decompiler.ir.expressions import RawExpression
from hermes_decompiler.runtime import HermesAnalysis


# (total size 0)
# DEFINE_OPCODE_0(CompleteGenerator)
# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Set the generator status to complete, but do not return."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        if not self._PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        expression = RawExpression(source="// CompleteGenerator")

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
