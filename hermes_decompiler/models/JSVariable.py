from __future__ import annotations

from typing import Any

from hermes_decompiler.ir import Expression


class JSVariable:
    """
    Represents a single-assignment register/variable produced while
    analyzing Hermes bytecode.

    `value` is always a plain IR `Expression` - never a statement. Opcode
    handlers that produce control flow (`Throw`, `Ret`, ...) must not
    route their statement through here; see `HermesAnalysis.add_result`
    and the handler-level TODO on separating expression results from
    statement/terminator results.
    """

    def __init__(
        self,
        handler: str,
        address: int,
        name: str,
        value: Expression,
    ) -> None:
        """
        Args:
            handler: Name of the opcode handler that produced this
                variable (e.g. "Call1").
            address: Address of the opcode in the bytecode.
            name: Destination register (e.g. "r8").
            value: The IR expression this register now holds.
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
    #         f"value={self.value!r}, "
    #         f"used={self.used})"
    #     )
    #
    # def to_dict(self) -> dict[str, Any]:
    #     """Converts the JSVariable to a dictionary for serialization."""
    #
    #     return {
    #         "handler": self.handler,
    #         "address": self.address,
    #         "name": self.name,
    #         "value": self.value,
    #         "used": self.used,
    #     }