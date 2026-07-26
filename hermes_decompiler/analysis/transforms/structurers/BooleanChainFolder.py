from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
)
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression
from hermes_decompiler.analysis.transforms.structurers._negation import _negate_condition


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
