from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
from hermes_decompiler.frontend.handlers.shared import fold_into_literal
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    AssignmentExpression,
    MemberExpression,
    NumericLiteral,
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

        # Resolve the element first: inlining it marks its own definition as
        # folded, which the "nothing else happened since" check below relies on.
        value = self.get_register_expression(ctx.analysis, value_reg)

        # `NewArray` + element stores -> one literal. A gap (index past the
        # end) would be a hole, not `undefined`, so only the next free index
        # extends it.
        folded = fold_into_literal(
            ctx, dest_reg, ArrayExpression,
            lambda array: (
                ArrayExpression(elements=array.elements + (value,))
                if index == len(array.elements) else None
            ),
        )

        if folded is not None:
            return folded

        # Not foldable: a plain statement, `arr[i] = value`. It must NOT
        # define `dest_reg` - the assignment's VALUE is the element, not the
        # array, so publishing it as `rN = (rN[0] = a)[1] = b` made rN hold
        # the last element (`"Woof"`) instead of the array.
        array = self.get_register_expression(ctx.analysis, dest_reg)

        expression = AssignmentExpression(
            left=MemberExpression(obj=array, prop=NumericLiteral(index), computed=True),
            operator=AssignmentOperator.ASSIGN,
            right=value,
        )

        result = OpcodeResult(ctx.entry, value=expression, dest_reg=None)
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32")
