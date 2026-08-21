from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor
from hermes_decompiler.analysis.models.regions import LoopRegion
from hermes_decompiler.analysis.terminators import TerminatorJump
from hermes_decompiler.ir.statements import ContinueStatement

from ._base import RegionPass


class LoopContinueRegionPass(RegionPass, RegionVisitor):
    """Converts residual unconditional jumps into `continue`.

    A jump is considered a genuine unlabelled `continue` only when:

        1. It is inside the current loop.
        2. It is an unconditional TerminatorJump.
        3. Its target is the semantic `continue` target selected by
           LoopConditionRegionPass.
        4. It is not the loop's ordinary sequential completion edge.

    This distinction is important for `for` loops.

    Example:

        if (i === 3) {
            continue;
        }

        console.log(i);

    Hermes may compile both paths to the same update block:

        conditional continue path ──┐
                                    │
        normal body completion ────┤──> update
                                    │
                                    v
                                  update
                                    |
                                  guard

    Therefore, `target == update` alone is NOT enough to identify a
    `continue`.

    The pass intentionally remains conservative. A jump whose structural
    role cannot be established is left untouched rather than being
    incorrectly rendered as `continue`.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._try_recognize_continues(node)
        self.visit(node.body)

    # ------------------------------------------------------------------
    # Main recognition
    # ------------------------------------------------------------------

    def _try_recognize_continues(self, loop: LoopRegion) -> None:
        target = loop.continue_target

        if target is None:
            return

        covered = loop.body.covered_blocks

        for block in list(covered):
            if block is loop.header_block:
                continue

            terminator = block.terminator

            if not isinstance(terminator, TerminatorJump):
                continue

            if terminator.target != target.address:
                continue

            if not self._is_continue_edge(loop, block, target):
                continue

            self._convert(block, terminator)

    # ------------------------------------------------------------------
    # Structural validation
    # ------------------------------------------------------------------

    def _is_continue_edge(
            self,
            loop: LoopRegion,
            block: BasicBlock,
            target: BasicBlock,
    ) -> bool:
        """Determine whether `block` -> `target` is a semantic `continue` edge.

        Deliberately distinguishes::

            branch-arm -> update           = continue
            final-body-block -> update     = ordinary loop completion

        The distinction is made from the region tree rather than from
        the target address alone.
        """

        # --------------------------------------------------------------
        # A direct jump from the loop's condition/update block is never
        # a source-level continue.
        # --------------------------------------------------------------

        if block is loop.condition_block:
            return False

        if block is loop.update_block:
            return False

        # --------------------------------------------------------------
        # If the block is owned directly by an IfRegion, a jump from that
        # branch to the loop's continue target is the canonical residual
        # continue shape.
        # --------------------------------------------------------------

        if self._is_inside_if_branch(block, loop):
            return True

        # --------------------------------------------------------------
        # A block may be the final block of a nested SequenceRegion.
        # Walk upward and determine whether it is part of a conditional
        # branch that bypasses the remainder of the current loop body.
        # --------------------------------------------------------------

        if self._has_conditional_ancestor(block, loop):
            return True

        # --------------------------------------------------------------
        # Do NOT turn the ordinary final-body jump into `continue`.
        # --------------------------------------------------------------

        return False

    # ------------------------------------------------------------------
    # Region ownership helpers
    # ------------------------------------------------------------------

    def _is_inside_if_branch(
            self,
            block: BasicBlock,
            loop: LoopRegion,
    ) -> bool:
        """Return True if `block` belongs to an IfRegion contained by this loop.

        Intentionally stops at the current LoopRegion so an enclosing
        loop's IfRegion cannot accidentally cause a local `continue`.
        """

        region = self.graph.owner(block)

        while region is not None and region is not loop:
            if region.__class__.__name__ == "IfRegion":
                return True

            region = getattr(region, "parent", None)

        return False

    def _has_conditional_ancestor(
            self,
            block: BasicBlock,
            loop: LoopRegion,
    ) -> bool:
        """Return True if block is nested below an IfRegion before reaching loop."""

        region = self.graph.owner(block)

        while region is not None:
            if region is loop:
                return False

            if region.__class__.__name__ == "IfRegion":
                return True

            region = getattr(region, "parent", None)

        return False

    # ------------------------------------------------------------------
    # Conversion
    # ------------------------------------------------------------------

    @staticmethod
    def _convert(
            block: BasicBlock,
            terminator: TerminatorJump,
    ) -> None:
        if not block.instructions:
            return

        last = block.instructions[-1]

        if last.terminator is not terminator:
            # Preserve the invariant: only mutate the instruction that
            # actually owns the CFG terminator.
            return

        last.terminator = None
        last.value = None
        last.statement = ContinueStatement(label=None)

        block.terminator = None
