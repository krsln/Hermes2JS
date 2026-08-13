from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor
from hermes_decompiler.analysis.models.regions import IfRegion, SequenceRegion
from hermes_decompiler.analysis.transforms._shared import (
    _negate_condition,
    _TRIVIAL_NODE_TYPES,
    _IMPURE_EXPRESSION_TYPES
)
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import (
    ConditionalExpression, Expression, )

from ._base import RegionPass

logger = get_logger(__name__)


class ConditionalExpressionRegionPass(RegionPass, RegionVisitor):
    """
    Folds Hermes' bytecode encoding of a *value-producing* ternary
    (`c ? a : b`) back into a single ConditionalExpression, once
    IfStructurer has already built an IfRegion WITH an else_body.

    Sibling to BooleanChainRegionPass, not a replacement: that pass
    explicitly declines whenever `if_region.else_body is not None`
    (see its `_try_fold`) - this pass exists specifically to cover
    that declined case. The two are disjoint on that one condition,
    so both can run in the same stage without overlap.

    Must run after BooleanChainRegionPass in the pass ordering: a
    then/else arm's own condition may itself be an `&&`/`||` chain
    that needs folding first, so this pass reads clean conditions
    rather than needing to fold sub-chains itself.

    Traversal is inherited from `RegionVisitor` - see
    `BooleanChainRegionPass`'s docstring for why the previous
    hand-rolled `_visit` (identical shape to this one) silently
    skipped `SwitchRegion` bodies.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._fold_sequence(node)

    def _fold_sequence(self, region: SequenceRegion):
        region.children = [
            c for c in region.children
            if not (isinstance(c, BasicBlock) and not c.instructions)
        ]

        index = 0
        while index < len(region.children) - 1:
            block = region.children[index]
            if_region = region.children[index + 1]
            if self._try_fold(block, if_region):
                del region.children[index + 1]
                continue
            index += 1

    def _try_fold(self, block, if_region) -> bool:
        if not isinstance(block, BasicBlock) or not isinstance(if_region, IfRegion):
            return False
        if not block.instructions:
            return False

        condition = if_region.condition
        if condition is None:
            return False

        if if_region.else_body is not None:
            # Two-armed if/else (both `then` and `else` present) is a
            # genuinely different shape from the no-else case below and
            # is NOT handled by it: the no-else logic treats
            # `if_region.then_body` as a single value-producing arm to
            # merge against a "default" expression sitting in `block`
            # - which is meaningless once there's a real `else_body`
            # too (there's no single "default", there are two full
            # arms, each of which may hold real, order-sensitive
            # statements - e.g. a `console.log` call - that must stay
            # as statements, not get silently absorbed into a
            # ConditionalExpression's operand). Falling through to that
            # logic here would misapply it to an unrelated shape and
            # can silently drop real side-effecting statements from
            # one arm. Explicitly bail; two-armed folding is not yet
            # implemented.
            return False

        # no-else case: don't assume block.instructions[-1] is the default
        # value - it may instead be the branch-condition-computing
        # instruction itself (e.g. `r4 = param1 > 100` immediately
        # preceding the terminator), with the real default sitting
        # earlier in the same block (e.g. `r3 = 100`). Try each
        # dest_reg-bearing instruction from last to first, using the
        # FIRST one whose register also has a matching arm - not
        # positional order.
        for last in reversed(block.instructions):
            if last.dest_reg is None or not isinstance(last.value, Expression):
                continue
            then_arm = self._single_result(if_region.then_body, last.dest_reg)
            if then_arm is None:
                continue
            # found a genuine match
            arm_block, arm_result = then_arm
            default_expr = last.value
            arm_expr = arm_result.value
            new_expr = ConditionalExpression(
                test=_negate_condition(condition),
                consequent=default_expr,
                alternate=arm_expr,
            )
            last.value = new_expr
            self._repoint_references(arm_expr, new_expr, min_block_id=arm_block.id, exclude={arm_result, last})
            return True

        return False

    def _single_result(self, body: SequenceRegion, dest_reg: int):
        children = [c for c in body.children if not (isinstance(c, BasicBlock) and not c.instructions)]
        if not children or not all(isinstance(c, BasicBlock) for c in children):
            return None  # only handle flat all-BasicBlock arms for now

        last_block = children[-1]
        if not last_block.instructions:
            return None

        result = last_block.instructions[-1]
        if result.dest_reg != dest_reg or not isinstance(result.value, Expression):
            return None
        if not result.definition_used:
            return None

        # Every instruction across the WHOLE arm except this final merge
        # write must be non-observable-as-its-own-statement - same bar as
        # before, just checked over every block in the arm, not just one.
        #
        # `.statement is not None` alone isn't sufficient: an
        # instruction can be independently observable (a call's side
        # effect, an assignment's mutation) WITHOUT yet having been
        # promoted to its own `.statement` node at this point in the
        # pipeline - Printer falls back to printing such instructions
        # as bare expression statements from `.value` directly (see
        # `Printer._emit_block`). Also reject by expression TYPE, same
        # as `BooleanChainRegionPass._is_pure` already does, so a call
        # (etc.) sitting earlier in the arm can't be silently absorbed
        # into the folded ConditionalExpression's operand tree.
        for blk in children:
            for instr in blk.instructions:
                if instr is result:
                    continue
                if instr.statement is not None:
                    return None
                if isinstance(instr.value, _IMPURE_EXPRESSION_TYPES):
                    return None

        return last_block, result

    def _repoint_references(self, old_expr, new_expr, min_block_id: int, exclude: set) -> None:

        for blk in self.cfg.blocks:
            if blk.id < min_block_id:
                continue

            for instr in blk.instructions:
                if instr in exclude:
                    continue

                new_value, value_changed = self._repoint_node(instr.value, old_expr, new_expr)
                if value_changed:
                    instr.value = new_value

                if instr.statement is not None:
                    new_stmt, stmt_changed = self._repoint_node(instr.statement, old_expr, new_expr)
                    if stmt_changed:
                        instr.statement = new_stmt

    def _repoint_node(self, node, old_expr, new_expr):
        """
        Same generic identity/structural-equality deep-replace as
        BooleanChainRegionPass._repoint_node - see that class for the
        full rationale, including why the structural-equality branch
        is needed for Mov-introduced copies. Kept duplicated here
        rather than shared, per earlier decision to avoid guessing at
        an extraction target.
        """

        if node is old_expr:
            return new_expr, True

        if (not isinstance(old_expr, _TRIVIAL_NODE_TYPES)
                and isinstance(node, type(old_expr))
                and node.structurally_equal(old_expr)):
            return new_expr, True

        if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
            return node, False

        updates = {}
        any_changed = False

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            if isinstance(value, Node):
                new_value, changed = self._repoint_node(value, old_expr, new_expr)
                if changed:
                    updates[field.name] = new_value
                    any_changed = True

            elif isinstance(value, tuple):
                new_items = []
                tuple_changed = False
                for item in value:
                    if isinstance(item, Node):
                        new_item, changed = self._repoint_node(item, old_expr, new_expr)
                        if changed:
                            tuple_changed = True
                        new_items.append(new_item)
                    else:
                        new_items.append(item)
                if tuple_changed:
                    updates[field.name] = tuple(new_items)
                    any_changed = True

        if not any_changed:
            return node, False

        return dataclasses.replace(node, **updates), True