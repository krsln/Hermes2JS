from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor
from hermes_decompiler.analysis.models.regions import IfRegion, SequenceRegion
# noinspection PyProtectedMember
from hermes_decompiler.analysis.transforms._shared import (
    _negate_condition,
    _is_pure,
    _TRIVIAL_NODE_TYPES
)  # noqa: SLF001
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.Operators import LogicalOperator
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    Expression)
from ._base import RegionPass

logger = get_logger(__name__)


class BooleanChainRegionPass(RegionPass, RegionVisitor):
    """
    Folds the common short-circuit `||`/`&&` compiled idiom back into a
    single expression, once `IfStructurer` has already turned the raw
    conditional jump into an `IfRegion`. See prior revisions for the
    full fold-mechanics docstring; this revision additionally fixes a
    stale-reference bug:

    NOT responsible for pure control-flow `&&`/`||` (e.g. a bare
    `if (a || b) { ... }` with no intermediate assignment): that's
    `cfg_passes.BranchChainMerger`'s job, which runs much earlier, on
    the raw CFG, before any region exists. This pass specifically
    requires the folded block to end in an assignment (`dest_reg is
    not None`, see `_try_fold`) - the value-producing case
    (`const x = a || b;`). See `BranchChainMerger`'s docstring for the
    full disjointness argument from the other side.

    IR generation (see e.g. `Ret`'s opcode handler) resolves a
    register's value *once*, at the point in the original bytecode
    order where it's read, and freezes that resolved `Expression`
    object directly into e.g. `ReturnStatement.argument`. That
    resolution happens long before this pass runs, and it grabs
    whatever the *last* writer to that register was in raw bytecode
    order - which, for our chain idiom, is the `then_block`'s bare
    `E3` (not the header's `E1`, and definitely not the folded
    `E1 || E2 || E3`).

    When we fold, `then_result.value` (`E3`) is reused unchanged as
    the new `BinaryExpression`'s `.right` - its *object identity*
    never changes, so anything holding a bare reference to that same
    object (like `Ret`'s frozen `argument`) doesn't "see" the fold at
    all; it just keeps rendering the old standalone `E3`.

    `_repoint_references` fixes this by walking every block in the
    CFG after a successful fold and replacing any other reference to
    the pre-fold `E3` object (by identity, not equality - two
    structurally-equal-but-distinct `E3`s elsewhere must NOT be
    touched) with the newly folded expression. `OpcodeResult.value` is
    a plain mutable attribute and can be reassigned directly;
    `ReturnStatement` is a frozen dataclass, so its `argument` field
    is swapped via `dataclasses.replace` instead of direct mutation.

    Traversal is inherited from `RegionVisitor` rather than
    hand-rolled here: the previous hand-rolled `_visit` had no case
    for `SwitchRegion` (and its `hasattr(region, "body")` fallback
    doesn't match it either, since a `SwitchRegion`'s children live
    under `.cases`/`.default_body`, not `.body`) - a chain idiom
    sitting inside a `switch` case or `default` body was silently
    never folded. `RegionVisitor` already knows how to reach those.
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
            if not _is_pure(earlier):
                return False

        condition = if_region.condition

        if condition is None:
            return False

        tail = self._chain_tail(last.value)

        if _negate_condition(tail).structurally_equal(condition):
            operator = LogicalOperator.OR

        elif tail.structurally_equal(condition):
            operator = LogicalOperator.AND

        else:
            return False

        old_tail_expr = then_result.value
        last.value = BinaryExpression(left=last.value, operator=operator, right=old_tail_expr)

        self._repoint_references(old_tail_expr, last.value, min_block_id=then_block.id, exclude={then_result, last})

        return True

    def _repoint_references(self, old_expr, new_expr, min_block_id: int, exclude: set) -> None:

        for blk in self.cfg.blocks:

            if blk.id < min_block_id:
                continue

            for instr in blk.instructions:

                if instr in exclude:
                    continue

                new_value, value_changed = self._repoint_node(
                    instr.value,
                    old_expr,
                    new_expr,
                )

                if value_changed:
                    instr.value = new_value

                if instr.statement is not None:
                    new_stmt, stmt_changed = self._repoint_node(
                        instr.statement,
                        old_expr,
                        new_expr,
                    )

                    if stmt_changed:
                        instr.statement = new_stmt

    def _repoint_node(self, node, old_expr, new_expr):
        """
        Generic, type-agnostic deep replace of `old_expr` (by identity)
        with `new_expr` inside any frozen-dataclass IR `Node` tree.

        Every IR node (Expression *and* Statement, e.g. ReturnStatement)
        is a `frozen=True, slots=True` dataclass whose fields are either
        a `Node`/`Node | None`, or a `tuple[Node, ...]` (see `.children`
        across expressions.py/ControlFlow.py). Rather than hand-listing
        every wrapper shape (`AssignmentExpression.right`,
        `MemberExpression.receiver`, `ReturnStatement.argument`, ...) -
        which is exactly what broke last time, silently, for
        `StoreNPToEnvironment` - we walk `dataclasses.fields(node)`
        generically and rebuild via `dataclasses.replace` wherever a
        field (or a tuple element) is `old_expr` by identity, or
        recursively contains it.

        Returns (possibly-rebuilt node, changed?). Non-dataclass /
        non-Node leaves (str, bool, enums, int, None) are returned
        unchanged - only Node identity/recursion is inspected.
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

            # else: plain value (str/bool/enum/int/None) - nothing to do

        if not any_changed:
            return node, False

        return dataclasses.replace(node, **updates), True

    def _chain_tail(self, value: Expression) -> Expression:

        if isinstance(value, BinaryExpression) and value.operator in self._LOGICAL_OPERATORS:
            return value.right

        return value
