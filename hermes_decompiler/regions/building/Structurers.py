from __future__ import annotations

from hermes_decompiler.ir.expressions import BinaryExpression, Expression, UnaryExpression
from hermes_decompiler.ir.Operators import BinaryOperator, LogicalOperator, UnaryOperator
from hermes_decompiler.regions.building.RegionGraph import RegionGraph
from hermes_decompiler.regions.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
)
from hermes_decompiler.regions.models.Statements import IfGotoStatement


class SequenceStructurer:

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self):
        root = SequenceRegion()
        root.children.extend(self.cfg.blocks)

        return root


class LoopStructurer:

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):

        if self.cfg.loop_analysis is None:
            return

        roots = [
            loop
            for loop in self.cfg.loop_analysis.loops.values()
            if loop.parent is None
        ]

        for loop in roots:
            self._build_loop(loop, self.graph.root)

        # TODO: activate with a condition
        # print("\n===== REGION TREE =====")
        # self._dump(self.graph.root)

    def _build_loop(
            self,
            loop,
            parent_sequence: SequenceRegion,
    ):

        region = LoopRegion(loop)

        if loop.header not in parent_sequence.children:

            old_owner = self.graph.owner(loop.header)

            if old_owner and loop.header in old_owner.children:
                old_owner.children.remove(loop.header)

            parent_sequence.children.append(
                loop.header
            )

            loop.header.parent = parent_sequence

            self.graph.block_owner[loop.header] = parent_sequence

        index = parent_sequence.children.index(
            loop.header
        )

        parent_sequence.children[index] = region

        region.parent = parent_sequence

        region.body.children.append(
            loop.header
        )

        self.graph.block_owner[loop.header] = region.body

        child_members = set()

        for child in loop.children:
            child_members.update(child.members)

        for block in sorted(loop.members, key=lambda b: b.id):

            if block == loop.header:
                continue

            if block in child_members:
                continue

            self.graph.move(
                block,
                region.body
            )

        for child in sorted(
                loop.children,
                key=lambda l: l.header.id
        ):
            self._build_loop(child, region.body)

    def _dump(self, region, indent=0):

        prefix = " " * indent

        if isinstance(region, SequenceRegion):
            print(f"{prefix}SequenceRegion")

            for child in region.children:
                self._dump(child, indent + 4)

            return

        if isinstance(region, LoopRegion):
            print(f"{prefix}LoopRegion(header={region.header_block.id})")
            self._dump(region.body, indent + 4)
            return

        if isinstance(region, BasicBlock):
            print(f"{prefix}Block {region.id}")
            return

        print(f"{prefix}{type(region).__name__}")


# ============================================================================
# Condition negation - shared by IfStructurer and BooleanChainFolder
# ============================================================================

_INVERSE_COMPARISON = {
    BinaryOperator.EQUAL: BinaryOperator.NOT_EQUAL,
    BinaryOperator.NOT_EQUAL: BinaryOperator.EQUAL,
    BinaryOperator.STRICT_EQUAL: BinaryOperator.STRICT_NOT_EQUAL,
    BinaryOperator.STRICT_NOT_EQUAL: BinaryOperator.STRICT_EQUAL,
    BinaryOperator.LESS_THAN: BinaryOperator.GREATER_EQUAL,
    BinaryOperator.GREATER_EQUAL: BinaryOperator.LESS_THAN,
    BinaryOperator.LESS_EQUAL: BinaryOperator.GREATER_THAN,
    BinaryOperator.GREATER_THAN: BinaryOperator.LESS_EQUAL,
}


def _negate_condition(expr: Expression) -> Expression:
    """
    Produce the logical negation of `expr`, preferring a flipped
    comparison operator (`!==` instead of `!(=== )`) or unwrapping an
    existing `!` over a generic `UnaryExpression(NOT, expr)` wrap, to
    match how a human would actually write the condition.

    Shared by `IfStructurer` (negating a no-else jump condition) and
    `BooleanChainFolder` (checking whether an `if`'s condition is
    exactly the negation of a preceding assignment's value).
    """

    if isinstance(expr, UnaryExpression) and expr.operator == UnaryOperator.LOGICAL_NOT:
        return expr.operand

    if isinstance(expr, BinaryExpression) and expr.operator in _INVERSE_COMPARISON:
        return BinaryExpression(
            left=expr.left,
            operator=_INVERSE_COMPARISON[expr.operator],
            right=expr.right,
        )

    return UnaryExpression(UnaryOperator.LOGICAL_NOT, expr)


