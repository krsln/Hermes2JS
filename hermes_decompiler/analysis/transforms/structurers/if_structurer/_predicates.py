from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models.regions import IfRegion, SequenceRegion
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.ir.Operators import LogicalOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, UnaryExpression

"""
Pure, stateless helpers shared by `_DominanceIfBuilder` and
`_CompoundConditionFolder`. Nothing here touches `RegionGraph` or
mutates a tree in place - every function either inspects a region/
expression and returns a bool, or builds and returns a brand new
expression node. Keeping this module side-effect-free is what makes
it safely importable from both buckets without coupling them to each
other.
"""


def is_empty_body(body) -> bool:
    if body is None:
        return True
    if isinstance(body, SequenceRegion):
        return len(body.children) == 0
    return False


def is_inert_block(item) -> bool:
    """Empty or terminator-free BasicBlock with no statements."""
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

    Accepts either a bare IfRegion or a SequenceRegion whose only
    non-inert child is an IfRegion (Hermes often leaves empty /
    const-load blocks as siblings).
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
    """True when expr is a logical-not (UnaryOperator.LOGICAL_NOT)."""
    if expr is None:
        return False
    if isinstance(expr, UnaryExpression):
        return expr.operator == UnaryOperator.LOGICAL_NOT
    return getattr(expr, "operator", None) == UnaryOperator.LOGICAL_NOT


def unwrap_negation(expr):
    if isinstance(expr, UnaryExpression):
        return expr.operand
    return getattr(expr, "operand", expr)


def make_logical_and(left, right) -> BinaryExpression:
    return BinaryExpression(left=left, operator=LogicalOperator.AND, right=right)


def make_logical_or(left, right) -> BinaryExpression:
    return BinaryExpression(left=left, operator=LogicalOperator.OR, right=right)


def is_backward_branch(block: BasicBlock) -> bool:
    """
    True iff `block`'s conditional-branch target address is <= its own
    address - always loop machinery (a guard or continue-test), never
    a genuine forward if/goto-merge residual. Shared by
    `_DominanceIfBuilder` (to skip such blocks when picking an if/else
    candidate) and `_CompoundConditionFolder` (to skip them when
    absorbing residual conditionals) - both need to leave these
    completely untouched so `LoopConditionExtractor` (region_passes,
    runs later) can still recognize them as the loop's actual guard.
    """
    branch = block.terminator
    if not isinstance(branch, TerminatorConditionalBranch):
        return False
    return branch.target <= block.address


def representative_block(item) -> BasicBlock | None:
    """
    Any single `BasicBlock` that dominance checks against `item` can
    be run on. For a raw `BasicBlock`, that's `item` itself. For an
    already-built region (`IfRegion`/`LoopRegion`/`TryRegion`), every
    block it covers shares the same dominance relationship to blocks
    *outside* it - single-entry regions are dominated as a unit, by
    construction - so any element of `covered_blocks` is an equally
    valid representative.
    """
    if isinstance(item, BasicBlock):
        return item

    covered = item.covered_blocks
    if not covered:
        return None

    # `min(..., key=...)` rather than `next(iter(...))`: both are
    # deterministic now that `BasicBlock.__hash__` is id-based (see
    # that class), but picking explicitly by `.id` documents *why*
    # any element works (dominance is invariant across a single-entry
    # region's covered blocks) instead of leaving it to look like an
    # arbitrary/unspecified choice.
    return min(covered, key=lambda b: b.id)
