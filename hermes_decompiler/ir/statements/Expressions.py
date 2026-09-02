from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from hermes_decompiler.ir.expressions import Expression
from ._base import Statement

__all__ = [
    "ExpressionStatement",
]


@dataclass(frozen=True, slots=True, eq=False)
class ExpressionStatement(Statement):
    """
    An expression evaluated for its side effects, with the resulting
    value discarded.

    Examples:
        foo();
        a = b;
        ++i;
        new Foo();
        delete object.property;
    """

    expression: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.expression,)