from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ._Base import Expression

__all__ = [
    "AwaitExpression",
    "YieldExpression",
]


# ============================================================================
# Async
# ============================================================================


@dataclass(frozen=True, slots=True)
class AwaitExpression(Expression):
    """
    Represents an await expression.

    Example:
        await value
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True)
class YieldExpression(Expression):
    """
    Represents a yield expression.

    Examples:
        yield value
        yield* iterable
    """

    argument: Expression | None = None

    delegate: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.argument is None else (self.argument,)
