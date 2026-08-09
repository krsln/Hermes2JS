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
        receiver.property
        receiver["property"]
        receiver[index]
        receiver?.property
        receiver?.[index]
    """

    receiver: Expression
    member: Expression
    computed: bool = False
    optional: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return self.receiver, self.member


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