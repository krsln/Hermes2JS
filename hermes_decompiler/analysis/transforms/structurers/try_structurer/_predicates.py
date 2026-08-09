from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.regions.Regions import SequenceRegion

"""
Pure, stateless helpers shared by `_finally_matcher` and
`_FinallyAttacher`. Both need to answer "does this run of instruction
values match that run of instruction values" - the matcher to decide
whether a wider handler's body is a duplicate of code already inside
a narrower handler's try/catch (i.e. it's really a `finally`), the
attacher to then strip those duplicated copies out once a real
`finally` clause is being emitted instead.
"""


def structural_key(value):
    """
    Value-based key for an expression node, independent of whether its
    class defines `__eq__` (many of the IR expression classes don't,
    so plain `==` silently falls back to object identity and never
    matches two separately-built-but-equivalent trees). Deeply unpacks
    dataclasses into tuples so structurally identical trees -
    regardless of which registers produced them - compare equal.
    Falls back to `repr()` for anything that isn't a dataclass.
    """

    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return tuple(
            structural_key(getattr(value, f.name))
            for f in dataclasses.fields(value)
        )

    if isinstance(value, (list, tuple)):
        return tuple(structural_key(v) for v in value)

    try:
        hash(value)
        return value
    except TypeError:
        return repr(value)


def strip_duplicate_run(region: SequenceRegion, finally_values: list) -> None:
    """
    Removes the first contiguous run of instructions in `region` whose
    `.value`s exactly match `finally_values`, if any. The duplicate
    isn't necessarily at the very end of a block - e.g. a catch body
    normally continues with more statements (and a `return`) after its
    inlined finally-copy - so this scans for the run anywhere, not
    just as a trailing slice.
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