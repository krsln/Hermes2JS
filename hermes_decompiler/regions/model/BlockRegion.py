from dataclasses import dataclass

from hermes_decompiler.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions.model.Region import Region


@dataclass(slots=True)
class BlockRegion(Region):
    """
    Leaf region wrapping a single BasicBlock.

    NOTE / BUG FIX: the previous version of this class defined no
    `accept()` method. Since `Region.accept` is an `@abstractmethod`
    and BlockRegion inherited from Region without overriding it,
    BlockRegion was *still abstract* - `BlockRegion(block=...)` would
    have raised `TypeError: Can't instantiate abstract class
    BlockRegion with abstract method accept` the moment anything tried
    to construct one. It just never surfaced because nothing in the
    old RegionBuilder ever built one.
    """

    block: BasicBlock

    def accept(self, visitor):
        return visitor.visit_block(self)
