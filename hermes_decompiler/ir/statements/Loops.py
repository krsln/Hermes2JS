from __future__ import annotations

from dataclasses import dataclass

from ..expressions import Expression
from ..Node import Node
from ._Base import Statement

__all__ = [
    "WhileStatement",
    "DoWhileStatement",
    "ForStatement",
    "ForInStatement",
    "ForOfStatement",
]


# ============================================================================
# While
# ============================================================================


@dataclass(frozen=True, slots=True)
class WhileStatement(Statement):
    """
    Represents a while loop.

    Example:
        while (condition) {
            ...
        }
    """

    test: Expression

    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.test,
            self.body,
        )


# ============================================================================
# Do While
# ============================================================================


@dataclass(frozen=True, slots=True)
class DoWhileStatement(Statement):
    """
    Represents a do-while loop.

    Example:
        do {
            ...
        } while (condition);
    """

    body: Statement

    test: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.body,
            self.test,
        )


# ============================================================================
# For
# ============================================================================


@dataclass(frozen=True, slots=True)
class ForStatement(Statement):
    """
    Represents a classic for loop.

    Example:
        for (init; test; update) {
            ...
        }
    """

    body: Statement
    initializer: Statement | Expression | None = None
    test: Expression | None = None
    update: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = []

        if self.initializer is not None:
            children.append(self.initializer)

        if self.test is not None:
            children.append(self.test)

        if self.update is not None:
            children.append(self.update)

        children.append(self.body)

        return tuple(children)


# ============================================================================
# For In
# ============================================================================


@dataclass(frozen=True, slots=True)
class ForInStatement(Statement):
    """
    Represents a for-in loop.

    Example:
        for (key in object) {
            ...
        }
    """

    left: Statement | Expression

    right: Expression

    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.left,
            self.right,
            self.body,
        )


# ============================================================================
# For Of
# ============================================================================


@dataclass(frozen=True, slots=True)
class ForOfStatement(Statement):
    """
    Represents a for-of loop.

    Examples:
        for (value of iterable) { ... }

        for await (value of iterable) { ... }
    """

    left: Statement | Expression

    right: Expression

    body: Statement

    await_: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.left,
            self.right,
            self.body,
        )
