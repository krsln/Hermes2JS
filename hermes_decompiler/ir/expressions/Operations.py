from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.Operators import (
    AssignmentOperator,
    BinaryOperator,
    LogicalOperator,
    UnaryOperator,
    UpdateOperator,
)
from ._Base import Expression

__all__ = [
    "UnaryExpression",
    "UpdateExpression",
    "BinaryExpression",
    "AssignmentExpression",
    "ConditionalExpression",
    "SequenceExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class UnaryExpression(Expression):
    """
    Unary operation.

    Example:
        !value
    """

    operator: UnaryOperator
    operand: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.operand,)


@dataclass(frozen=True, slots=True, eq=False)
class UpdateExpression(Expression):
    """
    Increment/decrement operation.

    Examples:
        ++i
        i--
    """

    operator: UpdateOperator
    argument: Expression
    prefix: bool = True

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True, eq=False)
class BinaryExpression(Expression):
    """
    Binary or logical operation.

    Example:
        a + b
    """

    left: Expression
    operator: BinaryOperator | LogicalOperator
    right: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return self.left, self.right


@dataclass(frozen=True, slots=True, eq=False)
class AssignmentExpression(Expression):
    """
    Assignment operation.

    Example:
        a = b
    """

    left: Expression
    operator: AssignmentOperator
    right: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return self.left, self.right


@dataclass(frozen=True, slots=True, eq=False)
class ConditionalExpression(Expression):
    """
    Ternary conditional expression.

    Example:
        condition ? consequent : alternate
    """

    test: Expression
    consequent: Expression
    alternate: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return self.test, self.consequent, self.alternate


@dataclass(frozen=True, slots=True, eq=False)
class SequenceExpression(Expression):
    """
    Comma-separated expression sequence.

    Example:
        a, b, c
    """

    expressions: tuple[Expression, ...]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.expressions
