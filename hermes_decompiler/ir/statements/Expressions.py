from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ..Expressions import Expression
from .Base import Statement

__all__ = [
    "ExpressionStatement",
]


# ============================================================================
# Expression Statement
# ============================================================================


@dataclass(frozen=True, slots=True)
class ExpressionStatement(Statement):
    """
    Represents an expression used as a statement.

    Expression statements evaluate an expression for its side effects while
    discarding the resulting value.

    Examples:
        foo();

        a = b;

        ++i;

        new Foo();

        delete object.property;
    """

    expression: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.expression,)
