from __future__ import annotations

import copy

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import BreakStatement
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump
from ._base import RegionPass

logger = get_logger(__name__)


class LoopExitBreakRegionPass(RegionPass, RegionVisitor):
    """`break` for the way out of a `while (true) { try { ... } catch { ... } }` body.

    The loop is entered again only from the `catch`, so everything that leaves the protected body (a jump to the
    code behind the loop, or the body's last block falling into it) leaves the loop. `LoopBreakStructurer` only
    knows an exit that is the branch of a test, and skips one whose target has other predecessors, which is every
    exit of such a body (96/2139 `renderRootSync`: three arms reach the `workLoopSync()` block).

    Only loops `LoopAnalysis.include_protected_blocks` grew, only blocks that belong to the loop itself (not to a
    nested loop or switch: that `break` would need a label), and only exits to the code that follows the loop in
    its own sequence. A jump into a small block that runs plain statements and then leaves the loop gets a copy
    of those statements and the `break` (a conditional one becomes `if (c) { ...; break; }`).
    """

    _MAX_COPIED = 6

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._convert_loop(node)
        self.visit(node.body)

    def _convert_loop(self, loop: LoopRegion) -> None:
        around_a_try = getattr(getattr(self.cfg, "loop_analysis", None), "loops_around_a_try", ())

        if loop.header_block is None or loop.header_block.address not in around_a_try:
            return

        follow = self._block_after(loop)

        if follow is None:
            return

        for block in list(loop.body.covered_blocks):
            if not self._owned_directly_by(loop, block):
                continue

            terminator = block.terminator
            exit_block = self._exit_block(loop, follow, terminator)

            if exit_block is not None and exit_block is not block:
                self._jump_into_an_exit_block(block, terminator, exit_block)
                continue

            if isinstance(terminator, TerminatorJump):
                if terminator.target != follow.address:
                    continue

                if not block.instructions or block.instructions[-1].terminator is not terminator:
                    continue

                block.instructions.pop()
                block.terminator = None
            elif terminator is None and list(block.successors) == [follow]:
                pass
            else:
                continue

            self._append_break(block)
            logger.debug("loop exit break: block %d", block.id)

    def _exit_block(self, loop: LoopRegion, follow: BasicBlock, terminator):
        """The small block `terminator` jumps to when that block only runs plain statements and then leaves the loop."""
        if not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
            return None

        target = next((b for b in self.cfg.blocks if b.address == terminator.target), None)

        if (
                target is None
                or target not in loop.body.covered_blocks
                or list(target.successors) != [follow]
                or len(target.instructions) > self._MAX_COPIED
        ):
            return None

        for instruction in target.instructions:
            if instruction.terminator is not None and not isinstance(instruction.terminator, TerminatorJump):
                return None

        return target

    def _jump_into_an_exit_block(self, block: BasicBlock, terminator, exit_block: BasicBlock) -> None:
        """`goto exit` -> a copy of the exit block's statements and a `break` (a plain jump, or the taken side of a test)."""
        from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult

        if not block.instructions or block.instructions[-1].terminator is not terminator:
            return

        copies = [copy.deepcopy(i) for i in exit_block.instructions if i.terminator is None]

        if isinstance(terminator, TerminatorJump):
            block.instructions.pop()
            block.terminator = None
            block.instructions.extend(copies)
            self._append_break(block)

            return

        owner = self.graph.owner(block)

        if owner is None or block not in getattr(owner, "children", ()):
            return

        block.instructions.pop()
        block.terminator = None

        new_id = max((b.id for b in self.cfg.blocks), default=0) + 1
        marker = BasicBlock(new_id, address=-1)
        marker.instructions.extend(copies)
        entry = OpcodeEntry(bytecode="<synthetic>: BreakStatement", hex_address="")
        marker.instructions.append(OpcodeResult(entry, statement=BreakStatement(label=None)))
        self.cfg.blocks.append(marker)

        then_body = SequenceRegion()
        self.graph.transfer([marker], then_body)

        if_region = IfRegion()
        if_region.condition = terminator.condition
        if_region.then_body = then_body
        if_region.else_body = None

        self.graph.insert_at(owner, owner.children.index(block) + 1, if_region)

    def _block_after(self, loop: LoopRegion) -> BasicBlock | None:
        parent = getattr(loop, "parent", None)
        children = getattr(parent, "children", None)

        if not children or loop not in children:
            return None

        index = children.index(loop) + 1

        if index >= len(children):
            return None

        node = children[index]

        while not isinstance(node, BasicBlock):
            inner = getattr(node, "children", None)

            if not inner:
                return None

            node = inner[0]

        return node

    def _owned_directly_by(self, loop: LoopRegion, block: BasicBlock) -> bool:
        region = self.graph.owner(block)

        while region is not None and region is not loop:
            if region.__class__.__name__ in ("LoopRegion", "SwitchRegion"):
                return False

            region = getattr(region, "parent", None)

        return region is loop

    @staticmethod
    def _append_break(block: BasicBlock) -> None:
        from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult

        entry = OpcodeEntry(bytecode="<synthetic>: BreakStatement", hex_address="")
        block.instructions.append(OpcodeResult(entry, statement=BreakStatement(label=None)))
