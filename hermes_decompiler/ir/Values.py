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
        # print(type(self).__name__)
        return self.render()


@dataclass(frozen=True)
class RegisterValue(Value):
    register: int

    def render(self):
        return f"r{self.register}"


@dataclass(frozen=True)
class CommentValue(Value):
    value: str

    def render(self):
        return f"{self.value}"


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


@dataclass(frozen=True)
class RegExpValue(Value):
    pattern: str
    flags: str = ""

    def render(self):
        return f"/{self.pattern}/{self.flags}"


@dataclass
class ArrayValue(Value):
    elements: list[Value]
    capacity_hint: int | None = None

    def render(self):
        rendered = ", ".join(e.render() for e in self.elements)

        text = f"[{rendered}]"

        if self.capacity_hint:
            text += f" /* capacity hint: {self.capacity_hint} */"

        return text


@dataclass(frozen=True)
class GeneratorValue(Value):
    name: str
    environment_register: int | None
    environment: Value | None

    def render(self):
        if self.environment is not None:
            return f"generator {self.name} /* env={self.environment.render()} */"
        return f"generator {self.name}"


@dataclass(frozen=True)
class ReturnValue(Value):
    value: Value | None = None

    def render(self):
        if self.value is None:
            return "return;"
        return f"return {self.value.render()};"


@dataclass(frozen=True)
class ThrowValue(Value):
    value: Value

    def render(self):
        return f"throw {self.value.render()};"


@dataclass(frozen=True)
class ThisValue(Value):
    def render(self):
        return "this"


@dataclass(frozen=True)
class BuiltinValue(Value):
    builtin: int

    def render(self):
        return f"builtin_{self.builtin}"


@dataclass(frozen=True)
class ObjectLiteralValue(Value):
    properties: dict[str, Value]

    def render(self):
        parts = []

        for key, value in self.properties.items():
            parts.append(f"{key}: {value.render()}")

        return "{ " + ", ".join(parts) + " }"
