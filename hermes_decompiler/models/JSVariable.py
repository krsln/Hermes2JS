from __future__ import annotations

from typing import Any

from hermes_decompiler.ir import Expression, Statement


class JSVariable:
    """
    Represents a single-assignment register/variable produced while
    analyzing Hermes bytecode.

    `value` is always a plain IR `Expression` - never a statement.
    `statement` is populated only by handlers whose opcode is itself a
    statement/terminator (e.g. `Throw`, `Ret`) rather than a value
    computation; for those, `value` still holds the operand expression
    (e.g. the thrown value) so existing register-lookup code keeps
    working, while `statement` carries the actual IR statement for the
    CFG/region builder to consume as a terminator.
    """

    def __init__(
        self,
        handler: str,
        address: int,
        name: str,
        value: Expression,
        statement: Statement | None = None,
    ) -> None:
        self.handler = handler
        self.address = address
        self.name = name
        self.value = value
        self.statement = statement

        self.used = False

    def __str__(self) -> str:
        return (
            f"JSVariable("
            f"address={self.address}, "
            f"handler={self.handler}, "
            f"name={self.name}, "
            f"value={self.value!r}, "
            f"statement={self.statement!r}, "
            f"used={self.used})"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "handler": self.handler,
            "address": self.address,
            "name": self.name,
            "value": self.value,
            "statement": self.statement,
            "used": self.used,
        }