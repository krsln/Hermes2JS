"""Stateless recognition logic for finally-wrapper handlers.

Answers: does a wider exception handler look like a `finally` wrapper
for an already-structured try/catch, or is it an ordinary, independent
handler? Never touches `RegionGraph`; it does read `cfg.post_dominator_tree`
to locate the shared continuation block Hermes sometimes inlines the
`finally` copy into (see `_finally_content_matches`). The actual tree
mutation that commits to treating a handler as `finally` lives in
`_finally_attacher`.
"""

from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.analysis.models import TerminatorThrow
from hermes_decompiler.analysis.models.regions import TryRegion
from hermes_decompiler.ir.expressions import Identifier
from ._predicates import structural_key


def find_finally_wrapper_target(handler: dict, processed: list, cfg: CFG):
    """Return the (handler, try_region) pair handler wraps, or None.

    `handler` wraps `inner` when its range swallows `inner`'s own
    catch-entry target (i.e. `handler` is reached whenever either the
    try or the catch of `inner` throws) AND `handler`'s own body content
    duplicates code that already appears inside `inner`'s try/catch
    bodies. Or in the block immediately following `inner`'s normal
    completion. This is a characteristic artifact of Hermes inlining
    `finally` code at each normal exit point.

    The content check matters because the two handlers' `start`
    addresses aren't always byte-identical (the wider one can start
    a few instructions earlier or later depending on what setup code
    precedes the try). Therefore, range containment alone is too strict,
    while relying on it exclusively is also too permissive and may
    incorrectly match genuinely unrelated nested handlers.
    """

    best = None

    for inner_handler, inner_region in processed:
        if inner_handler["target"] == handler["target"]:
            continue

        # This region already has its own ``finally`` clause, most likely from
        # a narrower wrapper match processed earlier.
        #
        # Content alone is not enough to reconsider the region. Two
        # unrelated ``finally`` blocks may coincidentally contain the same
        # string or expression (see section_15181, where the inner and
        # outer finally blocks use the same log message).
        #
        # Once a region is associated with a ``finally`` handler, it cannot be
        # claimed by another handler.
        if inner_region.finally_ is not None:
            continue

        if not (handler["start"] <= inner_handler["target"] < handler["end"]):
            continue

        if _finally_content_matches(handler, inner_region, inner_handler, cfg):
            # Multiple candidates may satisfy the content-matching criteria.
            # Hermes tail duplication can cause a shared merge block to
            # produce a false-positive match for otherwise unrelated nested
            # handlers (see the section_15082 regression).
            #
            # The correct match is not necessarily the outermost candidate,
            # but the closest enclosing handler (i.e., the candidate with the
            # greatest target address). Handlers are opened in source order
            # using LIFO semantics, so the most recently opened handler is
            # the one directly wrapped by the wider handler.
            if best is None or inner_handler["target"] > best[0]["target"]:
                best = (inner_handler, inner_region)

    return best


def _finally_content_matches(handler: dict, inner_region: TryRegion, inner_handler: dict, cfg: CFG) -> bool:
    values = _candidate_finally_values(handler["handler_block"])

    if not values:
        return False

    keys = [structural_key(v) for v in values]
    n = len(keys)

    regions = [inner_region.try_body]

    inner_region_catch = inner_region.catch
    if inner_region_catch is not None:
        regions.append(inner_region_catch.body)

    # Hermes may place the duplicated finally sequence not inside the
    # try/catch bodies, but in the shared continuation block immediately
    # following their normal completion (the immediate post-dominator of
    # the inner handler). This block may not yet have been incorporated
    # into the region tree, so inspect the raw CFG separately.
    if cfg is not None and cfg.post_dominator_tree is not None:
        merge_block = cfg.post_dominator_tree.immediate_post_dominator(
            inner_handler["handler_block"]
        )
        if merge_block is not None:
            candidates = [i for i in merge_block.instructions if i.value is not None]
            candidate_keys = [structural_key(c.value) for c in candidates]
            for start in range(len(candidate_keys) - n + 1):
                if candidate_keys[start:start + n] == keys:
                    return True

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
