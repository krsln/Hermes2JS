from dataclasses import dataclass

from .Value import Value


@dataclass(frozen=True)
class UnknownValue(Value):

    def render(self):
        return "<?>"