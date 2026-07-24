from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from .old import Expression
from .Operators import BinaryOperator, UnaryOperator
from .Values import Value


@dataclass(frozen=True)
class PostfixUnaryExpression(Expression):
    operand: Value
    operator: UnaryOperator

    def render(self):
        return f"{self.operand.render()}{self.operator.value}"


@dataclass(frozen=True)
class UnaryExpression(Expression):
    operator: UnaryOperator
    operand: Value

    def render(self):
        return f"{self.operator.value}{self.operand.render()}"


@dataclass(frozen=True)
class BinaryExpression(Expression):
    left: Value
    operator: BinaryOperator
    right: Value

    def render(self):
        return f"{self.left.render()} {self.operator.value} {self.right.render()}"


@dataclass(frozen=True)
class ComparisonExpression(BinaryExpression):
    pass


@dataclass(frozen=True)
class MemberExpression(Expression):
    object: Value
    property: Value
    computed: bool = False

    def render(self):
        if self.computed:
            return f"{self.object.render()}[{self.property.render()}]"

        return f"{self.object.render()}.{self.property.render()}"


@dataclass(frozen=True)
class IndexExpression(Expression):
    object: Value
    index: Value

    def render(self):
        return f"{self.object.render()}[{self.index.render()}]"


@dataclass(frozen=True)
class CallExpression(Expression):
    callee: Value
    arguments: list[Value | str]

    # None => normal çağrı
    this_arg: Value | None = None

    def render(self):
        args = ", ".join(
            arg.render() if isinstance(arg, Value) else arg
            for arg in self.arguments
        )

        if self.this_arg is not None:
            values = [self.this_arg.render()]
            if args:
                values.append(args)

            return f"{self.callee.render()}.call({', '.join(values)})"

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
        args = ", ".join(arg.render() for arg in self.arguments)
        return f"new {self.constructor.render()}({args})"


@dataclass(frozen=True)
class AssignmentExpression(Expression):
    left: Value
    operator: str
    right: Value

    def render(self):
        return f"{self.left.render()} {self.operator} {self.right.render()}"


@dataclass(frozen=True)
class CreateThisExpression(Expression):
    prototype: Value
    constructor: Value

    def render(self):
        return (
            "createThis("
            f"prototype={self.prototype.render()}, "
            f"constructor={self.constructor.render()}"
            ")"
        )


@dataclass(frozen=True)
class TypeOfExpression(Expression):
    value: Value

    def render(self):
        return f"typeof {self.value.render()}"


@dataclass(frozen=True)
class ComputedMemberExpression(Expression):
    object: Value
    property: Value

    def render(self):
        return f"{self.object.render()}[{self.property.render()}]"


@dataclass(frozen=True)
class SwitchStatement(Expression):
    expression: Value
    targets: list[int]

    def render(self):
        labels = ", ".join(f"label_{t}" for t in self.targets)
        return f"/* switch ({self.expression.render()}) -> {labels} */"


@dataclass(frozen=True)
class GetIteratorExpression(Expression):
    iterable: Value

    def render(self):
        return f"GetIterator({self.iterable.render()})"


@dataclass(frozen=True)
class PropertyIteratorExpression(Expression):
    object: Value

    def render(self):
        return f"HermesPropertyIterator({self.object.render()})"
