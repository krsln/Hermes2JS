from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import TryRegion
from hermes_decompiler.analysis.terminators import TerminatorThrow
from hermes_decompiler.ir.expressions import Identifier

from ._predicates import structural_key

"""
Stateless recognition logic: does a wider exception handler look like
a `finally` wrapper for an already-structured try/catch, or is it an
ordinary, independent handler? Never touches `RegionGraph` or `cfg` -
every function here only inspects data already on the CFG/region tree
and returns a plain bool/tuple. The actual tree mutation that commits
to treating a handler as `finally` lives in `_finally_attacher`.
"""


def find_finally_wrapper_target(handler: dict, processed: list):
    """
    Returns the (handler, try_region) pair that `handler` is a
    finally-wrapper for, or None if `handler` looks like an ordinary
    (non-finally) handler.

    `handler` wraps `inner` when its range swallows `inner`'s own
    catch-entry target (i.e. `handler` is reached whenever either the
    try *or* the catch of `inner` throws) AND `handler`'s own body
    content is a duplicate of code that already appears inside
    `inner`'s try/catch bodies - the tell-tale sign Hermes left behind
    from inlining the finally code at every normal exit point. The
    content check matters because the two handlers' `start` addresses
    aren't always byte-identical (the wider one can start a few
    instructions earlier or later depending on what setup code
    precedes the try), so range containment alone is too strict AND,
    on its own, too easy to satisfy by coincidence for genuinely
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
    """
    The value-bearing instructions of `handler_block` that would
    actually constitute a `finally` body: the leading `Catch`
    exception-binding and a trailing bare rethrow (if present)
    excluded, since neither has any JS-visible surface inside a real
    `finally` clause. Read-only - callers that intend to commit to
    treating the block as a finally must still perform the actual
    mutation themselves (see `_finally_attacher.attach`).
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
            and isinstance(handler_block.terminator, TerminatorThrow)
            and isinstance(handler_block.terminator.value, Identifier)
    ):
        instructions = instructions[:-1]

    return [i.value for i in instructions if i.value is not None]