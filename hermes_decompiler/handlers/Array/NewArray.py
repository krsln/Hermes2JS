import re
import json

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT16, sequence


# DEFINE_OPCODE_2(NewArray, Reg8, UInt16)
# Example: <NewArray>: <Reg8: 1, UInt16: 4>
class NewArray(OpcodeHandler):
    """Create a new, empty Array with a preallocation size hint."""
    _PATTERN = sequence(REG, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8 and UInt16 arguments")

        dest_reg, capacity_hint = map(int, match.groups())

        js_array = "[]" if capacity_hint == 0 else f"[] /* capacity hint: {capacity_hint} */"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class NewArrayWithBuffer(OpcodeHandler):
    """Create a new array from a static buffer."""
    _PATTERN = sequence(REG, UINT16, UINT16, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        array_str = self._extract_array_from_comment(entry.comment)
        if not array_str:
            return self.build_exception_result(analysis, entry, "// Warning: No array data in comment")

        try:
            clean_str = array_str.replace("'", '"')
            parsed = json.loads(clean_str)
            js_array = json.dumps(parsed, ensure_ascii=False)
        except json.JSONDecodeError as e:
            return self.build_exception_result(analysis, entry, f"// Warning: JSON decode failed: {e}")

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _extract_array_from_comment(comment: str) -> str:
        if not comment:
            return ""
        match = re.search(r'Array:\s*(\[.*?])', comment, re.DOTALL)
        return match.group(1) if match else ""


class NewArrayWithBufferLong(NewArrayWithBuffer):
    """Long variant."""
    pass
