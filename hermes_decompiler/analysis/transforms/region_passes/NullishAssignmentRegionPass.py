from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionVisitor import RegionVisitor
from hermes_decompiler.analysis.regions.Regions import IfRegion, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import AssignmentOperator, BinaryOperator
from hermes_decompiler.ir.expressions import (
    AssignmentExpression, BinaryExpression, MemberExpression, NullLiteral,
)

from ._base import RegionPass

logger = get_logger(__name__)


class NullishAssignmentRegionPass(RegionPass, RegionVisitor):
    """
    Folds:
        if (obj.prop == null) { obj.prop = default; }
    into:
        obj.prop ??= default;

    Distinct from BooleanChainRegionPass/ConditionalExpressionRegionPass:
    those match by dest_reg (a register-valued merge). PutById has NO
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
        if if_region.else_body is not None:
            return None
        if target_member is None:
            return None

        children = [
            c for c in if_region.then_body.children
            if not (isinstance(c, BasicBlock) and not c.instructions)
        ]
        if len(children) != 1 or not isinstance(children[0], BasicBlock):
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
        # same purity bar as ConditionalExpressionRegionPass._single_result.
        for earlier in block.instructions[:-1]:
            if earlier.statement is not None:
                return None

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