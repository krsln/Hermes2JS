from __future__ import annotations

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions_new.models.Regions import (
    Region,
    SequenceRegion,
)


class RegionGraph:

    def __init__(self, root: SequenceRegion):

        self.root = root

        # BasicBlock -> owner SequenceRegion
        self.block_owner: dict[BasicBlock, SequenceRegion] = {}

        self._index(root)

    # ---------------------------------------------------------
    def _index(self, region):

        if isinstance(region, SequenceRegion):

            for child in region.children:

                if isinstance(child, BasicBlock):

                    self.block_owner[child] = region

                elif isinstance(child, Region):

                    self._index(child)

            return

        if hasattr(region, "body"):
            self._index(region.body)

        if hasattr(region, "then_body"):
            self._index(region.then_body)

        if getattr(region, "else_body", None):
            self._index(region.else_body)

    # ---------------------------------------------------------

    def detach(self, block: BasicBlock):

        owner = self.block_owner.get(block)

        if owner is None:
            return

        owner.children.remove(block)

        del self.block_owner[block]

    # ---------------------------------------------------------

    def insert_before(
            self,
            target: BasicBlock,
            region: Region,
    ):

        owner = self.block_owner[target]

        index = owner.children.index(target)

        owner.children.insert(index, region)

        region.parent = owner

    # ---------------------------------------------------------

    def append_to(
            self,
            sequence: SequenceRegion,
            block: BasicBlock,
    ):

        sequence.children.append(block)

        self.block_owner[block] = sequence

    # ---------------------------------------------------------

    def replace(
            self,
            old: Region,
            new: Region,
    ):

        owner = old.parent

        if owner is None:
            raise RuntimeError("Region has no parent")

        index = owner.children.index(old)

        owner.children[index] = new

        new.parent = owner

    # ---------------------------------------------------------

    def move(
            self,
            block: BasicBlock,
            sequence: SequenceRegion,
    ):

        self.detach(block)

        self.append_to(sequence, block)

    # ---------------------------------------------------------

    def blocks(self):

        return list(self.block_owner.keys())

    # ---------------------------------------------------------

    def owner(
            self,
            block: BasicBlock,
    ) -> SequenceRegion | None:

        return self.block_owner.get(block)

    # ---------------------------------------------------------

    def contains(
            self,
            block: BasicBlock,
    ) -> bool:

        return block in self.block_owner
