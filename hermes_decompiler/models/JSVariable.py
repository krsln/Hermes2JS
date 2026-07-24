from typing import Dict, Any

from hermes_decompiler.ir import Expression


class JSVariable:
    """Represents a variable or register in Hermes bytecode analysis."""

    def __init__(
            self,
            handler: str,
            address: int,
            name: str,
            value: Expression,
    ):
        """Initialize a JSVariable for Hermes bytecode analysis.

        Args:
            handler: The name of the opcode handler (e.g., Call1).
            address: The opcode's address in the bytecode.
            name: The destination register (e.g., r8).
            value: The value or expression (e.g., 'r6.call(this, r5, r1)').
        """
        self.handler = handler
        self.address = address
        self.name = name
        self.value = value

        self.used = False

    # def __str__(self) -> str:
    #     return (
    #         f"JSVariable("
    #         f"address={self.address}, "
    #         f"handler={self.handler}, "
    #         f"name={self.name}, "
    #         f"value={self.value}, "
    #         f"used={self.used})"
    #     )
    #
    # def to_dict(self) -> Dict[str, Any]:
    #     """Converts the JSVariable to a dictionary for serialization."""
    #     return {
    #         "handler": self.handler,
    #         "address": self.address,
    #         "name": self.name,
    #         "value": self.value,
    #         "used": self.used,
    #     }
