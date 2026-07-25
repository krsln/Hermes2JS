from enum import Enum, auto
from typing import Optional

from hermes_decompiler.ir import Expression, Statement
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.JSVariable import JSVariable


class ControlFlowType(Enum):
    NORMAL = auto()
    CONDITIONAL = auto()
    UNCONDITIONAL = auto()
    RETURN = auto()
    THROW = auto()
    TERMINATOR = auto()  # optional


class OpcodeResult:
    opcode: OpcodeEntry
    variable: JSVariable
    result: str
    goto: Optional[int]
    extra_gotos: list[int]
    control_flow: ControlFlowType

    def __init__(
        self,
        opcode: OpcodeEntry,
        variable: JSVariable,
        goto: Optional[int] = None,
        extra_gotos: Optional[list[int]] = None,
        control_flow=ControlFlowType.NORMAL,
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
        self.control_flow = control_flow

        self.result = self._render_result(variable)

    @staticmethod
    def _render_result(variable: JSVariable) -> str:
        """
        Human-readable one-line summary of this instruction's effect,
        used by verbose logging/dumps and any legacy code path that
        hasn't moved to `JSRenderer`/`Printer` yet.

        `variable.statement`/`variable.value` may already be proper `ir`
        nodes (post-migration handlers) or plain strings (handlers not
        yet migrated) - both are supported here so mixed-migration state
        doesn't crash. `variable.value` may also legitimately be `None`
        for pure control-flow opcodes (e.g. `Jmp`), which carry only a
        `statement`.
        """

        # Imported lazily to avoid a hard dependency from `models` on
        # `regions` at module load time; `models` is the lower layer.
        from hermes_decompiler.regions.render.Printer import Printer

        printer = Printer()

        if isinstance(variable.statement, Statement):
            return printer.print_statement(variable.statement)

        if isinstance(variable.value, Expression):
            rendered = printer.print_expression(variable.value)

            if variable.name:
                return f"{variable.name} = {rendered}"

            return rendered

        if variable.value is None:
            # No statement and no value: nothing meaningful to show.
            # Shouldn't normally happen for a well-formed handler.
            return ""

        # Legacy fallback: value is still a plain string (handler not
        # yet migrated to the `ir` package).
        if variable.name:
            return f"{variable.name} = {variable.value}"

        return f"{variable.value}"

    @property
    def handler(self) -> str:
        return self.variable.handler