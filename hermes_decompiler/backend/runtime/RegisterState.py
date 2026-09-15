from dataclasses import dataclass

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir import Expression

__all__ = ["RegisterState"]


@dataclass(slots=True)
class RegisterState:
    definition: OpcodeResult
    version: int = 0
    reads: int = 0

    @property
    def value(self) -> Expression | None:
        return self.definition.value

    @property
    def handler(self) -> str:
        return self.definition.handler

    def mark_read(self) -> None:
        self.reads += 1

    def mark_used(self) -> None:
        self.definition.definition_used = True
