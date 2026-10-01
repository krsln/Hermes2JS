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

Matching is register-aware via `transforms.shared.resolved_structural_equal`
(built on the same `resolve_identifier` reaching-definition walk
`ForEachRegionPass` uses) rather than plain `structural_key` equality:
Hermes' finally-duplication routinely re-derives the same logical
value through a different physical register at each copy (see
`resolved_structural_equal`'s own docstring), so an exact-value match
alone misses those and leaves a genuine `finally` mis-recognized as an
ordinary handler. This needs each instruction's own (instruction,
block) - its point of use - alongside its `.value`, not just the bare
value, which is why the run-matching helpers below take `(value,
instr, block)` triples rather than flat value lists.
"""

from __future__ import annotations

from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.transforms.shared import structural_key as structural_key
from hermes_decompiler.backend.transforms.shared import resolved_structural_equal

__all__ = ["structural_key", "strip_duplicate_run", "strip_duplicate_span", "find_run_match", "triples_for_block"]


def triples_for_block(block: BasicBlock) -> list:
    """Build the `(value, instr, block)` triples `find_run_match` /
    `strip_duplicate_run` need, for every value-bearing instruction of
    a single BasicBlock.
    """
    return [(i.value, i, block) for i in block.instructions if i.value is not None]


def find_run_match(candidates: list, candidate_block: BasicBlock, item_triples: list):
    """Does any contiguous run of `candidates` (instructions of
    `candidate_block`) register-aware-match `item_triples`? Returns
    the matching `(start, end)` exclusive index range within
    `candidates`, or None.
    """
    n = len(item_triples)

    if n == 0:
        return 0, 0

    for start in range(len(candidates) - n + 1):
        if all(
                resolved_structural_equal(
                    c.value, c, candidate_block,
                    v, i, item_block,
                )
                for c, (v, i, item_block) in zip(candidates[start:start + n], item_triples)
        ):
            return start, start + n

    return None


def strip_duplicate_run(region: SequenceRegion, item_triples: list) -> None:
    """Remove the first run in each block register-aware-matching
    `item_triples`, if any.

    Hermes may duplicate the same finally sequence independently
    across MULTIPLE blocks (e.g. both branches of a resume-check, each
    with their own inlined cleanup copy) - so this scans and strips
    per-block across the whole region, not just the first occurrence
    found anywhere.
    """

    if not item_triples:
        return

    n = len(item_triples)

    for block in list(region.covered_blocks):

        candidates = [i for i in block.instructions if i.value is not None]
        match = find_run_match(candidates, block, item_triples)

        if match is None:
            continue

        start, end = match

        for instr in candidates[start:end]:
            block.instructions.remove(instr)


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
        a_pairs = [(i.value, i) for i in a.instructions if i.value is not None]
        b_pairs = [(i.value, i) for i in b.instructions if i.value is not None]

        if len(a_pairs) != len(b_pairs):
            return False

        return all(
            resolved_structural_equal(x, xi, a, y, yi, b)
            for (x, xi), (y, yi) in zip(a_pairs, b_pairs)
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
        # `param1`'s original register directly). This module now has
        # the register-definition infrastructure
        # (`transforms.shared.resolve_identifier`/
        # `resolved_structural_equal`, the same `ForEachRegionPass`
        # uses) to resolve exactly that aliasing - and the BasicBlock
        # branch above, and `find_run_match` used elsewhere in this
        # module, both do. It's deliberately still not applied to a
        # condition specifically: `resolve_identifier` needs a single
        # concrete (instruction, block) point of use to walk backward
        # from, but a condition here is compared without reference to
        # either side's own containing handler block (this function
        # only ever receives the two IfRegions themselves) - reusing
        # it would need threading that context through every caller
        # for a comparison this function can already make reliably
        # without it: requiring exact condition equality would simply
        # never match a genuinely duplicated branching finally, which
        # is worse than the narrow false-positive risk accepted by
        # skipping it: a wrong match would require an unrelated
        # `if/else` elsewhere in the try/catch printing the exact same
        # literal content in the same order, which - given every
        # `__BC:...` marker string in this codebase's own fixtures is
        # unique per call site - is a non-issue in practice, and the
        # body comparison below still requires full structural
        # equality of both branches.
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
            target_triples = [(value, instr, target) for value, instr in _block_value_instr_pairs(target)]
            candidates = [instr for _, instr in _block_value_instr_pairs(candidate)]

            match_range = find_run_match(candidates, candidate, target_triples)

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
