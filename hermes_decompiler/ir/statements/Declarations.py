from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.Operators import VariableKind
from hermes_decompiler.ir.expressions import Expression, Identifier
from ._Base import Statement
from .Block import BlockStatement

__all__ = [
    "VariableDeclarator",
    "VariableDeclaration",
    "FunctionDeclaration",
    "ClassDeclaration",
]


@dataclass(frozen=True, slots=True, eq=False)
class VariableDeclarator(Node):
    """
    Single binding within a variable declaration.

    Examples:
        x
        x = 10
    """

    id: Expression
    init: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [self.id]

        if self.init is not None:
            children.append(self.init)

        return tuple(children)


@dataclass(frozen=True, slots=True, eq=False)
class VariableDeclaration(Statement):
    """
    Variable declaration statement.

    Examples:
        let a;
        const x = 1;
        var a = 1, b = 2;
    """

    kind: VariableKind
    declarations: tuple[VariableDeclarator, ...]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.declarations


@dataclass(frozen=True, slots=True, eq=False)
class FunctionDeclaration(Statement):
    """
    Function declaration.

    Example:
        function foo(a) {
            return a;
        }
    """

    id: Identifier
    params: tuple[Identifier, ...]
    body: BlockStatement
    async_: bool = False
    generator: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return self.id, *self.params, self.body


@dataclass(frozen=True, slots=True, eq=False)
class ClassDeclaration(Statement):
    """
    Class declaration.

    Example:
        class Foo {
        }
    """

    id: Identifier
    body: BlockStatement
    super_class: Expression | None = None

    @property
    def children(self) -> tuple[Node, ...]:
        children: list[Node] = [self.id]

        if self.super_class is not None:
            children.append(self.super_class)

        children.append(self.body)

        return tuple(children)
