from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ..Operators import (
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


# ============================================================================
# Unary
# ============================================================================


@dataclass(frozen=True, slots=True)
class UnaryExpression(Expression):
    """
    Represents a unary operation.
    """

    operator: UnaryOperator
    operand: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.operand,)


@dataclass(frozen=True, slots=True)
class UpdateExpression(Expression):
    """
    Represents an update operation.
    """

    operator: UpdateOperator
    argument: Expression
    prefix: bool = True

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


# ============================================================================
# Binary
# ============================================================================


@dataclass(frozen=True, slots=True)
class BinaryExpression(Expression):
    """
    Represents a binary operation.
    """

    left: Expression
    operator: BinaryOperator | LogicalOperator
    right: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.left,
            self.right,
        )


# ============================================================================
# Assignment
# ============================================================================


@dataclass(frozen=True, slots=True)
class AssignmentExpression(Expression):
    """
    Represents an assignment operation.
    """

    left: Expression
    operator: AssignmentOperator
    right: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.left,
            self.right,
        )


# ============================================================================
# Conditional
# ============================================================================


@dataclass(frozen=True, slots=True)
class ConditionalExpression(Expression):
    """
    Represents a conditional expression.

    condition ? consequent : alternate
    """

    test: Expression
    consequent: Expression
    alternate: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.test,
            self.consequent,
            self.alternate,
        )


# ============================================================================
# Sequence
# ============================================================================


@dataclass(frozen=True, slots=True)
class SequenceExpression(Expression):
    """
    Represents a comma-separated expression sequence.

    Example:
        a, b, c
    """

    expressions: tuple[Expression, ...]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.expressions
