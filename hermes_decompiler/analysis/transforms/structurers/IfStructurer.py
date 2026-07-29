from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.analysis.regions.Regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer


class IfStructurer(RegionStructurer):
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

    Both patterns generalize automatically to `else if` chains and to
    any physical block layout the compiler chose: `then`/`else`
    membership is decided by dominance (see `_convert`), not by
    position in `region.children`, so nested tests, interleaved
    sibling statements, or an else-target placed far from its "then"
    counterpart are all handled without special-casing - each level of
    the chain just becomes its own nested IfRegion once this pass
    revisits `region.children` after the outer one converts.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)

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

        Classifies every item after `block` by DOMINANCE rather than
        physical list position: an item belongs to the "then" side iff
        it's dominated by the fallthrough block (`then_root`), and to
        the "else" side iff dominated by the branch target
        (`else_root`) - regardless of how the compiler physically
        interleaved the two branches' blocks in the flat sequence, and
        regardless of whether `merge_block` happens to sit before or
        after `else_root` in that sequence. The old adjacency-based
        version required `goto_block` to be the literal next item after
        "then" ended, which broke for else-if chains and any layout
        where intervening not-yet-structured blocks (or even an
        unrelated sibling statement) sat between "then" and "else".

        Dominance also subsumes the single-entry check this class used
        to run separately: an item with a predecessor outside its
        claimed side's dominated subtree simply fails the `dominates()`
        test below and this candidate correctly bails.
        """

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        if self.cfg.dominator_tree is None:
            # Can't safely classify anything without it - every caller
            # in this codebase computes it before structuring runs.
            return False

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor at all - can't structure safely.
            return False

        then_root = region.children[then_start]
        then_entry = self._representative_block(then_root)

        merge_block = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(branch.target)

        has_else = (
                goto_block is not None
                and goto_block is not merge_block
        )

        else_root = None
        else_entry = None

        if has_else:

            else_root = self.graph.find_covering_item(region, goto_block)

            if else_root is None or else_root is then_root:
                # goto target isn't reachable as a distinct sibling in
                # this region - bail rather than guess.
                return False

            else_entry = self._representative_block(else_root)

        # -------------------------------------------------------------
        # Classify region.children[then_start:] by dominance until the
        # merge point (or end of region) is reached.
        # -------------------------------------------------------------

        dominators = self.cfg.dominator_tree

        then_items: list = []
        else_items: list = []

        index = then_start
        boundary = len(region.children)

        while index < len(region.children):

            item = region.children[index]

            if item is merge_block:
                boundary = index
                break

            rep = self._representative_block(item)

            if dominators.dominates(then_entry, rep):
                then_items.append(item)

            elif has_else and dominators.dominates(else_entry, rep):
                else_items.append(item)

            else:
                # Neither side dominates this item: it's reachable some
                # other way we don't account for here (e.g. a join we
                # didn't expect). Bail rather than misclassify it.
                return False

            index += 1

        if has_else and not else_items:
            # else_root dominates itself, so it must have been
            # classified above - empty means something upstream is
            # inconsistent. Bail rather than build a broken else.
            return False

        del region.children[then_start:boundary]

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

    @staticmethod
    def _representative_block(item) -> BasicBlock:
        """
        Any single `BasicBlock` that dominance checks against `item`
        can be run on. For a raw `BasicBlock`, that's `item` itself.
        For an already-built region (`IfRegion`/`LoopRegion`/
        `TryRegion`), every block it covers shares the same dominance
        relationship to blocks *outside* it - single-entry regions are
        dominated as a unit, by construction - so any element of
        `covered_blocks` is an equally valid representative.
        """

        if isinstance(item, BasicBlock):
            return item

        return next(iter(item.covered_blocks))
