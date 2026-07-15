import re

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

_NEW_ARRAY_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*UInt16:\s*(\d+)$')
_PUT_OWN_BY_INDEX_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*UInt(?:8|32):\s*(\d+)$')


# /// Create a new, empty Array with a preallocation size hint.
# /// Arg1 = new Array(); the capacity hint (Arg2) only affects the initial
# /// backing-storage size and has no observable effect on the resulting
# /// value, so it is recorded as a comment rather than emitted as code.
# DEFINE_OPCODE_2(NewArray, Reg8, UInt16)
# Example: <NewArray>: <Reg8: 1, UInt16: 4>
class NewArray(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _NEW_ARRAY_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and UInt16 arguments")

        dest_reg, capacity_hint = (int(x) for x in match.groups())

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
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _PUT_OWN_BY_INDEX_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8 and UInt8/UInt32 arguments")

        dest_reg, value_reg, index = (int(x) for x in match.groups())

        value_var = self.GetVariableByReg(analysis.results, value_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        dest_var = self.GetVariableByReg(analysis.results, dest_reg)
        elements = self._parse_array_elements(dest_var.value if dest_var else None, handler, entry)

        # Extend with `undefined` placeholders if the index is sparse/ahead
        # of the currently known elements, then set/overwrite the slot.
        if index >= len(elements):
            elements.extend(['undefined'] * (index - len(elements) + 1))
        elements[index] = value

        js_array = "[" + ", ".join(elements) + "]"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _parse_array_elements(current_value, handler: str, entry: OpcodeEntry) -> list:
        """
        Best-effort recovery of the element list from a previously emitted
        array-literal string (e.g. produced by NewArray/NewArrayWithBuffer or
        an earlier PutOwnByIndex). Falls back to an empty list if the prior
        value isn't a recognizable array literal — this mirrors the
        best-effort object-literal mutation approach used by PutById, with
        the same caveat: nested arrays/objects containing top-level commas
        inside strings are not handled by this simple split.
        """
        if not current_value:
            return []

        text = current_value.split(" /* capacity hint:", 1)[0].strip()
        if not (text.startswith('[') and text.endswith(']')):
            logger.warning(
                f"{handler} at address {entry.address}: destination register did not "
                f"contain a recognizable array literal ({current_value!r}); starting fresh"
            )
            return []

        inner = text[1:-1].strip()
        if not inner:
            return []
        return [part.strip() for part in inner.split(",")]


class PutOwnByIndexL(PutOwnByIndex):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)