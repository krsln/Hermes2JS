from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.core.Exceptions import StructurerInvariantError
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from hermes_decompiler.backend.transforms.shared import negate_condition, TRIVIAL_NODE_TYPES


class ShortCircuitConditionCfgPass:
    """Collapses pure control-flow short-circuit condition chains.

    This pass runs before RegionGraph and IfStructurer and recognizes
    control-flow-only `&&` / `||` expressions lowered into multiple
    conditional test blocks that share a branch target::
        if (a) goto T; if (!a) goto ELSE;
        if (b) goto T; if (!b) goto ELSE;
        ... ...
    The exact source operator is already reflected in the polarity of
    the individual conditions. For example, JmpTrue and JmpFalse may
    negate operands as required by the original short-circuit expression.
    At the CFG level, this pass therefore only needs to recognize a chain
    of single-purpose test blocks whose conditional branches share the
    same target, then combine their conditions into one logical expression.

    This allows source constructs such as `a || b` to be represented as
    one structured condition rather than multiple independent branches.
    Without this normalization, the shared target may have multiple
    predecessors, causing IfStructurer's single-entry validation to reject
    what was originally a single source-level condition. After the chain
    is merged, the shared target has one predecessor and can be structured
    normally.

    This pass handles only control-flow conditions. Value-producing
    short-circuit expressions, such as ``const x = a || b;``
    are handled later by `region_passes.BooleanChainRegionPass`. The two
    passes operate on intentionally disjoint inputs: this pass only merges
    pure test blocks, while BooleanChainRegionPass handles blocks that
    participate in value-producing assignments. Re-check this separation
    before loosening `_is_pure_test_block`.

    The pass must run after `cfg.compute_loops()` so loop blocks can be
    excluded from merging. Loop rotation may duplicate the same source
    condition into separate guard and continue-test blocks that resemble
    a short-circuit chain but must remain structurally distinct.

    It must also run before ``RegionGraph`` is constructed.
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self._loop_blocks = self._collect_loop_blocks(cfg)

    @staticmethod
    def _collect_loop_blocks(cfg: CFG) -> frozenset[BasicBlock]:
        """Return every block that belongs to a discovered loop."""

        loop_analysis = cfg.loop_analysis

        if loop_analysis is None:
            raise StructurerInvariantError(
                "Loop analysis must be computed before "
                "ShortCircuitConditionCfgPass."
            )

        blocks: set[BasicBlock] = set()

        for loop in loop_analysis.loops.values():
            blocks.add(loop.header)
            blocks.update(loop.members)

        return frozenset(blocks)

    def run(self) -> None:
        while self._merge_one_pass():
            pass

    def _merge_one_pass(self) -> bool:
        """Find and merge the first eligible (block, fallthrough) pair.

        Returns True if a merge happened (caller should re-scan, since
        merging can expose further chains: a||b||c merges pairwise).
        """

        for block in self.cfg.blocks:

            merged = self._try_merge(block)

            if merged:
                return True

        return False

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

        pure = self._is_pure_test_block(successor)

        if not pure and not self._is_inlined_setup_block(successor):
            # Has real work in it (side effects) - not just a test,
            # can't be folded into block's condition.
            return False

        if list(successor.predecessors) != [block]:
            # Reached from somewhere other than block's fallthrough -
            # not part of the same short-circuit chain.
            return False

        next_branch = successor.terminator

        if not isinstance(next_branch, TerminatorConditionalBranch):
            return False

        if next_branch.target <= successor.address:
            # Same reasoning as the guard on `branch` above - a
            # backward second test means this is loop machinery, not
            # a short-circuit chain, even if the target happens to
            # coincide with branch.target.
            return False

        if next_branch.target != branch.target or not pure:
            # Different targets: not a same-target chain. It can still be the
            # crossed form (see `_try_merge_crossed`).
            return self._try_merge_crossed(block, successor, next_branch)

        self._merge(block, successor, next_branch)
        return True

    def _try_merge_crossed(self, block, successor, next_branch) -> bool:
        """`if (!a || b) { A } END` compiles to

            X: if (!a) goto A          (first jump lands on the second
            Y: if (b') goto END         test's fall-through)
            A: ...

        `END` is reached exactly when X's test fails and Y's holds, so the
        two blocks are one test `!c1 && c2` jumping to `END`, falling through
        to `A`. The tests may have been given their constants as setup
        (`r3 = "px"; if (r4 !== r3)`) that the condition already inlined.
        """
        branch = block.terminator
        fall_through = self._fallthrough(successor)

        if fall_through is None or fall_through.address != branch.target:
            return False

        if not self._is_inlined_setup_block(successor) or self._setup_feeds_a_join(successor,
                                                                                   self._arm_of(block, branch)):
            return False

        combined = BinaryExpression(
            left=negate_condition(branch.condition),
            operator=LogicalOperator.AND,
            right=next_branch.condition,
        )

        merged = TerminatorConditionalBranch(condition=combined, target=next_branch.target)

        # `block` now jumps to Y's old target and falls through to `A`.
        self._rewire_crossed(block, successor, branch, merged)
        return True

    @staticmethod
    def _is_inlined_setup_block(block: BasicBlock) -> bool:
        """Only constants the test already inlined, plus its own branch."""
        for instr in block.instructions:
            if instr.terminator is not None:
                continue

            if not (instr.definition_used and isinstance(instr.value, TRIVIAL_NODE_TYPES)):
                return False

        return True

    def _arm_of(self, block, branch):
        return next(s for s in block.successors if s.address == branch.target)

    @staticmethod
    def _setup_feeds_a_join(successor: BasicBlock, arm: BasicBlock) -> bool:
        """True if `arm` (the other way out of the pair) writes a register the
        removed setup writes and then flows straight into the exit. The two
        writes are the arms of one join (`r14 = r20` / `r14 = null`, then
        `r14` is read): deleting one with the block leaves the readers on
        the wrong value."""
        written = {i.dest_reg for i in successor.instructions if i.dest_reg is not None}

        if not written or len(arm.successors) != 1:
            return False

        end_block = next((s for s in successor.successors if s is not arm), None)

        return (
                end_block is not None
                and arm.successors[0] is end_block
                and any(i.dest_reg in written for i in arm.instructions)
        )

    def _rewire_crossed(self, block, successor, branch, merged) -> None:
        end_block = next(s for s in successor.successors if s.address == merged.target)
        a_block = next(s for s in block.successors if s.address == branch.target)

        block.terminator = merged

        for instr in block.instructions:
            if instr.terminator is branch:
                instr.terminator = merged
                break

        successor.instructions.clear()

        for target in (end_block, a_block):
            if successor in target.predecessors:
                target.predecessors.remove(successor)

        block.successors = []
        self._connect(block, end_block)
        self._connect(block, a_block)

        if successor in self.cfg.blocks:
            self.cfg.blocks.remove(successor)

    @staticmethod
    def _fallthrough(block: BasicBlock) -> BasicBlock | None:
        """Return the successor reached when `block`'s condition is false.

        I.e., the one that isn't the branch target.
        """

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return None

        candidates = [s for s in block.successors if s.address != branch.target]

        if len(candidates) != 1:
            return None

        return candidates[0]

    @staticmethod
    def _is_pure_test_block(block: BasicBlock) -> bool:
        """Return True if `block` contains nothing but its own terminator.

        I.e., it exists solely to evaluate one more condition and
        branch, with no other observable side effects that would be
        lost if folded into the preceding block's condition.

        This is also what keeps this pass disjoint from
        BooleanChainRegionPass: any block that assigns a value (the
        pattern that pass folds) has more than one instruction here
        and is correctly rejected. See the class docstring's "Not
        responsible for value-producing &&/||" section before
        loosening this check.
        """

        return len(block.instructions) <= 1

    def _merge(
            self,
            block: BasicBlock,
            successor: BasicBlock,
            next_branch: TerminatorConditionalBranch,
    ) -> None:

        branch = block.terminator
        if not isinstance(branch, TerminatorConditionalBranch):
            raise StructurerInvariantError(
                f"ShortCircuitConditionCfgPass expected block {block.id!r} to "
                f"end in a TerminatorConditionalBranch, got {type(branch).__name__}"
            )

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

        # Printer walks block.instructions (a list of OpcodeResult),
        # rendering each entry's own .terminator - not
        # block.terminator. CFGBuilder points both at the same object
        # when the block is first built, but they're independent
        # references from here on: updating only block.terminator
        # (above) fixes CFG/IfStructurer analysis but leaves the
        # printed text showing the stale, unmerged condition. Find
        # that instruction and update it too.
        for instr in block.instructions:
            if instr.terminator is branch:
                instr.terminator = merged_terminator
                break

        # successor had exactly one instruction (its own terminator
        # entry, per _is_pure_test_block) - drop it, it's now folded
        # into block.terminator.
        successor.instructions.clear()

        new_fallthrough = self._fallthrough(successor)

        # -------------------------------------------------------------
        # Rewire edges: block -> {target_block, new_fallthrough},
        # bypassing successor entirely.
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

    @staticmethod
    def _connect(source: BasicBlock, target: BasicBlock) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)
