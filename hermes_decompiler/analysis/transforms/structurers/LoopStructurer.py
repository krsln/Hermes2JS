from __future__ import annotations

from analysis.loops import NaturalLoop
from hermes_decompiler.analysis.models.regions import LoopRegion, SequenceRegion
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
        """
        Structure all top-level natural loops in the CFG.

        ``cfg.compute_loops()`` must have completed before this pass
        runs because the structurer depends on loop membership and
        nesting information produced by ``LoopAnalysis``.
        """

        loop_analysis = self.cfg.loop_analysis

        if loop_analysis is None:
            raise RuntimeError(
                "LoopStructurer requires loop analysis to be computed "
                "before the structuring pass runs."
            )

        roots = [
            loop
            for loop in loop_analysis.loops.values()
            if loop.is_top_level
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
        """
        Build and insert a ``LoopRegion`` for a natural loop.

        The loop header replaces its original position in
        ``parent_sequence``. The header is then inserted as the first
        element of the new loop body.

        Nested child loops are built recursively, while member blocks
        belonging exclusively to the current loop are moved directly
        into the loop body.

        Args:
            loop: The natural loop to structure.
            parent_sequence: The sequence region that should receive the
                resulting ``LoopRegion``.
        """

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

        children_by_header_id = {
            child.header.id: child
            for child in loop.children
        }

        child_members = {
            block
            for child in loop.children
            for block in child.members
        }

        loose_blocks_by_id = {
            block.id: block
            for block in loop.members
            if block is not loop.header
               and block not in child_members
        }

        # One merged, id-ordered worklist covering both loose blocks
        # and child loops - see class docstring for why this single
        # order matters.
        ordered_ids = sorted(
            set(loose_blocks_by_id)
            | set(children_by_header_id)
        )

        for block_id in ordered_ids:
            child = children_by_header_id.get(block_id)

            if child is not None:
                self._build_loop(child, region.body)
                continue

            block = loose_blocks_by_id[block_id]
            self.graph.move(block, region.body)
