from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.backend.transforms.region_passes._base import RegionPass
from hermes_decompiler.backend.transforms.shared import has_side_effects, negate_condition
from hermes_decompiler.ir.expressions import Identifier


class EmptyIfArmRegionPass(RegionPass, RegionVisitor):
    """Removes `if` arms that print nothing.

    Structuring leaves an arm behind when a branch only skips over code the earlier passes
    folded or dropped. Three shapes come out of that, all of them noise:

        if (c) { } else { X }   ->   if (!c) { X }       (96/10021 `if (r2 == null) { } else { ... }`)
        if (c) { X } else { }   ->   if (c) { X }
        if (c) { }              ->   (nothing)           only when `c` cannot run anything

    The last one is the leftover of a test whose two branches meet again at once
    (`if (r15.call === builtin_56) { }`, `if (r5 === "function") { }`); with a call in the test
    the `if` stays, since that call must still run.

    Must run after every pass that can empty an arm (`DeadMovEliminationPass`,
    `DeadUndefinedStorePass`, `TrailingReturnRegionPass`): an arm only counts as empty once
    nothing in it prints. That is decided the way `RegionPrinter._emit_block` does: a
    statement, a jump, or a definition no reader folded away is a line of output; a folded
    definition (`definition_used`) is not.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        # Children first: an `else if` whose own arms vanish may leave its parent's arm empty.
        for child in list(node.children):
            self.visit(child)

        for child in list(node.children):
            if isinstance(child, IfRegion) and self._simplify(child) and self._is_removable(child):
                node.children.remove(child)
                node.invalidate_coverage()

    @staticmethod
    def _is_removable(region: IfRegion) -> bool:
        return (
                region.else_body is None
                and EmptyIfArmRegionPass._is_empty(region.then_body)
                and region.condition is not None
                and not has_side_effects(region.condition)
        )

    def _simplify(self, region: IfRegion) -> bool:
        """Rewrite one `if` in place. True when the result may be removable altogether."""
        if region.condition is None:
            return False

        if region.else_body is not None and self._is_empty(region.else_body):
            region.else_body = None

        if region.else_body is not None and self._is_empty(region.then_body):
            region.condition = negate_condition(region.condition)
            region.then_body = region.else_body
            region.else_body = None

        return True

    @staticmethod
    def _is_empty(body) -> bool:
        if body is None:
            return True

        if not isinstance(body, SequenceRegion):
            return False

        return all(isinstance(child, BasicBlock) and not EmptyIfArmRegionPass._prints(child) for child in body.children)

    @staticmethod
    def _prints(block: BasicBlock) -> bool:
        """True if `RegionPrinter._emit_block` would write a line for `block`."""
        for instr in block.instructions:
            if instr.statement is not None or instr.terminator is not None:
                return True

            if instr.value is None or instr.definition_used:
                continue

            # `rN = rN` is never printed.
            if (
                    instr.dest_reg is not None
                    and isinstance(instr.value, Identifier)
                    and instr.value.name == f"r{instr.dest_reg}"
            ):
                continue

            return True

        return False
