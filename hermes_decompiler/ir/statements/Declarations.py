from __future__ import annotations

from dataclasses import dataclass

from ..expressions import Expression
from ..Node import Node
from ._Base import Statement

__all__ = [
    "VariableDeclaration",
    "VariableDeclarator",
    "FunctionDeclaration",
    "ClassDeclaration",
]


# ============================================================================
# Variable Declarator
# ============================================================================


@dataclass(frozen=True, slots=True)
class VariableDeclarator(Node):
    """
    Represents a single variable declaration.

    Examples:

        let x;

        let x = 10;
    """

    id: Expression

    init: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [
            self.id,
        ]

        if self.init is not None:
            children.append(self.init)

        return tuple(children)


# ============================================================================
# Variable Declaration
# ============================================================================


@dataclass(frozen=True, slots=True)
class VariableDeclaration(Statement):
    """
    Represents variable declaration.

    Examples:

        let a;

        const x = 1;

        var a = 1, b = 2;
    """

    kind: str

    declarations: tuple[VariableDeclarator, ...]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.declarations


# ============================================================================
# Function Declaration
# ============================================================================


@dataclass(frozen=True, slots=True)
class FunctionDeclaration(Statement):
    """
    Represents a function declaration.

    Example:

        function foo(a) {
            return a;
        }
    """

    id: Expression

    params: tuple[Expression, ...]

    body: Statement

    async_: bool = False

    generator: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.id,
            *self.params,
            self.body,
        )


# ============================================================================
# Class Declaration
# ============================================================================


@dataclass(frozen=True, slots=True)
class ClassDeclaration(Statement):
    """
    Represents a class declaration.

    Example:

        class Foo {
        }
    """

    id: Expression

    body: Statement

    super_class: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [
            self.id,
        ]

        if self.super_class is not None:
            children.append(self.super_class)

        children.append(self.body)

        return tuple(children)
