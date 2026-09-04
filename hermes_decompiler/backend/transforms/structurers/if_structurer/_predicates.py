"""Shared, side-effect-free helpers for the IfStructurer pass.

Used by both `_DominanceIfBuilder` and `_CompoundConditionFolder`.
Each function inspects a region/expression and returns a bool, or
builds and returns a new expression node. - Nothing here mutates a
region tree or touches `RegionGraph` directly, so this module stays
safely importable from both without coupling them to each other.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.ir.Operators import LogicalOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, UnaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch


def is_empty_body(body) -> bool:
    """Return True if the body is None or an empty SequenceRegion."""
    if body is None:
        return True
    if isinstance(body, SequenceRegion):
        return len(body.children) == 0
    return False


def is_inert_block(item) -> bool:
    """Return True if the item is a BasicBlock with no real statements."""
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


def single_if_child(body) -> IfRegion | None:
    """Return the sole meaningful IfRegion inside body, or None.

    Accepts a bare IfRegion, or a SequenceRegion whose only non-inert
    child is an IfRegion (Hermes often leaves empty/const-load blocks
    as siblings).
    """
    if isinstance(body, IfRegion):
        return body
    if not isinstance(body, SequenceRegion):
        return None
    meaningful = [c for c in body.children if not is_inert_block(c)]
    if len(meaningful) == 1 and isinstance(meaningful[0], IfRegion):
        return meaningful[0]
    return None


def is_negation(expr) -> bool:
    """Return True if expr is a logical-not (UnaryOperator.LOGICAL_NOT)."""
    if expr is None:
        return False
    if isinstance(expr, UnaryExpression):
        return expr.operator == UnaryOperator.LOGICAL_NOT
    return getattr(expr, "operator", None) == UnaryOperator.LOGICAL_NOT


def unwrap_negation(expr):
    """Return the operand of a negation expression, or expr unchanged."""
    if isinstance(expr, UnaryExpression):
        return expr.operand
    return getattr(expr, "operand", expr)


def make_logical_and(left, right) -> BinaryExpression:
    """Build a `left && right` expression node."""
    return BinaryExpression(left=left, operator=LogicalOperator.AND, right=right)


def make_logical_or(left, right) -> BinaryExpression:
    """Build a `left || right` expression node."""
    return BinaryExpression(left=left, operator=LogicalOperator.OR, right=right)


def is_backward_branch(block: BasicBlock) -> bool:
    """Return True if the block's conditional branch targets itself or earlier.

    Such a branch is always loop machinery (a guard or continue test),
    never a genuine forward if/goto-merge residual. Shared by
    `_DominanceIfBuilder` and `_CompoundConditionFolder`, which both
    must leave these blocks untouched so `LoopConditionExtractor`
    (runs later, in region_passes) can still recognize them as the
    loop's actual guard.
    """
    branch = block.terminator
    if not isinstance(branch, TerminatorConditionalBranch):
        return False
    return branch.target <= block.address


def representative_block(item) -> BasicBlock | None:
    """Return a single BasicBlock usable for a dominance check on an item.

    For a raw BasicBlock, that's the block itself. For an already-built
    region (IfRegion/LoopRegion/TryRegion), any covered block works -
    a single-entry region is dominated as a unit, so every member
    shares the same dominance relationship to blocks outside it. The
    lowest-id block is picked for a deterministic result.
    """
    if isinstance(item, BasicBlock):
        return item

    covered = item.covered_blocks
    if not covered:
        return None

    return min(covered, key=lambda b: b.id)
