from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor
from hermes_decompiler.analysis.models.regions import LoopKind, LoopRegion
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.expressions import Expression, UnaryExpression

from ._base import RegionPass

logger = get_logger(__name__)


class LoopConditionRegionPass(RegionPass, RegionVisitor):
    """
    Extracts the loop condition and classifies the physical loop shape.

    Supported shapes:

        while:

            header
              |
              +-- condition false --> exit
              |
              v
             body
              |
              +--------------------> header


        do-while:

            header
              |
             body
              |
            condition
              |
              +-- true ------------> header
              |
              +-- false -----------> exit


        for:

            header
              |
             body
              |
             update
              |
            condition
              |
              +-- true ------------> header
              |
              +-- false -----------> exit

    The important distinction between `do-while` and `for` is that a
    source-level `for` has a distinct update phase immediately before
    the loop guard.

    The pass is deliberately conservative. If the CFG does not provide
    enough evidence to distinguish the shapes, it does not invent a
    `for` loop.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._extract(node)
        self.visit(node.body)

    # ------------------------------------------------------------------
    # Main extraction
    # ------------------------------------------------------------------

    def _extract(self, loop: LoopRegion) -> None:
        header = loop.header_block

        if header is None:
            return

        # Defensive reset. This matters if the pass is ever run twice
        # against the same region tree.
        loop.condition = None
        loop.condition_block = None
        loop.update_block = None
        loop.continue_target = None
        loop.break_target = None
        loop.loop_kind = LoopKind.WHILE

        # ------------------------------------------------------------------
        # 1. Self-loop
        # ------------------------------------------------------------------

        if header in loop.latches:
            if self._consume_guard(
                    header,
                    loop,
                    LoopKind.DO_WHILE,
                    update_block=None,
            ):
                loop.continue_target = header
                return

            logger.warning(
                "Loop header block %d (0x%x): self-loop with no valid "
                "guard; leaving loop unclassified.",
                header.id,
                header.address,
            )
            return

        # ------------------------------------------------------------------
        # 2. Top-tested loop: while (...)
        # ------------------------------------------------------------------

        if self._consume_guard(
                header,
                loop,
                LoopKind.WHILE,
                update_block=None,
        ):
            loop.continue_target = header
            return

        # ------------------------------------------------------------------
        # 3. Bottom-tested loop
        # ------------------------------------------------------------------

        if len(loop.latches) != 1:
            logger.warning(
                "Loop header block %d (0x%x): expected exactly one latch "
                "for bottom-tested loop classification, got %d.",
                header.id,
                header.address,
                len(loop.latches),
            )
            return

        latch = next(iter(loop.latches))

        if latch is header:
            return

        # The latch must carry the actual loop guard.
        if not isinstance(latch.terminator, TerminatorConditionalBranch):
            logger.debug(
                "Loop header block %d (0x%x): latch block %d (0x%x) "
                "does not contain a conditional guard.",
                header.id,
                header.address,
                latch.id,
                latch.address,
            )
            return

        # A bottom-tested loop can be either:
        #
        #     do { body } while (cond)
        #
        # or:
        #
        #     for (...; cond; update) { body }
        #
        # First determine whether this is the canonical `for` shape.
        update_block = self._find_for_update_block(loop, latch)

        if update_block is not None:
            if self._consume_guard(
                    latch,
                    loop,
                    LoopKind.FOR,
                    update_block=update_block,
            ):
                loop.update_block = update_block
                loop.continue_target = update_block
                return

        # Otherwise it is a normal bottom-tested loop.
        if self._consume_guard(
                latch,
                loop,
                LoopKind.DO_WHILE,
                update_block=None,
        ):
            loop.continue_target = latch
            return

        logger.warning(
            "Loop header block %d (0x%x): no valid loop guard found.",
            header.id,
            header.address,
        )

    # ------------------------------------------------------------------
    # Guard extraction
    # ------------------------------------------------------------------

    def _consume_guard(
            self,
            block: BasicBlock,
            loop: LoopRegion,
            kind: LoopKind,
            update_block: BasicBlock | None,
    ) -> bool:
        """
        Consume a conditional branch that has exactly one edge leaving
        the current loop.

        The branch is removed from the BasicBlock because its condition
        becomes `loop.condition`.

        `update_block` is metadata only; it is not used to determine
        the condition itself.
        """

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return False

        exits = set(loop.exits)

        target_block = next(
            (
                successor
                for successor in block.successors
                if successor.address == branch.target
            ),
            None,
        )

        fallthrough_candidates = [
            successor
            for successor in block.successors
            if successor is not target_block
        ]

        if len(fallthrough_candidates) != 1:
            return False

        fallthrough_block = fallthrough_candidates[0]

        target_is_exit = (
                target_block is not None
                and target_block in exits
        )

        fallthrough_is_exit = fallthrough_block in exits

        if target_is_exit and not fallthrough_is_exit:
            # if (condition) goto exit
            #
            # Continue looping while !condition.
            condition: Expression = UnaryExpression(
                UnaryOperator.LOGICAL_NOT,
                branch.condition,
            )

        elif fallthrough_is_exit and not target_is_exit:
            # if (condition) goto body
            #
            # Continue looping while condition.
            condition = branch.condition

        else:
            # Both edges leave, or both edges stay inside.
            # This is not a loop guard.
            return False

        # ------------------------------------------------------------------
        # Consume the terminator.
        # ------------------------------------------------------------------

        block.terminator = None

        if (
                block.instructions
                and block.instructions[-1].terminator is branch
        ):
            block.instructions.pop()

        loop.condition = condition
        loop.condition_block = block
        loop.loop_kind = kind

        if update_block is not None:
            loop.update_block = update_block

        return True

    # ------------------------------------------------------------------
    # FOR detection
    # ------------------------------------------------------------------

    @staticmethod
    def _find_for_update_block(
            loop: LoopRegion,
            condition_block: BasicBlock,
    ) -> BasicBlock | None:
        """
        For Hermes' canonical numeric-for lowering, the update operation
        and the loop guard can live in the same BasicBlock:

            Inc ...
            JLess ... -> header

        In that shape the condition block itself is the update block.

        For a separated update block, use the unique in-loop predecessor.
        """

        covered = loop.body.covered_blocks

        # Canonical Hermes:
        #
        #     update instruction
        #     conditional guard
        #
        # in the same block.
        if condition_block.instructions:
            non_terminator_instructions = [
                instruction
                for instruction in condition_block.instructions
                if instruction.terminator is None
            ]

            if non_terminator_instructions:
                return condition_block

        # Generic separated-update form:
        candidates = [
            predecessor
            for predecessor in condition_block.predecessors
            if predecessor in covered
               and predecessor is not condition_block
        ]

        if len(candidates) != 1:
            return None

        candidate = candidates[0]

        if candidate is loop.header_block:
            return None

        if condition_block not in candidate.successors:
            return None

        return candidate
