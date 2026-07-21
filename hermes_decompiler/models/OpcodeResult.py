from typing import Optional

from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.JSVariable import JSVariable


class OpcodeResult:
    opcode: OpcodeEntry
    variable: JSVariable
    result: str
    goto: Optional[int]
    extra_gotos: list[int]

    def __init__(
            self,
            opcode: OpcodeEntry,
            variable: JSVariable,
            goto: Optional[int] = None,
            extra_gotos: Optional[list[int]] = None,
    ):
        """
        Args:
            goto: single jump target, used by unconditional/conditional
                jumps (Jmp*, SaveGenerator's resume address, ...).
            extra_gotos: ADDITIONAL jump targets beyond `goto`, for
                instructions with more than one possible successor that
                isn't expressible as a single fallthrough - currently
                only SwitchImm (one target per case label). Kept
                separate from `goto` rather than making `goto` a list,
                so every existing single-target call site (Jmp.py,
                the whole conditional-jump family, BasicBlockBuilder's
                leader-finding `result.goto is not None` checks, etc.)
                keeps working unchanged; only the few call sites that
                actually need multiple targets opt in.
        """
        self.opcode = opcode
        self.variable = variable
        self.goto = goto
        self.extra_gotos = extra_gotos or []

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
            "ExtraGoTos": self.extra_gotos,
        }
