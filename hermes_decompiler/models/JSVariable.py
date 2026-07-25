from __future__ import annotations

from typing import Any

from hermes_decompiler.ir import Expression, Statement


class JSVariable:
    """
    Represents a single-assignment register/variable produced while
    analyzing Hermes bytecode.

    `value` holds the IR expression this register now evaluates to, when
    there is one - it's `None` for opcodes that are pure control flow
    with no operand of their own (e.g. an unconditional `Jmp`, which
    carries only a `statement` (`GotoStatement`) and nothing else).

    `statement` is populated only by handlers whose opcode is itself a
    statement/terminator (e.g. `Throw`, `Ret`, `Jmp`, `JCompareX`) rather
    than a value computation. For operand-bearing statements (Throw,
    Ret), `value` still holds the operand expression so existing
    register-lookup code keeps working; for pure control flow (Jmp),
    `value` is simply `None`.
    """

    def __init__(
        self,
        handler: str,
        address: int,
        name: str,
        value: Expression | None,
        statement: Statement | None = None,
    ) -> None:
        """
        Args:
            handler: Name of the opcode handler that produced this
                variable (e.g. "Call1").
            address: Address of the opcode in the bytecode.
            name: Destination register (e.g. "r8").
            value: The IR expression this register now holds, or `None`
                for pure control-flow opcodes with no operand.
            statement: The IR statement this opcode represents, if the
                opcode is a statement/terminator rather than a plain
                value computation.
        """

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
        """Converts the JSVariable to a dictionary for serialization."""

        return {
            "handler": self.handler,
            "address": self.address,
            "name": self.name,
            "value": self.value,
            "statement": self.statement,
            "used": self.used,
        }