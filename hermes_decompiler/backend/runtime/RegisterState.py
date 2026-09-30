from dataclasses import dataclass

from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir import Expression

__all__ = ["RegisterState"]


@dataclass(slots=True)
class RegisterState:
    definition: OpcodeResult
    version: int = 0
    reads: int = 0
    #: `(register name, version)` of every register `definition.value`
    #: refers to, captured when this definition was created - see
    #: `HermesAnalysis.is_stale_value`.
    operand_versions: tuple[tuple[str, int], ...] = ()

    @property
    def value(self) -> Expression | None:
        return self.definition.value

    @property
    def handler(self) -> str:
        return self.definition.handler

    def mark_read(self) -> None:
        self.reads += 1

    def mark_used(self) -> None:
        # A pinned definition has a bare `rN` reference in the output and
        # must keep its defining statement (see `materialize`).
        if not self.definition.definition_pinned:
            self.definition.definition_used = True

    def materialize(self) -> None:
        """A bare symbolic `rN` reference to this definition is about to
        be emitted: keep (or restore) the defining statement.

        `mark_used` is a one-way fold - an earlier read that inlined the
        value suppressed the statement. If a later read then returns the
        symbolic `rN` instead of the value, the statement has to be
        un-folded, otherwise `rN` dangles with no definition printed (the
        earlier inlined uses stay valid - they carry the value itself).
        Pinning makes this order-independent: reads arriving afterwards
        can no longer fold the statement away again.
        """
        self.definition.definition_pinned = True
        self.definition.definition_used = False
