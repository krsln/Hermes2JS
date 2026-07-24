from __future__ import annotations

from dataclasses import dataclass

from ..expressions import Expression, Identifier
from ..Node import Node
from ._Base import Statement

__all__ = [
    "IfStatement",
    "ReturnStatement",
    "BreakStatement",
    "ContinueStatement",
    "DebuggerStatement",
]


# ============================================================================
# Return
# ============================================================================


@dataclass(frozen=True, slots=True)
class ReturnStatement(Statement):
    """
    Represents a return statement.

    Examples:
        return;

        return value;
    """

    argument: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.argument is None else (self.argument,)


# ============================================================================
# If
# ============================================================================


@dataclass(frozen=True, slots=True)
class IfStatement(Statement):
    """
    Represents an if statement.

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
        children: list[Node] = [
            self.test,
            self.consequent,
        ]

        if self.alternate is not None:
            children.append(self.alternate)

        return tuple(children)


# ============================================================================
# Break
# ============================================================================


@dataclass(frozen=True, slots=True)
class BreakStatement(Statement):
    """
    Represents a break statement.

    Examples:
        break;

        break outerLoop;
    """

    label: Identifier | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.label is None else (self.label,)


# ============================================================================
# Continue
# ============================================================================


@dataclass(frozen=True, slots=True)
class ContinueStatement(Statement):
    """
    Represents a continue statement.

    Examples:
        continue;

        continue outerLoop;
    """

    label: Identifier | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        return () if self.label is None else (self.label,)


# ============================================================================
# Debugger
# ============================================================================


@dataclass(frozen=True, slots=True)
class DebuggerStatement(Statement):
    """
    Represents a debugger statement.

    Example:
        debugger;
    """

    @property
    def children(self) -> tuple[Node, ...]:
        return ()
