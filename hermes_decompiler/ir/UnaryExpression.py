from dataclasses import dataclass

from .Operators import UnaryOperator
from .Value import Value


@dataclass(frozen=True)
class UnaryExpression(Value):

    operator: UnaryOperator

    operand: Value

    def render(self):

        return (
            f"{self.operator.value}"
            f"{self.operand.render()}"
        )