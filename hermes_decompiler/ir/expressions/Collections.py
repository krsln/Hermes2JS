from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from hermes_decompiler.ir.Node import Node
from ._Base import Expression

__all__ = [
    "PropertyKind",
    "SpreadElement",
    "ObjectProperty",
    "ArrayExpression",
    "ObjectExpression",
]


class PropertyKind(StrEnum):
    """Kind of an object literal property."""

    INIT = "init"
    GET = "get"
    SET = "set"


@dataclass(frozen=True, slots=True, eq=False)
class SpreadElement(Node):
    """
    Spread element.

    Examples:
        [...items]
        foo(...args)
        { ...object }
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True, eq=False)
class ObjectProperty(Node):
    """
    Single property within an object literal.

    Examples:
        { foo: 1 }
        { [key]: value }
        { foo }
        { foo() {} }
        { get name() {} }
        { set name(v) {} }
    """

    key: Expression
    value: Expression
    kind: PropertyKind = PropertyKind.INIT
    computed: bool = False
    method: bool = False
    shorthand: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return self.key, self.value


@dataclass(frozen=True, slots=True, eq=False)
class ArrayExpression(Expression):
    """
    Array literal.

    Examples:
        []
        [1, 2, 3]
        [foo, ...bar]
    """

    elements: tuple[Expression | SpreadElement, ...] = ()

    @property
    def children(self) -> tuple[Node, ...]:
        return self.elements


@dataclass(frozen=True, slots=True, eq=False)
class ObjectExpression(Expression):
    """
    Object literal.

    Examples:
        {}
        { foo: 1 }
        { foo, bar: 2, [key]: value, ...other }
    """

    properties: tuple[ObjectProperty | SpreadElement, ...] = ()

    @property
    def children(self) -> tuple[Node, ...]:
        return self.properties