class IfStructurer:
    """
    Converts conditional-jump-terminated basic blocks (whose last
    instruction carries an `IfGotoStatement`) into real `IfRegion`s with
    `then_body`/`else_body`.

    Two bytecode shapes are recognized, both driven by
    `cfg.post_dominator_tree.immediate_post_dominator(block)` (the
    merge point where control reconverges after the branch):

        1. No else - the jump target IS the merge point:

               if (C) goto MERGE;
               <fallthrough-body>
               MERGE:

           `C` true means "skip fallthrough-body entirely". The natural
           JS "then" is therefore the fallthrough-body, taken when `C`
           is false - shown as `if (!C) { <fallthrough-body> }`
           (negated; see `_negate_condition`).

        2. If/else - the jump target is a distinct block that itself
           reconverges at MERGE:

               if (C) goto ELSE;
               <fallthrough-body>
               [goto MERGE]
               ELSE:
               <else-body>
               MERGE:

           `C` true genuinely leads into the jump target's code, so no
           negation is needed: `if (C) { <jump-target body> } else {
           <fallthrough-body> }`.

    Loop header blocks are passed in via `exclude` and left untouched:
    their terminal `IfGotoStatement` is consumed later by
    `LoopConditionExtractor` to build the loop's `while (...)` header,
    and `StructuralAnalyzer` runs this class before that extraction -
    converting the header here would remove the instruction
    `LoopConditionExtractor` expects to find.

    Where the algorithm can't confidently determine a branch boundary
    (e.g. an unexpected block ordering), it leaves the block untouched
    rather than guessing - the raw `if (...) goto label_N;` line still
    renders correctly on its own, just unstructured.
    """

    def __init__(self, graph: RegionGraph, cfg):
        self.graph = graph
        self.cfg = cfg

        self._address_to_block = {
            block.first.opcode.address: block
            for block in cfg.blocks
            if block.instructions
        }

    def run(self):
        self._visit(self.graph.root, exclude=frozenset())

    # ------------------------------------------------------------------
    # Tree walk
    # ------------------------------------------------------------------

    def _visit(self, region, exclude: frozenset):
        """Recursively structure every SequenceRegion in the tree."""

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

        # CatchRegion / FinallyRegion, if present.
        if hasattr(region, "body"):
            self._visit(region.body, frozenset())

    # ------------------------------------------------------------------
    # Finding + converting candidates
    # ------------------------------------------------------------------

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

            target = self._find_candidate(region, exclude | failed)

            if target is None:
                return

            if not self._convert(region, target):
                failed.add(target)

    def _find_candidate(self, region: SequenceRegion, exclude: frozenset) -> BasicBlock | None:

        for item in region.children:

            if not isinstance(item, BasicBlock):
                continue

            if item in exclude:
                continue

            if not item.instructions:
                continue

            last = item.instructions[-1]

            if isinstance(last.statement, IfGotoStatement):
                return item

        return None

    def _convert(self, region: SequenceRegion, block: BasicBlock) -> bool:
        """
        Returns True if `block` was converted into an IfRegion, False
        if it was left untouched (see `_structure_sequence` for why the
        return value matters).
        """

        header_result = block.instructions[-1]
        goto_stmt: IfGotoStatement = header_result.statement

        block_index = region.children.index(block)
        then_start = block_index + 1

        if then_start >= len(region.children):
            # No fallthrough successor at all - can't structure safely.
            return False

        merge_block = None
        if self.cfg.post_dominator_tree is not None:
            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(block)

        goto_block = self._address_to_block.get(goto_stmt.target)

        has_else = goto_block is not None and goto_block is not merge_block

        # -------------------------------------------------------------
        # Find the boundary between "then" and (optional) "else"/merge.
        # -------------------------------------------------------------

        stop_at_first = {b for b in (merge_block, goto_block if has_else else None) if b is not None}
        then_end = self._find_boundary(region, then_start, stop_at_first)

        if has_else:

            else_start = then_end

            if else_start >= len(region.children) or region.children[else_start] is not goto_block:
                # goto target isn't where expected right after "then" -
                # bail out rather than guess incorrectly.
                return False

            stop_at_second = {merge_block} if merge_block is not None else set()
            else_end = self._find_boundary(region, else_start, stop_at_second)

        else:
            else_start = then_end
            else_end = then_end

        # -------------------------------------------------------------
        # Splice the collected ranges out of `region.children`.
        # -------------------------------------------------------------

        then_items = region.children[then_start:then_end]
        else_items = region.children[else_start:else_end]

        del region.children[then_start:else_end]

        then_body = SequenceRegion()
        else_body = SequenceRegion() if has_else else None

        if has_else:
            # fallthrough -> else, goto target -> then (see class docstring)
            self.graph.transfer(then_items, else_body)
            self.graph.transfer(else_items, then_body)
            condition_expr = goto_stmt.condition
        else:
            # fallthrough -> then, negated condition (see class docstring)
            self.graph.transfer(then_items, then_body)
            condition_expr = _negate_condition(goto_stmt.condition)

        if_region = IfRegion()
        if_region.condition = condition_expr
        if_region.then_body = then_body
        if_region.else_body = else_body

        # Drop the header's own terminal jump instruction - its meaning
        # is now carried by `if_region.condition`; any earlier
        # instructions in `block` still render normally right before it.
        block.instructions.pop()

        insert_at = region.children.index(block) + 1
        region.children.insert(insert_at, if_region)
        if_region.parent = region

        return True

    def _find_boundary(self, region: SequenceRegion, start: int, stop_at: set) -> int:
        """
        Walks `region.children` from `start`, returning the index of the
        first item found in `stop_at`, or `len(region.children)` if none
        is found (the branch runs to the end of this region - e.g. both
        sides terminate via return/throw with no common merge point).
        """

        index = start

        while index < len(region.children):

            if region.children[index] in stop_at:
                return index

            index += 1

        return index


