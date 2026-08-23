from hermes_decompiler.analysis.models.regions import LoopRegion

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import TerminatorConditionalBranch


def has_bottom_tested_guard(loop_region: LoopRegion) -> bool:
    """Return True if the loop's latch itself carries a conditional
    guard - the CFG-level signature of a bottom-tested `do-while`/`for`
    loop (the real condition lives at the LATCH, not the header).

    Only meaningful for the single-latch case: with multiple latches
    there's no single "the" latch guard to defer to, and
    LoopConditionRegionPass's own bottom-tested classification already
    requires exactly one latch (see that pass's step 3) - so this
    predicate agrees by construction rather than needing its own
    separate multi-latch policy.

    Shared by `is_loop_guard_shaped` (so a header whose OWN branch
    happens to look guard-shaped, per that function's own edge-exits
    check, doesn't win by default when the loop's real guard is
    actually sitting at the latch instead - see that function's
    docstring) and by `LoopBreakStructurer._find_candidate` (so it
    knows the header must NOT be excluded from ordinary break-testing
    when the loop is really bottom-tested - the header's own branch is
    then just an in-body if, not loop machinery).
    """
    if len(loop_region.latches) != 1:
        return False

    latch = next(iter(loop_region.latches))

    return isinstance(latch.terminator, TerminatorConditionalBranch)


def is_loop_guard_shaped(header: BasicBlock, loop_region: LoopRegion) -> bool:
    """Return True if `header`'s own branch can be the loop's guard.

    True for a top-tested `while`, where at least one of `header`'s
    edges leaves the loop (`loop_region.exits`). False for a
    bottom-tested `do-while`/`for` (or any loop whose real guard lives
    at the latch): the header can hold an ordinary in-body `if`
    with both edges staying inside the loop, and structuring it
    unconditionally would force it through
    `_absorb_residual_conditional`'s crude fallback - risking
    silently dropped code (e.g., the increment) on one arm.

    Also, False whenever the loop's single latch itself carries a
    conditional guard (`has_bottom_tested_guard`), even if `header`'s
    own branch structurally satisfies the edge-exits check below.
    Hermes can legitimately place an ordinary early-exit `if` at the
    very start of a loop body - its target happens to leave the loop
    (e.g., a `break`-shaped test), which is indistinguishable from a
    genuine top-tested guard by the edge-exits check alone. The
    tie-breaker is the latch: a REAL top-tested `while`'s latch is an
    unconditional back-edge only, while a loop whose true condition
    lives at the latch (bottom-tested) has that latch carrying its own
    conditional branch. When both signals are present, the latch wins
    the header's branch is left as ordinary in-body control flow for
    LoopBreakStructurer / IfStructurer to handle normally, and
    LoopConditionRegionPass classifies the loop from the latch
    instead.

    Must agree with `LoopConditionRegionPass`, which performs the
    equivalent `header-vs-latch` check when building the
    while/do-while/for shape.
    """

    if not isinstance(header.terminator, TerminatorConditionalBranch):
        return False

    if has_bottom_tested_guard(loop_region):
        return False

    exits = set(loop_region.exits)

    return any(successor in exits for successor in header.successors)
