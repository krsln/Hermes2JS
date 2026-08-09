from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression


class ShortCircuitConditionCfgPass:
    """
    Collapses Hermes' bytecode encoding of a *pure control-flow*
    `&&` / `||` condition into a single branch, before RegionGraph/
    IfStructurer ever see the CFG.

        if (a) goto T;      if (!a) goto ELSE;
        if (b) goto T;      if (!b) goto ELSE;
        ...                 ...

    Both patterns compile the same way at the CFG level: two (or more)
    blocks, each ending in a TerminatorConditionalBranch, all jumping
    to the SAME target, with NOTHING else in between (see
    `_is_pure_test_block`). The branch is taken if EITHER condition is
    true, regardless of whether the source used `&&` or `||` -  De
    Morgan's laws are already baked into which operand got negated by
    JmpTrue/JmpFalse (see Jmp.py). So structurally there is exactly one
    thing to detect: a chain of single-purpose test blocks that all
    share a branch target, and merge them by OR-ing their conditions.

    This is what let ifElseChainTest's `a || b` ("either") test compile
    to two separate blocks (Block1: `if (b) goto label_124`, and later
    Block2/Block3: `if (a) goto label_82` / `if (b) goto label_82`)
    that IfStructurer could never single-entry-validate into one
    IfRegion - label_82 legitimately has two predecessors *in the
    original program*, but only because it's one condition, not two.
    After this pass runs, label_82's predecessors collapse to one
    merged block, and IfStructurer's single-entry check (see
    IfStructurer._is_single_entry) succeeds normally.

    NOT responsible for value-producing `&&`/`||` (e.g. `const x = a
    || b;`, where the bytecode assigns an intermediate register
    instead of just branching): that's `region_passes.BooleanChainFolder`'s
    job, which runs much later, on the already-built region tree, and
    specifically requires the block it folds to end in an assignment
    (`dest_reg is not None`). This pass requires the exact opposite -
    `_is_pure_test_block` rejects any successor that assigns anything
    at all - so the two passes' inputs are structurally disjoint and
    can never both claim the same block. If you're tempted to loosen
    `_is_pure_test_block`'s instruction-count check, re-check that
    disjointness holds first.

    Must run after cfg.compute_loops() (needs loop membership to avoid
    touching loop rotation's duplicated guard/continue tests - see
    _collect_loop_blocks) and before RegionGraph is built.
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self._loop_blocks = self._collect_loop_blocks(cfg)

    # -------------------------------------------------------------

    @staticmethod
    def _collect_loop_blocks(cfg: CFG) -> frozenset:
        """
        Every block that's part of any loop, at any nesting level -
        headers and members alike. `cfg.loop_analysis.loops` holds one
        entry per loop (nested loops included, not just top-level -
        see LoopStructurer, which filters `loop.parent is None` for
        roots specifically, implying the dict already contains every
        loop object).

        Blocks in this set must never participate in a merge, in
        either role (as `block` or as `successor`): loop rotation
        routinely duplicates the same source condition into two
        physically different test blocks (a pre-header guard and an
        in-loop continue check) that both jump forward to the same
        exit target - which looks identical, from a purely local
        two-forward-branches-same-target view, to a genuine `a || b`
        chain, but folding them together destroys the loop (see the
        `nestedLoopTest` regression this guard fixes).

        Returns an empty set if loop analysis hasn't run yet (or found
        no loops) - callers get no loop protection in that case, so
        this must only be used once `cfg.compute_loops()` has already
        run.
        """

        loop_analysis = getattr(cfg, "loop_analysis", None)

        if loop_analysis is None:
            return frozenset()

        loops = getattr(loop_analysis, "loops", None)

        if not loops:
            return frozenset()

        blocks = set()

        for loop in loops.values():
            header = getattr(loop, "header", None)
            if header is not None:
                blocks.add(header)
            blocks.update(getattr(loop, "members", ()) or ())

        return frozenset(blocks)

    # -------------------------------------------------------------

    def run(self) -> None:
        while self._merge_one_pass():
            pass

    # -------------------------------------------------------------

    def _merge_one_pass(self) -> bool:
        """
        Finds and merges the first eligible (block, fallthrough) pair.
        Returns True if a merge happened (caller should re-scan, since
        merging can expose further chains: a||b||c merges pairwise).
        """

        for block in self.cfg.blocks:

            merged = self._try_merge(block)

            if merged:
                return True

        return False

    # -------------------------------------------------------------

    def _try_merge(self, block: BasicBlock) -> bool:

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return False

        if block in self._loop_blocks:
            # Loop header/latch/member - never fold its condition into
            # or out of another block. See _collect_loop_blocks.
            return False

        successor = self._fallthrough(block)

        if successor is None:
            return False

        if successor in self._loop_blocks:
            return False

        if branch.target <= block.address:
            # Backward branch = loop latch/continue test, never a
            # short-circuit && / || chain (those only ever jump
            # forward toward a merge point). Must not touch these -
            # loop structuring / LoopConditionExtractor needs the
            # original per-iteration test blocks intact.
            return False

        if not self._is_pure_test_block(successor):
            # Has real work in it (side effects) - not just a test,
            # can't be folded into `block`'s condition.
            return False

        if list(successor.predecessors) != [block]:
            # Reached from somewhere other than `block`'s fallthrough -
            # not part of the same short-circuit chain.
            return False

        next_branch = successor.terminator

        if not isinstance(next_branch, TerminatorConditionalBranch):
            return False

        if next_branch.target <= successor.address:
            # Same reasoning as the guard on `branch` above - a
            # backward second test means this is loop machinery, not
            # a short-circuit chain, even if the target happens to
            # coincide with `branch.target`.
            return False

        if next_branch.target != branch.target:
            # Different targets - not the same logical condition.
            return False

        self._merge(block, successor, next_branch)
        return True

    # -------------------------------------------------------------

    def _fallthrough(self, block: BasicBlock) -> BasicBlock | None:
        """
        The successor reached when `block`'s branch condition is
        false, i.e. the one that isn't the branch target.
        """

        branch = block.terminator

        candidates = [s for s in block.successors if s.address != branch.target]

        if len(candidates) != 1:
            return None

        return candidates[0]

    # -------------------------------------------------------------

    @staticmethod
    def _is_pure_test_block(block: BasicBlock) -> bool:
        """
        True if `block` contains nothing but its own terminator - i.e.
        it exists solely to evaluate one more condition and branch,
        with no other observable side effects that would be lost if we
        fold it into the preceding block's condition.

        This is also what keeps this pass disjoint from
        `BooleanChainFolder`: any block that assigns a value (the
        pattern *that* pass folds) has more than one instruction here
        and is correctly rejected. See the class docstring's
        "NOT responsible for value-producing &&/||" section before
        loosening this check.
        """

        return len(block.instructions) <= 1

    # -------------------------------------------------------------

    def _merge(
            self,
            block: BasicBlock,
            successor: BasicBlock,
            next_branch: TerminatorConditionalBranch,
    ) -> None:

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        combined_condition = BinaryExpression(
            left=branch.condition,
            operator=LogicalOperator.OR,
            right=next_branch.condition,
        )

        merged_terminator = TerminatorConditionalBranch(
            condition=combined_condition,
            target=branch.target,
        )

        block.terminator = merged_terminator

        # Printer walks `block.instructions` (a list of OpcodeResult),
        # rendering each entry's *own* `.terminator` - not
        # `block.terminator`. CFGBuilder points both at the same
        # object when the block is first built, but they're
        # independent references from here on: updating only
        # `block.terminator` (above) fixes CFG/IfStructurer analysis
        # but leaves the printed text showing the stale, un-merged
        # condition. Find that instruction and update it too.
        for instr in block.instructions:
            if instr.terminator is branch:
                instr.terminator = merged_terminator
                break

        # `successor` had exactly one instruction (its own terminator
        # entry, per _is_pure_test_block) - drop it, it's now folded
        # into block.terminator.
        successor.instructions.clear()

        new_fallthrough = self._fallthrough(successor)

        # -------------------------------------------------------------
        # Rewire edges: block -> {target_block, new_fallthrough},
        # bypassing `successor` entirely.
        # -------------------------------------------------------------

        target_block = None
        for s in block.successors:
            if s.address == branch.target:
                target_block = s
                break

        block.successors = []

        if target_block is not None:
            self._connect(block, target_block)
            if successor in target_block.predecessors:
                target_block.predecessors.remove(successor)

        if new_fallthrough is not None:
            self._connect(block, new_fallthrough)
            if successor in new_fallthrough.predecessors:
                new_fallthrough.predecessors.remove(successor)

        if successor in self.cfg.blocks:
            self.cfg.blocks.remove(successor)

    # -------------------------------------------------------------

    @staticmethod
    def _connect(source: BasicBlock, target: BasicBlock) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)
