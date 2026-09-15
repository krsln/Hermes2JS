from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.expressions import Expression
from ._base import Statement

__all__ = [
    "IfStatement",
    "ReturnStatement",
    "DebuggerStatement",
]


@dataclass(frozen=True, slots=True, eq=False)
class IfStatement(Statement):
    """
    Conditional statement.

    Examples:
        if (condition)
            statement;

        if (condition)
            statement;
        else
            otherStatement;
    """

    test: Expression
    consequent: Statement
    alternate: Statement | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [self.test, self.consequent]

        if self.alternate is not None:
            children.append(self.alternate)

        return tuple(children)


@dataclass(frozen=True, slots=True, eq=False)
class ReturnStatement(Statement):
    """
    Return statement.

    Examples:
        return;
        return value;
    """

    argument: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.argument is None else (self.argument,)


@dataclass(frozen=True, slots=True, eq=False)
class DebuggerStatement(Statement):
    """
    Debugger statement.

    Example:
        debugger;
    """

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
