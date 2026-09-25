from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import CatchRegion, IfRegion, LoopRegion, SequenceRegion, TryRegion
from hermes_decompiler.ir.expressions import Expression, Identifier
from hermes_decompiler.ir.expressions.Literals import Literal, TemplateLiteral
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow

TERMINATING_TERMINATORS = (TerminatorReturn, TerminatorThrow)

# Generous bound on how many IfRegion wrappers `_find_loop_nested_home`
# will walk through before reaching a LoopRegion (or giving up). Purely
# a safety net against an unforeseen cyclic/self-referential region
# shape - real nesting depths are always tiny (single digits).
_MAX_LOOP_DESCENT = 20


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

    Loop-nested try bodies
    ----------------------
    `LoopStructurer`/`IfStructurer` both run BEFORE this class (see
    `StructuralAnalyzer`), so by the time a handler is processed here,
    a loop the try's protected range only partially covers has already
    been folded into one opaque `LoopRegion` sibling. The ordinary
    `lowest_common_sequence`-based path below can only ever splice
    whole top-level siblings out of the sequence it's given - handed
    that opaque `LoopRegion` (or an `IfRegion` wrapping it) as the
    try's own `start_repr`, it has no way to take just part of it, so
    it swallows the ENTIRE loop (every iteration, plus the loop's own
    condition/update) into the try. For a `try`/`finally` that sits
    INSIDE a loop's body in the source - protecting one iteration at a
    time, with Hermes duplicating the `finally` inline at each of that
    iteration's normal exits (fallthrough, `continue`, `break`) under
    ONE shared handler - that produces a `finally` that only runs once,
    after the whole loop, instead of once per iteration (see
    `loopBreakCrossesTryBoundaryTest`/section_15089).

    `_find_loop_nested_home` detects this shape ahead of the ordinary
    path: it walks down from `start_repr` through any `IfRegion`
    wrappers to the first `LoopRegion` actually containing
    `start_block`, then measures the protected extent INSIDE that
    loop's own body sequence instead - by address, exactly like
    `_scan_protected_extent` does at the outer level, but additionally
    never crossing into the loop's own latch (back-edge) block, since
    that always holds the loop's condition/update check and is never
    part of one iteration's try body in the source. When found, `build`
    splices the try content out of the loop's body sequence and nests
    the new `TryRegion` there - leaving the `IfRegion`/`LoopRegion`
    wrapper that used to swallow everything untouched around it - while
    the catch/handler side is spliced out exactly as before, from
    wherever `handler_block` actually sits (normally well outside the
    loop entirely, since it's shared, unduplicated cleanup/rethrow
    code). `LoopConditionRegionPass`, which extracts the loop's actual
    `for (...; ...; update)` header, runs well after this
    (`StructuralAnalyzer`'s pass order) and locates the latch/condition
    block by its own `LoopRegion.latches`/`header_block` references
    rather than tree position, so leaving the latch behind as an
    ordinary sibling right after the new `TryRegion` - instead of
    swallowed inside it - doesn't interfere with that later
    classification.

    Doesn't attempt to descend further than one `LoopRegion` (a loop
    nested inside another loop, where the try's real target is the
    INNER one) - `_find_loop_nested_home` simply stops at the first
    `LoopRegion` it reaches from `start_repr`; nothing currently
    exercises a deeper case, and the ordinary top-level path remains
    the safe fallback (unchanged output) whenever no redirect target is
    found, so an unrecognized shape here never regresses past what the
    non-loop-aware code already produced.
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

        # Try the loop-nested redirect FIRST (see class docstring). It
        # only ever fires when `start_repr` actually routes through a
        # `LoopRegion`/`IfRegion` chain down to `start_block` AND that
        # loop's own body sequence yields a genuine protected extent
        # (never both conditions at once by accident) - anything else
        # (no loop on the path, an unrecognized container, an empty
        # extent) returns `None` and falls straight through to the
        # ordinary path below, unchanged.
        loop_home = self._find_loop_nested_home(start_repr, start_block, handler["end"])

        if loop_home is not None:
            body, body_start_idx, body_end_idx = loop_home

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

            # Same ordering requirement as the ordinary path below:
            # the catch content sits in a DIFFERENT sequence (`lca_seq`)
            # than the try content (`body`), so the two splices can't
            # invalidate each other's indices either way - but keeping
            # catch first mirrors the ordinary path for consistency.
            catch_items = self.graph.splice_out(
                lca_seq,
                handler_idx,
                catch_end,
            )

            try_items = self.graph.splice_out(
                body,
                body_start_idx,
                body_end_idx + 1,
            )

            try_region = self._assemble(try_items, catch_items, handler_block)

            self.graph.insert_at(
                body,
                body_start_idx,
                try_region,
            )

            return try_region

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

        try_region = self._assemble(try_items, catch_items, handler_block)

        self.graph.insert_at(
            lca_seq,
            start_idx,
            try_region,
        )

        return try_region

    # -------------------------------------------------------------

    def _assemble(self, try_items: list, catch_items: list, handler_block: BasicBlock) -> TryRegion:
        """Build a `TryRegion` (with a plain `CatchRegion`, no
        `finally` yet) from already-spliced-out try/catch content.

        Shared by both the ordinary same-sequence path and the
        loop-nested redirect in `build` - the two differ only in WHERE
        `try_items` came from and where the resulting region gets
        reinserted, never in how the region itself is assembled.
        """
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

        return try_region

    # -------------------------------------------------------------

    def _find_loop_nested_home(
            self,
            start_repr,
            start_block: BasicBlock,
            handler_end: int,
    ) -> tuple[SequenceRegion, int, int] | None:
        """If `start_repr` routes down to `start_block` through a
        `LoopRegion` (optionally via one or more `IfRegion` wrappers
        first - see `nestedTryCatchFinallyTest`-style shapes where
        IfStructurer already folded an outer guard around the loop),
        return `(body, start_idx, end_idx)` describing where the try's
        real protected content lives INSIDE that loop's own body
        sequence, rather than at the outer level `start_repr` sits at.

        Returns `None` when `start_repr` IS `start_block` (nothing to
        redirect - the ordinary path already operates at the right
        granularity), when the descent hits a container this doesn't
        know how to look inside (a `SwitchRegion`, an already-built
        `TryRegion` from an earlier/narrower handler, etc. - see class
        docstring), or when the loop's body doesn't actually yield a
        non-empty protected extent (e.g. `start_block` sits in the
        loop but not a single instruction of it is `< handler_end` -
        shouldn't normally happen given `start_block` is the handler's
        own first protected block, but this isn't guessed past).
        """
        node = start_repr

        for _ in range(_MAX_LOOP_DESCENT):

            if isinstance(node, LoopRegion):
                body = node.body
                child = self.graph.find_covering_item(body, start_block)

                if child is None:
                    return None

                body_start_idx = body.children.index(child)
                latches = set(node.latches)

                body_end_idx = self._scan_loop_body_protected_extent(
                    body,
                    body_start_idx,
                    handler_end,
                    latches,
                )

                if body_end_idx is None:
                    return None

                return body, body_start_idx, body_end_idx

            if isinstance(node, IfRegion):
                if start_block in node.then_body.covered_blocks:
                    branch = node.then_body
                elif (
                        node.else_body is not None
                        and start_block in node.else_body.covered_blocks
                ):
                    branch = node.else_body
                else:
                    return None

                child = self.graph.find_covering_item(branch, start_block)

                if child is None:
                    return None

                node = child
                continue

            # Not a container this redirect knows how to descend into
            # (includes `node is start_block` itself, on the very first
            # iteration - a plain `BasicBlock` matches neither
            # `isinstance` check above). Every such case is exactly
            # "no redirect" - fall through to the ordinary path.
            return None

        return None

    # -------------------------------------------------------------

    @staticmethod
    def _scan_loop_body_protected_extent(
            body: SequenceRegion,
            start_idx: int,
            handler_end: int,
            latches: set,
    ) -> int | None:
        """`_scan_protected_extent`'s counterpart for a loop's own body
        sequence: extends `end_idx` sibling-by-sibling from `start_idx`
        for as long as each one still has some address `< handler_end`
        (same rule, same rationale - see `_scan_protected_extent`), but
        scans to the end of `body.children` rather than stopping at a
        handler sibling's index (the handler lives in a completely
        different sequence here - see `_find_loop_nested_home`).

        Additionally never crosses into a sibling that IS, or contains,
        one of the loop's own `latches`: the latch always carries the
        loop's condition/update check, which - regardless of what the
        handler's raw protected BYTE range happens to also cover - is
        never part of one iteration's try body in the source (see class
        docstring). Whatever's left at/after the latch simply stays
        behind as an ordinary sibling right after the new `TryRegion`.
        """
        end_idx = None

        for index in range(start_idx, len(body.children)):
            item = body.children[index]

            if isinstance(item, BasicBlock):
                if item in latches:
                    break
                addresses = [item.address]
            else:
                if latches & item.covered_blocks:
                    break
                addresses = [block.address for block in item.covered_blocks]

            if any(address < handler_end for address in addresses):
                end_idx = index
            else:
                break

        return end_idx

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

    def split_trailing_unprotected_content(self, handler: dict, try_region: TryRegion) -> None:
        """Move code that runs AFTER the protected range out of the try
        body, into a sibling block right after the TryRegion.

        The mirror of `_split_leading_unprotected_content`, and it exists
        for the same reason: `CFGBuilder` picks a handler's blocks by
        address-range OVERLAP and only ever splits blocks at handler
        TARGET addresses, so the last protected block can also hold
        instructions at or beyond `handler["end"]` that the handler does
        NOT cover. `try { x = f() } catch (e) { return g(e) } return h(x)`
        compiles to one block holding both `f()` and `h(x)`, protected only
        up to the end of `f()`; left in `try_body`, `h(x)` would be caught
        by the very catch that never covered it.

        Run once, AFTER every handler has been built and after
        finally-recognition (`TryStructurer.run`). Earlier would hide the
        inlined `finally` copy that lives in exactly this tail from
        `_finally_matcher` and `_FinallyAttacher`, which look for it in the
        try body and strip/relocate it themselves; whatever they leave
        behind is what this moves.

        Handlers are processed in ascending `end`, so when an inner and an
        outer try share a last block, the inner's tail lands in the outer's
        try body and is then split again at the outer's own end.

        Only splits when the tail contains something that can actually
        run code (`_is_effectful`). A bare `Jmp`/`Ret` carrier or a plain
        register/literal load changes nothing about which handler covers
        what, so those stay put rather than churning every output.
        """
        try_body = try_region.try_body

        if not try_body.children:
            return

        block = try_body.children[-1]

        if not isinstance(block, BasicBlock):
            return

        instructions = block.instructions

        split_pos = next(
            (i for i, instr in enumerate(instructions) if instr.address >= handler["end"]),
            None,
        )

        # None: the block ends inside the protected range. 0: nothing in
        # it is protected - `CFGBuilder` selected it through a stale
        # block address; not a shape this knows how to repair.
        if not split_pos:
            return

        tail_instructions = instructions[split_pos:]

        if not any(self._is_effectful(instr, block) for instr in tail_instructions):
            return

        parent = try_region.parent

        if not isinstance(parent, SequenceRegion):
            return

        new_id = max((b.id for b in self.cfg.blocks), default=0) + 1

        tail = BasicBlock(new_id, address=tail_instructions[0].address)
        tail.instructions = tail_instructions
        tail.terminator = block.terminator
        tail.successors = list(block.successors)
        tail.predecessors = [block]

        for successor in tail.successors:
            successor.predecessors = [tail if p is block else p for p in successor.predecessors]

        block.instructions = instructions[:split_pos]
        block.terminator = None
        block.successors = [tail]

        self.cfg.blocks.append(tail)

        try_body.invalidate_coverage()

        self.graph.insert_at(parent, parent.children.index(try_region) + 1, tail)

    @staticmethod
    def _is_effectful(instr, block: BasicBlock) -> bool:
        """True if `instr` can run code or observably change state.

        Not effectful: no value at all, the block's own terminator carrier
        (`Jmp`/`Ret`/`Throw`), a bare register read, a literal (template
        literals excepted: they stringify their parts).
        """
        value = instr.value

        if value is None:
            return False

        if instr.terminator is not None and instr.terminator is block.terminator:
            return False

        if isinstance(value, Identifier):
            return False

        if isinstance(value, Literal) and not isinstance(value, TemplateLiteral):
            return False

        return True

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
