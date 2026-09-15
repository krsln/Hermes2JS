from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.expressions import Identifier
from ._base import Statement

__all__ = [
    "LabeledStatement",
    "BreakStatement",
    "ContinueStatement",
]


# NOTE: The previous flat layout defined BreakStatement/ContinueStatement
# twice (ControlFlow.py with an Identifier label, Labels.py with a str
# label), and __init__.py silently let the second import win. This module
# is now the single source of truth for all jump-target statements
# (break, continue, labeled), using Identifier consistently for labels
# so label nodes can carry a `loc` and be visited like any other node.


@dataclass(frozen=True, slots=True, eq=False)
class LabeledStatement(Statement):
    """
    Labeled statement, the target of a `break`/`continue` with a label.

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

    label: Identifier
    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return self.label, self.body


@dataclass(frozen=True, slots=True, eq=False)
class BreakStatement(Statement):
    """
    Break statement.

    Examples:
        break;
        break outerLoop;
    """

    label: Identifier | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.label is None else (self.label,)


@dataclass(frozen=True, slots=True, eq=False)
class ContinueStatement(Statement):
    """
    Continue statement.

    Examples:
        continue;
        continue outerLoop;
    """

    label: Identifier | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.label is None else (self.label,)
