from dataclasses import dataclass
from typing import Optional

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.analysis.Region import Region


@dataclass(slots=True)
class IfRegion(Region):
    """
    Structured if / if-else region.
    Detected using:
    - Block with 2 outgoing edges (true/false)
    - Dominator + post-dominator relations
    """

    condition: str
    then_region: Region
    else_region: Optional[Region] = None
    header_block: BasicBlock | None = None

    def accept(self, visitor):
        return visitor.visit_if(self)

    @classmethod
    def from_header(cls, header: BasicBlock, condition: str,
                    then_region: Region, else_region: Optional[Region] = None):
        return cls(
            condition=condition,
            then_region=then_region,
            else_region=else_region,
            header_block=header
        )
