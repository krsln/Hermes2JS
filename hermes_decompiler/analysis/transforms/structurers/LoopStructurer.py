from __future__ import annotations

from analysis.loops import NaturalLoop
from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import SequenceRegion, LoopRegion
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class LoopStructurer(RegionStructurer):
    """
    Wraps each natural loop's header and members in a LoopRegion,
    innermost-first.

    All structural edits go through RegionGraph's mutation primitives
    (append/move/replace_block), so covered_blocks caching stays
    correct for later passes (IfStructurer, TryStructurer).

    Within a loop's own body, loose blocks (e.g., its latch/increment
    block) and nested child loops are placed in one merged,
    id-ordered sequence rather than "loose blocks first, children
    last": a loop's latch almost always sits textually after any
    loop nested inside it, so processing children last would place
    a nested loop after its enclosing loop's own increment/back-edge
    test.
    """

    def run(self) -> None:

        if self.cfg.loop_analysis is None:
            raise RuntimeError(
                "LoopStructurer requires cfg.compute_loops() to have "
                "run first - loop analysis is a caller precondition."
            )

        roots: list[NaturalLoop] = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        logger.debug("LoopStructurer: building %d top-level loop(s).", len(roots))

        for loop in roots:
            # Build each top-level loop under whatever SequenceRegion
            # currently owns its header block, not unconditionally
            # graph.root - a prior pass (TryStructurer) may have
            # already relocated the header into a try/catch body.
            # Hardcoding root here would strand it there.
            parent_sequence = self.graph.owner(loop.header)

            if parent_sequence is None:
                # Header isn't tracked anywhere yet - fall back to
                # root rather than crashing.
                parent_sequence = self.graph.root

            self._build_loop(loop, parent_sequence)

        self.dump_region_tree_if_debug(type(self).__name__)

    def _build_loop(self, loop: NaturalLoop, parent_sequence: SequenceRegion) -> None:

        region = LoopRegion(loop)

        header_owner = self.graph.owner(loop.header)

        if header_owner is not parent_sequence:
            if header_owner is not None:
                self.graph.move(loop.header, parent_sequence)
            else:
                self.graph.append(parent_sequence, loop.header)

        # Replace the header's slot in parent_sequence with the new
        # LoopRegion, then re-attach the header as the first block
        # inside the loop's own body - its dual role (both "the block
        # that used to sit here" and "the loop's first statement").
        self.graph.replace_block(loop.header, region)
        self.graph.append(region.body, loop.header)

        children_by_header_id: dict[int, NaturalLoop] = {}
        child_members = set()

        for child in loop.children:
            children_by_header_id[child.header.id] = child
            child_members.update(child.members)

        loose_blocks_by_id: dict[int, BasicBlock] = {
            block.id: block
            for block in loop.members
            if block is not loop.header and block not in child_members
        }

        # One merged, id-ordered worklist covering both loose blocks
        # and child loops - see class docstring for why this single
        # order matters.
        ordered_ids = sorted(set(loose_blocks_by_id) | set(children_by_header_id))

        for item_id in ordered_ids:

            child = children_by_header_id.get(item_id)

            if child is not None:
                self._build_loop(child, region.body)
                continue

            self.graph.move(loose_blocks_by_id[item_id], region.body)
