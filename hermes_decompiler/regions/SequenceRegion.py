from dataclasses import dataclass, field

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions.Region import Region


@dataclass(slots=True)
class SequenceRegion(Region):
    """
    Linear sequence of basic blocks.
    """

    blocks: list[BasicBlock] = field(default_factory=list)

    def accept(self, visitor):
        return visitor.visit_sequence(self)