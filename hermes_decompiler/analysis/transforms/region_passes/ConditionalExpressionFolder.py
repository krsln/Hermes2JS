from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion, LoopRegion, IfRegion, TryRegion,
)
from hermes_decompiler.analysis.transforms._shared import _negate_condition
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import ConditionalExpression, Expression, Identifier,StringLiteral, NumericLiteral, BooleanLiteral

logger = get_logger(__name__)

_TRIVIAL_NODE_TYPES = (Identifier, StringLiteral, NumericLiteral, BooleanLiteral)  # adjust to actual literal type names

class ConditionalExpressionFolder:
    """
    Folds Hermes' bytecode encoding of a *value-producing* ternary
    (`c ? a : b`) back into a single ConditionalExpression, once
    IfStructurer has already built an IfRegion WITH an else_body.

    Sibling to BooleanChainFolder, not a replacement: that pass
    explicitly declines whenever `if_region.else_body is not None`
    (see its `_try_fold`) - this pass exists specifically to cover
    that declined case. The two are disjoint on that one condition,
    so both can run in the same stage without overlap.

    Must run after BooleanChainFolder in the pass ordering: a
    then/else arm's own condition may itself be an `&&`/`||` chain
    that needs folding first, so this pass reads clean conditions
    rather than needing to fold sub-chains itself.
    """

    def __init__(self, cfg):
        self.cfg = cfg

    def run(self, root: SequenceRegion):
        self._visit(root)

    def _visit(self, region):
        if isinstance(region, SequenceRegion):
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
        if isinstance(region, TryRegion):
            self._visit(region.try_body)
            if region.catch:
                self._visit(region.catch.body)
            if region.finally_:
                self._visit(region.finally_.body)
            return
        if hasattr(region, "body"):
            self._visit(region.body)

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
            # two-armed case unchanged, still uses last instruction - TODO:
            # same fix may be needed here too, not yet confirmed necessary
            ...

        # no-else case: don't assume block.instructions[-1] is the default
        # value - it may instead be the branch-condition-computing
        # instruction itself (e.g. `r4 = param1 > 100` immediately
        # preceding the terminator), with the real default sitting
        # earlier in the same block (e.g. `r3 = 100`). Try each
        # dest_reg-bearing instruction from last to first, using the
        # FIRST one whose register also has a matching arm - not
        # positional order.
        for last in reversed(block.instructions):
            # logger.debug(
            #     "ConditionalExpressionFolder._try_fold: block=%d dest_reg=%r default_value=%r, "
            #     "if_region.else_body=%r, if_region.condition=%r",
            #     block.id, last.dest_reg if block.instructions else None,
            #     last.value if block.instructions else None,
            #     if_region.else_body, if_region.condition,
            # )
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
            # logger.debug(
            #     "  no-else fold: arm_block=%d arm_expr=%r default_expr=%r -> new_expr test=%r",
            #     arm_block.id, arm_expr, default_expr, _negate_condition(condition),
            # )
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
        for blk in children:
            for instr in blk.instructions:
                if instr is result:
                    continue
                if instr.statement is not None:
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
        BooleanChainFolder._repoint_node - see that class for the full
        rationale, including why the structural-equality branch is
        needed for Mov-introduced copies. Kept duplicated here rather
        than shared, per earlier decision to avoid guessing at an
        extraction target; TODO: extract to a shared helper once both
        copies are confirmed working, so they can't silently diverge
        again the way this one did (this method didn't exist at all
        until now, despite the comment claiming parity).
        """

        if node is old_expr:
            return new_expr, True

        # Structural-equality fallback only for non-trivial expressions
        # (BinaryExpression, ConditionalExpression, CallExpression, etc) -
        # a bare Identifier or Literal is structurally equal to every OTHER
        # unrelated read of the same name/value throughout the function, so
        # matching those by structural equality corrupts every downstream
        # occurrence, not just the intended Mov-copy target. Only apply this
        # fallback when old_expr's shape is specific enough that a match is
        # actually likely to BE the same logical value, not a coincidence.
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
