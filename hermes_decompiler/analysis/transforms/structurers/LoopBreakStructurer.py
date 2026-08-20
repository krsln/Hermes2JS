from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import SequenceRegion, LoopRegion, IfRegion
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import BreakStatement

logger = get_logger(__name__)


class LoopBreakStructurer(RegionStructurer):
    """
    Converts a mid-loop conditional exit into a structured `break`.

    Recognized shape:

        <loop body block>:
            if (cond) goto EXIT;   # EXIT is outside loop.members
            ...

        EXIT:
            <exit body>
            goto MERGE;            # loop's own back-edge exit target

    Rewritten to:

        <loop body block>:
            if (cond) {
                <exit body>
                break;
            }
            ...

    Must run after LoopStructurer (needs loop.body.covered_blocks) and
    before IfStructurer, which would otherwise consume the branch as
    an ordinary conditional and strand it - see StructuralAnalyzer's
    unstructured-block audit.

    Deliberately narrow: only a single-block exit body with an
    unconditional trailing jump to the loop's natural post-loop
    address is matched. Anything else is left as an unstructured
    conditional branch rather than guessed at.
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

        # IfRegion (created by this pass itself, on an earlier
        # candidate) is the only other region kind reachable at this
        # point in the pipeline. then_body/else_body/body/try_body
        # covers it; the catch/finally checks below are defensive -
        # TryStructurer has not run yet, so TryRegion cannot exist
        # here in the current pipeline order.
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
        Converts one break candidate at a time in loop.body.children,
        restarting the scan after each conversion since mutation
        invalidates iteration.
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
                # The header's own branch is either the loop guard
                # (consumed later by LoopConditionRegionPass) or a
                # genuine in-loop if - never a break edge here.
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
            logger.debug(
                "LoopBreakStructurer: block %d's exit target %d has other "
                "predecessors; skipping.", block.id, exit_block.id,
            )
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
        else:
            # Invariant violated: the branch we're converting isn't
            # owned by block's last instruction. Bail rather than
            # clear block.terminator while leaving a stale
            # branch-owning instruction behind.
            logger.warning(
                "LoopBreakStructurer: block %d's terminator instruction "
                "was not found where expected; aborting conversion.",
                block.id,
            )
            return False

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
        Address a `break` (or the loop's own normal completion) lands
        on: the loop-leaving successor of the loop's back-edge
        test(s). Returns None unless every latch agrees on the same
        address - disagreement signals an irregular loop shape this
        pass should not guess about.
        """
        covered = loop.body.covered_blocks

        merge_addresses = {
            succ.address
            for latch in loop.latches
            for succ in latch.successors
            if succ not in covered
        }

        if len(merge_addresses) != 1:
            return None

        return merge_addresses.pop()
