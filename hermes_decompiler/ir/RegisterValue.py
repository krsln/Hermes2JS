from dataclasses import dataclass

from .Value import Value


@dataclass(frozen=True)
class RegisterValue(Value):

    register: int

    def render(self):
        return f"r{self.register}"