from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node
from ._Base import Expression

__all__ = [
    "Literal",
    "NumericLiteral",
    "BigIntLiteral",
    "StringLiteral",
    "BooleanLiteral",
    "NullLiteral",
    "UndefinedLiteral",
    "RegExpLiteral",
    "TemplateElement",
    "TemplateLiteral",
]


@dataclass(frozen=True, slots=True, eq=False)
class Literal(Expression, ABC):
    """Abstract base class for every JavaScript literal."""

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


@dataclass(frozen=True, slots=True, eq=False)
class NumericLiteral(Literal):
    """
    JavaScript numeric literal.

    Examples:
        42
        3.14
    """

    value: int | float


@dataclass(frozen=True, slots=True, eq=False)
class BigIntLiteral(Literal):
    """
    JavaScript BigInt literal.

    Example:
        123n
    """

    value: int


@dataclass(frozen=True, slots=True, eq=False)
class StringLiteral(Literal):
    """
    JavaScript string literal.

    Example:
        "Hello"
    """

    value: str


@dataclass(frozen=True, slots=True, eq=False)
class BooleanLiteral(Literal):
    """JavaScript boolean literal."""

    value: bool


@dataclass(frozen=True, slots=True, eq=False)
class NullLiteral(Literal):
    """JavaScript `null` literal."""


@dataclass(frozen=True, slots=True, eq=False)
class UndefinedLiteral(Literal):
    """JavaScript `undefined` literal."""


@dataclass(frozen=True, slots=True, eq=False)
class RegExpLiteral(Literal):
    """
    JavaScript regular expression literal.

    Example:
        /abc/gi
    """

    pattern: str
    flags: str = ""


@dataclass(frozen=True, slots=True, eq=False)
class TemplateElement(Node):
    """Static (non-interpolated) segment of a template literal."""

    raw: str
    cooked: str

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


@dataclass(frozen=True, slots=True, eq=False)
class TemplateLiteral(Literal):
    """
    JavaScript template literal.

    Example:
        `Hello ${name}!`
    """

    quasis: tuple[TemplateElement, ...]
    expressions: tuple[Expression, ...]

    @property
    def children(self) -> tuple[Node, ...]:
        return *self.quasis, *self.expressions