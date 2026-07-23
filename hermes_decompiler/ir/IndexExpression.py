from dataclasses import dataclass

from .Values import Value


@dataclass(frozen=True)
class IndexExpression(Value):

    object: Value

    index: Value

    def render(self):

        return (
            f"{self.object.render()}"
            f"[{self.index.render()}]"
        )