from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    Region,
    SequenceRegion,
)


class RegionGraph:

    def __init__(self, root: SequenceRegion):

        self.root = root
        self.block_owner: dict[BasicBlock, SequenceRegion] = {}
        self._index(root)

    # ---------------------------------------------------------
    # Indexing (block -> direct SequenceRegion owner)
    # ---------------------------------------------------------

    def _index(self, region):

        if isinstance(region, SequenceRegion):
            for child in region.children:
                if isinstance(child, BasicBlock):
                    self.block_owner[child] = region
                else:
                    self._index(child)
            return

        if hasattr(region, "body"):
            self._index(region.body)
        if hasattr(region, "then_body"):
            self._index(region.then_body)
        if getattr(region, "else_body", None):
            self._index(region.else_body)
        if hasattr(region, "try_body"):
            self._index(region.try_body)
        if getattr(region, "catch", None):
            self._index(region.catch)
        if getattr(region, "finally_", None):
            self._index(region.finally_)

    def owner(self, block: BasicBlock) -> SequenceRegion | None:
        return self.block_owner.get(block)

    # ---------------------------------------------------------
    # Coverage-based lookup - the replacement for the old
    # _build_paths/_find_lca/_representative_in trio.
    # ---------------------------------------------------------

    def find_covering_item(self, sequence: SequenceRegion, block: BasicBlock):
        """
        Returns the direct child of `sequence` (a raw `BasicBlock`, or
        whatever `Region` now contains it - a `LoopRegion`, `IfRegion`,
        `TryRegion`, etc) whose subtree covers `block`, or `None` if
        `block` isn't reachable from `sequence` at all.

        O(children) via `covered_blocks`, no tree walking.
        """

        for item in sequence.children:

            if item is block:
                return item

            if isinstance(item, BasicBlock):
                continue

            if block in item.covered_blocks:
                return item

        return None

    def lowest_common_sequence(self, block_a, block_b):
        owner_a = self.owner(block_a)

        seq = owner_a
        depth = 0
        while seq is not None:
            contains_b = block_b in seq.covered_blocks
            if contains_b:
                repr_a = self.find_covering_item(seq, block_a)
                repr_b = self.find_covering_item(seq, block_b)
                if repr_a is not None and repr_b is not None:
                    return seq, repr_a, repr_b

            next_seq = seq.parent if isinstance(seq.parent, SequenceRegion) else self._enclosing_sequence(seq)
            seq = next_seq
            depth += 1
            if depth > 20:
                break

        print("DEBUG returning None")
        return None

    def _sequence_contains_block(self, seq: SequenceRegion, block: BasicBlock) -> bool:
        return block in seq.covered_blocks

    def _enclosing_sequence(self, region: Region) -> SequenceRegion | None:
        """Walks .parent up until hitting a SequenceRegion (region.parent
        may be a LoopRegion/IfRegion/etc, not directly a sequence)."""

        current = region.parent

        while current is not None and not isinstance(current, SequenceRegion):
            current = current.parent

        return current

    # ---------------------------------------------------------
    # Mutation primitives - ALL structural changes to the tree must
    # go through these, since they're the only places that call
    # invalidate_coverage(). A structurer that mutates
    # region.children directly (bypassing these) will silently
    # desync covered_blocks from reality.
    # ---------------------------------------------------------

    def detach(self, block: BasicBlock):
        owner = self.block_owner.get(block)
        if owner is None:
            return
        owner.children.remove(block)
        owner.invalidate_coverage()
        del self.block_owner[block]

    def append(self, sequence: SequenceRegion, block: BasicBlock):
        sequence.children.append(block)
        block.parent = sequence
        self.block_owner[block] = sequence
        sequence.invalidate_coverage()

    def move(self, block: BasicBlock, sequence: SequenceRegion):
        self.detach(block)
        self.append(sequence, block)

    def insert_before(self, target: BasicBlock, region: Region):
        owner = self.block_owner[target]
        index = owner.children.index(target)
        owner.children.insert(index, region)
        region.parent = owner
        owner.invalidate_coverage()

    def replace(self, old, new):
        owner = old.parent
        idx = owner.children.index(old)
        owner.children[idx] = new
        new.parent = owner
        owner.invalidate_coverage()

    def replace_block(self, old: BasicBlock, new: Region) -> None:
        owner = self.owner(old)
        if owner is None:
            raise RuntimeError("Block has no owner")
        idx = owner.children.index(old)
        owner.children[idx] = new
        new.parent = owner
        owner.invalidate_coverage()
        del self.block_owner[old]

    def remove_block_reference(self, block: BasicBlock):
        owner = self.block_owner.get(block)
        if owner and block in owner.children:
            owner.children.remove(block)
            owner.invalidate_coverage()

    def extract_block(self, block):
        owner = self.owner(block)
        if owner:
            owner.children.remove(block)
            owner.invalidate_coverage()
        del self.block_owner[block]

    def transfer(self, items: list, target: SequenceRegion) -> None:
        for item in items:
            if isinstance(item, BasicBlock):
                self.block_owner[item] = target
            else:
                item.parent = target
            target.children.append(item)

        target.invalidate_coverage()

    def splice_out(self, sequence: SequenceRegion, start_idx: int, end_idx: int) -> list:
        """
        Removes and returns sequence.children[start_idx:end_idx],
        invalidating coverage exactly once. Prefer this over raw
        `del sequence.children[a:b]` so mutation always goes through
        one audited path.
        """
        removed = sequence.children[start_idx:end_idx]
        del sequence.children[start_idx:end_idx]
        sequence.invalidate_coverage()
        return removed

    def insert_at(self, sequence: SequenceRegion, index: int, item) -> None:
        sequence.children.insert(index, item)
        if isinstance(item, Region):
            item.parent = sequence
        elif isinstance(item, BasicBlock):
            self.block_owner[item] = sequence
        sequence.invalidate_coverage()

    def blocks(self):
        return list(self.block_owner.keys())

    def contains(self, block: BasicBlock) -> bool:
        return block in self.block_owner