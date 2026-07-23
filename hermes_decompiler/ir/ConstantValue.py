from dataclasses import dataclass

from .Value import Value


@dataclass(frozen=True)
class ConstantValue(Value):

    value: object

    def render(self):

        if isinstance(self.value, str):
            return repr(self.value)

        return str(self.value)