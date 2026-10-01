import re
from dataclasses import dataclass
from enum import Enum, auto

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.frontend.batch_pipeline.tables import BatchTables
from hermes_decompiler.frontend.opcode import OpcodeEntry


@dataclass(slots=True)
class OpcodeContext:
    analysis: HermesAnalysis
    entry: OpcodeEntry
    entries: list[OpcodeEntry]
    index: int
    # The function id MetadataStage parsed for the section currently
    # being decompiled (PipelineContext.function_id) and every
    # batch-resolved table it can consult (PipelineContext.batch_tables) -
    # both None when decompiling a lone section with no batch at all, or
    # threaded through from a section whose own MetadataStage hasn't run
    # yet (shouldn't happen in practice: DispatchStage always runs after
    # SignatureStage - see Pipeline's own stage order in Decompiler.py).
    function_id: int | None = None
    batch_tables: "BatchTables | None" = None


@dataclass(frozen=True, slots=True)
class ArgsPattern:
    regex: re.Pattern[str]
    desc: str


class OperandMode(Enum):
    """
    Controls how a register operand is resolved into an IR expression.
    Opcode subclasses declare *which* mode each of their operands needs
    (class attribute), instead of each one hand-rolling its own
    resolution override the way `Inc`/`Dec` previously did.

    EXPRESSION - substitute the register's current defining expression
        (constant folding / inlining, via `get_register_expression`).
        This is the default and matches all pre-existing behavior for
        opcodes that don't opt into REFERENCE.

    REFERENCE - always resolve to a bare symbolic identifier `rN` (via
        `get_register_reference`), never inlining the defining
        expression. Required whenever an operand is a loop/accumulator
        register that gets redefined on a back-edge (e.g., the `x` in
        `Inc`/`Dec`, or the counter operand of `AddN`/`SubN` when they
        desugar `i++`/`i--`): substituting a traced snapshot value there
        silently bakes a single iteration's value into every iteration
        (e.g. `r0 = 0 + 1` instead of `r0 = r1 + 1`), which can produce
        a non-advancing loop counter.
    """

    EXPRESSION = auto()
    REFERENCE = auto()
