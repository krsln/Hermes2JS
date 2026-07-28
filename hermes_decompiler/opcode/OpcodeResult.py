from __future__ import annotations

from enum import Enum, auto
from typing import Any, Optional

from hermes_decompiler.analysis.terminators import Terminator
from hermes_decompiler.ir.expressions import Expression
from hermes_decompiler.ir.statements import Statement
from hermes_decompiler.opcode import OpcodeEntry


class ControlFlowType(Enum):
    NORMAL = auto()
    CONDITIONAL = auto()
    UNCONDITIONAL = auto()
    RETURN = auto()
    THROW = auto()
    TERMINATOR = auto()  # optional


class OpcodeResult:
    """
    The single record produced by handling one bytecode opcode.

    Replaces the earlier OpcodeResult + JSVariable pair. `handler` and
    `address` were pure duplicates of `entry.opcode`/`entry.address` and
    are now derived properties; `value`/`statement`/`used`/destination
    register are owned directly here instead of through a separate
    wrapper object, so a handler builds exactly one `OpcodeResult`,
    registers it via `analysis.add_result(result)`, and returns that
    same instance - there is no longer a second, separately-constructed
    `OpcodeResult` for the same opcode.
    """

    def __init__(
            self,
            entry: OpcodeEntry,
            value: Expression | None = None,
            terminator: Terminator | None = None,
            dest_reg: int | None = None,

            statement: Statement | None = None,
            goto: Optional[int] = None,
            control_flow: ControlFlowType = ControlFlowType.NORMAL,
    ):
        """
        Args:
            entry: The opcode this result was produced from. Also the
                source of `handler`/`address` (see properties below).
            value: The IR expression this opcode's destination register
                now holds, if any (`None` for pure control flow with no
                operand, e.g. an unconditional jump).
            statement: The IR statement this opcode represents, if it's
                a statement/terminator (Throw, Ret, Jmp, ...) rather
                than a plain value computation.
            dest_reg: The destination register index, if this opcode
                writes one. Used to derive `name` (`"r{dest_reg}"`).
            goto: Single jump target, used by unconditional/conditional
                jumps (Jmp*, SaveGenerator's resume address, ...).
            control_flow: How this opcode affects control flow.
        """

        self.opcode = entry
        self.value = value
        self.dest_reg = dest_reg
        self.used = False

        # todo: remove rest
        self.statement = statement
        self.goto = goto
        self.control_flow = control_flow

        self.result = self._render_result()

    # ------------------------------------------------------------------
    # Derived from `entry` - no longer separately stored/duplicated.
    # ------------------------------------------------------------------

    @property
    def address(self):
        return self.opcode.address

    @property
    def handler(self):
        return self.opcode.opcode

    @property
    def name(self):
        if self.dest_reg is None:
            return ""
        return f"r{self.dest_reg}"

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------

    def _render_result(self) -> str:
        """
        Human-readable one-line summary of this instruction's effect,
        used by verbose logging/dumps and any legacy code path that
        hasn't moved to `JSRenderer`/`Printer` yet.

        Callable again after mutating `value`/`statement` (e.g.
        `Dispatcher._handle_generator_await` wraps a previous result's
        `value` in an `AwaitExpression` and recomputes `.result`).
        """

        # Imported lazily to avoid a hard dependency from `models` on
        # `regions` at module load time; `models` is the lower layer.
        from hermes_decompiler.emit import Printer

        printer = Printer()

        if isinstance(self.statement, Statement):
            return printer.print_statement(self.statement)

        if isinstance(self.value, Expression):
            rendered = printer.print_expression(self.value)

            if self.name:
                return f"{self.name} = {rendered}"

            return rendered

        if self.value is None:
            # No statement and no value: nothing meaningful to show.
            # Shouldn't normally happen for a well-formed handler.
            return ""

        # Legacy fallback: value is still a plain string (handler not
        # yet migrated to the `ir` package).
        if self.name:
            return f"{self.name} = {self.value}"

        return f"{self.value}"

    def refresh_result(self) -> None:
        """Recompute `.result` after mutating `value`/`statement` in place."""

        self.result = self._render_result()

    # ------------------------------------------------------------------

    def __str__(self) -> str:
        return (
            f"OpcodeResult("
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
            "goto": self.goto,
        }
