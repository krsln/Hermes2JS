import re

from hermes_decompiler.ir.Values import RegExpValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


# DEFINE_OPCODE_4(CreateRegExp, Reg8, UInt32, UInt32, UInt32)
# Example: <CreateRegExp>: <Reg8: 0, UInt32: 12, UInt32: 13, UInt32: 0>  # String: '^\d+$'  String: 'g'
class CreateRegExp(OpcodeHandler):
    """Create a RegExp literal."""
    _PATTERN = re.compile(
        r'^Reg\d+:\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:string_id|UInt32):\s*(\d+),\s*(?:UInt32|Reg\d+):\s*(\d+)$'
    )

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry,
                "Expected Reg8, (string_id|UInt32), (string_id|UInt32), UInt32"
            )

        dest_reg, pattern_id, flags_id, _ = map(int, match.groups())

        pattern, flags = entry.resolve_pattern_and_flags()

        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (id {pattern_id}) */'
            return self.build_exception_result(analysis, entry, error)

        # value = f"/{pattern}/{flags or ''}"
        value = RegExpValue(pattern=pattern, flags=flags or "")

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
