from hermes_decompiler.ir.Expressions import AssignmentExpression, IndexExpression
from hermes_decompiler.ir.Values import ArrayValue, UndefinedValue, ConstantValue
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

        value = self.get_register_value(analysis, value_reg)
        array = self.get_register_value(analysis, dest_reg)

        if isinstance(array, ArrayValue):
            old = list(array.elements)

            while len(old) <= index:
                old.append(UndefinedValue())

            old[index] = value
            result = ArrayValue(old)
        else:
            result = AssignmentExpression(
                left=IndexExpression(
                    object=array,
                    index=ConstantValue(index),
                ),
                operator="=",
                right=value
            )

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', result)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""
    pass
