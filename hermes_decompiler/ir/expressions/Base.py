from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from ..Node import Node


# @dataclass(frozen=True, slots=True)
# class Expression(Node, ABC):
#     """
#     Base class for every JavaScript expression.
#     """

@dataclass(frozen=True, slots=True)
class Expression(Node, ABC):
    pass


@dataclass(frozen=True, slots=True)
class Identifier(Expression):
    """
    JavaScript identifier.

    Example:
        foo
    """

    name: str


@dataclass(frozen=True, slots=True)
class ParenthesizedExpression(Expression):
    """
    Parenthesized expression.

    Example:
        (a + b)
    """

    expression: Expression

    @property
    def children(self):
        return (self.expression,)
