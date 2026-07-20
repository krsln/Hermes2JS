from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, UINT32, sequence


# DEFINE_OPCODE_3(PutOwnByIndex, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
class PutOwnByIndex(OpcodeHandler):
    """Set an array element by (statically known) numeric index."""
    # PutOwnByIndex 2 pattern (UInt8 ve UInt32)
    _PATTERN = sequence(REG, REG, UINT8)
    _PATTERN_LONG = sequence(REG, REG, UINT32)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Try both UInt8 and UInt32 variants
        match = self._PATTERN.match(entry.args.strip()) or \
                self._PATTERN_LONG.match(entry.args.strip())

        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 and UInt8/UInt32 arguments")

        dest_reg, value_reg, index = map(int, match.groups())

        reg_var = self.get_register_variable(analysis, value_reg)
        reg_value = reg_var.value if reg_var and reg_var.value is not None else 'undefined'

        elements = self._parse_array_elements(self.get_register_variable(analysis, dest_reg), handler, entry)

        # Extend array if needed
        if index >= len(elements):
            elements.extend(['undefined'] * (index - len(elements) + 1))

        elements[index] = reg_value

        js_array = "[" + ", ".join(elements) + "]"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_array)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _parse_array_elements(dest_var: JSVariable | None, handler: str, entry: OpcodeEntry) -> list[str]:
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
