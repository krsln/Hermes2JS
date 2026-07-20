from typing import Optional

from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.JSVariable import JSVariable


class OpcodeResult:
    opcode: OpcodeEntry
    variable: JSVariable
    result: str
    goto: Optional[int]

    def __init__(
            self,
            opcode: OpcodeEntry,
            variable: JSVariable,
            goto: Optional[int] = None
    ):
        self.opcode = opcode
        self.variable = variable
        self.goto = goto

        if variable.name:
            self.result = f'{variable.name} = {variable.value}'
        else:
            self.result = f'{variable.value}'

    @property
    def handler(self) -> str:
        return self.variable.handler

    @property
    def value(self) -> str:
        return self.variable.value

    def __str__(self):
        return f"OpcodeResult(Opcode={self.opcode}, Variable='{self.variable}',Result='{self.result}', GoTo='{self.goto}')"

    def to_dict(self):
        """Converts the OpcodeResult object to a dictionary."""
        return {
            "Opcode": self.opcode.to_dict(),
            "Variable": self.variable.to_dict(),  # Serialize JSVariable
            "result": self.result,
            "GoTo": self.goto,
        }
