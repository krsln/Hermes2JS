from __future__ import annotations

from typing import cast

from hermes_decompiler.ir.Operators import BinaryOperator, LogicalOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression

# ============================================================================
# Condition negation - shared by IfStructurer and BooleanChainFolder
# ============================================================================

_INVERSE_COMPARISON: dict[BinaryOperator, BinaryOperator] = {
    BinaryOperator.EQUAL: BinaryOperator.NOT_EQUAL,
    BinaryOperator.NOT_EQUAL: BinaryOperator.EQUAL,
    BinaryOperator.STRICT_EQUAL: BinaryOperator.STRICT_NOT_EQUAL,
    BinaryOperator.STRICT_NOT_EQUAL: BinaryOperator.STRICT_EQUAL,
    BinaryOperator.LESS_THAN: BinaryOperator.GREATER_EQUAL,
    BinaryOperator.GREATER_EQUAL: BinaryOperator.LESS_THAN,
    BinaryOperator.LESS_EQUAL: BinaryOperator.GREATER_THAN,
    BinaryOperator.GREATER_THAN: BinaryOperator.LESS_EQUAL,
}

_EQUALITY = frozenset({
    BinaryOperator.EQUAL, BinaryOperator.NOT_EQUAL, BinaryOperator.STRICT_EQUAL, BinaryOperator.STRICT_NOT_EQUAL,
})


def negate_condition(expr: Expression) -> Expression:
    """
    Produce the logical negation of `expr`, preferring a flipped
    comparison operator (`!==` instead of `!(===)`) or unwrapping an
    existing `!` over a generic `UnaryExpression(NOT, expr)` wrap, to
    match how a human would actually write the condition.

    Shared by `IfStructurer` (negating a no-else jump condition) and
    `BooleanChainFolder` (checking whether an `if`'s condition is
    exactly the negation of a preceding assignment's value).
    """

    if isinstance(expr, UnaryExpression) and expr.operator == UnaryOperator.LOGICAL_NOT:
        return expr.operand

    if isinstance(expr, BinaryExpression) and expr.operator in _INVERSE_COMPARISON:
        operator = cast(BinaryOperator, expr.operator)

        return BinaryExpression(left=expr.left, operator=_INVERSE_COMPARISON[operator], right=expr.right)

    return UnaryExpression(UnaryOperator.LOGICAL_NOT, expr)


def negate_for_display(expr: Expression) -> Expression:
    """`negate_condition`, plus De Morgan where it reads better, for a condition that is
    only printed. Passes that COMPARE a negation with another condition keep
    `negate_condition`: a rewritten shape would change what they match."""
    if isinstance(expr, BinaryExpression) and expr.operator in (LogicalOperator.AND, LogicalOperator.OR):
        # Only when some operand negates for free (`!x`, a flipped comparison), so
        # `!(a && !b)` becomes `!a || b` and `!(a && b)` stays as written.
        left, right = negate_for_display(expr.left), negate_for_display(expr.right)

        if _is_free(expr.left, left) or _is_free(expr.right, right):
            flipped = LogicalOperator.OR if expr.operator == LogicalOperator.AND else LogicalOperator.AND

            return BinaryExpression(left=left, operator=flipped, right=right)

    # Equality flips are exact; `!(a < b)` is not `a >= b` for NaN, so an ordering
    # comparison written with a `!` keeps it.
    if isinstance(expr, BinaryExpression) and expr.operator in _INVERSE_COMPARISON and expr.operator not in _EQUALITY:
        return UnaryExpression(UnaryOperator.LOGICAL_NOT, expr)

    return negate_condition(expr)


def _is_free(original: Expression, negated: Expression) -> bool:
    """The negation is not just a `!` put in front of the original."""
    return not (isinstance(negated, UnaryExpression) and negated.operand is original)
