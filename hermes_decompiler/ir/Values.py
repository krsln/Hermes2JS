from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Value(ABC):

    @property
    def inlineable(self) -> bool:
        return True

    @abstractmethod
    def render(self) -> str:
        ...

    def __str__(self):
        return self.render()


@dataclass(frozen=True)
class RegisterValue(Value):
    register: int

    def render(self):
        return f"r{self.register}"


@dataclass(frozen=True)
class ConstantValue(Value):
    value: object

    def render(self):

        if self.value is None:
            return "null"

        if isinstance(self.value, bool):
            return "true" if self.value else "false"

        if isinstance(self.value, str):
            return json.dumps(self.value)

        return str(self.value)


# --------------

@dataclass(frozen=True)
class UnknownValue(Value):

    def render(self):
        return "<?>"


@dataclass(frozen=True)
class UndefinedValue(Value):

    def render(self):
        return "undefined"


@dataclass(frozen=True)
class EmptyValue(Value):
    def render(self):
        return "<empty>"


@dataclass(frozen=True)
class IdentifierValue(Value):
    name: str

    def render(self) -> str:
        return self.name

@dataclass(frozen=True)
class ClosureValue(Value):
    name: str
    environment_register: int | None
    environment: Value | None

    def render(self):
        if self.environment_register is not None:
            return (
                f"{self.name} "
                f"/* Closure with env r{self.environment_register} = "
                f"{self.environment.render()} */"
            )
        if self.environment:
            return (
                f"{self.name} "
                f"/* Closure with env {self.environment.render()} */"
            )
        return self.name