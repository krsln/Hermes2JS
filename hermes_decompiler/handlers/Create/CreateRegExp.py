import re

from hermes_decompiler.Logger import logger
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

        dest_reg = int(match.group(1))
        pattern_id = int(match.group(2))
        flags_id = int(match.group(3))

        pattern, flags = self._resolve_pattern_and_flags(analysis, entry, pattern_id, flags_id)

        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (id {pattern_id}) */'
            return self.build_exception_result(analysis, entry, error)

        js_regex = f"/{pattern}/{flags or ''}"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_regex)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _resolve_pattern_and_flags(analysis: HermesAnalysis, entry: OpcodeEntry,
                                   pattern_id: int, flags_id: int):
        """Prefer comment, fallback to stringTable."""
        comment_matches = re.findall(r"String:\s*'([^']*)'", entry.comment or "")
        if len(comment_matches) >= 2:
            return comment_matches[0], comment_matches[1]

        pattern = analysis.stringTable.get(str(pattern_id))
        flags = analysis.stringTable.get(str(flags_id))

        if pattern is None:
            logger.warning(f"CreateRegExp at {entry.address}: unresolved pattern id {pattern_id}")

        return pattern, flags
