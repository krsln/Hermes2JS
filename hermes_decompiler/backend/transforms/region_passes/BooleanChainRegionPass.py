from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, IfRegion, SequenceRegion
from hermes_decompiler.backend.transforms.region_passes._base import RegionPass
from hermes_decompiler.backend.transforms.shared import (
    negate_condition, is_pure, has_side_effects, repoint_references, reclaim_definition,
    reclaim_unfolded_definition, TRIVIAL_NODE_TYPES
)
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression

logger = get_logger(__name__)


class BooleanChainRegionPass(RegionPass, RegionVisitor):
    """Folds the short-circuit ||/&& compiled idiom into a single expression.

    Runs once IfStructurer has already turned the raw conditional jump
    into an IfRegion.

    Not responsible for pure control-flow &&/|| (e.g., a bare
    `if (a || b) { ... }` with no intermediate assignment) - that's
    `cfg_passes.ShortCircuitConditionCfgPass`'s job, which runs much earlier, on
    the raw CFG, before any region exists. This pass specifically
    requires the folded block to end in an assignment (`dest_reg is
    not None`, see `_try_fold`) - the value-producing case
    (`const x = a || b;`). See ShortCircuitConditionCfgPass's docstring for the
    full disjointness argument from the other side.

    Stale-reference fix
    --------------------
    IR generation (see e.g., `Ret`'s opcode handler) resolves a
    register's value once, at the point in the original bytecode order
    where it's read, and freezes that resolved Expression object
    directly into e.g., ReturnStatement.argument. That resolution
    happens long before this pass runs, and grabs whatever the last
    writer to that register was in raw bytecode order - which, for our
    chain idiom, is the then_block's bare E3 (not the header's E1, and
    definitely not the folded E1 || E2 || E3).

    When we fold, then_result.value (E3) is reused unchanged as the
    new BinaryExpression's .right - its object identity never changes,
    so anything holding a bare reference to that same object (like
    Ret's frozen argument) doesn't "see" the fold at all; it just keeps
    rendering the old standalone E3.

    `_repoint_references` fixes this by walking every block in the CFG
    after a successful fold and replacing any other reference to the
    pre-fold E3 object (by identity, not equality - two
    structurally-equal-but-distinct E3s elsewhere must not be touched)
    with the newly folded expression. OpcodeResult.value is a plain
    mutable attribute and can be reassigned directly; ReturnStatement
    is a frozen dataclass, so its argument field is swapped via
    dataclasses.replace instead of direct mutation.

    Traversal is inherited from RegionVisitor rather than hand-rolled:
    a hand-rolled `_visit` with a `hasattr(region, "body")` fallback
    would miss SwitchRegion, whose children live under
    `.cases`/`.default_body`, not `.body` - silently skipping a chain
    idiom inside a switch case or default body. RegionVisitor already
    knows how to reach those.
    """

    _LOGICAL_OPERATORS = (LogicalOperator.OR, LogicalOperator.AND)

    def run(self) -> None:
        self.visit(self.graph.root)

    # ------------------------------------------------------------------
    # Traversal - only SequenceRegion needs pass-specific behavior
    # (fold after descending); every other region kind uses
    # RegionVisitor's default recursion unchanged.
    # ------------------------------------------------------------------

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._fold_sequence(node)

    # ------------------------------------------------------------------

    def _fold_sequence(self, region: SequenceRegion):

        # Empty BasicBlocks (no instructions - merge/passthrough points
        # left behind by IfStructurer) render nothing and would
        # otherwise break the adjacency `_try_fold` relies on.
        region.children = [
            child for child in region.children
            if not (isinstance(child, BasicBlock) and not child.instructions)
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

        if if_region.else_body is not None:
            return False

        if not block.instructions:
            return False

        last = block.instructions[-1]

        if last.dest_reg is None or not isinstance(last.value, Expression):
            return False

        then_children = if_region.then_body.children

        if len(then_children) != 1:
            return False

        then_block = then_children[0]

        if not isinstance(then_block, BasicBlock):
            return False

        if not then_block.instructions:
            return False

        then_result = then_block.instructions[-1]

        if then_result.dest_reg != last.dest_reg:
            return False

        if not isinstance(then_result.value, Expression):
            return False

        for earlier in then_block.instructions[:-1]:
            if not is_pure(earlier):
                return self._decline(last, then_result, then_block, if_region)

            # The fold below keeps ONLY `then_result.value` and deletes the
            # whole IfRegion, so an earlier instruction survives only if
            # its value is part of that expression (`a || f(g(x))` keeps
            # `g(x)` as an operand of `f`). One that isn't - e.g. a
            # `r7 = it.next()` whose result a LATER block reads - would be
            # dropped along with its side effect.
            if has_side_effects(earlier.value) and not self._is_operand_of(
                    earlier.value, then_result.value
            ):
                return self._decline(last, then_result, then_block, if_region)

        condition = if_region.condition

        if condition is None:
            return False

        # What does the `if` test? The value built so far: `r = a && b; if (!r)`
        # tests `a && b` as a whole, and once the earlier fold has been
        # repointed into the condition that is exactly what it holds.
        #
        # A condition read that no fold has repointed still carries the
        # arm's own value - the chain's RIGHT operand `b` - so that is
        # accepted too. (It is the weaker match: `!b` alone is not `!(a && b)`
        # when `a` is falsy, which is why the whole value is tried first.)
        tested = [last.value]
        tail = self._chain_tail(last.value)

        if tail is not last.value:
            tested.append(tail)

        for candidate in tested:
            if negate_condition(candidate).structurally_equal(condition):
                operator = LogicalOperator.OR
                break

            if candidate.structurally_equal(condition):
                operator = LogicalOperator.AND
                break

        else:
            return self._decline(last, then_result, then_block, if_region)

        old_tail_expr = then_result.value
        old_last_value = last.value
        last.value = BinaryExpression(left=old_last_value, operator=operator, right=old_tail_expr)

        # The fold result must be printed as `rN = ...`: see `reclaim_definition`.
        reclaim_definition(
            self.cfg, self.graph.root, last, old_last_value, then_result,
            ignore_blocks={then_block}, ignore_regions={if_region},
        )

        repoint_references(
            self.cfg,
            self.graph.root,
            old_tail_expr,
            last.value,
            min_block_id=then_block.id,
            exclude={then_result, last},
        )

        return True

    def _decline(self, last, then_result, then_block, if_region) -> bool:
        """The shape matched but the fold is refused: the merge stays an
        `if`. Make sure its head definition is still printed."""
        reclaim_unfolded_definition(
            self.cfg, self.graph.root, last, then_result,
            ignore_blocks={then_block}, ignore_regions={if_region},
        )

        return False

    @staticmethod
    def _is_operand_of(target: Node, root: Node) -> bool:
        """True if `target` occurs inside `root`'s expression tree: by
        identity, or - for a non-trivial `target` - by structural
        equality (see `shared._repoint.repoint_node` for why trivial nodes never match
        structurally).
        """
        if root is target:
            return True

        if (not isinstance(target, TRIVIAL_NODE_TYPES)
                and isinstance(root, type(target))
                and root.structurally_equal(target)):
            return True

        if not dataclasses.is_dataclass(root) or not isinstance(root, Node):
            return False

        for field in dataclasses.fields(root):
            value = getattr(root, field.name)

            children = value if isinstance(value, tuple) else (value,)

            for child in children:
                if isinstance(child, Node) and BooleanChainRegionPass._is_operand_of(target, child):
                    return True

        return False

    def _chain_tail(self, value: Expression) -> Expression:

        if isinstance(value, BinaryExpression) and value.operator in self._LOGICAL_OPERATORS:
            return value.right

        return value
