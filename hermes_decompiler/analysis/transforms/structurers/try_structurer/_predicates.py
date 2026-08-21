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

from hermes_decompiler.analysis.models.regions import SequenceRegion
# noinspection PyProtectedMember
from hermes_decompiler.analysis.transforms._shared import _structural_key as structural_key  # noqa: SLF001

__all__ = ["structural_key", "strip_duplicate_run"]


def strip_duplicate_run(region: SequenceRegion, finally_values: list) -> None:
    """Remove the first run in `region` matching finally_values, if any.

    Matches the first contiguous run of instructions whose `.value`s
    exactly equal finally_values. The duplicate isn't necessarily at
    the end of a block - e.g., a catch body normally continues with
    more statements (and a return) after its inlined finally-copy -
    so this scans for the run anywhere, not just as a trailing slice.
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
