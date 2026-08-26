"""Shared helpers for `_finally_matcher` and `_FinallyAttacher`.

Both need to answer "does this run of instruction values match that
run of instruction values" - the matcher to decide whether a wider
handler's body duplicates code already inside a narrower handler's
try/catch (i.e., it's really a `finally`). The attacher to then strip
those duplicated copies once a real `finally` clause is emitted
instead.

`structural_key` itself now lives in `transforms._shared` - see that
module's docstring; it used to be defined locally here (and, a third
time, independently in `region_passes.ForEachRegionPass`) before being
consolidated.
"""

from __future__ import annotations

from hermes_decompiler.analysis.models.regions import IfRegion, SequenceRegion
from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.transforms.shared import structural_key as structural_key

__all__ = ["structural_key", "strip_duplicate_run", "strip_duplicate_span"]


def strip_duplicate_run(region: SequenceRegion, finally_values: list) -> None:
    """Remove the first run in each block matching finally_values, if any.

    Matches the first contiguous run of instructions whose `.value`s
    exactly equal finally_values. Hermes may duplicate the same
    finally sequence independently across MULTIPLE blocks (e.g. both
    branches of a resume-check, each with their own inlined cleanup
    copy) - so this scans and strips per-block across the whole
    region, not just the first occurrence found anywhere.
    """

    if not finally_values:
        return

    finally_keys = [structural_key(v) for v in finally_values]
    n = len(finally_keys)

    for block in list(region.covered_blocks):

        candidates = [i for i in block.instructions if i.value is not None]
        candidate_keys = [structural_key(c.value) for c in candidates]

        for start in range(len(candidates) - n + 1):

            if candidate_keys[start:start + n] != finally_keys:
                continue

            for instr in candidates[start:start + n]:
                block.instructions.remove(instr)

            break


def _items_structurally_equal(a, b) -> bool:
    """Structural equality between two SequenceRegion children.

    `strip_duplicate_run` above only ever matches a flat run of
    instruction *values* within a single block - that can't represent
    a duplicated `if/else` (a `finally` body with its own branching
    gets folded into a sibling `IfRegion` by IfStructurer before
    `_FinallyAttacher` ever runs, the same as it would for any other
    conditional - see `_FinallyAttacher`'s own docstring). This
    compares two direct SequenceRegion children - either a BasicBlock
    (by its instruction values, in order) or an IfRegion (by its
    condition plus a recursive comparison of both branches) - so a
    duplicated branching span can be recognized as a whole.

    Deliberately narrow: only BasicBlock and IfRegion are handled,
    since those are the only shapes Hermes' finally-duplication can
    plausibly produce at the point `_FinallyAttacher` runs (a
    duplicated loop or switch inside a `finally` body isn't a shape
    any current fixture exercises, and guessing at one risks silently
    matching the wrong thing). Anything else compares unequal rather
    than guessing.
    """

    if isinstance(a, BasicBlock) and isinstance(b, BasicBlock):
        a_values = [i.value for i in a.instructions if i.value is not None]
        b_values = [i.value for i in b.instructions if i.value is not None]

        if len(a_values) != len(b_values):
            return False

        return all(
            structural_key(x) == structural_key(y)
            for x, y in zip(a_values, b_values)
        )

    if isinstance(a, IfRegion) and isinstance(b, IfRegion):

        # Deliberately NOT comparing `a.condition`/`b.condition` here.
        # Hermes' finally-duplication routinely re-derives the "same"
        # logical value through a different register at each physical
        # copy - e.g. one copy tests a `Mov`-aliased register while
        # the other tests the original parameter register directly
        # (see tryCatchFinallyBranchInFinallyTest's raw disassembly:
        # the catch-side copy branches on a register freshly `Mov`-ed
        # from `param1`, the finally-wrapper's own copy branches on
        # `param1`'s original register directly) - neither this module
        # nor `_FinallyAttacher` has the register-definition
        # infrastructure (`cfg.reg_definitions`) needed to resolve
        # that aliasing at this level, unlike e.g.
        # `ForEachRegionPass._resolve_identifier`. Requiring exact
        # condition equality would then simply never match a
        # genuinely duplicated branching finally, which is worse than
        # the narrow false-positive risk accepted by skipping it: a
        # wrong match would require an unrelated `if/else` elsewhere
        # in the try/catch printing the exact same literal content in
        # the same order, which - given every `__BC:...` marker string
        # in this codebase's own fixtures is unique per call site - is
        # a non-issue in practice, and the body comparison below still
        # requires full structural equality of both branches.
        if not _sequence_structurally_equal(a.then_body, b.then_body):
            return False

        a_else, b_else = a.else_body, b.else_body

        if (a_else is None) != (b_else is None):
            return False

        if a_else is not None and not _sequence_structurally_equal(a_else, b_else):
            return False

        return True

    return False


def _sequence_structurally_equal(a: SequenceRegion, b: SequenceRegion) -> bool:
    if len(a.children) != len(b.children):
        return False
    return all(_items_structurally_equal(x, y) for x, y in zip(a.children, b.children))


def strip_duplicate_span(region: SequenceRegion, span: list) -> bool:
    """Remove the first contiguous run of `region`'s DIRECT children
    that structurally matches `span` (see `_items_structurally_equal`).

    Generalizes `strip_duplicate_run` to the region-tree level: needed
    once a `finally` body's own content spans multiple siblings (a
    condition block, an `IfRegion` for its own branching, a trailing
    rethrow block - see `_FinallyAttacher._finally_extent`), since
    none of that can be expressed as a flat run of instruction values
    within one block.

    Unlike `strip_duplicate_run`, this requires each matched
    BasicBlock to equal the corresponding span item *entirely* (not
    just contain it as a subrun) - `span` here is the *already
    fully-extracted* finally body, so a whole-item match is the
    correct comparison; a partial/subrun match at this level would
    risk matching an unrelated block that merely happens to start the
    same way.

    Returns True if a match was found and removed.
    """
    if not span:
        return False

    n = len(span)
    children = region.children

    for start in range(len(children) - n + 1):
        if all(
                _items_structurally_equal(children[start + i], span[i])
                for i in range(n)
        ):
            del children[start:start + n]
            region.invalidate_coverage()
            return True

    return False
