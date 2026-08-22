from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor, TerminatorJump
from hermes_decompiler.analysis.models.regions import SequenceRegion
from hermes_decompiler.core.logging import get_logger

from ._base import RegionPass

logger = get_logger(__name__)


class RedundantJumpRegionPass(RegionPass, RegionVisitor):
    """Drops a bare unconditional-Jmp block whose target is simply the
    next sibling block that already executes right after it.

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
    left as an explicit goto rather than guessed at - resolving "the
    first address a compound sibling region would execute" would
    require walking region-kind-specific internals (LoopRegion.body,
    IfRegion.then_body, SwitchRegion.cases, ...) this pass has no need
    to become coupled to for the one narrow shape actually observed in
    practice.

    Pipeline placement
    -------------------
    Safe to run any time after all structurers have finished producing
    the final SequenceRegion shape - it only ever removes a block,
    never rewrites a ``condition`` or ``register``, so it has no data
    dependency on LoopConditionRegionPass / LoopInductionAliasPass /
    ForEachRegionPass. Grouped alongside LoopContinueRegionPass in
    StructuralAnalyzer.build() since both clean up residual
    TerminatorJump-only blocks, though neither depends on the other's
    output - ordering between the two doesn't matter.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)
        self._strip_redundant_jumps(node)

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
