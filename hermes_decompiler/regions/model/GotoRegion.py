from dataclasses import dataclass
from enum import Enum, auto

from hermes_decompiler.regions.model.Region import Region


class ControlTransferKind(Enum):
    BREAK = auto()
    CONTINUE = auto()
    GOTO = auto()    # last-resort fallback for edges the structurer
                      # couldn't attribute to break/continue


@dataclass(slots=True)
class GotoRegion(Region):
    """
    Explicit, unstructured control transfer.

    Structural analysis cannot turn every real-world CFG into pure
    if/else/while nesting - irreducible loops, multi-entry regions,
    and compiler-generated jump patterns genuinely occur. Rather than
    raising or spinning forever when the structurer hits one of these,
    it emits a GotoRegion so the pipeline always terminates with SOME
    valid, inspectable output instead of crashing the whole
    conversion.

    BREAK / CONTINUE are the common, well-understood cases (a branch
    that leaves the current loop's body, or jumps back to its header).
    A bare GOTO (with `label` set) is the true last resort, used when
    the structurer can't even attribute the jump to an enclosing loop -
    it should be rare, and its presence in generated output is a signal
    worth grepping for and investigating against a real bytecode sample.
    """

    kind: ControlTransferKind
    label: str | None = None

    def accept(self, visitor):
        return visitor.visit_goto(self)
