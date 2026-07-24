from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from ..Node import Node

__all__ = [
    "Statement",
]


# class Statement(Node, ABC):
#     """
#     Base class for all JavaScript statements.
#
#     Statements represent executable program constructs that perform actions,
#     control program flow, or declare bindings. Unlike expressions, statements
#     do not directly produce a value.
#
#     Examples:
#         - ExpressionStatement
#         - BlockStatement
#         - IfStatement
#         - ReturnStatement
#         - WhileStatement
#         - VariableDeclaration
#     """
#
#     __slots__ = ()


@dataclass(frozen=True, slots=True)
class Statement(Node, ABC):
    pass
