from __future__ import annotations

from dataclasses import dataclass

from ..Node import Node
from .Base import Expression
from .Collections import SpreadElement

__all__ = [
    "MemberExpression",
    "CallExpression",
    "NewExpression",
]


# ============================================================================
# Member Access
# ============================================================================


@dataclass(frozen=True, slots=True)
class MemberExpression(Expression):
    """
    Represents a JavaScript member access.

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
        return (
            self.receiver,
            self.member,
        )


# ============================================================================
# Function Calls
# ============================================================================


@dataclass(frozen=True, slots=True)
class CallExpression(Expression):
    """
    Represents a JavaScript function call.

    Examples:
        foo()
        foo(a, b)
        foo(...args)
        foo?.()
    """

    callee: Expression

    arguments: tuple[
        Expression | SpreadElement,
        ...
    ] = ()

    optional: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.callee,
            *self.arguments,
        )


# ============================================================================
# Constructor Calls
# ============================================================================


@dataclass(frozen=True, slots=True)
class NewExpression(Expression):
    """
    Represents a JavaScript constructor invocation.

    Examples:
        new Foo()
        new Foo(a, b)
    """

    callee: Expression

    arguments: tuple[
        Expression | SpreadElement,
        ...
    ] = ()

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.callee,
            *self.arguments,
        )