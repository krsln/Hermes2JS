from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    RegionVisitor,
    IfRegion,
    SequenceRegion,
)
from hermes_decompiler.backend.transforms.shared import is_pure
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import (
    AssignmentOperator,
    BinaryOperator,
)
from hermes_decompiler.ir.expressions import (
    AssignmentExpression,
    BinaryExpression,
    Identifier,
    MemberExpression,
    NullLiteral,
)
from .BaseRegionPass import RegionPass

logger = get_logger(__name__)


class NullishAssignmentRegionPass(RegionPass, RegionVisitor):
    """
    Fold:

        if (obj.prop == null) {
            obj.prop = value;
        }

    into:

        obj.prop ??= value;

    The Hermes bytecode usually represents the nullish check through
    temporary registers:

        r3 = obj.prop
        r2 = null

        if (r3 == r2) {
            r1.prop = value
        }

    Therefore, this pass resolves register definitions locally instead
    of requiring the condition itself to contain a MemberExpression.

    The pass deliberately remains narrow:

    - equality only (`==`)
    - null only
    - no else branch
    - exactly one executable then-block
    - exactly one final assignment
    - assignment target must match the checked MemberExpression
    - no observable statements before the assignment

    This keeps the transformation semantics-preserving.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    # ------------------------------------------------------------------
    # Traversal
    # ------------------------------------------------------------------

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)

        self._fold_sequence(node)

    def _fold_sequence(self, region: SequenceRegion) -> None:
        # Remove empty blocks first. They are not semantically relevant
        # for the structural pattern matching below.
        region.children = [
            child
            for child in region.children
            if not (
                    isinstance(child, BasicBlock)
                    and not child.instructions
            )
        ]

        index = 0

        while index < len(region.children):
            child = region.children[index]

            if isinstance(child, IfRegion):
                replacement = self._try_fold(child)

                if replacement is not None:
                    region.children[index] = replacement

            index += 1

    # ------------------------------------------------------------------
    # Main pattern
    # ------------------------------------------------------------------

    def _try_fold(self, if_region: IfRegion):
        """
        Try to transform:

            if (X == null) {
                X = value;
            }

        into:

            X ??= value;
        """

        # `??=` only represents the no-else form.
        if if_region.else_body is not None:
            return None

        target_member = self._extract_null_check_target(
            if_region.condition,
            if_region,
        )

        if target_member is None:
            return None

        assignment_block = self._get_single_assignment_block(
            if_region
        )

        if assignment_block is None:
            return None

        assignment = assignment_block.instructions[-1]

        if not isinstance(
                assignment.value,
                AssignmentExpression,
        ):
            return None

        expression = assignment.value

        if expression.operator != AssignmentOperator.ASSIGN:
            return None

        if not isinstance(
                expression.left,
                MemberExpression,
        ):
            return None

        # The checked property and assigned property must be the same.
        if not expression.left.structurally_equal(target_member):
            return None

        # Anything before the assignment must be non-observable.
        if not self._has_only_consumable_setup(
                assignment_block
        ):
            return None

        # The condition was only needed to establish the nullish guard.
        # Its register definitions can now be marked as consumed.
        self._mark_guard_definitions_used(
            if_region.condition,
            if_region,
        )

        # Replace:
        #
        #     obj.prop = value
        #
        # with:
        #
        #     obj.prop ??= value
        #
        assignment.value = dataclasses.replace(
            expression,
            operator=AssignmentOperator.NULLISH_ASSIGN,
        )

        return assignment_block

    # ------------------------------------------------------------------
    # Then-body validation
    # ------------------------------------------------------------------

    @staticmethod
    def _get_single_assignment_block(
            if_region: IfRegion,
    ) -> BasicBlock | None:

        children = [
            child
            for child in if_region.then_body.children
            if not (
                    isinstance(child, BasicBlock)
                    and not child.instructions
            )
        ]

        if len(children) != 1:
            return None

        block = children[0]

        if not isinstance(block, BasicBlock):
            return None

        if not block.instructions:
            return None

        return block

    @staticmethod
    def _has_only_consumable_setup(
            block: BasicBlock,
    ) -> bool:
        """Return True if everything before the final assignment is
        inlineable compiler setup, with no observable side effects.

        Checking `.statement is not None` alone is not sufficient: an
        instruction can be independently observable (a call's side
        effect, a mutation) without yet having been promoted to its
        own `.statement` node at this point in the pipeline - see
        `ConditionalExpressionRegionPass._single_result`'s docstring
        for the same problem. `_is_pure` (shared with
        `BooleanChainRegionPass`) already applies both checks, so a
        call such as `foo();` sitting before the assignment is never
        silently absorbed into the fold.
        """

        return all(is_pure(instruction) for instruction in block.instructions[:-1])

    # ------------------------------------------------------------------
    # Condition analysis
    # ------------------------------------------------------------------

    def _extract_null_check_target(
            self,
            condition,
            if_region: IfRegion,
    ) -> MemberExpression | None:
        """
        Resolve:

            obj.prop == null

        as well as the register-based form:

            r3 == r2

        where:

            r3 = obj.prop
            r2 = null
        """

        if not isinstance(condition, BinaryExpression):
            return None

        if condition.operator != BinaryOperator.EQUAL:
            return None

        # --------------------------------------------------------------
        # Direct form:
        #
        #     obj.prop == null
        # --------------------------------------------------------------

        direct = self._extract_direct_member_null_check(condition)

        if direct is not None:
            return direct

        # --------------------------------------------------------------
        # Register form:
        #
        #     r3 == r2
        #
        # Resolve whichever side is the member register and whichever
        # side is the null register.
        # --------------------------------------------------------------

        left = condition.left
        right = condition.right

        if isinstance(left, Identifier):
            if self._is_nullish_value(right, if_region):
                member = self._resolve_member_register(
                    left.name,
                    if_region,
                )

                if member is not None:
                    return member

        if isinstance(right, Identifier):
            if self._is_nullish_value(left, if_region):
                member = self._resolve_member_register(
                    right.name,
                    if_region,
                )

                if member is not None:
                    return member

        return None

    @staticmethod
    def _extract_direct_member_null_check(
            condition: BinaryExpression,
    ) -> MemberExpression | None:

        left = condition.left
        right = condition.right

        if (
                isinstance(left, MemberExpression)
                and isinstance(right, NullLiteral)
        ):
            return left

        if (
                isinstance(right, MemberExpression)
                and isinstance(left, NullLiteral)
        ):
            return right

        return None

    # ------------------------------------------------------------------
    # Register resolution
    # ------------------------------------------------------------------

    def _is_nullish_value(
            self,
            expression,
            if_region: IfRegion,
    ) -> bool:
        """
        Return True when `expression` is either:

            null

        or a register whose definition is:

            rX = null
        """

        if isinstance(expression, NullLiteral):
            return True

        if not isinstance(expression, Identifier):
            return False

        if not expression.name.startswith("r"):
            return False

        value = self._find_register_definition(
            expression.name,
            if_region,
        )

        return isinstance(value, NullLiteral)

    def _resolve_member_register(
            self,
            register_name: str,
            if_region: IfRegion,
    ) -> MemberExpression | None:
        """
        Resolve:

            r3

        to its preceding definition:

            r3 = obj.prop
        """

        value = self._find_register_definition(
            register_name,
            if_region,
        )

        if isinstance(value, MemberExpression):
            return value

        return None

    def _find_register_definition(
            self,
            register_name: str,
            if_region: IfRegion,
    ):
        """
        Find the nearest dominating definition of `register_name`
        immediately before the IfRegion in its parent SequenceRegion.

        This is intentionally local. We do not perform arbitrary CFG
        data-flow here.
        """

        parent = if_region.parent

        if not isinstance(parent, SequenceRegion):
            return None

        try:
            index = parent.children.index(if_region)
        except ValueError:
            return None

        for previous in reversed(parent.children[:index]):
            if not isinstance(previous, BasicBlock):
                continue

            for instruction in reversed(
                    previous.instructions or []
            ):
                dest_reg = getattr(
                    instruction,
                    "dest_reg",
                    None,
                )

                if dest_reg is None:
                    continue

                if f"r{dest_reg}" != register_name:
                    continue

                return getattr(
                    instruction,
                    "value",
                    None,
                )

        return None

    # ------------------------------------------------------------------
    # Definition usage
    # ------------------------------------------------------------------

    def _mark_guard_definitions_used(
            self,
            condition,
            if_region: IfRegion,
    ) -> None:
        """
        The condition's temporary registers become dead after folding.

        Example:

            r3 = obj.count
            r2 = null

            if (r3 == r2) {
                ...
            }

        After folding:

            obj.count ??= 0

        therefore, r3/r2 should not be emitted as standalone definitions.
        """

        if not isinstance(condition, BinaryExpression):
            return

        for operand in (
                condition.left,
                condition.right,
        ):
            if not isinstance(operand, Identifier):
                continue

            if not operand.name.startswith("r"):
                continue

            self._mark_register_definition_used(
                operand.name,
                if_region,
            )

    def _mark_register_definition_used(
            self,
            register_name: str,
            if_region: IfRegion,
    ) -> None:
        """
        Mark the actual defining OpcodeResult as consumed.

        This works on the region structure rather than depending on
        HermesAnalysis.registers still representing the exact point
        at which the region pass runs.
        """

        parent = if_region.parent

        if not isinstance(parent, SequenceRegion):
            return

        try:
            index = parent.children.index(if_region)
        except ValueError:
            return

        for previous in reversed(parent.children[:index]):
            if not isinstance(previous, BasicBlock):
                continue

            for instruction in reversed(
                    previous.instructions or []
            ):
                dest_reg = getattr(
                    instruction,
                    "dest_reg",
                    None,
                )

                if dest_reg is None:
                    continue

                if f"r{dest_reg}" != register_name:
                    continue

                instruction.definition_used = True
                return
