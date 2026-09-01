from __future__ import annotations

from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._base import Expression
from .Collections import SpreadElement

__all__ = [
    "MemberExpression",
    "CallExpression",
    "NewExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class MemberExpression(Expression):
    """
    Property access, static or computed.

    Examples:
        obj.property
        obj["property"]
        obj?.[index]

    `receiver` preserves an explicit ECMAScript [[Get]] receiver
    when it differs from `obj`.
    """

    obj: Expression
    prop: Expression
    receiver: Expression | None = None  # explicit [[Get]] receiver, if distinct from `obj`

    computed: bool = False
    optional: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        base = (self.obj, self.prop)
        return (base + (self.receiver,)) if (self.receiver is not None) else base


@dataclass(frozen=True, slots=True, eq=False)
class CallExpression(Expression):
    """
    Function call.

    Examples:
        foo()
        foo(a, b)
        foo(...args)
        foo?.()
    """

    callee: Expression
    arguments: tuple[Expression | SpreadElement, ...] = ()
    optional: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return self.callee, *self.arguments


@dataclass(frozen=True, slots=True, eq=False)
class NewExpression(Expression):
    """
    Constructor invocation.

    Example:
        new Foo(a, b)
    """

    callee: Expression
    arguments: tuple[Expression | SpreadElement, ...] = ()

    @property
    def children(self) -> tuple[Node, ...]:
        return self.callee, *self.arguments
