from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from .Base import Expression
from ..Node import Node

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


# ============================================================================
# Base
# ============================================================================


@dataclass(frozen=True, slots=True)
class Literal(Expression, ABC):
    """
    Base class for every JavaScript literal.
    """

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


# ============================================================================
# Primitive Literals
# ============================================================================


@dataclass(frozen=True, slots=True)
class NumericLiteral(Literal):
    """
    JavaScript numeric literal.

    Examples:
        42
        3.14
    """

    value: int | float


@dataclass(frozen=True, slots=True)
class BigIntLiteral(Literal):
    """
    JavaScript BigInt literal.

    Example:
        123n
    """

    value: int


@dataclass(frozen=True, slots=True)
class StringLiteral(Literal):
    """
    JavaScript string literal.

    Example:
        "Hello"
    """

    value: str


@dataclass(frozen=True, slots=True)
class BooleanLiteral(Literal):
    """
    JavaScript boolean literal.
    """

    value: bool


@dataclass(frozen=True, slots=True)
class NullLiteral(Literal):
    """
    JavaScript null literal.
    """


@dataclass(frozen=True, slots=True)
class UndefinedLiteral(Literal):
    """
    JavaScript undefined literal.
    """


# ============================================================================
# Complex Literals
# ============================================================================


@dataclass(frozen=True, slots=True)
class RegExpLiteral(Literal):
    """
    JavaScript regular expression literal.

    Example:
        /abc/gi
    """

    pattern: str
    flags: str = ""


@dataclass(frozen=True, slots=True)
class TemplateElement(Node):
    """
    Static segment of a template literal.
    """

    raw: str
    cooked: str

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


@dataclass(frozen=True, slots=True)
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
