from typing import List

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT32, UINT16, sequence


# /// Set an array element by (statically known) numeric index.
# /// Arg1[Arg3] = Arg2. This is an "own" property write on an object already
# /// known to be an array — the counterpart of PutById for indexed access.
# /// PutOwnByIndexL is the long-index (UInt32) variant of the same op.
# DEFINE_OPCODE_3(PutOwnByIndex, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
# Example: <PutOwnByIndex>: <Reg8: 1, Reg8: 2, UInt8: 0>
class PutOwnByIndex(OpcodeHandler):
    """Set an array element by (statically known) numeric index."""
    # PutOwnByIndex 2 pattern (UInt8 ve UInt32)
    _PATTERN = sequence(REG, REG, UINT8)
    _PATTERN_LONG = sequence(REG, REG, UINT32)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Try both UInt8 and UInt32 variants
        match = self._PATTERN.match(entry.args.strip()) or \
                self._PATTERN_LONG.match(entry.args.strip())

        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8, Reg8 and UInt8/UInt32 arguments")

        dest_reg, value_reg, index = map(int, match.groups())

        value = self._get_register_value(analysis, value_reg)
        elements = self._parse_array_elements(
            self.GetVariableByReg(analysis, dest_reg), handler, entry
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
        var = self.GetVariableByReg(analysis, reg)
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
    pass
