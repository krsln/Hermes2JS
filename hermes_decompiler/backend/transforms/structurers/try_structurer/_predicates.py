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

from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.transforms.shared import structural_key as structural_key

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
    that structurally matches `span` (see `_items_structurally_equal`
    for non-edge items).

    Generalizes `strip_duplicate_run` to the region-tree level: needed
    once a `finally` body's own content spans multiple siblings (a
    condition block, an `IfRegion` for its own branching, a trailing
    rethrow block - see `_FinallyAttacher._finally_extent`), since
    none of that can be expressed as a flat run of instruction values
    within one block.

    The FIRST and LAST items of `span`, when they are BasicBlocks, are
    matched as a partial SUBRUN of the corresponding candidate block's
    own instruction values, not a whole-block match - mirroring
    `strip_duplicate_run`'s own per-block partial matching. This
    matters whenever unrelated genuine content shares a physical block
    with the duplicated span's own leading/trailing setup instructions
    purely because nothing in the ORIGINAL bytecode ever branched
    between them - see tryCatchFinallyBranchInFinallyTest: the
    finally-wrapper's own span is `[<console/console.log-fetch block>,
    IfRegion]` (the fetch is hoisted once, shared by both the `if` and
    `else` arms' own `console.log` calls), but the catch clause's
    matching copy has that SAME fetch sharing a block with an
    unrelated, genuine "catch-block" print that must NOT be swept away
    with it - a whole-block match would never find this duplicate at
    all, since the two blocks' FULL instruction lists differ (extra
    "catch-block" content on one side), even though the meaningful,
    duplicated PART of each is identical.

    Any MIDDLE item (when `span` has more than 2 items) still requires
    a full, whole-item match - only a span's own edges can plausibly
    share a block with adjacent, unrelated content; the codebase's
    finally-duplication has never been observed splicing unrelated
    statements into the MIDDLE of a duplicated span.

    Returns True if a match was found and removed.
    """
    if not span:
        return False

    n = len(span)
    children = region.children

    for start in range(len(children) - n + 1):
        window = children[start:start + n]

        plan = _match_span_window(window, span)

        if plan is None:
            continue

        _apply_span_removal(children, start, window, plan)
        region.invalidate_coverage()
        return True

    return False


def _block_value_instr_pairs(block: BasicBlock) -> list:
    return [(instr.value, instr) for instr in block.instructions if instr.value is not None]


def _find_subrun(candidate_keys: list, target_keys: list):
    """Return the (start, end) exclusive-end index range within
    `candidate_keys` where `target_keys` appears as a contiguous
    subrun, or None if it doesn't appear at all. An empty
    `target_keys` trivially matches at position (0, 0).
    """
    n = len(target_keys)

    if n == 0:
        return 0, 0

    for start in range(len(candidate_keys) - n + 1):
        if candidate_keys[start:start + n] == target_keys:
            return start, start + n

    return None


def _match_span_window(window: list, span: list):
    """Try to match `window` (a same-length slice of some region's
    children) against `span`. Returns a per-item removal plan (a list
    the same length as `span`) on success, or None on failure.

    Each plan entry is either:
      - `None`         - the window item is a full, whole-item match
                          for the span item; remove it entirely.
      - `(start, end)`  - the window item is a BasicBlock whose
                          VALUE-bearing instructions[start:end] match
                          the span item's own values as a subrun;
                          remove only that subrun (see
                          `_apply_span_removal`), keeping the rest of
                          the block's content in place.

    Only the first (index 0) and last (index `len(span)-1`) positions
    are ever considered for subrun matching - see `strip_duplicate_span`'s
    own docstring for why.
    """
    n = len(span)
    plan = []

    for i in range(n):
        candidate = window[i]
        target = span[i]
        is_edge = i == 0 or i == n - 1

        if is_edge and isinstance(candidate, BasicBlock) and isinstance(target, BasicBlock):
            target_keys = [
                structural_key(value)
                for value, _ in _block_value_instr_pairs(target)
            ]
            candidate_keys = [
                structural_key(value)
                for value, _ in _block_value_instr_pairs(candidate)
            ]

            match_range = _find_subrun(candidate_keys, target_keys)

            if match_range is None:
                return None

            plan.append(match_range)
            continue

        if not _items_structurally_equal(candidate, target):
            return None

        plan.append(None)

    return plan


def _apply_span_removal(children: list, start: int, window: list, plan: list) -> None:
    """Perform the removal described by `plan` (see
    `_match_span_window`) against `children[start:start + len(window)]`.

    Whole-item matches (`plan[i] is None`) are deleted from `children`
    outright. Subrun matches (`plan[i] = (lo, hi)`) instead remove
    just that instruction subrun from the matched BasicBlock's own
    `.instructions`, leaving the block itself in place with whatever
    unrelated content surrounded the duplicate.
    """
    whole_item_indices = []

    for offset, (item, entry) in enumerate(zip(window, plan)):
        if entry is None:
            whole_item_indices.append(start + offset)
            continue

        lo, hi = entry
        pairs = _block_value_instr_pairs(item)

        for _, instr in pairs[lo:hi]:
            item.instructions.remove(instr)

    for index in sorted(whole_item_indices, reverse=True):
        del children[index]
