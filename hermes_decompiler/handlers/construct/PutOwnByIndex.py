from hermes_decompiler.handlers import OpcodeHandler, REG, UINT8, UINT32, sequence
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    AssignmentExpression,
    MemberExpression,
    NumericLiteral,
    UndefinedLiteral,
)
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(PutOwnByIndex, Reg8, Reg8, UInt8)
# Example: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 2>
class PutOwnByIndex(OpcodeHandler):
    """Set an array element by (statically known) numeric index."""

    _PATTERN = sequence(REG, REG, UINT8)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        # Try both UInt8 and UInt32 variants
        match = self._PATTERN.match(entry.args.strip())  # or  self._PATTERN_LONG.match(entry.args.strip())

        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, Reg8 and UInt8/UInt32 arguments")

        dest_reg, value_reg, index = map(int, match.groups())

        value = self.get_register_expression(analysis, value_reg)
        array = self.get_register_expression(analysis, dest_reg)

        if isinstance(array, ArrayExpression):
            # ArrayExpression is frozen/immutable: pad-and-replace has to
            # build a new tuple rather than mutate `array.elements`.
            elements = list(array.elements)

            while len(elements) <= index:
                elements.append(UndefinedLiteral())

            elements[index] = value

            expression = ArrayExpression(elements=tuple(elements))
        else:
            expression = AssignmentExpression(
                left=MemberExpression(
                    receiver=array,
                    member=NumericLiteral(index),
                    computed=True,
                ),
                operator=AssignmentOperator.ASSIGN,
                right=value,
            )

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""

    _PATTERN = sequence(REG, REG, UINT32)
