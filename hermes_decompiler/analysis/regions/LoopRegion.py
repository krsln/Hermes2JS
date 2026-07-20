from dataclasses import dataclass

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.analysis.Region import Region


@dataclass(slots=True)
class LoopRegion(Region):
    """
    Natural loop region.
    Detected from back-edges in CFG (header dominated by latch).
    """

    header: BasicBlock
    latch: BasicBlock
    body: Region
    condition: str | None = None  # for while/for

    def accept(self, visitor):
        return visitor.visit_loop(self)