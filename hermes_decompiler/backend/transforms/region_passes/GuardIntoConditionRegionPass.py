from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.backend.transforms.shared import negate_condition
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from ._base import RegionPass
from ..structurers.if_structurer._predicates import representative_block

logger = get_logger(__name__)


class GuardIntoConditionRegionPass(RegionPass, RegionVisitor):
    """`if (A) { if (B) goto NEXT; X }` NEXT: ... becomes `if (A && !B) { X }`.

    The arm's first test jumps to the code that follows the whole `if`: where `!A` goes too. That happens when
    the arm ends in a `continue`/`return` (so the structurer found no join to give the guard) and the source was
    a shared label: `case "left": case "right":` compiled as `if (x !== "left") { if (x === "right") goto L; ...
    switch ...; continue } L: ...` (96/1351 `processTransformOrigin`).

    Only a guard that is nothing but its test (no statement before the branch) and sits first in the arm, so
    evaluating it after `A` and before `X` is exactly the order it already ran in.
    """

    def run(self) -> None:
        # The retry ladder's last rung only (`HermesAnalysis`): the earlier rungs may structure the shape better.
        if getattr(self.cfg, "fold_arm_guards", False):
            self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in list(node.children):
            if isinstance(child, IfRegion):
                self._try_fold(node, child)

        for child in list(node.children):
            if not isinstance(child, BasicBlock):
                self.visit(child)

    def _try_fold(self, owner: SequenceRegion, region: IfRegion) -> None:
        if region.else_body is not None or region not in owner.children:
            return

        arm = region.then_body.children

        if len(arm) < 2 or not isinstance(arm[0], BasicBlock):
            return

        guard = arm[0]
        branch = guard.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or len(guard.successors) != 2:
            return
        if any(i.terminator is None for i in guard.instructions) or guard.instructions[-1].terminator is not branch:
            return

        at = owner.children.index(region)

        if at + 1 >= len(owner.children):
            return

        after = representative_block(owner.children[at + 1])
        inside = representative_block(arm[1])

        if after is None or inside is None or branch.target != after.address:
            return

        taken = next((b for b in guard.successors if b.address == branch.target), None)
        fall = next((b for b in guard.successors if b is not taken), None)

        # The fall-through is the arm's next item, or a test an earlier pass folded into that item (a `switch`
        # takes its comparison blocks into the region and leaves its first address below the region's entry).
        if taken is not after or fall is None or not guard.address < fall.address <= inside.address:
            return

        guard.instructions.pop()
        guard.terminator = None

        region.condition = BinaryExpression(
            left=region.condition, operator=LogicalOperator.AND, right=negate_condition(branch.condition)
        )
        arm.remove(guard)
        region.then_body.invalidate_coverage()
        region.invalidate_coverage()
        logger.debug("guard folded into the condition: block %d", guard.id)
