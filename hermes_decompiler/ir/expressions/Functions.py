from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from ..statements import BlockStatement
from ._Base import Expression, Identifier

__all__ = [
    "FunctionExpression",
    "ArrowFunctionExpression",
    "ClassExpression",
]


# ============================================================================
# Function
# ============================================================================


@dataclass(frozen=True, slots=True)
class FunctionExpression(Expression):
    """
    Represents a function expression.

    Example:
        function foo(a, b) { ... }
    """

    name: Identifier | None

    parameters: tuple[Identifier, ...]

    body: BlockStatement

    async_: bool = False

    generator: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = []

        if self.name is not None:
            children.append(self.name)

        children.extend(self.parameters)
        children.append(self.body)

        return tuple(children)


# ============================================================================
# Arrow Function
# ============================================================================


@dataclass(frozen=True, slots=True)
class ArrowFunctionExpression(Expression):
    """
    Represents an arrow function.

    Example:
        (a, b) => a + b
    """

    parameters: tuple[Identifier, ...]

    body: Expression | BlockStatement

    async_: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            *self.parameters,
            self.body,
        )


# ============================================================================
# Class
# ============================================================================


@dataclass(frozen=True, slots=True)
class ClassExpression(Expression):
    """
    Represents a class expression.

    Example:
        class Foo {}
    """

    name: Identifier | None = None

    super_class: Expression | None = None

    body: BlockStatement | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = []

        if self.name is not None:
            children.append(self.name)

        if self.super_class is not None:
            children.append(self.super_class)

        if self.body is not None:
            children.append(self.body)

        return tuple(children)
