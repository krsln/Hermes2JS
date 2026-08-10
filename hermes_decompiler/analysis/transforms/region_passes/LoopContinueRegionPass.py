from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.RegionVisitor import RegionVisitor
from hermes_decompiler.analysis.regions.Regions import LoopRegion
from hermes_decompiler.analysis.terminators import TerminatorJump
from hermes_decompiler.ir.statements import ContinueStatement

from ._base import RegionPass


class LoopContinueRegionPass(RegionPass, RegionVisitor):
    """
    Recognizes a residual, already-unconditional jump inside a loop's
    body whose target is the loop's own latch block - exactly what a
    `continue` compiles to - and rewrites that terminator instruction
    into an explicit `ContinueStatement` in place.

    Unlike `LoopBreakStructurer`, no block relocation or new region is
    built: the jump already sits at the tail of whatever block emits
    it, in whatever if/else nesting `IfStructurer` already gave it,
    and a `continue;` there is a plain leaf statement - not a
    control-flow region. That's why this is a `RegionPass`, not a
    `RegionStructurer` (see that distinction in each base class's own
    docstring).

    Why this residual survives every structurer untouched:
    `IfStructurer`'s own trailing-jump stripping only removes a jump
    whose target is exactly the natural merge point of the SPECIFIC
    if/else level being converted at that step. A jump sitting several
    nesting levels deep - e.g. inside a second, inner `if` - has its
    own, different immediate post-dominator at that inner step, which
    doesn't have to equal the loop's latch address even though the
    jump's actual target does. The jump is consequently never anyone's
    responsibility to strip until now: nothing else revisits an
    already-built region tree looking specifically for "a jump to this
    loop's own latch, wherever it ended up nested."

    Must run in `region_passes` (stage 3), after every structurer:
    - after `LoopStructurer` (needs `loop.latches` to know each
      candidate jump's real target address)
    - after `IfStructurer` in particular - not because converting the
      terminator earlier would corrupt anything (dominance and
      post-dominance are computed once on the raw CFG and don't depend
      on this pass having run), but because there is no reason for a
      pass that never restructures the tree to run any earlier than
      the stage its own base class belongs to.

    Order relative to `LoopBreakStructurer`, `LoopConditionRegionPass`,
    and every other region pass does not matter: each recognizes a
    disjoint terminator shape on a disjoint block (this one only
    touches an already-unconditional `TerminatorJump`, never the
    loop's own header/latch guard, which is always a
    `TerminatorConditionalBranch`), so none of their outputs can ever
    become a valid input for another.

    Deliberately narrow, same philosophy as `LoopBreakStructurer`:
    only the single-instruction unconditional-jump shape is
    recognized. A residual CONDITIONAL branch whose guard should
    become `if (cond) continue;` is not handled here - no fixture seen
    so far leaves that shape unresolved by the time this pass runs; if
    one is found, this class should gain a sibling case rather than
    being stretched to guess at it.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._try_recognize_continues(node)
        self.visit(node.body)

    # -------------------------------------------------------------

    def _try_recognize_continues(self, loop: LoopRegion) -> None:

        latch_addresses = {latch.address for latch in loop.latches}

        if not latch_addresses:
            return

        for block in loop.body.covered_blocks:

            if block is loop.header_block:
                # The header's own back-edge test is consumed
                # separately, by LoopConditionRegionPass, and is
                # always a conditional branch, never the plain
                # unconditional jump this pass looks for - excluded
                # defensively for the same reason LoopBreakStructurer
                # excludes it from its own candidate search.
                continue

            terminator = block.terminator

            if not isinstance(terminator, TerminatorJump):
                continue

            if terminator.target not in latch_addresses:
                continue

            self._convert(block, terminator)

    @staticmethod
    def _convert(block: BasicBlock, terminator: TerminatorJump) -> None:

        if not block.instructions:
            return

        last = block.instructions[-1]

        if last.terminator is not terminator:
            # Shouldn't happen (the terminator is always its own
            # instruction's), but don't guess if the invariant this
            # relies on doesn't hold.
            return

        last.terminator = None
        last.value = None
        last.statement = ContinueStatement(label=None)

        block.terminator = None
