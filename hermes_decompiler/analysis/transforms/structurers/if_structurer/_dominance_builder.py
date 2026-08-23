from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.models.regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
)
# noinspection PyProtectedMember
from hermes_decompiler.analysis.transforms._shared import _negate_condition, is_loop_guard_shaped  # noqa: SLF001
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger
from ._predicates import is_backward_branch, representative_block

logger = get_logger(__name__)


class _DominanceIfBuilder(RegionStructurer):
    """Converts BasicBlocks ending in a ConditionalBranch into IfRegions.

    Two CFG shapes are recognized:

    1. No else::

           if (C) goto MERGE;
           THEN
           MERGE:

       becomes::

           if (!C) { THEN }

    2. If/else::

           if (C) goto ELSE;
           THEN
           goto MERGE;
           ELSE:
               ELSE_BODY
           MERGE:

       becomes::

           if (C) { ELSE_BODY } else { THEN }

    Loop header blocks are excluded - their ConditionalBranch is
    consumed later by LoopConditionExtractor when building
    while/do-while regions.

    then/else membership is decided by dominance (see `_convert`), not
    by position in `region.children`, so else-if chains and any block
    layout the compiler chose are handled without special-casing.

    Purely structural: only decides which blocks become then/else of a
    new IfRegion and splices the tree accordingly. Condition-shape
    rewrites (`&&`/`||` folding, cascade recovery) are
    `_CompoundConditionFolder`'s job and always run after this builder
    (see `IfStructurer.run`).
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)

        self._address_to_block: dict[int, BasicBlock] = {
            block.address: block
            for block in cfg.blocks
        }

    # -------------------------------------------------------------

    def run(self) -> None:
        """Structure the tree, then re-sweep for residual branches.

        A second sweep (not a fixed-point loop) is required: the first
        pass can leave a freshly created else-arm's own residual
        branch unconverted, since that branch didn't exist yet when
        the sweep reached it. One extra sweep always catches it, since
        at most one new residual is introduced per level of `&&`/`||`
        nesting; deeper nesting is folded afterward by
        `_CompoundConditionFolder`, not built fresh here.
        """
        self._visit(self.graph.root, exclude=frozenset())
        self._visit(self.graph.root, exclude=frozenset())
        self.dump_region_tree_if_debug(type(self).__name__)

    # -------------------------------------------------------------
    # Tree traversal
    # -------------------------------------------------------------

    def _visit(self, region, exclude: frozenset):
        """Recursively structure conditional blocks throughout region."""

        if isinstance(region, SequenceRegion):
            self._structure_sequence(region, exclude)

            for child in region.children:
                self._visit(child, frozenset())

            return

        if isinstance(region, LoopRegion):
            exclude = (
                frozenset({region.header_block})
                if is_loop_guard_shaped(region.header_block, region)
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

            region_catch = region.catch
            if region_catch is not None:
                self._visit(region_catch.body, frozenset())

            region_finally = region.finally_
            if region_finally is not None:
                self._visit(region_finally.body, frozenset())

            return

        if hasattr(region, "body"):
            self._visit(region.body, frozenset())

    # -------------------------------------------------------------
    # Sequence conversion
    # -------------------------------------------------------------

    def _structure_sequence(self, region: SequenceRegion, exclude: frozenset):
        """Convert eligible conditional blocks in region.children.

        Repeatedly converts the leftmost eligible block, restarting
        after each conversion since the list is mutated in place.
        Blocks where `_convert` bails out are tracked in `failed` and
        never retried, since `_convert` leaves them unchanged and the
        next search would otherwise find the same candidate forever.
        """

        failed: set = set()

        while True:

            block = self._find_candidate(region, exclude | failed)

            if block is None:
                return

            if not self._convert(region, block):
                failed.add(block)

    # -------------------------------------------------------------

    @staticmethod
    def _find_candidate(region: SequenceRegion, exclude: frozenset) -> BasicBlock | None:
        """Return the first convertible conditional block, or None."""

        for item in region.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if not isinstance(item.terminator, TerminatorConditionalBranch):
                continue

            if is_backward_branch(item):
                # Loop machinery (guard/continue test), never a
                # genuine forward if/goto-merge residual. Must stay
                # untouched here so LoopConditionExtractor (runs later,
                # in region_passes) can recognize it as the loop guard.
                continue

            return item

        return None

    # -------------------------------------------------------------

    def _convert(self, region: SequenceRegion, block: BasicBlock) -> bool:
        """Try to convert `block` into an IfRegion; return success.

        Classifies every item after `block` by dominance rather than
        list position: an item is "then" iff dominated by the
        fallthrough block, and "else" iff dominated by the branch
        target - regardless of how the compiler interleaved the two
        arms in the flat sequence, or where `merge_block` sits. This
        also subsumes the single-entry check: an item with a
        predecessor outside its claimed side simply fails the
        `dominates()` test below and the candidate correctly bails.
        """

        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        if self.cfg.dominator_tree is None:
            # Dominator tree must be precomputed by the caller before
            # structuring runs; nothing can be safely classified without it.
            return False

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor - can't structure safely.
            return False

        then_root = region.children[then_start]
        then_entry = representative_block(then_root)

        merge_block: BasicBlock | None = None

        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(branch.target)

        has_else = goto_block is not merge_block and goto_block is not None

        # else_root = None
        else_entry = None

        if has_else and goto_block is not None:

            else_root = self.graph.find_covering_item(region, goto_block)

            if else_root is None or else_root is then_root:
                # goto target isn't a distinct sibling in this region -
                # bail rather than guess.
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
                # Neither side dominates - this is the true merge
                # point. `merge_block` is only a heuristic shortcut for
                # finding it in advance and can legitimately differ,
                # e.g., when a break (or other loop-exit edge) already
                # carved out into its own region bypasses the merge on
                # the raw CFG. Safe to stop here regardless, since
                # `then_root` always self-dominates and is guaranteed
                # to already be in `then_items` by this point.
                boundary = index
                break

            index += 1

        if has_else and not else_items:
            # else_root dominates itself and must have been classified
            # above; empty here means something upstream is
            # inconsistent. Bail rather than build a broken else.
            return False

        # A trailing unconditional jump to merge_block is the
        # compiled-away "goto past the if/else" and would otherwise
        # print as a confusing literal `goto label_N;`. Only a jump to
        # *this* merge_block, on the branch's last block, is stripped;
        # jumps elsewhere (genuine tail-merged code) are left alone -
        # that's labeled break/continue support, not handled here.
        if merge_block is not None:
            self._strip_trailing_jump_to(then_items, merge_block)
            if has_else:
                self._strip_trailing_jump_to(else_items, merge_block)

        # Prefer RegionGraph mutation APIs so covered_blocks stays in sync.
        self.graph.splice_out(region, then_start, boundary)

        then_body = SequenceRegion()
        else_body = SequenceRegion() if has_else else None

        if has_else and else_body is not None:

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

        # The ConditionalBranch is now represented by the IfRegion.
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
        """Remove a trailing jump/branch to merge_block from items.

        Handles both an unconditional jump straight to `merge_block`,
        and a ConditionalBranch whose true edge targets merge_block
        (empty then-body) - dropping the terminator lets the later
        compound-condition pass fold the surrounding IfRegion cleanly.
        """
        if not items:
            return

        last = items[-1]
        if not isinstance(last, BasicBlock):
            return

        terminator = last.terminator

        # Unconditional jump to merge.
        if isinstance(terminator, TerminatorJump):
            if terminator.target != merge_block.address:
                return
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
            return

        # Conditional whose true edge is the merge (empty then).
        if isinstance(terminator, TerminatorConditionalBranch):
            if terminator.target != merge_block.address:
                return
            # The false edge falls through; after stripping, the block
            # becomes a pure condition holder that higher-level folding
            # can turn into part of a compound expression.
            if last.instructions and last.instructions[-1].terminator is terminator:
                last.instructions.pop()
            last.terminator = None
