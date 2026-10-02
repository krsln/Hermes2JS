from hermes_decompiler.frontend.handlers import OpcodeHandler, OpcodeContext, ArgsPattern, sequence, REG, UINT8, UINT32
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

        folded = self._fold_into_array_literal(ctx, dest_reg, index, value)

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

    @staticmethod
    def _fold_into_array_literal(ctx: OpcodeContext, dest_reg: int, index: int, value) -> OpcodeResult | None:
        """`NewArray rN` + `PutOwnByIndex rN, v, i` ... -> `rN = [v0, v1, ...]`.

        Only when that is exactly equivalent:

        - the register still holds the array literal being built, which no
          one has read, pinned or folded away yet (so nothing observed the
          intermediate array);
        - the element goes at the next free index (a gap would be a hole,
          not `undefined`);
        - since the literal was created nothing else happened - no
          control flow and no printed statement - so evaluating the element
          here instead of at the original `Put` position reorders nothing.

        The previous definition's statement is suppressed; the new one
        (printed where this `Put` is) carries the longer literal.
        """
        state = ctx.analysis.get_register_state(dest_reg)

        if state is None or not isinstance(state.value, ArrayExpression):
            return None

        previous = state.definition

        if state.reads != 0 or previous.definition_pinned or previous.definition_used:
            return None

        if index != len(state.value.elements):
            return None

        results = ctx.analysis.results
        start = next((i for i in range(len(results) - 1, -1, -1) if results[i] is previous), None)

        if start is None:
            return None

        for later in results[start + 1:]:
            if later.terminator is not None or not later.definition_used:
                return None

        previous.definition_used = True

        result = OpcodeResult(
            ctx.entry,
            value=ArrayExpression(elements=state.value.elements + (value,)),
            dest_reg=dest_reg,
        )
        ctx.analysis.add_result(result)

        return result


# Reg8, Reg8, UInt32 (total size 6)
# DEFINE_OPCODE_3(PutOwnByIndexL, Reg8, Reg8, UInt32)
class PutOwnByIndexL(PutOwnByIndex):
    """Long index variant (UInt32)."""

    ARGUMENTS = ArgsPattern(sequence(REG, REG, UINT32), "Reg8, Reg8, UInt32")
