from __future__ import annotations

from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression

# ============================================================================
# Condition negation - shared by IfStructurer and BooleanChainFolder
# ============================================================================

_INVERSE_COMPARISON = {
    BinaryOperator.EQUAL: BinaryOperator.NOT_EQUAL,
    BinaryOperator.NOT_EQUAL: BinaryOperator.EQUAL,
    BinaryOperator.STRICT_EQUAL: BinaryOperator.STRICT_NOT_EQUAL,
    BinaryOperator.STRICT_NOT_EQUAL: BinaryOperator.STRICT_EQUAL,
    BinaryOperator.LESS_THAN: BinaryOperator.GREATER_EQUAL,
    BinaryOperator.GREATER_EQUAL: BinaryOperator.LESS_THAN,
    BinaryOperator.LESS_EQUAL: BinaryOperator.GREATER_THAN,
    BinaryOperator.GREATER_THAN: BinaryOperator.LESS_EQUAL,
}


def _negate_condition(expr: Expression) -> Expression:
    """
    Produce the logical negation of `expr`, preferring a flipped
    comparison operator (`!==` instead of `!(=== )`) or unwrapping an
    existing `!` over a generic `UnaryExpression(NOT, expr)` wrap, to
    match how a human would actually write the condition.

    Shared by `IfStructurer` (negating a no-else jump condition) and
    `BooleanChainFolder` (checking whether an `if`'s condition is
    exactly the negation of a preceding assignment's value).
    """

    if isinstance(expr, UnaryExpression) and expr.operator == UnaryOperator.LOGICAL_NOT:
        return expr.operand

    if isinstance(expr, BinaryExpression) and expr.operator in _INVERSE_COMPARISON:
        return BinaryExpression(
            left=expr.left,
            operator=_INVERSE_COMPARISON[expr.operator],
            right=expr.right,
        )

    return UnaryExpression(UnaryOperator.LOGICAL_NOT, expr)


