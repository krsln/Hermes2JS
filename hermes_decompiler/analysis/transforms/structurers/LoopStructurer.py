from __future__ import annotations

from hermes_decompiler.analysis.models.regions import SequenceRegion, LoopRegion
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

    Ordering within a loop's own body (bug fix)
    --------------------------------------------
    `_build_loop` must place two kinds of items directly into
    `region.body`: plain "loose" blocks the loop owns directly (most
    commonly its own latch/increment block), and nested child loops
    (built recursively). These need to end up in `region.body` in
    their real relative source order - a loop's own latch/increment
    code almost always comes AFTER any loop nested inside it, since
    it's textually the loop's last statement.

    An earlier version of this method moved every loose block first
    (in a single pass over `sorted(loop.members, key=id)`, skipping
    child-owned members) and only afterward recursed into
    `loop.children`, appending each child's freshly-built `LoopRegion`
    last, UNCONDITIONALLY - regardless of whether that child loop
    should have appeared before or after the loose blocks just moved.
    Since a loop's own latch is a loose (non-child) member and nearly
    always sits textually after any nested loop, this was silently
    wrong for essentially every doubly-or-more-nested loop: the
    nested loop would end up placed AFTER the outer loop's own
    increment/back-edge test in the region tree, i.e. printed as if
    it ran after the very code that's supposed to run once the
    nested loop has already finished each outer iteration.

    Fixed by computing one merged, id-ordered list of "everything to
    place next" - loose block ids and immediate child loops' header
    ids together - and interleaving `graph.move()` calls with
    recursive `_build_loop()` calls in that single order, instead of
    processing all loose blocks up front and all children last.
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

        self.dump_region_tree_if_debug(type(self).__name__)

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

        children_by_header_id = {}
        child_members = set()

        for child in loop.children:
            children_by_header_id[child.header.id] = child
            child_members.update(child.members)

        loose_blocks_by_id = {
            block.id: block
            for block in loop.members
            if block is not loop.header and block not in child_members
        }

        # One merged, id-ordered worklist covering both kinds of item
        # this loop directly owns - see class docstring for why this
        # single order (rather than "loose blocks, then children")
        # matters.
        ordered_ids = sorted(set(loose_blocks_by_id) | set(children_by_header_id))

        for item_id in ordered_ids:

            child = children_by_header_id.get(item_id)

            if child is not None:
                self._build_loop(child, region.body)
                continue

            self.graph.move(loose_blocks_by_id[item_id], region.body)

    # -------------------------------------------------------------
