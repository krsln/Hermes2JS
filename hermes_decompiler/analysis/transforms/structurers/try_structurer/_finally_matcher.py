"""Stateless recognition logic for finally-wrapper handlers.

Answers: does a wider exception handler look like a `finally` wrapper
for an already-structured try/catch, or is it an ordinary, independent
handler? Never touches `RegionGraph` or `cfg` - every function here
only inspects data already on the CFG/region tree and returns a plain
bool/tuple. The actual tree mutation that commits to treating a
handler as `finally` lives in `_finally_attacher`.
"""

from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import TerminatorThrow
from hermes_decompiler.analysis.models.regions import TryRegion
from hermes_decompiler.ir.expressions import Identifier
from ._predicates import structural_key


def find_finally_wrapper_target(handler: dict, processed: list):
    """Return the (handler, try_region) pair handler wraps, or None.

    `handler` wraps `inner` when its range swallows `inner`'s own
    catch-entry target (i.e. `handler` is reached whenever either the
    try or the catch of `inner` throws) AND `handler`'s own body
    content duplicates code that already appears inside `inner`'s
    try/catch bodies. - The tell left behind by Hermes inlining the
    `finally` code at every normal exit point.

    The content check matters because the two handlers' `start`
    addresses aren't always byte-identical (the wider one can start a
    few instructions earlier or later depending on what setup code
    precedes the try). So range containment alone is too strict, and
    on its own too easy to satisfy by coincidence for genuinely
    unrelated nested handlers.
    """

    for inner_handler, inner_region in processed:

        if inner_handler["target"] == handler["target"]:
            continue

        if not (handler["start"] <= inner_handler["target"] < handler["end"]):
            continue

        if _finally_content_matches(handler, inner_region):
            return inner_handler, inner_region

    return None


def _finally_content_matches(handler: dict, inner_region: TryRegion) -> bool:
    values = _candidate_finally_values(handler["handler_block"])

    if not values:
        return False

    keys = [structural_key(v) for v in values]
    n = len(keys)

    regions = [inner_region.try_body]

    catch_region = inner_region.catch

    if catch_region is not None:
        regions.append(catch_region.body)

    for region in regions:

        for block in region.covered_blocks:

            candidates = [i for i in block.instructions if i.value is not None]
            candidate_keys = [structural_key(c.value) for c in candidates]

            for start in range(len(candidate_keys) - n + 1):
                if candidate_keys[start:start + n] == keys:
                    return True

    return False


def _candidate_finally_values(handler_block: BasicBlock) -> list:
    """Return the value-bearing instructions that would form a `finally` body.

    Excludes the leading Catch exception-binding and a trailing bare
    rethrow (if present), since neither has any JS-visible surface
    inside a real `finally` clause. The trailing rethrow is only
    excluded when the last instruction is confirmed to be the actual
    carrier of the block's terminator. - The same invariant enforced
    everywhere else in this codebase before treating a terminator as
    tied to a specific instruction. - So a genuine value-producing
    instruction is never mistaken for the rethrow's placeholder.

    Read-only - callers that intend to commit to treating the block as
    a `finally` must still perform the actual mutation themselves (see
    `_finally_attacher.attach`).
    """

    instructions = list(handler_block.instructions)

    if (
            instructions
            and instructions[0].dest_reg is not None
            and isinstance(instructions[0].value, Identifier)
    ):
        instructions = instructions[1:]

    if (
            instructions
            and instructions[-1].terminator is handler_block.terminator
            and isinstance(handler_block.terminator, TerminatorThrow)
            and isinstance(handler_block.terminator.value, Identifier)
    ):
        instructions = instructions[:-1]

    return [i.value for i in instructions if i.value is not None]
