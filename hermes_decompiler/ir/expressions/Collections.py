from __future__ import annotations

from dataclasses import dataclass

from enum import StrEnum
from ..Node import Node
from .Base import Expression

__all__ = [
    "PropertyKind",
    "SpreadElement",
    "ObjectProperty",
    "ArrayExpression",
    "ObjectExpression",
]


class PropertyKind(StrEnum):
    """
    Represents the kind of object property.
    """

    INIT = "init"
    GET = "get"
    SET = "set"


# ============================================================================
# Helper Nodes
# ============================================================================


@dataclass(frozen=True, slots=True)
class SpreadElement(Node):
    """
    Represents a spread element.

    Examples:
        [...items]
        foo(...args)
        { ...object }
    """

    argument: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.argument,)


@dataclass(frozen=True, slots=True)
class ObjectProperty(Node):
    """
    Represents a property within an object literal.

    Examples:
        { foo: 1 }

        { [key]: value }

        { foo }

        { foo() {} }

        {
            get name() {}
        }

        {
            set name(v) {}
        }
    """

    key: Expression

    value: Expression

    kind: PropertyKind = PropertyKind.INIT

    computed: bool = False

    method: bool = False

    shorthand: bool = False

    @property
    def children(self) -> tuple[Node, ...]:
        return (
            self.key,
            self.value,
        )


# ============================================================================
# Collection Expressions
# ============================================================================


@dataclass(frozen=True, slots=True)
class ArrayExpression(Expression):
    """
    Represents a JavaScript array literal.

    Examples:
        []

        [1, 2, 3]

        [foo, ...bar]
    """

    elements: tuple[
        Expression | SpreadElement,
        ...
    ]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.elements


@dataclass(frozen=True, slots=True)
class ObjectExpression(Expression):
    """
    Represents a JavaScript object literal.

    Examples:
        {}

        { foo: 1 }

        {
            foo,
            bar: 2,
            [key]: value,
            ...other
        }
    """

    properties: tuple[
        ObjectProperty | SpreadElement,
        ...
    ]

    @property
    def children(self) -> tuple[Node, ...]:
        return self.properties
