from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ._Base import Statement

__all__ = [
    "LabeledStatement",
    "BreakStatement",
    "ContinueStatement",
]


# ============================================================================
# Labeled Statement
# ============================================================================


@dataclass(frozen=True, slots=True)
class LabeledStatement(Statement):
    """
    Represents a labeled statement.

    Examples:

        loop:
        while (true) {
            ...
        }


        block:
        {
            break block;
        }
    """

    label: str

    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.body,
        )


# ============================================================================
# Break
# ============================================================================


@dataclass(frozen=True, slots=True)
class BreakStatement(Statement):
    """
    Represents break statement.

    Examples:

        break;

        break outer;
    """

    label: str | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


# ============================================================================
# Continue
# ============================================================================


@dataclass(frozen=True, slots=True)
class ContinueStatement(Statement):
    """
    Represents continue statement.

    Examples:

        continue;

        continue outer;
    """

    label: str | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
