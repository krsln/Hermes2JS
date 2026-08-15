from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from hermes_decompiler.ir.Node import Node
from ._base import Expression, Identifier

if TYPE_CHECKING:
    # Deferred to avoid a runtime circular import: `statements` imports
    # from `expressions` (e.g. Declarations.py needs Expression), so
    # `expressions` cannot import `statements` at module load time.
    from hermes_decompiler.ir.statements.Block import BlockStatement

__all__ = [
    "FunctionExpression",
    "ArrowFunctionExpression",
    "ClassExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class FunctionExpression(Expression):
    """
    Function expression.

    Example:
        function foo(a, b) { ... }
    """

    name: Identifier | None
    parameters: tuple[Identifier, ...]
    body: "BlockStatement"
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


@dataclass(frozen=True, slots=True, eq=False)
class ArrowFunctionExpression(Expression):
    """
    Arrow function.

    Example:
        (a, b) => a + b
    """

    parameters: tuple[Identifier, ...]
    body: "Expression | BlockStatement"
    async_: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return *self.parameters, self.body


@dataclass(frozen=True, slots=True, eq=False)
class ClassExpression(Expression):
    """
    Class expression.

    Example:
        class Foo {}
    """

    name: Identifier | None = None
    super_class: Expression | None = None
    body: "BlockStatement | None" = None

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
