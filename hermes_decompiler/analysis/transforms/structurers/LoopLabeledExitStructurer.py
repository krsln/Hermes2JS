from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion, IfRegion
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.statements import BreakStatement, ContinueStatement

logger = get_logger(__name__)


class LoopLabeledExitStructurer(RegionStructurer):
    """
    Recognizes a mid-loop conditional branch whose "leave" edge escapes
    not just the loop it's directly inside (that's `LoopBreakStructurer`'s
    job, for the single-level case), but one or more ENCLOSING loops -
    the CFG shape for a labeled `break`/`continue`
    (`break outer;` / `continue outer;`) targeting an ancestor loop.

    Must run immediately after `LoopBreakStructurer`, still BEFORE
    `IfStructurer`. This ordering isn't just convention - it's load
    bearing: `IfStructurer` only sees region-local siblings when
    classifying a branch's target, so an edge escaping to an ancestor
    loop's sibling scope isn't recognized as "else" at all - it's
    silently collapsed into a same-level `if` with NO else and a
    NEGATED condition, discarding the escape edge entirely. Left alone
    long enough for `LoopConditionRegionPass` to also run, that's not
    just a readability gap - it's a genuine correctness bug: the
    escaping path falls through into the loop's OWN back-edge test
    using whatever loop variable value it had at the moment of escape,
    which was never incremented on that path. Concretely observed
    turning a `continue outer;` into an effectively infinite inner
    loop before this pass existed. Running here, before `IfStructurer`
    ever gets a chance to build that broken shape, avoids it entirely
    rather than needing to detect and repair it afterward.

    For each innermost `LoopRegion` first, and each of its directly
    owned candidate blocks (same shape `LoopBreakStructurer` looks
    for - see that class for the target/fallthrough classification
    this shares), when the "leave" edge does NOT match that loop's own
    natural merge/latch (i.e. `LoopBreakStructurer` already declined
    it), walk every ENCLOSING `LoopRegion` outward and test whether
    the exit block's own single CFG successor address matches that
    ancestor's latch (-> `continue <label>`) or its own natural merge
    (-> `break <label>`). The first ancestor that matches is the
    target; a label is assigned to it (`loop_<header_block_id>`,
    reused if an earlier match already labeled it) and the exit block
    is spliced into the originating branch as the missing arm, ending
    in a synthesized labeled statement.

    Unlike `LoopBreakStructurer`/`LoopContinueRegionPass`, the
    synthesized statement is never forced to commandeer an existing
    terminator-only instruction (the exit block frequently has none -
    Hermes commonly leaves this edge as a bare physical fallthrough
    into the target address rather than an explicit `Jmp`, since nothing
    else was scheduled to run first). Instead a fresh, minimal
    `OpcodeResult` is appended to the exit block, carrying only the
    labeled statement - see `_append_labeled_statement`.

    Deliberately narrow, same philosophy as `LoopBreakStructurer`: only
    the single-BasicBlock exit-body case with a single CFG successor is
    recognized. Anything else is left unconverted rather than guessed
    at.
    """

    def run(self) -> None:
        self._visit(self.graph.root)
        self.dump_region_tree_if_debug(type(self).__name__)

    # -------------------------------------------------------------

    def _visit(self, region) -> None:

        if isinstance(region, SequenceRegion):
            for child in list(region.children):
                self._visit(child)
            return

        if isinstance(region, LoopRegion):
            # Innermost-first: resolve this loop's own escapes only
            # after its nested loops (if any) have already resolved
            # theirs, so an escape that's genuinely only one level
            # deep isn't reconsidered here after its inner structure
            # has already changed shape.
            self._visit(region.body)
            self._try_recognize_labeled_exits(region)
            return

        for attr in ("then_body", "else_body", "body", "try_body"):
            child = getattr(region, attr, None)
            if child is not None:
                self._visit(child)

        catch = getattr(region, "catch", None)
        if catch is not None:
            self._visit(catch.body)

        finally_ = getattr(region, "finally_", None)
        if finally_ is not None:
            self._visit(finally_.body)

    # -------------------------------------------------------------

    def _find_candidate(self, loop: LoopRegion, exclude: set) -> BasicBlock | None:
        """
        Unlike `LoopBreakStructurer._find_candidate`, the loop's own
        HEADER is not excluded here. `LoopBreakStructurer` excludes it
        because a header's own branch is nearly always that loop's
        own continuation guard - but for a labeled exit, the header
        can just as easily be the actual source of the escaping edge
        (see e.g. `labeledContinueTest`'s inner loop: the header tests
        `j === 1` and escapes directly to an ancestor's latch on that
        edge). Safety against misclassifying a genuine loop guard as
        an escape doesn't come from excluding the header - it comes
        from `_find_target_loop` below, which only ever matches when
        the edge's target address equals an ANCESTOR loop's own
        latch/merge address. A normal guard's exit edge leads to
        unrelated code in a completely different part of the CFG, so
        it essentially never collides with an ancestor's addresses by
        construction, and `_convert` cleanly bails (returns False,
        leaving the block untouched) whenever it doesn't.
        """

        for item in loop.body.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if isinstance(item.terminator, TerminatorConditionalBranch):
                return item

        return None

    def _try_recognize_labeled_exits(self, loop: LoopRegion) -> None:
        failed: set = set()
        while True:
            # Collect ALL candidates first (stable snapshot), then try one.
            candidates = []
            for item in list(loop.body.children):
                if not isinstance(item, BasicBlock):
                    continue
                if item in failed:
                    continue
                if isinstance(item.terminator, TerminatorConditionalBranch):
                    candidates.append(item)

            if not candidates:
                return

            converted_any = False
            for block in candidates:
                if self._convert(loop, block):
                    converted_any = True
                    break  # body mutated — restart full scan
                failed.add(block)

            if not converted_any:
                return

    def _convert(self, loop: LoopRegion, block: BasicBlock) -> bool:
        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        covered = loop.body.covered_blocks

        target_block = next(
            (s for s in block.successors if s.address == branch.target), None
        )
        fallthrough = [s for s in block.successors if s is not target_block]
        if target_block is None or len(fallthrough) != 1:
            return False
        fallthrough_block = fallthrough[0]

        target_inside = target_block in covered
        fallthrough_inside = fallthrough_block in covered
        if target_inside == fallthrough_inside:
            return False

        if target_inside:
            exit_block, condition = fallthrough_block, _negate_condition(branch.condition)
        else:
            exit_block, condition = target_block, branch.condition

        # ---- CRITICAL: natural exit of THIS loop is not a labeled exit ----
        # For nested loops, inner's natural merge address == parent's latch.
        # Without this filter those edges become spurious `continue parent`.
        natural_merge = self._natural_loop_merge(loop)
        exit_addrs = {exit_block.address}
        for s in exit_block.successors:
            exit_addrs.add(s.address)


        # Also skip if this block is one of the current loop's own latches
        # (back-edge test belongs to LoopConditionRegionPass / LoopBreak).
        if block in getattr(loop, "latches", ()):
            return False

        target_loop, kind = self._find_target_loop_for_address(loop, exit_block.address)
        if target_loop is None and len(list(exit_block.successors)) == 1:
            target_loop, kind = self._find_target_loop_for_address(
                loop, list(exit_block.successors)[0].address
            )

        if target_loop is None or target_loop is loop:
            logger.debug(
                "LLExit no-match block=%s exit=%s addr=%s",
                block.id, exit_block.id, exit_block.address,
            )
            return False

        if target_loop.label is None:
            target_loop.label = f"loop_{target_loop.header_block.id}"

        label_node = Identifier(name=target_loop.label)
        statement = (
            ContinueStatement(label=label_node)
            if kind == "continue"
            else BreakStatement(label=label_node)
        )

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
        block.terminator = None

        synth_id = self._allocate_block_id()
        synth = BasicBlock(synth_id, address=0)
        self._append_labeled_statement(synth, statement)

        then_body = SequenceRegion()
        self.graph.transfer([synth], then_body)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = None

        insert_at = loop.body.children.index(block) + 1
        self.graph.insert_at(loop.body, insert_at, if_region)

        if hasattr(self.graph, "remove_edge"):
            self.graph.remove_edge(block, exit_block)
        else:
            block.successors = [s for s in block.successors if s is not exit_block]
            exit_block.predecessors = [
                p for p in exit_block.predecessors if p is not block
            ]

        logger.debug(
            "LLExit OK block=%s -> %s %s (header=%s)",
            block.id, kind, target_loop.label, target_loop.header_block.id,
        )
        return True

    def _allocate_block_id(self) -> int:
        if not hasattr(self, "_synth_id_counter"):
            max_id = 0
            cfg = getattr(self, "cfg", None)
            if cfg is not None and hasattr(cfg, "blocks"):
                for b in cfg.blocks:
                    if b.id > max_id:
                        max_id = b.id
            self._synth_id_counter = max_id + 1
        bid = self._synth_id_counter
        self._synth_id_counter += 1
        return bid

    @staticmethod
    def _find_target_loop_for_address(inner_loop: LoopRegion, target_address: int):
        node = inner_loop.parent
        while node is not None:
            if isinstance(node, LoopRegion):
                latch_addrs = {latch.address for latch in node.latches}
                if target_address in latch_addrs:
                    return node, "continue"

                header_addr = getattr(node.header_block, "address", None)
                if header_addr is not None and target_address == header_addr:
                    return node, "continue"

                merge = LoopLabeledExitStructurer._natural_loop_merge(node)
                if merge is not None and target_address == merge:
                    return node, "break"

            node = node.parent
        return None, None

    @staticmethod
    def _find_target_loop(inner_loop: LoopRegion, exit_block: BasicBlock):
        succs = list(exit_block.successors)
        if len(succs) != 1:
            return None, None
        target_address = succs[0].address

        node = inner_loop.parent
        while node is not None:
            if isinstance(node, LoopRegion):
                latch_addrs = {latch.address for latch in node.latches}

                # continue: must land on a latch of this ancestor
                if target_address in latch_addrs:
                    return node, "continue"

                # continue (alt): some Hermes builds jump to the header
                # of the target loop for continue. Accept only if header
                # is not also a latch of a deeper loop we already passed.
                header_addr = getattr(node.header_block, "address", None)
                if header_addr is not None and target_address == header_addr:
                    return node, "continue"

                # break: natural merge (first successor of any latch that
                # leaves the loop body)
                merge = LoopLabeledExitStructurer._natural_loop_merge(node)
                if merge is not None and target_address == merge:
                    return node, "break"

            node = node.parent
        return None, None

    @staticmethod
    def _resolve_exit_target_address(exit_block: BasicBlock) -> int | None:
        """
        Follow a chain of pure jump blocks (no real instructions, single
        successor) to the real destination address. Hermes often emits a
        bare physical fallthrough or a one-instruction Jmp block between
        the conditional and the ancestor latch/merge.
        """
        seen: set[int] = set()
        current = exit_block

        while True:
            if id(current) in seen:
                return None
            seen.add(id(current))

            succs = list(current.successors)
            if len(succs) != 1:
                # Not a pure forward edge — use this block's own address
                # only if we never moved (caller will decide).
                return current.address if current is exit_block else None

            # Pure jump / empty block → keep walking.
            has_real_work = any(
                getattr(ins, "statement", None) is not None
                or (getattr(ins, "terminator", None) is not None
                    and not isinstance(getattr(ins, "terminator", None), TerminatorJump))
                for ins in (current.instructions or [])
            )
            # Also treat "only a TerminatorJump" as pure.
            only_jump = (
                    current.terminator is not None
                    and isinstance(current.terminator, TerminatorJump)
                    and (
                            not current.instructions
                            or (
                                    len(current.instructions) == 1
                                    and current.instructions[-1].terminator is current.terminator
                            )
                    )
            )

            if current is not exit_block and (has_real_work and not only_jump):
                # Landed on a block that does real work — that address is the target.
                return current.address

            nxt = succs[0]
            # Stop when successor looks like a loop header / latch candidate
            # (multiple preds or already visited); still return its address.
            if nxt is current:
                return current.address

            # Prefer the successor address when we are still on a pure edge.
            if only_jump or current is exit_block:
                current = nxt
                continue

            return current.address

    @staticmethod
    def _natural_loop_merge(loop: LoopRegion) -> int | None:
        covered = loop.body.covered_blocks
        for latch in loop.latches:
            for succ in latch.successors:
                if succ not in covered:
                    return succ.address
        return None

    # -------------------------------------------------------------

    @staticmethod
    def _append_labeled_statement(block: BasicBlock, statement) -> None:
        """
        Appends a fresh, minimal `OpcodeResult` carrying only
        `statement` - unlike `LoopBreakStructurer`/
        `LoopContinueRegionPass`, which always commandeer an EXISTING
        terminator-bearing instruction, this pass can't assume one
        exists (see class docstring). `hex_address=""` is safe -
        `OpcodeEntry._safe_parse_address` maps an empty/invalid address
        string to `0` rather than raising; nothing downstream keys off
        this synthetic entry's address. `bytecode` is only ever shown
        in `--verbose` output as a human-readable marker.
        """

        entry = OpcodeEntry(
            bytecode=f"<synthetic>: {type(statement).__name__}",
            hex_address="",
        )

        block.instructions.append(OpcodeResult(entry, statement=statement))
