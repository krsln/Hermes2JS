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

    def _try_recognize_labeled_exits(self, loop: LoopRegion) -> None:
        """
        Same "find one, convert, restart" shape as
        `LoopBreakStructurer._try_recognize_breaks` - mutation
        invalidates iteration over `loop.body.children`, and a block
        `_convert` declines is added to `failed` so it isn't retried
        forever.
        """

        failed: set = set()

        while True:
            block = self._find_candidate(loop, failed)

            if block is None:
                return

            if not self._convert(loop, block):
                failed.add(block)

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

    def _convert(self, loop: LoopRegion, block: BasicBlock) -> bool:

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        covered = loop.body.covered_blocks

        target_block = next(
            (s for s in block.successors if s.address == branch.target), None
        )
        fallthrough_candidates = [s for s in block.successors if s is not target_block]
        fallthrough_block = fallthrough_candidates[0] if len(fallthrough_candidates) == 1 else None

        if target_block is None or fallthrough_block is None:
            return False

        target_inside = target_block in covered
        fallthrough_inside = fallthrough_block in covered

        if target_inside == fallthrough_inside:
            # Both inside (ordinary in-loop if) or both outside (not
            # this pass's shape) - `LoopBreakStructurer` already
            # claimed the "leaves THIS loop to its own natural merge"
            # case, earlier in the pipeline.
            return False

        if target_inside:
            exit_block, condition = fallthrough_block, _negate_condition(branch.condition)
        else:
            exit_block, condition = target_block, branch.condition

        if list(exit_block.predecessors) != [block]:
            # Reached some other way too - not a clean single-purpose
            # exit body, don't risk duplicating/misplacing it.
            return False

        if self.graph.owner(exit_block) is None:
            return False

        target_loop, kind = self._find_target_loop(loop, exit_block)

        if target_loop is None:
            # No enclosing loop's latch/merge address matches where
            # this edge actually goes - could be a genuinely different
            # shape (e.g. escaping into unrelated cleanup code, or a
            # skip depth this pass doesn't try to classify). Don't guess.
            return False

        if target_loop.label is None:
            target_loop.label = f"loop_{target_loop.header_block.id}"

        label_node = Identifier(name=target_loop.label)
        statement = (
            ContinueStatement(label=label_node)
            if kind == "continue"
            else BreakStatement(label=label_node)
        )

        # ---- convert `block`'s branch into a structured IfRegion ----

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
        block.terminator = None

        # ---- drop exit_block's own trailing jump, if it has one ----

        exit_terminator = exit_block.terminator

        if isinstance(exit_terminator, TerminatorJump):
            if exit_block.instructions and exit_block.instructions[-1].terminator is exit_terminator:
                exit_block.instructions.pop()
            exit_block.terminator = None
        elif exit_terminator is not None:
            # Some other terminator kind on this "single exit block" -
            # not the shape this pass expects; bail rather than guess.
            return False

        self._append_labeled_statement(exit_block, statement)

        # ---- move exit_block out of its old home, into a fresh then_body ----

        self.graph.extract_block(exit_block)

        then_body = SequenceRegion()
        self.graph.transfer([exit_block], then_body)

        if_region = IfRegion()
        if_region.condition = condition
        if_region.then_body = then_body
        if_region.else_body = None

        insert_at = loop.body.children.index(block) + 1
        self.graph.insert_at(loop.body, insert_at, if_region)

        return True

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

    # -------------------------------------------------------------

    @staticmethod
    def _find_target_loop(inner_loop: LoopRegion, exit_block: BasicBlock):
        """
        Walk every `LoopRegion` enclosing `inner_loop`, nearest first,
        testing whether `exit_block`'s own single CFG successor
        matches that ancestor's latch (a `continue`) or its natural
        merge/exit address (a `break`). Returns `(LoopRegion, "break"
        | "continue")` for the first match, or `(None, None)` if no
        enclosing loop's shape matches - safer to leave the edge
        unconverted than to guess which ancestor was really intended.
        """

        successors = list(exit_block.successors)

        if len(successors) != 1:
            return None, None

        target_address = successors[0].address

        node = inner_loop.parent

        while node is not None:

            if isinstance(node, LoopRegion):

                latch_addresses = {latch.address for latch in node.latches}

                if target_address in latch_addresses:
                    return node, "continue"

                merge_address = LoopLabeledExitStructurer._natural_loop_merge(node)

                if merge_address is not None and target_address == merge_address:
                    return node, "break"

            node = node.parent

        return None, None

    @staticmethod
    def _natural_loop_merge(loop: LoopRegion) -> int | None:
        """
        Same computation as `LoopBreakStructurer._natural_loop_merge`
        (see that class for the full rationale) - duplicated rather
        than imported since it's a small, self-contained static method
        and the two classes are independent siblings, not one
        depending on the other.
        """
        covered = loop.body.covered_blocks

        for latch in loop.latches:
            for succ in latch.successors:
                if succ not in covered:
                    return succ.address

        return None
