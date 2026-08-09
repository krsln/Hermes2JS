from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion, IfRegion
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import BreakStatement

logger = get_logger(__name__)


class LoopBreakStructurer(RegionStructurer):
    """
    Recognizes the CFG shape Hermes emits for a mid-loop `break`:

        <loop body block>:
            if (cond) goto EXIT;   # EXIT is NOT part of loop.members
            ... rest of iteration ...

        EXIT:
            <exit body>
            goto MERGE;            # MERGE == where the loop's own
                                    # back-edge test falls through to
                                    # on normal completion

    and rewrites it in place to:

        <loop body block>:
            if (cond) {
                <exit body>
                break;
            }
            ... rest of iteration ...

    moving `EXIT`'s content bodily from wherever it currently sits
    (a sibling of the LoopRegion, per LoopStructurer/SequenceStructurer)
    into the loop body, and deleting it from its old location.

    Must run AFTER `LoopStructurer` (needs `LoopRegion.body.covered_blocks`
    / `loop.header_block`'s natural CFG successors to know what's inside
    vs. outside the loop) and BEFORE `IfStructurer` (which would otherwise
    permanently strand this block's terminator - see StructuralAnalyzer's
    audit warning for exactly this shape - since a target outside the
    current region is something IfStructurer correctly refuses to guess
    about, by design).

    Deliberately narrow, same philosophy as ForEachRecognizer: only
    matches the single-BasicBlock exit-body case with an unconditional
    trailing jump landing exactly on the loop's natural post-loop
    address. Anything less exact is left as a plain unstructured
    conditional branch rather than guessed at - a missed `break` still
    prints as a raw `if (...) goto label_N;` (readability regression),
    while a wrongly-claimed one would silently relocate and gate code
    that should have stayed unconditional (correctness regression).
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
            self._try_recognize_breaks(region)
            self._visit(region.body)
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

    def _try_recognize_breaks(self, loop: LoopRegion) -> None:
        """
        Repeatedly scan `loop.body.children` for a directly-owned
        BasicBlock matching the break shape, converting one at a time
        (mutation invalidates iteration, so restart the scan after
        each success - same pattern as IfStructurer._structure_sequence).
        """

        failed: set = set()

        while True:
            block = self._find_candidate(loop, failed)

            if block is None:
                return

            if not self._convert(loop, block):
                failed.add(block)

    def _find_candidate(self, loop: LoopRegion, exclude: set) -> BasicBlock | None:

        for item in loop.body.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if item is loop.header_block:
                # Header's own branch is either the loop guard
                # (consumed later by LoopConditionExtractor) or a
                # genuine in-loop if - never itself a break edge in
                # the shapes this pass targets.
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
            # Both inside (ordinary in-loop if) or both outside
            # (shouldn't happen for a block that's itself in the
            # loop) - not the shape this pass handles.
            return False

        if target_inside:
            exit_block, stay_block, condition = fallthrough_block, target_block, _negate_condition(branch.condition)
        else:
            exit_block, stay_block, condition = target_block, fallthrough_block, branch.condition

        if list(exit_block.predecessors) != [block]:
            # Reached some other way too - not a clean single-purpose
            # exit body, don't risk duplicating/misplacing it.
            return False

        exit_owner = self.graph.owner(exit_block)

        if exit_owner is None:
            return False

        exit_terminator = exit_block.terminator

        if not isinstance(exit_terminator, TerminatorJump):
            # Only the single-block, unconditional-trailing-jump shape
            # is handled - see class docstring.
            return False

        natural_merge = self._natural_loop_merge(loop)

        if natural_merge is None or exit_terminator.target != natural_merge:
            # Doesn't land where the loop itself exits to normally -
            # could be a genuine different control-flow shape (e.g. a
            # jump to an unrelated label). Don't guess.
            return False

        # ---- convert `block`'s branch into a structured IfRegion ----

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
        block.terminator = None

        # ---- strip exit_block's trailing jump, append synthetic break ----

        if exit_block.instructions and exit_block.instructions[-1].terminator is exit_terminator:
            break_instr = exit_block.instructions[-1]
            break_instr.terminator = None
            break_instr.value = None
            break_instr.statement = BreakStatement(label=None)
        else:
            return False

        exit_block.terminator = None

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
    def _natural_loop_merge(loop: LoopRegion) -> int | None:
        """
        The address a `break` (or the loop's own normal completion)
        lands on: the target of the loop's back-edge test's
        loop-leaving edge. Found by walking `loop.latches` - each
        latch's out-of-loop successor address is that merge point;
        for the well-formed single-latch loops this pass targets they
        must all agree, so any one is authoritative.
        """
        covered = loop.body.covered_blocks

        for latch in loop.latches:
            for succ in latch.successors:
                if succ not in covered:
                    return succ.address

        return None
