from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.analysis.regions.Regions import (
    IfRegion,
    LoopRegion,
    SequenceRegion,
    TryRegion,
    Region,
)
from hermes_decompiler.analysis.transforms._shared._negation import _negate_condition
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer
from hermes_decompiler.core.logging import get_logger

from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    UnaryExpression,
)
from hermes_decompiler.ir.Operators import LogicalOperator, UnaryOperator

logger = get_logger(__name__)


class IfStructurer(RegionStructurer):
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

    ------------------------------------------------------------------
    Robustness additions (compound conditions & leftover jumps)
    ------------------------------------------------------------------

    After the classic dominance-based conversion a second pass
    (`_fold_compound_conditions`) walks every SequenceRegion and
    collapses the common short-circuit patterns that Hermes emits for
    `&&` / `||`:

        if (C1) {
            if (C2) { BODY }
        }                       →  if (C1 && C2) { BODY }

        if (C1) {
        } else {
            if (C2) { BODY }
        }                       →  if (C1 || C2) { BODY }

        if (C1) { BODY }
        else if (C2) { … }      (already produced by nested conversion;
                                 the Printer later pretty-prints it)

    Empty then/else bodies that only contain a single conditional jump
    to the merge point are also absorbed, eliminating the residual
    `if (x) goto label_N;` that previously survived into the printed
    source.
    """

    def __init__(self, graph, cfg):
        super().__init__(graph, cfg)

        self._address_to_block = {
            block.address: block
            for block in cfg.blocks
        }

    # -------------------------------------------------------------

    def run(self):
        self._visit(self.graph.root, exclude=frozenset())
        # Re-structure any residual ConditionalBranches that live
        # inside already-built IfRegion bodies (common after the first
        # pass leaves a short-circuit test in the else arm of `a && b`).
        self._visit(self.graph.root, exclude=frozenset())
        # Second pass: fold short-circuit chains into compound
        # conditions.  Must run *after* the structural conversion so
        # that nested IfRegions already exist.
        self._fold_all(self.graph.root)
        # Final cleanup of empty BasicBlocks left behind by stripping.
        self._prune_empty_blocks(self.graph.root)
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
            self._visit(region.body, frozenset({region.header_block}))
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

            if isinstance(item.terminator, TerminatorConditionalBranch):
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
        then_entry = self._representative_block(then_root)

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

            else_entry = self._representative_block(else_root)

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

            rep = self._representative_block(item)

            if dominators.dominates(then_entry, rep):
                then_items.append(item)

            elif has_else and dominators.dominates(else_entry, rep):
                else_items.append(item)

            else:
                # Neither side dominates this item: it's reachable some
                # other way we don't account for here (e.g. a join we
                # didn't expect). Bail rather than misclassify it.
                return False

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
        # problem (see module docstring), not something to paper over
        # here.
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
    # Trailing-jump / empty-body cleanup
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

    # -------------------------------------------------------------
    # Compound-condition folding (&& / ||)
    # -------------------------------------------------------------

    def _fold_all(self, region) -> None:
        """Post-order walk: fold children first so nested || / && are
        already collapsed before a parent cascade (a && b / a || b)
        tries to match against them."""
        if isinstance(region, SequenceRegion):
            # Children first
            for child in list(region.children):
                self._fold_all(child)
            # Then fold this sequence to fixed point
            changed = True
            while changed:
                changed = self._fold_compound_conditions(region)
            return

        if isinstance(region, IfRegion):
            self._fold_all(region.then_body)
            if region.else_body:
                self._fold_all(region.else_body)
            # Try cascade on this IfRegion directly after its bodies are
            # folded (covers inverted a&&b even when not a root child).
            self._try_fold_and_or_cascade(region)
            return

        if isinstance(region, LoopRegion):
            self._fold_all(region.body)
            return

        if isinstance(region, TryRegion):
            self._fold_all(region.try_body)
            if region.catch:
                self._fold_all(region.catch.body)
            if region.finally_:
                self._fold_all(region.finally_.body)
            return

        if hasattr(region, "body"):
            self._fold_all(region.body)

    def _fold_compound_conditions(self, region: SequenceRegion) -> bool:
        """
        One sweep over `region.children`.  Returns True if any
        transformation was performed (caller should re-run until
        fixed-point).

        Patterns recognised (Hermes short-circuit lowering):

        1. Nested AND
               if (C1) {
                   if (C2) { BODY }          # no else
               }                             # no else
           →   if (C1 && C2) { BODY }

        2. Nested OR  (empty then + nested if in else)
               if (C1) {
               } else {
                   if (C2) { BODY }
               }
           →   if (C1 || C2) { BODY }

        3. OR with inverted outer test (very common for `a || b`)
               if (!C1) {
                   if (C2) { BODY }
               }
           →   if (C1 || C2) { BODY }   (after double-negation cleanup)

        4. Residual short-circuit jump inside a body
               if (C) goto MERGE; BODY
           →   if (!C) { BODY }

        5. High-level `a && b` recovery from the inverted form Hermes
           emits for `if (a && b) … else if (a || b) … else …`:
               if (!a) {
                   if (a || b) { EITHER } else { NEITHER }
               } else {
                   [optional residual if(b) goto]
                   BOTH
               }
           →   if (a && b) { BOTH }
               else if (a || b) { EITHER }
               else { NEITHER }
        """
        changed = False
        i = 0
        while i < len(region.children):
            child = region.children[i]
            if not isinstance(child, IfRegion):
                # --- pattern 4: residual conditional block ---
                if isinstance(child, BasicBlock) and isinstance(
                        child.terminator, TerminatorConditionalBranch
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
            inner = self._single_if_child(child.then_body)
            if inner is not None and child.else_body is None and inner.else_body is None:
                child.condition = self._make_logical_and(child.condition, inner.condition)
                # Splice inner's then_body in at inner's OWN position, preserving
                # any sibling (e.g. Block1's real `r3 = "zero"`) that _single_if_child
                # deemed "inert" for classification purposes only - that check exists
                # to look PAST no-op clutter when deciding whether an IfRegion is the
                # sole meaningful content, not to license discarding real statements
                # that happen to sit alongside it. Outright reassigning then_body
                # (the prior behavior) silently dropped those statements instead.
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
            if (self._is_empty_body(child.then_body)
                    and child.else_body is not None):
                inner = self._single_if_child(child.else_body)
                if inner is not None and inner.else_body is None:
                    # (!C1) || C2   or   C1 || C2   depending on polarity
                    # Hermes often emits `if (!a) { if (b) … }` for `a || b`
                    outer_cond = child.condition
                    # Prefer the positive form when the outer condition is
                    # already a negation.
                    if self._is_negation(outer_cond):
                        # if (!C1) { if (C2) BODY }  →  if (C1 || C2)
                        positive = self._unwrap_negation(outer_cond)
                        child.condition = self._make_logical_or(positive, inner.condition)
                    else:
                        # if (C1) {} else { if (C2) BODY }  →  if (C1 || C2)
                        child.condition = self._make_logical_or(
                            outer_cond, inner.condition
                        )
                    child.then_body = inner.then_body
                    child.then_body.parent = child
                    child.else_body = None
                    changed = True
                    continue

            # --- pattern: then empty, else non-empty → invert & swap ---
            # (helps later AND/OR folding and produces cleaner source)
            if (self._is_empty_body(child.then_body)
                    and child.else_body is not None
                    and not self._is_empty_body(child.else_body)):
                child.condition = _negate_condition(child.condition)
                child.then_body, child.else_body = child.else_body, child.then_body
                # then_body may still be empty after swap; leave it
                if self._is_empty_body(child.else_body):
                    child.else_body = None
                changed = True
                continue

            i += 1

        return changed

    # -------------------------------------------------------------
    # Residual conditional absorption & a&&b cascade recovery
    # -------------------------------------------------------------

    def _absorb_residual_conditional(self, region: SequenceRegion, index: int) -> bool:
        """
        Convert a leftover
            BasicBlock: if (C) goto T;   FALLTHROUGH…
        into
            if (!C) { FALLTHROUGH… }
        when the jump target is not among the following siblings
        (i.e. it jumps *out* / to the merge).  This is exactly the
        residual that Hermes leaves in the else-arm of `a && b`.
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

        # Remove the residual block itself
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

        # Keep any non-terminator instructions that were on the block
        # (rare) by inserting the (now terminator-free) block first.
        insert_at = index
        if block.instructions:
            self.graph.insert_at(region, insert_at, block)
            insert_at += 1
        self.graph.insert_at(region, insert_at, if_region)
        return True

    def _try_fold_and_or_cascade(self, outer: IfRegion) -> bool:
        """
        Recognise the classic Hermes lowering of

            if (a && b) { BOTH }
            else if (a || b) { EITHER }
            else { NEITHER }

        which appears after structuring + residual absorption as either:

            if (!a) {
                if (a || b) { EITHER } else { NEITHER }
            } else {
                if (!b) { BOTH }          # residual was absorbed
            }

        or still with a raw residual jump.  Rewrite in-place to the
        source-level cascade with positive polarity.
        """
        if not self._is_negation(outer.condition):
            return False
        if outer.else_body is None:
            return False

        # then side must be a single if that looks like (a || b) / either-neither
        inner = self._single_if_child(outer.then_body)
        if inner is None:
            return False

        a = self._unwrap_negation(outer.condition)

        # ---- extract BOTH body + the second conjunct b from else side ----
        both_body = None
        b = None

        else_body = outer.else_body

        # Case A: else is a single IfRegion  if (!b) { BOTH }  or  if (b) { BOTH }
        else_if = self._single_if_child(else_body) if not isinstance(else_body, IfRegion) else else_body
        if else_if is None and isinstance(else_body, IfRegion):
            else_if = else_body

        if isinstance(else_if, IfRegion) and else_if.else_body is None:
            both_body = else_if.then_body
            cond = else_if.condition
            # Residual absorption produced if (!b) { BOTH } because the
            # original jump was "if (b) goto merge".  Unwrap so we recover
            # the positive conjunct b.
            if self._is_negation(cond):
                b = self._unwrap_negation(cond)
            else:
                b = cond

        # Case B: else is a SequenceRegion starting with residual BasicBlock
        elif isinstance(else_body, SequenceRegion) and else_body.children:
            first = else_body.children[0]
            if (isinstance(first, BasicBlock)
                    and isinstance(first.terminator, TerminatorConditionalBranch)):
                branch = first.terminator
                rest = else_body.children[1:]
                if rest:
                    new_seq = SequenceRegion()
                    self.graph.transfer(list(rest), new_seq)
                    # Original: if (b) goto merge; BOTH  →  b is the condition
                    b = branch.condition
                    both_body = new_seq
                    if first.instructions and first.instructions[-1].terminator is branch:
                        first.instructions.pop()
                    first.terminator = None
            elif isinstance(first, IfRegion) and first.else_body is None:
                both_body = first.then_body
                cond = first.condition
                if self._is_negation(cond):
                    b = self._unwrap_negation(cond)
                else:
                    b = cond

        if both_body is None or b is None:
            return False

        # ---- rewrite outer into: if (a && b) { BOTH } else if (a || b) … ----
        and_cond = self._make_logical_and(a, b)

        either_body = inner.then_body
        neither_body = inner.else_body

        outer.condition = and_cond
        outer.then_body = both_body
        both_body.parent = outer

        # Keep a sensible || condition for the else-if arm
        or_cond = inner.condition
        is_or = (
                BinaryExpression is not None
                and isinstance(or_cond, BinaryExpression)
                and (
                        getattr(or_cond, "operator", None) == "||"
                        or (LogicalOperator is not None
                            and getattr(or_cond, "operator", None) == LogicalOperator.OR)
                )
        )
        if not is_or:
            or_cond = self._make_logical_or(a, b)

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

    def _prune_empty_blocks(self, region) -> None:
        """Remove BasicBlocks that no longer hold any instructions or
        terminators – they only clutter else-if detection."""
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
            if region.catch:
                self._prune_empty_blocks(region.catch.body)
            if region.finally_:
                self._prune_empty_blocks(region.finally_.body)
            return
        if hasattr(region, "body"):
            self._prune_empty_blocks(region.body)

    # -------------------------------------------------------------
    # Helpers for compound-condition recognition
    # -------------------------------------------------------------

    @staticmethod
    def _is_empty_body(body) -> bool:
        if body is None:
            return True
        if isinstance(body, SequenceRegion):
            return len(body.children) == 0
        return False

    @staticmethod
    def _is_inert_block(item) -> bool:
        """Empty or terminator-free BasicBlock with no statements."""
        if not isinstance(item, BasicBlock):
            return False
        if item.terminator is not None:
            return False
        for instr in item.instructions:
            if instr.statement is not None or instr.terminator is not None:
                return False
            if instr.dest_reg is not None and instr.definition_used:
                return False
        return True

    @classmethod
    def _single_if_child(cls, body) -> IfRegion | None:
        """Return the sole meaningful IfRegion inside body, or None.

        Accepts either a bare IfRegion or a SequenceRegion whose only
        non-inert child is an IfRegion (Hermes often leaves empty /
        const-load blocks as siblings).
        """
        if isinstance(body, IfRegion):
            return body
        if not isinstance(body, SequenceRegion):
            return None
        meaningful = [c for c in body.children if not cls._is_inert_block(c)]
        if len(meaningful) == 1 and isinstance(meaningful[0], IfRegion):
            return meaningful[0]
        return None

    @staticmethod
    def _is_negation(expr) -> bool:
        """True when expr is a logical-not.

        Matches UnaryExpression(UnaryOperator.LOGICAL_NOT, …) which
        StrEnum-compares equal to the string \"!\".
        """
        if expr is None:
            return False
        if isinstance(expr, UnaryExpression):
            return expr.operator == UnaryOperator.LOGICAL_NOT or expr.operator == "!"
        # Fallback if the import failed and we only have a duck-typed node
        op = getattr(expr, "operator", None)
        return op == "!" or op == UnaryOperator.LOGICAL_NOT if UnaryOperator else op == "!"

    @staticmethod
    def _unwrap_negation(expr):
        if isinstance(expr, UnaryExpression):
            return expr.operand
        return getattr(expr, "operand", expr)

    @staticmethod
    def _make_logical_and(left, right):
        if BinaryExpression is None or LogicalOperator is None:
            # Offline fallback – keep left unchanged (safe but incomplete).
            return left
        # Must use LogicalOperator enum – string "&&" is rejected by the IR.
        return BinaryExpression(left=left, operator=LogicalOperator.AND, right=right)

    @staticmethod
    def _make_logical_or(left, right):
        if BinaryExpression is None or LogicalOperator is None:
            return left
        return BinaryExpression(left=left, operator=LogicalOperator.OR, right=right)

    # -------------------------------------------------------------

    @staticmethod
    def _representative_block(item) -> BasicBlock | None:
        """
        Any single `BasicBlock` that dominance checks against `item`
        can be run on. For a raw `BasicBlock`, that's `item` itself.
        For an already-built region (`IfRegion`/`LoopRegion`/
        `TryRegion`), every block it covers shares the same dominance
        relationship to blocks *outside* it - single-entry regions are
        dominated as a unit, by construction - so any element of
        `covered_blocks` is an equally valid representative.
        """

        if isinstance(item, BasicBlock):
            return item

        covered = item.covered_blocks
        if not covered:
            return None

        # `min(..., key=...)` rather than `next(iter(...))`: both are
        # deterministic now that `BasicBlock.__hash__` is id-based (see
        # that class), but picking explicitly by `.id` documents *why*
        # any element works (dominance is invariant across a single-entry
        # region's covered blocks) instead of leaving it to look like an
        # arbitrary/unspecified choice.
        return min(covered, key=lambda b: b.id)
