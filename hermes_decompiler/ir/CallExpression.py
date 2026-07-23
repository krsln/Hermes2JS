from dataclasses import dataclass

from .Value import Value


@dataclass(frozen=True)
class CallExpression(Value):

    callee: Value

    arguments: tuple[Value, ...]

    def render(self):

        args = ", ".join(
            arg.render()
            for arg in self.arguments
        )

        return (
            f"{self.callee.render()}({args})"
        )