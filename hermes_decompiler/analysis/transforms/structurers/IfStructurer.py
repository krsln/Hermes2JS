from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.regions.Regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.analysis.transforms.structurers._negation import _negate_condition


class IfStructurer:
    """
    Converts BasicBlocks terminated by a ConditionalBranch into
    structured IfRegions.

    Two CFG patterns are recognized:

        1. No else

               if (C) goto MERGE;
               THEN
               MERGE:

           becomes

               if (!C) {
                   THEN
               }

        2. If / Else

               if (C) goto ELSE;
               THEN
               goto MERGE;

               ELSE:
               ELSE_BODY

               MERGE:

           becomes

               if (C) {
                   ELSE_BODY
               } else {
                   THEN
               }

    Loop header blocks are excluded because their ConditionalBranch is
    consumed later by LoopConditionExtractor when building while/do-while
    regions.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

        self._address_to_block = {
            block.address: block
            for block in cfg.blocks
        }

    # -------------------------------------------------------------

    def run(self):
        self._visit(self.graph.root, exclude=frozenset())

    # -------------------------------------------------------------
    # Tree traversal
    # -------------------------------------------------------------

    def _visit(self, region, exclude: frozenset):

        if isinstance(region, SequenceRegion):
            self._structure_sequence(region, exclude)

            for child in region.children:
                self._visit(child, frozenset())

            return

        if isinstance(region, LoopRegion):
            self._visit(region.body, frozenset({region.header_block}))
            return

        if isinstance(region, IfRegion):
            self._visit(region.then_body, frozenset())

            if region.else_body:
                self._visit(region.else_body, frozenset())

            return

        if isinstance(region, TryRegion):
            self._visit(region.try_body, frozenset())

            if region.catch:
                self._visit(region.catch.body, frozenset())

            if region.finally_:
                self._visit(region.finally_.body, frozenset())

            return

        if hasattr(region, "body"):
            self._visit(region.body, frozenset())

    # -------------------------------------------------------------
    # Sequence conversion
    # -------------------------------------------------------------

    def _structure_sequence(self, region: SequenceRegion, exclude: frozenset):
        """
        Repeatedly find and convert the first (leftmost) eligible
        conditional block directly in `region.children`, restarting
        after each conversion since the list is mutated in place.

        Blocks where `_convert` bails out (returns `False` - e.g. no
        fallthrough successor, or an unexpected block ordering) are
        added to `failed` and never retried: without this, `_convert`
        leaves such a block completely unchanged, so the next search
        would find the exact same candidate again and loop forever.
        """

        failed: set = set()

        while True:

            block = self._find_candidate(region, exclude | failed)

            if block is None:
                return

            if not self._convert(region, block):
                failed.add(block)

    # -------------------------------------------------------------

    def _find_candidate(self, region: SequenceRegion, exclude: frozenset) -> BasicBlock | None:

        for item in region.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if isinstance(item.terminator, TerminatorConditionalBranch):
                return item

        return None

    # -------------------------------------------------------------

    def _convert(self, region: SequenceRegion, block: BasicBlock) -> bool:
        """
        Returns True if `block` was converted into an IfRegion, False
        if it was left untouched (see `_structure_sequence` for why the
        return value matters).
        """

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor at all - can't structure safely.
            return False

        merge_block = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(branch.target)

        has_else = (
                goto_block is not None
                and goto_block is not merge_block
        )

        # -------------------------------------------------------------
        # Find the boundary between "then" and (optional) "else"/merge.
        # -------------------------------------------------------------

        stop = {
            b
            for b in (
                merge_block,
                goto_block if has_else else None,
            )
            if b is not None
        }

        then_end = self._find_boundary(region, then_start, stop)

        if has_else:

            else_start = then_end

            if (
                    else_start >= len(region.children)
                    or region.children[else_start] is not goto_block
            ):
                # goto target isn't where expected right after "then" -
                # bail out rather than guess incorrectly.
                return False

            stop_at_second = {merge_block} if merge_block is not None else set()
            else_end = self._find_boundary(region, else_start, stop_at_second)

        else:

            else_start = then_end
            else_end = then_end

        then_items = region.children[then_start:then_end]
        else_items = region.children[else_start:else_end]

        del region.children[then_start:else_end]

        then_body = SequenceRegion()
        else_body = SequenceRegion() if has_else else None

        if has_else:

            self.graph.transfer(then_items, else_body)
            self.graph.transfer(else_items, then_body)

            condition = branch.condition

        else:

            self.graph.transfer(then_items, then_body)

            condition = _negate_condition(branch.condition)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = else_body

        #
        # The ConditionalBranch is now represented by the IfRegion.
        #
        block.instructions.pop()  # TODO: this is the way
        block.terminator = None

        insert_at = region.children.index(block) + 1

        region.children.insert(insert_at, if_region)
        if_region.parent = region

        return True

    # -------------------------------------------------------------

    @classmethod
    def _find_boundary(cls, region: SequenceRegion, start: int, stop_at: set) -> int:
        """
        Walks `region.children` from `start`, returning the index of the
        first item found in `stop_at`, or `len(region.children)` if none
        is found (the branch runs to the end of this region - e.g. both
        sides terminate via return/throw with no common merge point).
        """

        index = start

        while index < len(region.children):

            if region.children[index] in stop_at:
                return index

            index += 1

        return index
