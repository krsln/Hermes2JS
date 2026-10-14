from __future__ import annotations

from hermes_decompiler.backend.regions import LoopRegion, RegionVisitor
from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.backend.transforms.shared._repoint import _reads_register_by_name
from hermes_decompiler.core.logging import get_logger
from ._base import RegionPass

logger = get_logger(__name__)


class LoopCarriedDefinitionPass(RegionPass, RegionVisitor):
    """Prints the pre-loop definition a loop only sometimes overwrites.

        r0 = param1;                      // folded into its readers, never printed
        for (const x of xs) { r0 = f(x); }
        return r0;                        // reads the register by name

    A loop that may run zero times (or skip its write on some iteration)
    leaves the register holding the earlier value, so the code after the loop
    names a register whose first definition was folded away. The latest pure
    definition in front of the loop prints again; readers that already hold a
    copy of the value keep it.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._repair(node)
        self.visit(node.body)

    def _repair(self, loop: LoopRegion) -> None:
        blocks = list(loop.covered_blocks)

        if not blocks:
            return

        start = min(b.address for b in blocks)
        end = max(i.address for b in blocks for i in b.instructions) if any(b.instructions for b in blocks) else None

        if end is None:
            return

        inside = {id(b) for b in blocks}
        written = {i.dest_reg for b in blocks for i in b.instructions if i.dest_reg is not None}

        for register in sorted(written):
            earlier = [
                i for b in self.cfg.blocks if id(b) not in inside for i in b.instructions
                if i.address < start and i.dest_reg == register and i.value is not None
            ]

            if not earlier:
                continue

            definition = max(earlier, key=lambda i: i.address)

            if not definition.definition_used or definition.definition_pinned or has_side_effects(definition.value):
                continue

            if not _reads_register_by_name(self.cfg, register, end, root=self.graph.root):
                continue

            definition.definition_used = False
            logger.debug("loop carried: r%s keeps its definition before the loop", register)
