from dataclasses import dataclass

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions.Region import Region


@dataclass(slots=True)
class BlockRegion(Region):
    """
    Leaf region wrapping a single BasicBlock.
    """

    block: BasicBlock