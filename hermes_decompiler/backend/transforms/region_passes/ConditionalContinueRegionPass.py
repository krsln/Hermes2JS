from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.statements import ContinueStatement
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from hermes_decompiler.backend.transforms.shared._negation import negate_condition
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

        # A second latch: an empty block that only falls into the continue
        # target (`cloneObjectProperties`: `if (k !== K || o.k === undefined)
        # {...} else continue;` jumps to its own copy of the back edge).
        targets = {target.address} | {
            b.address
            for b in self.cfg.blocks
            if not b.instructions
               and b.terminator is None
               and list(b.successors) == [target]
        }

        for block in list(loop.body.covered_blocks):
            branch = block.terminator

            if (
                    not isinstance(branch, TerminatorConditionalBranch)
                    or branch.target not in targets
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
        self._rejoin_else_arm(owner, block)

        logger.debug("conditional continue: block %d", block.id)

    def _rejoin_else_arm(self, owner: SequenceRegion, block: BasicBlock) -> None:
        """`if (c) { T } else { F; if (d) continue; }` where F also falls into T.

        `IfStructurer` gave T and F to the two arms because F's own branch was
        still unresolved, losing F's fall-through edge into T. Once that branch
        is a `continue` the shape is `if (!c) { F; if (d) continue; } T`.
        """
        parent = getattr(owner, "parent", None)

        if (
                not isinstance(parent, IfRegion)
                or parent.else_body is not owner
                or not isinstance(parent.then_body, SequenceRegion)
                or not parent.then_body.children
        ):
            return

        entry = parent.then_body.children[0]

        if not isinstance(entry, BasicBlock) or entry not in block.successors:
            return

        inside = owner.covered_blocks
        then_blocks = parent.then_body.covered_blocks

        if any(
                pred not in inside and pred in then_blocks
                for pred in entry.predecessors
        ):
            return

        # the continue is the last thing the arm does, so the fall-through
        # edge is the only way out of it.
        last = owner.children[-1]

        if not isinstance(last, IfRegion) or last.else_body is not None:
            return

        sequence = getattr(parent, "parent", None)

        if not isinstance(sequence, SequenceRegion) or parent not in sequence.children:
            return

        then_body = parent.then_body
        parent.condition = negate_condition(parent.condition)
        parent.then_body = owner
        parent.else_body = None
        owner.parent = parent
        then_body.parent = sequence
        sequence.children.insert(sequence.children.index(parent) + 1, then_body)
        sequence.invalidate_coverage()
        logger.debug("conditional continue: rejoined fall-through into block %d", entry.id)
