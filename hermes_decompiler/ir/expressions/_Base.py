from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from hermes_decompiler.ir.Node import Node

__all__ = [
    "Expression",
    "Identifier",
    "ParenthesizedExpression",
]


@dataclass(frozen=True, slots=True, eq=False)
class Expression(Node, ABC):
    """Abstract base class for every JavaScript expression."""


@dataclass(frozen=True, slots=True, eq=False)
class Identifier(Expression):
    """
    JavaScript identifier.

    Example:
        foo
    """

    name: str

    @property
    def children(self) -> tuple[Node, ...]:
        return ()


@dataclass(frozen=True, slots=True, eq=False)
class ParenthesizedExpression(Expression):
    """
    Explicit parenthesization, preserved for rendering/precedence
    purposes. Semantically equivalent to `expression`.

    Example:
        (a + b)
    """

    expression: Expression

    @property
    def children(self) -> tuple[Node, ...]:
        return (self.expression,)