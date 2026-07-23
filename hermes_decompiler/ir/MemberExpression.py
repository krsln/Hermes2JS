from dataclasses import dataclass

from .Values import Value


@dataclass(frozen=True)
class MemberExpression(Value):

    object: Value

    property: str

    def render(self):

        return (
            f"{self.object.render()}."
            f"{self.property}"
        )