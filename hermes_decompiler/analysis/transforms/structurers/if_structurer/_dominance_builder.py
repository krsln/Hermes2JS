from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger

from ._predicates import is_backward_branch, representative_block

logger = get_logger(__name__)


class _DominanceIfBuilder(RegionStructurer):
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

    Purely structural: this class only decides *which* blocks become
    `then`/`else` of a new `IfRegion` and splices the tree accordingly.
    It never rewrites a condition's shape (`&&`/`||` folding, cascade
    recovery) - that is `_CompoundConditionFolder`'s job, and it always
    runs after this builder has finished (see `IfStructurer.run`).
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)

        self._address_to_block = {
            block.address: block
            for block in cfg.blocks
        }

    # -------------------------------------------------------------

    def run(self) -> None:
        self._visit(self.graph.root, exclude=frozenset())
        # Re-structure any residual ConditionalBranches that live
        # inside already-built IfRegion bodies (common after the first
        # pass leaves a short-circuit test in the else arm of `a && b`).
        # Run twice, not to a fixed point: a single sweep can leave a
        # freshly-created else-arm's own residual branch unconverted
        # since that branch didn't exist yet when the sweep reached
        # it; a second sweep always catches it because at most one new
        # residual can be introduced per level of `&&`/`||` nesting,
        # and nesting depth beyond two is folded by
        # `_CompoundConditionFolder` afterwards, not built fresh here.
        self._visit(self.graph.root, exclude=frozenset())
        self.dump_region_tree_if_debug(type(self).__name__)

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
            exclude = (
                frozenset({region.header_block})
                if self._is_loop_guard_shaped(region.header_block, region)
                else frozenset()
            )
            self._visit(region.body, exclude)
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

    @staticmethod
    def _is_loop_guard_shaped(header: BasicBlock, loop_region) -> bool:
        """
        True iff `header`'s own terminator is plausibly the loop's
        continuation test - i.e. it's a conditional branch where at
        least one outgoing edge actually LEAVES the loop
        (`loop_region.exits`, populated by `LoopAnalysis`).

        `LoopStructurer` picks a loop's header purely by CFG dominance
        (the natural loop's unique entry block) - that says nothing
        about whether the header's OWN branch is the loop's
        continuation test. It only is for a top-tested `while`; for a
        bottom-tested `do-while` (or any loop whose real guard lives at
        the latch), the header can hold an entirely ordinary in-body
        `if` whose both edges stay inside the loop. Excluding such a
        header from `_structure_sequence` unconditionally (the old
        behavior) forces that ordinary if through
        `_absorb_residual_conditional`'s crude "wrap everything
        remaining, unconditionally" fallback instead of a proper
        dominance-based then/else split - which, for a header whose
        two arms don't include the loop's own increment/latch code,
        can silently skip code (e.g. the increment) on one arm. See
        `LoopConditionExtractor`, which performs the equivalent
        header-vs-latch guard check for *building* the while/do-while
        shape; this must agree with it, since a header this function
        says isn't guard-shaped is exactly a header
        `LoopConditionExtractor` will also skip when looking for the
        loop's condition.
        """
        if not isinstance(header.terminator, TerminatorConditionalBranch):
            return False

        exits = set(loop_region.exits)

        return any(successor in exits for successor in header.successors)

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

            if not isinstance(item.terminator, TerminatorConditionalBranch):
                continue

            if is_backward_branch(item):
                # A conditional branch whose target address is <= its
                # own block's address is always loop machinery (a
                # guard or continue-test), never a genuine forward
                # if/goto-merge residual - the same criterion
                # ShortCircuitConditionMerger already relies on for
                # the identical reason. `_convert`'s dominance-based
                # classification has no concept of "this is really a
                # back-edge"; it would try to treat the loop's own
                # prior iteration content as an "else" arm reachable
                # through this "goto", corrupting the loop. Must be
                # left completely untouched for LoopConditionExtractor
                # (which runs much later, in region_passes) to
                # recognize as the loop's actual guard.
                continue

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
        then_entry = representative_block(then_root)

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

            else_entry = representative_block(else_root)

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

            rep = representative_block(item)

            if dominators.dominates(then_entry, rep):
                then_items.append(item)

            elif has_else and dominators.dominates(else_entry, rep):
                else_items.append(item)

            else:
                # Neither side dominates this item. This is NOT
                # necessarily an unexpected join we can't account for -
                # it's the exact defining property of a true merge
                # point: something reachable from BOTH arms cannot
                # belong to only one of them. `merge_block` (the raw
                # CFG's post-dominator of `block`) is only a heuristic
                # shortcut for finding this boundary in advance; it can
                # legitimately fail to equal this item when some OTHER
                # edge leaving one arm bypasses the merge entirely on
                # the raw CFG - most commonly a `break` (or any other
                # loop-exit edge) that a prior pass has already carved
                # out into its own region. That bypass edge is real for
                # raw post-dominance purposes but no longer relevant to
                # how this if/else should be shaped: the arm containing
                # the break still legitimately ends there, and
                # everything from here on is unambiguously "after the
                # if/else", exactly like hitting `merge_block` would
                # have signaled.
                #
                # Only safe once at least one item is already
                # classified on the required side(s) below - guaranteed
                # here since `then_root` itself (the loop's very first
                # iteration) always self-dominates and is always
                # appended to `then_items` before this branch can ever
                # be reached.
                boundary = index
                break

            index += 1

        if has_else and not else_items:
            # else_root dominates itself, so it must have been
            # classified above - empty means something upstream is
            # inconsistent. Bail rather than build a broken else.
            return False

        # Falling out of a `{ }` block already continues at whatever
        # comes next - which, by construction, IS `merge_block` (that's
        # what bounded this classification loop above). So if the last
        # block on either side ends in a plain unconditional jump
        # *specifically to merge_block*, that jump is exactly the
        # redundant "goto past the if/else" the source compiled away
        # into block-scoping; it must be consumed here, or it prints as
        # a literal, confusing `goto label_N;` as the last line of an
        # otherwise clean branch body.
        #
        # Deliberately narrow: only strips a jump whose target is
        # *this* merge_block, on the branch's *last* block. A jump to
        # anywhere else (e.g. genuine cross-branch shared/tail-merged
        # code) is left completely alone - that's a different, harder
        # problem (labeled break/continue - see the roadmap's Faz 4),
        # not something to paper over here.
        if merge_block is not None:
            self._strip_trailing_jump_to(then_items, merge_block)
            if has_else:
                self._strip_trailing_jump_to(else_items, merge_block)

        # Prefer RegionGraph mutation APIs so covered_blocks stays in sync.
        self.graph.splice_out(region, then_start, boundary)

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
        assert block.instructions[-1].terminator is not None
        block.instructions.pop()
        block.terminator = None

        insert_at = region.children.index(block) + 1
        self.graph.insert_at(region, insert_at, if_region)

        return True

    # -------------------------------------------------------------
    # Trailing-jump cleanup
    # -------------------------------------------------------------

    @staticmethod
    def _strip_trailing_jump_to(items: list, merge_block: BasicBlock) -> None:
        """
        If `items[-1]` is a `BasicBlock` whose terminator is an
        unconditional jump straight to `merge_block`, remove that jump
        (instruction + terminator) - see call site for why this is safe
        and why it's scoped this narrowly.

        Also handles the common Hermes pattern where the *last*
        instruction is still a ConditionalBranch whose *true* target is
        the merge (empty then-body).  In that case we simply drop the
        terminator so the later compound-condition pass can absorb the
        surrounding IfRegion cleanly.
        """
        if not items:
            return

        last = items[-1]
        if not isinstance(last, BasicBlock):
            return

        terminator = last.terminator

        # Unconditional jump to merge
        if isinstance(terminator, TerminatorJump):
            if terminator.target != merge_block.address:
                return
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
            return

        # Conditional whose *true* edge is the merge (empty then)
        if isinstance(terminator, TerminatorConditionalBranch):
            if terminator.target != merge_block.address:
                return
            # The false edge falls through; after stripping, the block
            # becomes a pure condition holder that higher-level folding
            # can turn into part of a compound expression.
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
