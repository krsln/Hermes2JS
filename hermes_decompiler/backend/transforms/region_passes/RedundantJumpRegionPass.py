from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, LoopRegion, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.terminators import TerminatorJump
from .BaseRegionPass import RegionPass

logger = get_logger(__name__)


class RedundantJumpRegionPass(RegionPass, RegionVisitor):
    """Drops a bare unconditional-Jmp block whose target is simply the
    next sibling block that already executes right after it, AND a
    loop's own trailing back-edge jump to its header.

    Upstream structurers (LoopBreakStructurer,
    LoopLabeledExitStructurer, ...) sometimes leave one of these
    behind as a byproduct of matching a loop's natural-completion
    address through it. - See
    `LoopLabeledExitStructurer._chase_trampoline_address`, which walks
    straight through a block exactly like this one to find the real
    merge address an escaping edge needs to compare against, but never
    revisits the trampoline block itself once that comparison
    succeeds. The escape edge it was chased through gets consumed and
    converted; the trampoline, still sitting harmlessly in sequence
    with nothing left pointing at it except plain fallthrough, is
    not. Left-alone it prints as a pointless `goto label_N`
    immediately followed by the very code label_N points to.

    Deliberately narrow: only handles the case where the jump's target
    address is the address of the VERY NEXT sibling BasicBlock in the
    same SequenceRegion - i.e., removing the jump changes nothing
    about control flow, since falling off the end of the previous
    statement already reaches the same place. Any other shape (target
    is a LoopRegion's/IfRegion's/SwitchRegion's first block rather
    than a bare sibling BasicBlock, target is further away, etc.) is
    left as an explicit goto rather than guessed at - resolving \"the
    first address a compound sibling region would execute\" would
    require walking region-kind-specific internals (LoopRegion.body,
    IfRegion.then_body, SwitchRegion.cases, ...) this pass has no need
    to become coupled to for the one narrow shape actually observed in
    practice.

    A second, related shape this pass also drops: a LOOP's own trailing
    back-edge jump (from one of `loop.latches`) straight to
    `loop.header_block`. Unlike the sibling-trampoline case above, this
    one has NOTHING analogous for `while (...)`/`for (...)` to fall
    through into - the `for`/`while` construct itself already implies
    "go back to the top", so printing the underlying `goto label_N;`
    is pure noise for a shape every structured loop already expresses
    without it (see forOfTest/section_15092, whose loop body used to
    end with a redundant `goto label_35;` pointing right back at its
    own header). Only removed when the latch's OWN terminator is still
    a bare `Jmp` (top-tested `while`/`for-of`/`for-in` loops, where the
    condition lives at the header and the latch carries nothing but
    the back-edge) - a bottom-tested loop's latch instead carries the
    loop's real guard, already consumed into `loop.condition` by
    `LoopConditionRegionPass` (leaving `latch.terminator` as `None` by
    the time this pass runs), so this never fires for that shape.

    Pipeline placement
    -------------------
    Safe to run any time after all structurers have finished producing
    the final SequenceRegion shape - it only ever removes a block or a
    terminator, never rewrites a ``condition`` or ``register``, so it
    has no data dependency on LoopConditionRegionPass /
    LoopInductionAliasPass / ForEachRegionPass, though it DOES rely on
    LoopConditionRegionPass having already run (see the previous
    paragraph on why a bottom-tested loop's latch is naturally exempt
    only once its own terminator has already been consumed). Grouped
    alongside LoopContinueRegionPass in StructuralAnalyzer.build()
    since both clean up residual TerminatorJump-only blocks, though
    neither depends on the other's output - ordering between the two
    doesn't matter.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._strip_redundant_jumps(node)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self.visit(node.body)
        self._strip_back_edge_jumps(node)

    def _strip_redundant_jumps(self, region: SequenceRegion) -> None:
        children = region.children

        index = 0
        while index < len(children) - 1:
            block = children[index]
            next_sibling = children[index + 1]

            if (
                    isinstance(block, BasicBlock) and isinstance(next_sibling, BasicBlock)
                    and self._is_redundant_jump(block, next_sibling)
            ):
                del children[index]
                logger.debug(
                    "RedundantJumpRegionPass: dropped bare jump block %d "
                    "(0x%x) - target was already the next statement.",
                    block.id, block.address,
                )
                continue

            index += 1

    @staticmethod
    def _is_redundant_jump(block: BasicBlock, next_sibling: BasicBlock) -> bool:
        if not isinstance(block.terminator, TerminatorJump):
            return False

        if len(block.instructions) > 1:
            return False

        if block.instructions and block.instructions[0].terminator is not block.terminator:
            # The one instruction here does more than just carry the
            # jump (e.g., also computes a value) - not a pure
            # trampoline, leave it alone.
            return False

        return block.terminator.target == next_sibling.address

    def _strip_back_edge_jumps(self, loop: LoopRegion) -> None:
        header = loop.header_block

        if header is None:
            return

        for latch in loop.latches:
            terminator = latch.terminator

            if not isinstance(terminator, TerminatorJump):
                # Either not a plain back-edge jump, or (bottom-tested
                # loop) already consumed by LoopConditionRegionPass
                # into loop.condition - nothing to strip either way.
                continue

            if terminator.target != header.address:
                # An escape/break edge or something else this pass
                # doesn't recognize - leave it as an explicit goto.
                continue

            if not latch.instructions or latch.instructions[-1].terminator is not terminator:
                # Invariant violated: the terminator isn't owned by
                # the last instruction where expected. Bail rather
                # than remove the wrong thing.
                continue

            last = latch.instructions[-1]

            if last.value is not None or last.statement is not None:
                # This instruction does more than just carry the jump
                # (unusual for a bare Jmp, but don't guess) - only
                # clear the terminator, keep the instruction itself.
                last.terminator = None
            else:
                latch.instructions.pop()

            latch.terminator = None

            logger.debug(
                "RedundantJumpRegionPass: dropped loop %d's own "
                "back-edge jump in latch block %d (0x%x) - implied by "
                "the loop construct itself.",
                header.id, latch.id, latch.address,
            )
