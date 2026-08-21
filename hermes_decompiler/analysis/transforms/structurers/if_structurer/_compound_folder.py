from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import (
    IfRegion,
    LoopRegion,
    Region,
    SequenceRegion,
    TryRegion,
)
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression

from ._predicates import (
    is_backward_branch,
    is_empty_body,
    is_negation,
    make_logical_and,
    make_logical_or,
    single_if_child,
    unwrap_negation,
)

logger = get_logger(__name__)


class _CompoundConditionFolder:
    """Second pass of `IfStructurer`: folds Hermes short-circuit idioms.

    Walks every SequenceRegion built by `_DominanceIfBuilder` and
    collapses the common `&&`/`||` patterns Hermes emits::

        if (C1) {
            if (C2) { BODY }
        }                       ->  if (C1 && C2) { BODY }

        if (C1) {
        } else {
            if (C2) { BODY }
        }                       ->  if (C1 || C2) { BODY }

    Empty then/else bodies holding only a single conditional jump to
    the merge point are also absorbed, eliminating the residual
    `if (x) goto label_N;` that would otherwise survive into the
    printed source.

    Purely a rewrite pass - it never turns a raw BasicBlock into a new
    IfRegion from scratch (that's `_DominanceIfBuilder`'s job, which
    always runs first - see `IfStructurer.run`). It does not extend
    `RegionStructurer` because it doesn't introduce a new region kind,
    only reshapes IfRegions that already exist.
    """

    def __init__(self, graph):
        self.graph = graph

    def run(self, root) -> None:
        self._fold_all(root)
        self._prune_empty_blocks(root)

    # -------------------------------------------------------------
    # Fold: post-order walk
    # -------------------------------------------------------------

    def _fold_all(self, region) -> None:
        """Post-order walk: fold children first so nested `||`/`&&` are
        already collapsed before a parent cascade tries to match against
        them."""
        if isinstance(region, SequenceRegion):
            # Children first.
            for child in list(region.children):
                self._fold_all(child)
            # Then fold this sequence to a fixed point.
            changed = True
            while changed:
                changed = self._fold_compound_conditions(region)
            return

        if isinstance(region, IfRegion):
            self._fold_all(region.then_body)
            if region.else_body:
                self._fold_all(region.else_body)
            # Try the cascade directly on this IfRegion after its
            # bodies are folded (covers inverted a&&b even when not a
            # root child).
            self._try_fold_and_or_cascade(region)
            return

        if isinstance(region, LoopRegion):
            self._fold_all(region.body)
            return

        if isinstance(region, TryRegion):
            self._fold_all(region.try_body)
            region_catch = region.catch
            if region_catch:
                self._fold_all(region_catch.body)
            region_finally_ = region.finally_
            if region_finally_:
                self._fold_all(region_finally_.body)
            return

        if hasattr(region, "body"):
            self._fold_all(region.body)

    def _fold_compound_conditions(self, region: SequenceRegion) -> bool:
        """Run one sweep over region.children; return True if changed.

        Caller re-runs until a fixed point is reached. Patterns
        recognized (Hermes short-circuit lowering):

        1. Nested AND - `if (C1) { if (C2) { BODY } }` (no else on
           either) -> `if (C1 && C2) { BODY }`.
        2. Nested OR - `if (C1) {} else { if (C2) { BODY } }` ->
           `if (C1 || C2) { BODY }`.
        3. OR with an inverted outer test - `if (!C1) { if (C2) { BODY } }`
           -> `if (C1 || C2) { BODY }` (after negation cleanup).
        4. Residual short-circuit jump - `if (C) goto MERGE; BODY` ->
           `if (!C) { BODY }`.
        5. High-level `a && b` recovery from the inverted form Hermes
           emits for `if (a && b) ... else if (a || b) ... else ...`
           (see `_try_fold_and_or_cascade`).
        """
        changed = False
        i = 0
        while i < len(region.children):
            child = region.children[i]
            if not isinstance(child, IfRegion):
                # --- pattern 4: residual conditional block ---
                if (
                        isinstance(child, BasicBlock)
                        and isinstance(child.terminator, TerminatorConditionalBranch)
                        and not is_backward_branch(child)
                ):
                    if self._absorb_residual_conditional(region, i):
                        changed = True
                        continue
                i += 1
                continue

            # --- pattern 5: inverted a&&b / a||b cascade ---
            if self._try_fold_and_or_cascade(child):
                changed = True
                continue

            # --- pattern 1: AND (then contains a single IfRegion, no else) ---
            inner = single_if_child(child.then_body)
            if inner is not None and child.else_body is None and inner.else_body is None:
                child.condition = make_logical_and(child.condition, inner.condition)
                # Splice inner's then_body in at inner's OWN position,
                # preserving any sibling that `single_if_child` treated
                # as "inert" for classification purposes only. - That
                # check exists to look past no-op clutter when deciding
                # whether an IfRegion is the sole meaningful content,
                # not to license discarding real statements alongside
                # it. A plain reassignment of then_body would silently
                # drop those statements instead.
                seq = child.then_body
                idx = seq.children.index(inner)
                replacement = inner.then_body.children
                seq.children[idx:idx + 1] = replacement
                for c in replacement:
                    if isinstance(c, Region):
                        c.parent = seq
                seq.invalidate_coverage()
                changed = True
                continue

            # --- pattern 2 / 3: OR (empty then + single IfRegion in else) ---
            if (is_empty_body(child.then_body)
                    and child.else_body is not None):
                inner = single_if_child(child.else_body)
                if inner is not None and inner.else_body is None:
                    # Hermes often emits `if (!a) { if (b) ... }` for
                    # `a || b`; prefer the positive form when the outer
                    # condition is already a negation.
                    outer_cond = child.condition
                    if is_negation(outer_cond):
                        # if (!C1) { if (C2) BODY } -> if (C1 || C2)
                        positive = unwrap_negation(outer_cond)
                        child.condition = make_logical_or(positive, inner.condition)
                    else:
                        # if (C1) {} else { if (C2) BODY } -> if (C1 || C2)
                        child.condition = make_logical_or(
                            outer_cond, inner.condition
                        )
                    child.then_body = inner.then_body
                    child.then_body.parent = child
                    child.else_body = None
                    changed = True
                    continue

            # --- then empty, else non-empty: invert & swap ---
            # (helps later AND/OR folding and produces cleaner source)
            if (is_empty_body(child.then_body)
                    and child.else_body is not None
                    and not is_empty_body(child.else_body)):
                child.condition = _negate_condition(child.condition)
                child.then_body, child.else_body = child.else_body, child.then_body
                # then_body may still be empty after the swap; leave it.
                if is_empty_body(child.else_body):
                    child.else_body = None
                changed = True
                continue

            i += 1

        return changed

    # -------------------------------------------------------------
    # Residual conditional absorption & a&&b cascade recovery
    # -------------------------------------------------------------

    def _absorb_residual_conditional(self, region: SequenceRegion, index: int) -> bool:
        """Fold a leftover `if (C) goto T; FALLTHROUGH...` block.

        Converts it into `if (!C) { FALLTHROUGH... }` when the jump
        target isn't among the following siblings (i.e., it jumps out,
        to the merge). This is exactly the residual Hermes leaves in
        the else-arm of `a && b`.
        """
        block = region.children[index]
        assert isinstance(block, BasicBlock)
        branch = block.terminator
        assert isinstance(branch, TerminatorConditionalBranch)

        if index + 1 >= len(region.children):
            return False

        rest = self.graph.splice_out(region, index + 1, len(region.children))
        if not rest:
            return False

        # Remove the residual block itself.
        self.graph.splice_out(region, index, index + 1)

        if block.instructions and block.instructions[-1].terminator is branch:
            block.instructions.pop()
        block.terminator = None

        then_body = SequenceRegion()
        self.graph.transfer(list(rest), then_body)

        if_region = IfRegion()
        if_region.condition = _negate_condition(branch.condition)
        if_region.then_body = then_body
        if_region.else_body = None
        then_body.parent = if_region

        # Keep any non-terminator instructions still on the block
        # (rare) by inserting the now terminator-free block first.
        insert_at = index
        if block.instructions:
            self.graph.insert_at(region, insert_at, block)
            insert_at += 1
        self.graph.insert_at(region, insert_at, if_region)
        return True

    def _try_fold_and_or_cascade(self, outer: IfRegion) -> bool:
        """Recover the `a && b` / `a || b` / `else` cascade in place.

        Recognizes the classic Hermes lowering of::

            if (a && b) { BOTH }
            else if (a || b) { EITHER }
            else { NEITHER }

        which appears after structuring and residual absorption as::

            if (!a) {
                if (a || b) { EITHER } else { NEITHER }
            } else {
                if (!b) { BOTH }          # residual was absorbed
            }

        or still with a raw residual jump. Rewrites in place to the
        source-level cascade with positive polarity.
        """
        if not is_negation(outer.condition):
            return False
        if outer.else_body is None:
            return False

        # The then side must be a single if shaped like (a || b) / either-neither.
        inner = single_if_child(outer.then_body)
        if inner is None:
            return False

        a = unwrap_negation(outer.condition)

        # ---- extract BOTH body + the second conjunct b from the else side ----
        both_body = None
        b = None

        else_body = outer.else_body

        # Case A: else is a single IfRegion - if (!b) { BOTH } or if (b) { BOTH }.
        else_if = else_body if isinstance(else_body, IfRegion) else single_if_child(else_body)

        if isinstance(else_if, IfRegion) and else_if.else_body is None:
            both_body = else_if.then_body
            cond = else_if.condition
            # Residual absorption produced if (!b) { BOTH } because the
            # original jump was "if (b) goto merge" - unwrap to recover
            # the positive conjunct b.
            if is_negation(cond):
                b = unwrap_negation(cond)
            else:
                b = cond

        # Case B: else is a SequenceRegion starting with a residual BasicBlock.
        elif isinstance(else_body, SequenceRegion) and else_body.children:
            first = else_body.children[0]
            if (isinstance(first, BasicBlock)
                    and isinstance(first.terminator, TerminatorConditionalBranch)):
                branch = first.terminator
                rest = else_body.children[1:]
                if rest:
                    new_seq = SequenceRegion()
                    self.graph.transfer(list(rest), new_seq)
                    # Original: if (b) goto merge; BOTH -> b is the condition.
                    b = branch.condition
                    both_body = new_seq
                    if first.instructions and first.instructions[-1].terminator is branch:
                        first.instructions.pop()
                    first.terminator = None
            elif isinstance(first, IfRegion) and first.else_body is None:
                both_body = first.then_body
                cond = first.condition
                if is_negation(cond):
                    b = unwrap_negation(cond)
                else:
                    b = cond

        if both_body is None or b is None:
            return False

        # ---- rewrite outer into: if (a && b) { BOTH } else if (a || b) ... ----
        and_cond = make_logical_and(a, b)

        either_body = inner.then_body
        neither_body = inner.else_body

        outer.condition = and_cond
        outer.then_body = both_body
        both_body.parent = outer

        # Keep a sensible || condition for the else-if arm.
        or_cond = inner.condition
        is_or = isinstance(or_cond, BinaryExpression) and or_cond.operator == LogicalOperator.OR
        if not is_or:
            or_cond = make_logical_or(a, b)

        else_if_region = IfRegion()
        else_if_region.condition = or_cond
        else_if_region.then_body = either_body
        else_if_region.else_body = neither_body
        if either_body is not None:
            either_body.parent = else_if_region
        if neither_body is not None:
            neither_body.parent = else_if_region

        else_seq = SequenceRegion()
        else_seq.children.append(else_if_region)
        else_if_region.parent = else_seq
        outer.else_body = else_seq
        else_seq.parent = outer
        return True

    # -------------------------------------------------------------
    # Post-fold cleanup
    # -------------------------------------------------------------

    def _prune_empty_blocks(self, region) -> None:
        """Remove BasicBlocks with no instructions or terminator.

        Leftover empty blocks only clutter else-if detection.
        """
        if isinstance(region, SequenceRegion):
            region.children = [
                c for c in region.children
                if not (isinstance(c, BasicBlock)
                        and not c.instructions
                        and c.terminator is None)
            ]
            for child in region.children:
                self._prune_empty_blocks(child)
            return
        if isinstance(region, IfRegion):
            self._prune_empty_blocks(region.then_body)
            if region.else_body:
                self._prune_empty_blocks(region.else_body)
            return
        if isinstance(region, LoopRegion):
            self._prune_empty_blocks(region.body)
            return
        if isinstance(region, TryRegion):
            self._prune_empty_blocks(region.try_body)
            region_catch = region.catch
            if region_catch:
                self._prune_empty_blocks(region_catch.body)
            region_finally_ = region.finally_
            if region_finally_:
                self._prune_empty_blocks(region_finally_.body)
            return
        if hasattr(region, "body"):
            self._prune_empty_blocks(region.body)
