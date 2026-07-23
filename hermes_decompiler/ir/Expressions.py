from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from .Values import Value


@dataclass(frozen=True)
class Expression(Value, ABC):
    pass


@dataclass(frozen=True)
class PrefixUnaryExpression(Expression):
    operator: str
    operand: Value

    def render(self):
        if self.operator.isalpha():
            return f"{self.operator} {self.operand.render()}"

        return f"{self.operator}{self.operand.render()}"


@dataclass(frozen=True)
class PostfixUnaryExpression(Expression):
    operand: Value
    operator: str

    def render(self):
        return f"{self.operand.render()}{self.operator}"


@dataclass(frozen=True)
class UnaryExpression(Value):
    operator: str
    operand: Value

    def render(self):
        return f"{self.operator}{self.operand.render()}"


@dataclass(frozen=True)
class BinaryExpression(Value):
    left: Value
    operator: str
    right: Value

    def render(self):
        return f"{self.left.render()} {self.operator} {self.right.render()}"


@dataclass(frozen=True)
class ComparisonExpression(BinaryExpression):
    pass


@dataclass(frozen=True)
class MemberExpression(Value):
    object: Value
    property: str

    def render(self):
        return f"{self.object.render()}.{self.property}"


@dataclass(frozen=True)
class IndexExpression(Value):
    object: Value
    index: Value

    def render(self):
        return f"{self.object.render()}[{self.index.render()}]"


@dataclass(frozen=True)
class CallExpression(Value):
    callee: Value
    arguments: tuple[Value, ...]

    @property
    def inlineable(self):
        return False

    def render(self):
        args = ", ".join(
            arg.render()
            for arg in self.arguments
        )

        return f"{self.callee.render()}({args})"


@dataclass(frozen=True)
class IteratorNextExpression(Value):
    iterator: Value

    @property
    def inlineable(self):
        return False

    def render(self):
        return f"{self.iterator.render()}.next()"


# @dataclass(frozen=True)
# class NewExpression(Value):
#     constructor: Value
#     arguments: tuple[Value, ...]
#
#     @property
#     def inlineable(self):
#         return False
#
#     def render(self):
#         pass
