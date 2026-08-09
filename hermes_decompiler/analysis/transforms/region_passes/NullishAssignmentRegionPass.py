from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion, LoopRegion, IfRegion, TryRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import AssignmentOperator, BinaryOperator
from hermes_decompiler.ir.expressions import (
    AssignmentExpression, BinaryExpression, MemberExpression, NullLiteral,
)

logger = get_logger(__name__)


class NullishAssignmentRegionPass:
    """
    Folds:
        if (obj.prop == null) { obj.prop = default; }
    into:
        obj.prop ??= default;

    Distinct from BooleanChainFolder/ConditionalExpressionFolder: those
    match by dest_reg (a register-valued merge). PutById has NO
    dest_reg (see PutById.handle - it's rendered as a bare statement,
    not a register-producing expression), so there is no register to
    key off. This pass instead matches by structural equality of the
    MemberExpression lvalue between the guard condition and the
    then-body's assignment.

    Deliberately narrow: only the `== null` guard / plain assignment
    shape. `||=`/`&&=` on a member expression would need the analogous
    truthy/falsy guard variants - not implemented here, no evidence
    yet that Hermes emits them for member-expression targets the same
    way it does for registers.
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
        while index < len(region.children):
            if_region = region.children[index]
            if isinstance(if_region, IfRegion):
                replacement = self._try_fold(if_region)
                if replacement is not None:
                    region.children[index] = replacement
                    index += 1
                    continue
            index += 1

    def _try_fold(self, if_region: IfRegion):
        target_member = self._extract_null_check_target(if_region.condition)
        # logger.debug(
        #     "NullishAssignmentFolder._try_fold: condition=%r -> target_member=%r",
        #     if_region.condition, target_member,
        # )
        if if_region.else_body is not None:
            # logger.debug("  bail: has else_body")
            return None
        if target_member is None:
            # logger.debug("  bail: condition isn't a MemberExpression == null check")
            return None

        children = [
            c for c in if_region.then_body.children
            if not (isinstance(c, BasicBlock) and not c.instructions)
        ]
        # logger.debug("  then_body children=%r", children)
        if len(children) != 1 or not isinstance(children[0], BasicBlock):
            # logger.debug("  bail: then_body isn't exactly one BasicBlock")
            return None

        block = children[0]
        if not block.instructions:
            return None

        instr = block.instructions[-1]
        if not isinstance(instr.value, AssignmentExpression):
            return None
        if instr.value.operator != AssignmentOperator.ASSIGN:
            return None
        if not isinstance(instr.value.left, MemberExpression):
            return None
        if not instr.value.left.structurally_equal(target_member):
            return None

        # Every earlier instruction in the block must be inlined-and-consumed
        # (LoadConstZero etc.), not an independently observable statement -
        # same purity bar as ConditionalExpressionFolder._single_result.
        for earlier in block.instructions[:-1]:
            if earlier.statement is not None:
                return None

        # logger.debug("  FOLDING to ??=")
        instr.value = AssignmentExpression(
            left=instr.value.left,
            operator=AssignmentOperator.NULLISH_ASSIGN,
            right=instr.value.right,
        )
        return block

    @staticmethod
    def _extract_null_check_target(condition):
        """
        Matches `X == null` (Hermes' `== null` idiom for nullish
        checks) and returns X if it's a MemberExpression, else None.
        Deliberately narrow to `==`/null - not `===`, not `undefined`,
        not the negated form - no evidence yet those show up for this
        lvalue shape; widen only against a real fixture that needs it.
        """
        if not isinstance(condition, BinaryExpression):
            return None
        if condition.operator != BinaryOperator.EQUAL:
            return None
        if isinstance(condition.left, MemberExpression) and isinstance(condition.right, NullLiteral):
            return condition.left
        if isinstance(condition.right, MemberExpression) and isinstance(condition.left, NullLiteral):
            return condition.right
        return None
