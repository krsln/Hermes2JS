"""
The test of a `? :` is printed without parentheses of its own when it is a comparison or a logical
expression (F-32): `a == null ? x : y`, not `(a == null) ? x : y`. A ternary, an assignment or a sequence
as the test, and a ternary used as an operand, keep their grouping.
"""

from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.ir.expressions import (
    BinaryExpression, ConditionalExpression, Identifier, NullLiteral, UndefinedLiteral,
)
from hermes_decompiler.ir.expressions.Operations import LogicalOperator


def _print(node) -> str:
    return ExpressionPrinter().print(node)


def _ident(name):
    return Identifier(name=name)


def test_a_comparison_test_has_no_parentheses():
    test = BinaryExpression(left=_ident("a"), operator="==", right=NullLiteral())
    node = ConditionalExpression(test=test, consequent=UndefinedLiteral(), alternate=_ident("b"))

    assert _print(node) == "a == null ? undefined : b"


def test_a_logical_test_has_no_parentheses():
    test = BinaryExpression(left=_ident("a"), operator=LogicalOperator.AND, right=_ident("b"))
    node = ConditionalExpression(test=test, consequent=_ident("x"), alternate=_ident("y"))

    assert _print(node) == "a && b ? x : y"


def test_a_ternary_test_keeps_its_parentheses():
    inner = ConditionalExpression(test=_ident("a"), consequent=_ident("b"), alternate=_ident("c"))
    node = ConditionalExpression(test=inner, consequent=_ident("x"), alternate=_ident("y"))

    assert _print(node) == "(a ? b : c) ? x : y"


def test_a_ternary_as_an_operand_keeps_its_parentheses():
    inner = ConditionalExpression(test=_ident("a"), consequent=_ident("b"), alternate=_ident("c"))
    node = BinaryExpression(left=inner, operator="===", right=_ident("d"))

    assert _print(node) == "(a ? b : c) === d"
