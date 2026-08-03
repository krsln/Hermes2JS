import re

from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler
from hermes_decompiler.ir.expressions import RegExpLiteral
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, UInt32 (string_id), UInt32 (string_id), UInt32 (total size 13)
# DEFINE_OPCODE_4(CreateRegExp, Reg8, UInt32, UInt32, UInt32)
# Example: <CreateRegExp>: <Reg8: 0, UInt32: 12, UInt32: 13, UInt32: 0>  # String: '^\d+$'  String: 'g'
class CreateRegExp(OpcodeHandler):
    """Create a RegExp literal."""

    _PATTERN = re.compile(
        r'^Reg\d+:\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:UInt32|Reg\d+):\s*(\d+)$'
    )

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            error = "Expected Reg8, (string_id|UInt32), (string_id|UInt32), UInt32"
            return self.build_invalid_args_result(analysis, entry, error)

        dest_reg, pattern_id, flags_id, _ = map(int, match.groups())

        pattern, flags = entry.resolve_pattern_and_flags()

        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (id {pattern_id}) */'
            return self.build_exception_result(analysis, entry, error)

        # expression = f"/{pattern}/{flags or ''}"
        expression = RegExpLiteral(pattern=pattern, flags=flags or "")

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result
