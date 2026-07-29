from __future__ import annotations

import logging

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion, Region
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class LoopStructurer(RegionStructurer):
    """
    Wraps each natural loop's header + members in a `LoopRegion`,
    innermost-first via recursion into `loop.children`.

    Every structural edit goes through `RegionGraph`'s mutation
    primitives (`append`/`move`/`replace_block`) - never raw
    `region.children`/`block_owner` manipulation - so `covered_blocks`
    caching stays correct for every pass that runs after this one
    (`IfStructurer`, `TryStructurer`, both of which rely on it).
    """

    def run(self) -> None:

        if self.cfg.loop_analysis is None:
            raise RuntimeError(
                "LoopStructurer requires cfg.compute_loops() to have "
                "already run - see StructuralAnalyzer's pipeline "
                "contract (loop analysis is a caller precondition, "
                "not something this pass can silently skip)."
            )

        roots = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        for loop in roots:
            # Build each top-level loop under whatever SequenceRegion
            # currently owns its header block - NOT unconditionally
            # graph.root. A prior pass (TryStructurer) may already have
            # relocated the header (and its would-be members) into a
            # try/catch body's own SequenceRegion; hardcoding root here
            # would silently rip those blocks back out of the try body
            # and re-home the loop at the top level, leaving an empty
            # `try {}` behind. See RegionGraph.owner().
            parent_sequence = self.graph.owner(loop.header)

            if parent_sequence is None:
                # Header isn't tracked anywhere yet (shouldn't normally
                # happen post-SequenceStructurer) - fall back to root
                # rather than crashing.
                parent_sequence = self.graph.root

            self._build_loop(loop, parent_sequence)

        if logger.isEnabledFor(logging.DEBUG):
            logger.debug("===== REGION TREE =====")
            self._dump_region_tree(self.graph.root)

    # -------------------------------------------------------------

    def _build_loop(self, loop, parent_sequence: SequenceRegion) -> None:

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

        child_members = set()

        for child in loop.children:
            child_members.update(child.members)

        for block in sorted(loop.members, key=lambda b: b.id):

            if block is loop.header or block in child_members:
                continue

            self.graph.move(block, region.body)

        for child in sorted(loop.children, key=lambda l: l.header.id):
            self._build_loop(child, region.body)

    def _dump_region_tree(self, node: Region | BasicBlock, indent: int = 0) -> None:
        prefix = " " * indent

        if isinstance(node, SequenceRegion):
            logger.debug("%sSequenceRegion", prefix)
            for child in node.children:
                self._dump_region_tree(child, indent + 4)

        elif isinstance(node, LoopRegion):
            logger.debug("%sLoopRegion(header=%d)", prefix, node.header_block.id)
            self._dump_region_tree(node.body, indent + 4)

        elif isinstance(node, BasicBlock):
            logger.debug("%sBlock %d", prefix, node.id)

        else:
            logger.debug("%s%s", prefix, type(node).__name__)
