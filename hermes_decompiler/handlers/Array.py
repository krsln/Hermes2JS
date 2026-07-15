import re
import json
from typing import List

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, UINT8, UINT32, UINT16, sequence

# === Patterns ===
NEW_ARRAY_PATTERN = sequence(REG, UINT16)
NEW_ARRAY_WITH_BUFFER_PATTERN = sequence(REG, UINT16, UINT16, UINT16)

# PutOwnByIndex 2 pattern (UInt8 ve UInt32)
PUT_OWN_BY_INDEX_PATTERN = sequence(REG, REG, UINT8)
PUT_OWN_BY_INDEX_L_PATTERN = sequence(REG, REG, UINT32)


# /// Create a new, empty Array with a preallocation size hint.
# /// Arg1 = new Array(); the capacity hint (Arg2) only affects the initial
# /// backing-storage size and has no observable effect on the resulting
# /// value, so it is recorded as a comment rather than emitted as code.
# DEFINE_OPCODE_2(NewArray, Reg8, UInt16)
# Example: <NewArray>: <Reg8: 1, UInt16: 4>
class NewArray(OpcodeHandler):
    """Create a new, empty Array with a preallocation size hint."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = NEW_ARRAY_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and UInt16 arguments")

        dest_reg, capacity_hint = map(int, match.groups())

        js_array = "[]" if capacity_hint == 0 else f"[] /* capacity hint: {capacity_hint} */"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Set an array element by (statically known) numeric index.
# /// Arg1[Arg3] = Arg2. This is an "own" property write on an object already
# /// known to be an array — the counterpart of PutById for indexed access.
# /// PutOwnByIndexL is the long-index (UInt32) variant of the same op.
# DEFINE_OPCODE_3(PutOwnByIndex, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
# Example: <PutOwnByIndex>: <Reg8: 1, Reg8: 2, UInt8: 0>
class PutOwnByIndex(OpcodeHandler):
    """Set an array element by (statically known) numeric index."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Try both UInt8 and UInt32 variants
        match = PUT_OWN_BY_INDEX_PATTERN.match(entry.args.strip()) or \
                PUT_OWN_BY_INDEX_L_PATTERN.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8 and UInt8/UInt32 arguments")

        dest_reg, value_reg, index = map(int, match.groups())

        value = self._get_register_value(analysis, value_reg)
        elements = self._parse_array_elements(
            self.GetVariableByReg(analysis.results, dest_reg), handler, entry
        )

        # Extend array if needed
        if index >= len(elements):
            elements.extend(['undefined'] * (index - len(elements) + 1))

        elements[index] = value

        js_array = "[" + ", ".join(elements) + "]"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _get_register_value(self, analysis: HermesAnalysis, reg: int) -> str:
        var = self.GetVariableByReg(analysis.results, reg)
        return var.value if var and var.value is not None else 'undefined'

    @staticmethod
    def _parse_array_elements(dest_var, handler: str, entry: OpcodeEntry) -> List[str]:
        if not dest_var or not dest_var.value:
            return []

        text = dest_var.value.split(" /* capacity hint:", 1)[0].strip()

        if not (text.startswith('[') and text.endswith(']')):
            logger.warning(
                f"{handler} at {entry.address}: Not a recognizable array literal. Starting fresh."
            )
            return []

        inner = text[1:-1].strip()
        return [part.strip() for part in inner.split(",") if part.strip()]


class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""
    pass   # Artık aynı Handle metodu yeterli


class NewArrayWithBuffer(OpcodeHandler):
    """Create a new array from static buffer."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = NEW_ARRAY_WITH_BUFFER_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        array_str = self._extract_array_from_comment(entry.comment)
        if not array_str:
            return self.Exception(analysis, entry, "// Warning: No array data in comment")

        try:
            clean_str = array_str.replace("'", '"')
            parsed = json.loads(clean_str)
            js_array = json.dumps(parsed, ensure_ascii=False)
        except json.JSONDecodeError as e:
            return self.Exception(analysis, entry, f"// Warning: JSON decode failed: {e}")

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.AddResult(entry, variable)

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