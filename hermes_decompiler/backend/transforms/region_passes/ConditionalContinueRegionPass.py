from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import ContinueStatement
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from ._base import RegionPass

logger = get_logger(__name__)


class ConditionalContinueRegionPass(RegionPass, RegionVisitor):
    """`if (c) continue;` compiled as a conditional branch back to the loop.

        header:  ...
                 JEqual   body_end_test -> header      # taken: next iteration
                 <rest of the body>
                 Jmp -> header

    `IfStructurer` leaves every backward branch alone (it may be the loop's own
    guard) and `LoopContinueRegionPass` only knows unconditional jumps, so such
    a branch survived as a raw `if (c) goto label`. The loop's own guard is
    consumed by `LoopConditionRegionPass`, so a conditional branch still left in
    the body whose target is the loop's continue target is a `continue` taken
    when the condition holds, with the rest of the body as its fall-through.

    Only the loop's own blocks (not a nested loop's: that would need a label).
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._convert_loop(node)
        self.visit(node.body)

    def _convert_loop(self, loop: LoopRegion) -> None:
        target = loop.continue_target

        if target is None:
            return

        for block in list(loop.body.covered_blocks):
            branch = block.terminator

            if (
                    not isinstance(branch, TerminatorConditionalBranch)
                    or branch.target != target.address
                    or block is loop.condition_block
                    or block is loop.update_block
                    or block is loop.header_block and loop.condition is not None
                    or not self._owned_directly_by(loop, block)
            ):
                continue

            self._convert(block, branch)

    def _owned_directly_by(self, loop: LoopRegion, block: BasicBlock) -> bool:
        region = self.graph.owner(block)

        while region is not None and region is not loop:
            if isinstance(region, LoopRegion):
                return False

            region = getattr(region, "parent", None)

        return region is loop

    def _convert(self, block: BasicBlock, branch: TerminatorConditionalBranch) -> None:
        from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult

        if not block.instructions or block.instructions[-1].terminator is not branch:
            return

        owner = self.graph.owner(block)

        block.instructions.pop()
        block.terminator = None

        new_id = max((b.id for b in self.cfg.blocks), default=0) + 1
        marker = BasicBlock(new_id, address=-1)
        entry = OpcodeEntry(bytecode="<synthetic>: ContinueStatement", hex_address="")
        marker.instructions.append(OpcodeResult(entry, statement=ContinueStatement(label=None)))
        self.cfg.blocks.append(marker)

        then_body = SequenceRegion()
        self.graph.transfer([marker], then_body)

        if_region = IfRegion()
        if_region.condition = branch.condition
        if_region.then_body = then_body
        if_region.else_body = None

        self.graph.insert_at(owner, owner.children.index(block) + 1, if_region)

        logger.debug("conditional continue: block %d", block.id)
