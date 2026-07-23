from dataclasses import dataclass

from .Values import Value
from .Operators import BinaryOperator


@dataclass(frozen=True)
class BinaryExpression(Value):

    operator: BinaryOperator

    left: Value

    right: Value

    def render(self):

        return (
            f"{self.left.render()} "
            f"{self.operator.value} "
            f"{self.right.render()}"
        )