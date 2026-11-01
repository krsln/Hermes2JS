"""
A `!` over `&&`/`||` is printed as its De Morgan form when the operands negate
cleanly (`!(a !== b && c === d)` -> `a === b || c !== d`). The parent of such a
node has to group it by the form that is actually printed, not by the `!` it was
built as. Before, a flipped `||` under `&&` lost its parentheses, which changed
the value (98/9594, F-02):

    !!((A && B) || C)  printed  !(P || Q) && R       (not the same value)
    !(A && B) && C     printed  P || Q && C          (`&&` binds tighter)
"""

import pytest

from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Identifier, UnaryExpression

_x, _y, _z = Identifier("x"), Identifier("y"), Identifier("z")


def _not(expression):
    return UnaryExpression(UnaryOperator.LOGICAL_NOT, expression)


def _eq(left, right):
    return BinaryExpression(left, BinaryOperator.STRICT_EQUAL, right)


def _ne(left, right):
    return BinaryExpression(left, BinaryOperator.STRICT_NOT_EQUAL, right)


def _and(left, right):
    return BinaryExpression(left, LogicalOperator.AND, right)


def _or(left, right):
    return BinaryExpression(left, LogicalOperator.OR, right)


_A, _B, _C = _eq(_x, _y), _ne(_x, _z), _eq(_y, _z)


def _print(expression) -> str:
    return ExpressionPrinter().visit(expression)


def test_the_flipped_form_alone_has_no_parentheses():
    assert _print(_not(_and(_A, _B))) == "x !== y || x === z"


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        # `||` (flipped from `!(&&)`) as the left operand of `&&`
        (_and(_not(_and(_A, _B)), _C), "(x !== y || x === z) && y === z"),
        # ... and as the right one
        (_and(_C, _not(_and(_A, _B))), "y === z && (x !== y || x === z)"),
        # `&&` (flipped from `!(||)`) under `||` needs none: `&&` binds tighter
        (_or(_not(_or(_A, _B)), _C), "x !== y && x === z || y === z"),
        # `||` as the left operand of `||` needs none; as the right one it keeps the
        # printer's usual grouping of an equal-precedence right operand
        (_or(_not(_and(_A, _B)), _C), "x !== y || x === z || y === z"),
        (_or(_C, _not(_and(_A, _B))), "y === z || (x !== y || x === z)"),
    ],
)
def test_a_flipped_negation_is_grouped_by_its_printed_form(expression, expected):
    assert _print(expression) == expected


def test_double_negation_keeps_the_value():
    """`!!((A && B) || C)`: the inner `!` flips to `(P || Q) && R`; the outer one
    must negate all of it."""
    expression = _not(_not(_or(_and(_A, _B), _C)))

    assert _print(expression) == "!((x !== y || x === z) && y !== z)"


def test_a_negation_that_does_not_flip_keeps_its_parentheses():
    a, b = Identifier("a"), Identifier("b")

    assert _print(_not(_and(a, b))) == "!(a && b)"
    assert _print(_and(_not(_and(a, b)), Identifier("c"))) == "!(a && b) && c"
