from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._base import Statement

__all__ = [
    "BlockStatement",
    "EmptyStatement",
]


@dataclass(frozen=True, slots=True, eq=False)
class BlockStatement(Statement):
    """
    Sequence of statements grouped into a single statement.

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


@dataclass(frozen=True, slots=True, eq=False)
class EmptyStatement(Statement):
    """
    Empty statement.

    Example:
        ;
    """

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
