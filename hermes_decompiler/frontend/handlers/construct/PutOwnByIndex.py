from hermes_decompiler.frontend.opcode import OpcodeResult
from frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    AssignmentExpression,
    MemberExpression,
    NumericLiteral,
    UndefinedLiteral,
)


# Reg8, Reg8, UInt8 (total size 3)
# DEFINE_OPCODE_3(PutOwnByIndex, Reg8, Reg8, UInt8)
# Example: <PutOwnByIndex>: <Reg8: 0, Reg8: 2, UInt8: 2>
class PutOwnByIndex(OpcodeHandler):
    """Set an array element by (statically known) numeric index."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT8), "Reg8, Reg8, UInt8")

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:
        match = self.match_arguments(ctx)
        if isinstance(match, OpcodeResult):
            return match

        dest_reg, value_reg, index = map(int, match.groups())

        value = self.get_register_expression(ctx.analysis, value_reg)
        array = self.get_register_expression(ctx.analysis, dest_reg)

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
                left=MemberExpression(obj=array, prop=NumericLiteral(index), computed=True),
                operator=AssignmentOperator.ASSIGN,
                right=value,
            )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=dest_reg)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32")
