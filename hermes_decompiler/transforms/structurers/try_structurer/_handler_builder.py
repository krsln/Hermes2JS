from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import CatchRegion, SequenceRegion, TryRegion
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow

TERMINATING_TERMINATORS = (TerminatorReturn, TerminatorThrow)


class _HandlerBuilder:
    """Builds the base TryRegion/CatchRegion shape from a raw handler.

    Splits the covering sequence into a try body and a catch body via
    the try/handler blocks' lowest common sequence ancestor.

    Purely structural: only decides where the try/catch boundaries
    fall and splices the tree accordingly. Has no concept of finally -
    a handler this builder structures may later be recognized as a
    finally-wrapper (`_finally_matcher`) or reinterpreted as one after
    the fact (`_finally_attacher`), both of which run afterward, in
    `TryStructurer.run`.
    """

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def build(self, handler: dict) -> TryRegion | None:

        try_blocks = handler["try_blocks"]
        handler_block = handler["handler_block"]

        start_block = try_blocks[0]

        lca = self.graph.lowest_common_sequence(
            start_block,
            handler_block,
        )

        if lca is None:
            return None

        lca_seq, start_repr, handler_repr = lca

        if (
                start_repr not in lca_seq.children
                or handler_repr not in lca_seq.children
        ):
            return None

        # `try_blocks` (and so `start_block`) is computed by
        # `CFGBuilder._resolve_exception_handlers` via ADDRESS-RANGE
        # OVERLAP against whole blocks, not exact instruction
        # boundaries - see that method's own docstring: "Hermes
        # records protected ranges at instruction granularity, so a
        # handler range may start or end inside a basic block."
        # `CFGBuilder` only ever splits blocks at exception HANDLER
        # TARGET addresses (`leaders.add(handler["target"])`), never
        # at a handler's own START address - so straight-line code
        # with no branch that happens to run immediately before this
        # handler's real protected range begins can end up sharing the
        # SAME physical block as the try's own first protected
        # instruction (see nestedTryCatchFinallyTest: an unconditional
        # `console.log` right before an inner `try` is literally one
        # block with the try's own first line, split only at the
        # handler's start address, which was never added as a CFG
        # leader). If `start_block` is DIRECTLY a child of `lca_seq`
        # (not already nested inside a Region some earlier-processed
        # handler built), split off any such leading unprotected
        # content BEFORE computing indices below, so they're all
        # computed against the corrected tree. A `start_repr` that
        # ISN'T `start_block` itself means it's already nested inside
        # a prior TryRegion - nothing to split; that content was
        # already resolved correctly when that earlier, narrower
        # handler was processed.
        if start_repr is start_block:
            self._split_leading_unprotected_content(
                lca_seq,
                lca_seq.children.index(start_block),
                start_block,
                handler["start"],
            )

        start_idx = lca_seq.children.index(start_repr)
        handler_idx = lca_seq.children.index(handler_repr)

        if handler_idx <= start_idx:
            return None

        # Determine how far the protected content actually extends by
        # scanning FORWARD from `start_idx` over the CURRENT tree,
        # rather than locating `try_blocks[-1]` (a reference fixed once,
        # up front, by `CFGBuilder`, before any structuring runs).
        #
        # That static reference goes stale the moment EARLIER handler
        # processing has already relocated content that used to sit
        # alongside it - see nestedTryCatchFinallyTest: the inner
        # try/catch/finally's own processing (`_FinallyAttacher`'s tail
        # relocation) splits "after-inner" off of what was originally
        # part of `try_blocks[-1]`'s own block and moves it to a NEW
        # sibling block positioned right after the inner TryRegion.
        # `find_covering_item(lca_seq, try_blocks[-1])` still faithfully
        # locates wherever the ORIGINAL block object ended up (correct
        # in isolation), but has no way to know that a DIFFERENT,
        # newly-created sibling right next to it is ALSO still
        # genuinely protected content that used to travel with it.
        #
        # Scanning current addresses instead is immune to this: it
        # doesn't care how many times content has been split or
        # relocated since `CFGBuilder` ran, only where it, right now,
        # actually falls relative to `handler["end"]`.
        end_idx = self._scan_protected_extent(
            lca_seq,
            start_idx,
            handler_idx,
            handler["end"],
        )

        if end_idx is None:
            return None

        merge_block = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = (
                self.cfg.post_dominator_tree
                .immediate_post_dominator(handler_block)
            )

        stop_at = {merge_block} if merge_block is not None else set()

        catch_end = self._find_catch_boundary(
            lca_seq,
            handler_idx,
            stop_at,
        )

        # Splice out the catch content FIRST (it sits at a position
        # AFTER the try content, per `start_idx <= end_idx < handler_idx`
        # above) - removing it before touching the try span keeps
        # `start_idx`/`end_idx` valid, since nothing before `handler_idx`
        # shifts as a result.
        catch_items = self.graph.splice_out(
            lca_seq,
            handler_idx,
            catch_end,
        )

        # Splice out ONLY the try content genuinely covered by the
        # handler's protected range: `[start_idx, end_idx]`, NOT
        # `[start_idx, handler_idx)`.
        #
        # These two are NOT interchangeable: `end_idx` (from
        # `find_covering_item` against the handler's own real
        # `try_blocks[-1]`) marks where the ACTUAL protected content
        # ends, but `handler_idx` is merely wherever the handler block
        # happens to sit positionally in `lca_seq` - which can be much
        # later. This gap is real, not just a rare edge case: Hermes
        # excludes a `finally`'s own inlined duplicate from the SAME
        # exception's protected range (so it can't recursively
        # re-trigger the handler it's part of), and a `try` wrapping
        # only part of a loop's body (see e.g.
        # loopBreakCrossesTryBoundaryTest, which protects 3 disjoint
        # per-iteration sub-ranges under one shared handler) leaves
        # the loop's own later iterations, its post-loop code, and
        # every one of those per-exit finally duplicates sitting
        # address-wise between the try's real end and the handler
        # block. Using `handler_idx` as the try boundary would sweep
        # all of that genuinely-unprotected code into `try_body`
        # too - it isn't try content, and code that runs unconditionally
        # after the whole loop (like that test's own "end" print and
        # return) would end up nested inside the try/finally it should
        # sit entirely outside of.
        #
        # Whatever sits between `end_idx` and `handler_idx` is
        # deliberately left untouched in `lca_seq` here - once the
        # `TryRegion` is inserted at `start_idx` below, it naturally
        # ends up as an ordinary sibling immediately after it.
        try_items = self.graph.splice_out(
            lca_seq,
            start_idx,
            end_idx + 1,
        )

        try_body = SequenceRegion()
        self.graph.transfer(
            try_items,
            try_body,
        )

        catch_body = SequenceRegion()
        self.graph.transfer(
            catch_items,
            catch_body,
        )

        catch_region = CatchRegion()
        catch_region.exception, catch_region.exception_reg = self._extract_catch_param(handler_block)
        catch_region.body = catch_body
        catch_body.parent = catch_region

        try_region = TryRegion()
        try_region.try_body = try_body
        try_body.parent = try_region

        try_region.catch = catch_region
        catch_region.parent = try_region

        self.graph.insert_at(
            lca_seq,
            start_idx,
            try_region,
        )

        return try_region

    # -------------------------------------------------------------

    @staticmethod
    def _scan_protected_extent(
            lca_seq: SequenceRegion,
            start_idx: int,
            handler_idx: int,
            handler_end: int,
    ) -> int | None:
        """Return the index of the LAST sibling in `lca_seq.children`,
        starting from `start_idx` and stopping before `handler_idx`,
        that still contains at least one block address `< handler_end`.

        See the call site's own comment for why this can't just reuse
        `try_blocks[-1]`'s original block reference. Extends `end_idx`
        sibling-by-sibling for as long as each one still has SOME
        address inside the protected range - covering both an ordinary
        single block and a Region (whose `covered_blocks` may include
        addresses spanning well past `handler_end` for a large nested
        loop/if, but only needs ONE qualifying address to mean "this
        sibling is still, at least partly, protected content").

        Returns None if `start_idx` itself doesn't qualify (nothing
        protected here at all - matches the old code's `None` return
        for an unrecognized shape).
        """
        end_idx = None

        for index in range(start_idx, handler_idx):
            item = lca_seq.children[index]

            if isinstance(item, BasicBlock):
                addresses = [item.address]
            else:
                addresses = [block.address for block in item.covered_blocks]

            if any(address < handler_end for address in addresses):
                end_idx = index
            else:
                break

        return end_idx

    # -------------------------------------------------------------

    def _split_leading_unprotected_content(
            self,
            lca_seq: SequenceRegion,
            start_idx: int,
            start_block: BasicBlock,
            handler_start: int,
    ) -> None:
        """If `start_block` contains instructions BEFORE `handler_start`,
        split them off into a new preceding sibling, so `start_block`
        itself only ever holds the genuinely protected portion from
        here on.

        See the call site's own comment for why this gap exists at
        all (`CFGBuilder` range-overlap block selection, never
        splitting at a handler's own start address).

        A no-op if every instruction in `start_block` already has an
        address `>= handler_start` (the common case - most try blocks
        start cleanly).
        """
        instructions = start_block.instructions

        split_pos = None

        for i, instr in enumerate(instructions):
            if instr.address >= handler_start:
                split_pos = i
                break

        if not split_pos:
            # split_pos is None (no instruction reaches handler_start -
            # shouldn't happen given `try_blocks` selection, but don't
            # guess) or 0 (nothing precedes it) - already correct.
            return

        leading_instructions = instructions[:split_pos]

        new_id = max((b.id for b in self.cfg.blocks), default=0) + 1

        leading_block = BasicBlock(new_id, address=start_block.address)
        leading_block.instructions = leading_instructions

        start_block.instructions = instructions[split_pos:]

        # Register the new block on `cfg.blocks` too - later handlers
        # in the same pass (e.g. `_FinallyAttacher._split_off_tail`)
        # allocate their own new block ids the same way
        # (`max(cfg.blocks) + 1`); leaving this one off that list
        # would let a later allocation collide with it.
        self.cfg.blocks.append(leading_block)

        self.graph.insert_at(lca_seq, start_idx, leading_block)

    # -------------------------------------------------------------

    @staticmethod
    def _extract_catch_param(handler_block: BasicBlock) -> tuple[str, int | None]:

        if not handler_block.instructions:
            return "e", None

        first = handler_block.instructions[0]

        name = (
            first.value.name
            if isinstance(first.value, Identifier)
            else "e"
        )

        reg = first.dest_reg

        if (
                first.dest_reg is not None
                and isinstance(first.value, Expression)
        ):
            handler_block.instructions.pop(0)

        return name, reg

    # -------------------------------------------------------------

    @staticmethod
    def _find_catch_boundary(region: SequenceRegion, start: int, stop_at: set) -> int:

        index = start

        while index < len(region.children):

            item = region.children[index]

            if item in stop_at:
                return index

            if (
                    isinstance(item, BasicBlock)
                    and isinstance(item.terminator, TERMINATING_TERMINATORS)
            ):
                return index + 1

            index += 1

        return index
