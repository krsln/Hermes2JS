from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.expressions import Expression
from ._Base import Statement

__all__ = [
    "WhileStatement",
    "DoWhileStatement",
    "ForStatement",
    "ForInStatement",
    "ForOfStatement",
]


@dataclass(frozen=True, slots=True, eq=False)
class WhileStatement(Statement):
    """
    While loop.

    Example:
        while (condition) {
            ...
        }
    """

    test: Expression
    body: Statement

    @property
    def children(self) -> tuple[Node, ...]:
        return self.test, self.body


@dataclass(frozen=True, slots=True, eq=False)
class DoWhileStatement(Statement):
    """
    Do-while loop.

    Example:
        do {
            ...
        /} while (condition);
    """

    body: Statement
    test: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return self.body, self.test


@dataclass(frozen=True, slots=True, eq=False)
class ForStatement(Statement):
    """
    Classic for loop.

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


@dataclass(frozen=True, slots=True, eq=False)
class ForInStatement(Statement):
    """
    For-in loop.

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
        return self.left, self.right, self.body


@dataclass(frozen=True, slots=True, eq=False)
class ForOfStatement(Statement):
    """
    For-of loop.

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
        return self.left, self.right, self.body
