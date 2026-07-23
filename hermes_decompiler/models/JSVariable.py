from typing import Optional, Dict, Any

from hermes_decompiler.ir.Value import Value

RenderableValue = str | Value

class JSVariable:
    """Represents a variable or register in Hermes bytecode analysis."""

    def __init__(
            self,
            handler: str,
            address: int,
            name: str,
            value: RenderableValue,
            function_base: Optional[str] = None,
            function_call: Optional[str] = None,
    ):
        """Initialize a JSVariable for Hermes bytecode analysis.

        Args:
            handler: The name of the opcode handler (e.g., Call1).
            address: The opcode's address in the bytecode.
            name: The destination register (e.g., r8).
            value: The value or expression (e.g., 'r6.call(this, r5, r1)').
            function_base: The base register for function calls (e.g., 'r6').
            function_call: The function call expression (e.g., '.call(this, r5, r1)').
        """
        self.handler = handler
        self.address = address
        self.name = name
        self.value = value
        self.function_base = function_base  # Base register for function calls (e.g., 'r6')
        self.function_call = function_call  # Function call expression (e.g., '.call(this, r5, r1)')

        self.used = False

    @property
    def rendered(self) -> str:
        if hasattr(self.value, "render"):
            return self.value.render()

        return str(self.value)

    def __str__(self) -> str:
        return (
            f"JSVariable("
            f"address={self.address}, "
            f"handler={self.handler}, "
            f"name={self.name}, "
            f"value={self.rendered}, "
            f"function_base={self.function_base}, "
            f"function_call={self.function_call}, "
            f"used={self.used})"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Converts the JSVariable to a dictionary for serialization."""
        return {
            "handler": self.handler,
            "address": self.address,
            "name": self.name,
            "value": self.value,
            "function_base": self.function_base,
            "function_call": self.function_call,
            "used": self.used,
        }
