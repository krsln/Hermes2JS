from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionGraph import RegionGraph
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion, TryRegion,
)
from hermes_decompiler.analysis.regions.Statements import IfGotoStatement
from hermes_decompiler.analysis.transforms.structurers._negation import _negate_condition


class IfStructurer:
    """
    Converts conditional-jump-terminated basic blocks (whose last
    instruction carries an `IfGotoStatement`) into real `IfRegion`s with
    `then_body`/`else_body`.

    Two bytecode shapes are recognized, both driven by
    `cfg.post_dominator_tree.immediate_post_dominator(block)` (the
    merge point where control reconverges after the branch):

        1. No else - the jump target IS the merge point:

               if (C) goto MERGE;
               <fallthrough-body>
               MERGE:

           `C` true means "skip fallthrough-body entirely". The natural
           JS "then" is therefore the fallthrough-body, taken when `C`
           is false - shown as `if (!C) { <fallthrough-body> }`
           (negated; see `_negate_condition`).

        2. If/else - the jump target is a distinct block that itself
           reconverges at MERGE:

               if (C) goto ELSE;
               <fallthrough-body>
               [goto MERGE]
               ELSE:
               <else-body>
               MERGE:

           `C` true genuinely leads into the jump target's code, so no
           negation is needed: `if (C) { <jump-target body> } else {
           <fallthrough-body> }`.

    Loop header blocks are passed in via `exclude` and left untouched:
    their terminal `IfGotoStatement` is consumed later by
    `LoopConditionExtractor` to build the loop's `while (...)` header,
    and `StructuralAnalyzer` runs this class before that extraction -
    converting the header here would remove the instruction
    `LoopConditionExtractor` expects to find.

    Where the algorithm can't confidently determine a branch boundary
    (e.g. an unexpected block ordering), it leaves the block untouched
    rather than guessing - the raw `if (...) goto label_N;` line still
    renders correctly on its own, just unstructured.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

        self._address_to_block = {
            block.first.opcode.address: block
            for block in cfg.blocks
            if block.instructions
        }

    def run(self):
        self._visit(self.graph.root, exclude=frozenset())

    # ------------------------------------------------------------------
    # Tree walk
    # ------------------------------------------------------------------

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

    # ------------------------------------------------------------------
    # Finding + converting candidates
    # ------------------------------------------------------------------

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

            target = self._find_candidate(region, exclude | failed)

            if target is None:
                return

            if not self._convert(region, target):
                failed.add(target)

    def _find_candidate(self, region: SequenceRegion, exclude: frozenset) -> BasicBlock | None:

        for item in region.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if not item.instructions:
                continue

            last = item.instructions[-1]

            if isinstance(last.statement, IfGotoStatement):
                return item

        return None

    def _convert(self, region: SequenceRegion, block: BasicBlock) -> bool:
        """
        Returns True if `block` was converted into an IfRegion, False
        if it was left untouched (see `_structure_sequence` for why the
        return value matters).
        """

        header_result = block.instructions[-1]
        goto_stmt: IfGotoStatement = header_result.statement

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor at all - can't structure safely.
            return False

        merge_block = None
        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(goto_stmt.target)

        has_else = goto_block is not None and goto_block is not merge_block

        # -------------------------------------------------------------
        # Find the boundary between "then" and (optional) "else"/merge.
        # -------------------------------------------------------------

        stop_at_first = {b for b in (merge_block, goto_block if has_else else None) if b is not None}
        then_end = self._find_boundary(region, then_start, stop_at_first)

        if has_else:

            else_start = then_end

            if else_start >= len(region.children) or region.children[else_start] is not goto_block:
                # goto target isn't where expected right after "then" -
                # bail out rather than guess incorrectly.
                return False

            stop_at_second = {merge_block} if merge_block is not None else set()
            else_end = self._find_boundary(region, else_start, stop_at_second)

        else:
            else_start = then_end
            else_end = then_end

        # -------------------------------------------------------------
        # Splice the collected ranges out of `region.children`.
        # -------------------------------------------------------------

        then_items = region.children[then_start:then_end]
        else_items = region.children[else_start:else_end]

        del region.children[then_start:else_end]

        then_body = SequenceRegion()
        else_body = SequenceRegion() if has_else else None

        if has_else:
            # fallthrough -> else, goto target -> then (see class docstring)
            self.graph.transfer(then_items, else_body)
            self.graph.transfer(else_items, then_body)
            condition_expr = goto_stmt.condition
        else:
            # fallthrough -> then, negated condition (see class docstring)
            self.graph.transfer(then_items, then_body)
            condition_expr = _negate_condition(goto_stmt.condition)

        if_region = IfRegion()
        if_region.condition = condition_expr
        if_region.then_body = then_body
        if_region.else_body = else_body

        # Drop the header's own terminal jump instruction - its meaning
        # is now carried by `if_region.condition`; any earlier
        # instructions in `block` still render normally right before it.
        block.instructions.pop()

        insert_at = region.children.index(block) + 1
        region.children.insert(insert_at, if_region)
        if_region.parent = region

        return True

    def _find_boundary(self, region: SequenceRegion, start: int, stop_at: set) -> int:
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
