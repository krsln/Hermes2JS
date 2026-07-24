from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ._Base import Statement

__all__ = [
    "BlockStatement",
    "EmptyStatement",
]


# ============================================================================
# Block
# ============================================================================


@dataclass(frozen=True, slots=True)
class BlockStatement(Statement):
    """
    Represents a JavaScript block statement.

    A block groups zero or more statements into a single statement.

    Examples:
        {
        }

        {
            foo();
            return bar;
        }
    """

    statements: tuple[Statement, ...] = ()

    @property
    def children(self) -> tuple[Node, ...]:
        return self.statements


# ============================================================================
# Empty
# ============================================================================


@dataclass(frozen=True, slots=True)
class EmptyStatement(Statement):
    """
    Represents an empty statement.

    Example:
        ;
    """

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
