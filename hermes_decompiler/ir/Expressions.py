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
class UnaryExpression(Expression):
    operator: str
    operand: Value

    def render(self):
        return f"{self.operator}{self.operand.render()}"


@dataclass(frozen=True)
class BinaryExpression(Expression):
    left: Value
    operator: str
    right: Value

    def render(self):
        return f"{self.left.render()} {self.operator} {self.right.render()}"


@dataclass(frozen=True)
class ComparisonExpression(BinaryExpression):
    pass


@dataclass(frozen=True)
class MemberExpression(Expression):
    object: Value
    property: str

    def render(self):
        return f"{self.object.render()}.{self.property}"


@dataclass(frozen=True)
class IndexExpression(Expression):
    object: Value
    index: Value

    def render(self):
        return f"{self.object.render()}[{self.index.render()}]"


@dataclass(frozen=True)
class CallExpression(Expression):
    callee: Value
    arguments: list[Value]

    def render(self):
        args = ", ".join(arg.render() for arg in self.arguments)
        return f"{self.callee.render()}({args})"


@dataclass(frozen=True)
class IteratorNextExpression(Expression):
    iterator: Value

    @property
    def inlineable(self):
        return False

    def render(self):
        return f"{self.iterator.render()}.next()"


@dataclass(frozen=True)
class NewExpression(Expression):
    constructor: Value
    arguments: list[Value]

    def render(self):
        args = ", ".join(a.render() for a in self.arguments)
        return f"new {self.constructor.render()}({args})"

# AssignmentExpression(
#     target=IndexExpression(...),
#     value=value
# )
# ConditionalExpression(
#     condition=...,
#     when_true=...,
#     when_false=...
# )
# ArrayExpression(
#     elements=[...]
# )