class BooleanChainFolder:
    """
    Folds the common short-circuit `||`/`&&` compiled idiom back into a
    single expression, once `IfStructurer` has already turned the raw
    conditional jump into an `IfRegion`:

        r0 = E1;
        if (<negation of E1>) {
            r0 = E2;
        }

    becomes:

        r0 = E1 || E2;

    and the AND counterpart (the original jump condition was `!E1`, so
    `IfStructurer`'s negation step unwrapped it back to plain `E1`):

        r0 = E1;
        if (E1) {
            r0 = E2;
        }

    becomes:

        r0 = E1 && E2;

    Chains longer than two operands (`E1 || E2 || E3 || ...`) fold
    naturally: after the first fold, `block`'s value becomes
    `E1 || E2`, and the loop re-checks the same block against whatever
    `IfRegion` now follows it, matching against the *new* combined value.

    `_visit` recurses post-order (children before folding at the
    current level) so a nested chain (e.g. `E2 || E3` inside an outer
    `if`'s `then_body`) is already collapsed to a single operand before
    the outer level attempts its own fold.

    Only folds when the `if` has no `else` and its `then_body` is
    exactly one `BasicBlock` with exactly one instruction (the
    reassignment) - anything more elaborate is left as a real `if` to
    avoid silently dropping side effects.

    Must run after `IfStructurer` (needs real `IfRegion`s) and before
    `StatementBuilder` flattens blocks into `InstructionState`s.
    """

    def run(self, root: SequenceRegion):
        self._visit(root)

    # ------------------------------------------------------------------

    def _visit(self, region):

        if isinstance(region, SequenceRegion):

            # Post-order: fold nested chains first, so that by the time
            # we try to fold at *this* level, an inner IfRegion whose
            # then_body just collapsed to a single block (e.g. a nested
            # `E2 || E3`) already looks like a single foldable operand
            # instead of a two-item [block, IfRegion] pair.
            for child in region.children:
                self._visit(child)

            self._fold_sequence(region)

            return

        if isinstance(region, LoopRegion):
            self._visit(region.body)
            return

        if isinstance(region, IfRegion):

            self._visit(region.then_body)

            if region.else_body:
                self._visit(region.else_body)

            return

        if hasattr(region, "body"):
            self._visit(region.body)

    # ------------------------------------------------------------------

    def _fold_sequence(self, region: SequenceRegion):

        index = 0

        while index < len(region.children) - 1:

            block = region.children[index]
            if_region = region.children[index + 1]

            if self._try_fold(block, if_region):
                # `if_region` was absorbed into `block`'s value; don't
                # advance - re-check `block` against its new neighbor
                # for a longer chain (E1 || E2 || E3 ...).
                del region.children[index + 1]
                continue

            index += 1

    def _try_fold(self, block, if_region) -> bool:

        if not isinstance(block, BasicBlock) or not isinstance(if_region, IfRegion):
            return False

        if if_region.else_body is not None:
            return False

        if not block.instructions:
            return False

        last = block.instructions[-1]

        if last.dest_reg is None or not isinstance(last.value, Expression):
            return False

        then_children = if_region.then_body.children

        if len(then_children) != 1 or not isinstance(then_children[0], BasicBlock):
            return False

        then_block = then_children[0]

        if len(then_block.instructions) != 1:
            return False

        then_result = then_block.instructions[0]

        if then_result.dest_reg != last.dest_reg:
            return False

        if not isinstance(then_result.value, Expression):
            return False

        e1 = last.value
        condition = if_region.condition

        if condition is None:
            return False

        if _negate_condition(e1).structurally_equal(condition):
            operator = LogicalOperator.OR

        elif e1.structurally_equal(condition):
            operator = LogicalOperator.AND

        else:
            return False

        last.value = BinaryExpression(left=e1, operator=operator, right=then_result.value)
        last.refresh_result()

        return True


class SwitchStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        return


class TryStructurer:

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def run(self):
        return
