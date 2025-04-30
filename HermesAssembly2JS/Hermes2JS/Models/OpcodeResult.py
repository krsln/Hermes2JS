from typing import Optional

from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable


class OpcodeResult:
    Opcode: OpcodeEntry
    Variable: JSVariable

    result: str
    GoTo: Optional[int]

    def __init__(self,   opcode: OpcodeEntry, val: JSVariable, goto: Optional[int] = None):
        self.Opcode = opcode
        self.Variable = val
        if val.name:
            self.result = f'{val.name} = {val.value}'
        else:
            self.result = f'{val.value}'
        self.GoTo = goto

    def __str__(self):
        return f"OpcodeResult(Opcode={self.Opcode}, Variable='{self.Variable}',Result='{self.result}', GoTo='{self.GoTo}')"

    def to_dict(self):
        """Converts the OpcodeResult object to a dictionary."""
        return {
            "Opcode": self.Opcode.to_dict(),
            "Variable": self.Variable.to_dict(),  # Serialize JSVariable
            "result": self.result,
            "GoTo": self.GoTo,
        }
