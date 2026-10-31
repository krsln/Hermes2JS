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
from hermes_decompiler.backend.transforms.shared import is_unfolded_literal_definition, prints_definition
from hermes_decompiler.ir.Operators import BinaryOperator, LogicalOperator, UnaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Literal, UndefinedLiteral, UnaryExpression
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
        # A printed array/object literal definition prints a statement that
        # later code reads by name: not inert (see `is_unfolded_literal_definition`).
        if is_unfolded_literal_definition(instr):
            return False
        # Any other PRINTED definition (`r6 = r4`, `r4 = r5[1]`, `r2 = 1`) is a
        # statement later code may read by name. Looking past it as clutter lets
        # a fold delete its only definition. A constant load is no exception:
        # the constant being embedded in the nested condition does not help a
        # reader that names the register.
        if prints_definition(instr):
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
    lowest-id real block is picked for a deterministic result.
    """
    if isinstance(item, BasicBlock):
        return item

    covered = item.covered_blocks
    if not covered:
        return None

    # A synthetic block (a `break`/`continue` marker the loop structurers
    # add, address -1) is not in the dominator tree: picking it as the
    # representative makes `dominates()` fail for the whole region.
    real = [b for b in covered if b.address >= 0]

    return min(real or covered, key=lambda b: b.id)


def is_constant_comparison(condition) -> bool:
    """`x === 3` / `x === undefined`: a link of a `case` chain, whose
    shared targets (`case 3: case 4:`) `SwitchStructurer` expects to
    find as a cascade of if/else, not as a join."""
    return (
            isinstance(condition, BinaryExpression)
            and condition.operator in (BinaryOperator.STRICT_EQUAL, BinaryOperator.STRICT_NOT_EQUAL)
            and (isinstance(condition.right, (Literal, UndefinedLiteral))
                 or isinstance(condition.left, (Literal, UndefinedLiteral)))
    )


def same_case_subject(condition, other) -> bool:
    """Do two constant comparisons test the same value (`x === 3`, `x === 4`)?

    A `case` chain tests ONE discriminant; `typeof v === "object"` next to
    `v === null` are two ordinary tests that merely both use a constant.
    """

    def subject(c):
        if not is_constant_comparison(c):
            return None

        return c.left if isinstance(c.right, (Literal, UndefinedLiteral)) else c.right

    a, b = subject(condition), subject(other)

    return a is not None and b is not None and a.structurally_equal(b)


def same_constant_test(condition, other) -> bool:
    """Do two constant comparisons test the same value against the SAME constant (`0 !== r6`, `0 === r6`)?

    A `case` chain tests one discriminant against DIFFERENT constants; the same constant twice is a
    re-test of a value the code recomputed in between (98/2618: `r6 = lanes & childLanes` again)."""

    if not (is_constant_comparison(condition) and is_constant_comparison(other)):
        return False

    def constant(c):
        return c.right if isinstance(c.right, (Literal, UndefinedLiteral)) else c.left

    return same_case_subject(condition, other) and constant(condition).structurally_equal(constant(other))
