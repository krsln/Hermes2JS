from __future__ import annotations

from hermes_decompiler.backend.regions import RegionVisitor
from hermes_decompiler.backend.transforms.shared._repoint import _REGION_EXPRESSION_ATTRIBUTES
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier, ThisPlaceholder
from ._base import RegionPass

logger = get_logger(__name__)


class _RegionCollector(RegionVisitor):
    def __init__(self) -> None:
        self.regions: list = []

    def visit(self, node) -> None:
        self.regions.append(node)
        super().visit(node)


def _names(node, out: dict[str, int]) -> None:
    if isinstance(node, Identifier):
        out[node.name] = out.get(node.name, 0) + 1
        return

    if not isinstance(node, Node):
        return

    for child in node.children:
        if isinstance(child, Node):
            _names(child, out)


class DeadThisPlaceholderPass(RegionPass):
    """Drops a printed `rN = CreateThisForNew(rM)` / `CreateThisForSuper(rM)`
    nothing refers to.

    The placeholder stands for the `this` a `new`/`super` call allocates; it
    has no surface syntax and no effect of its own. The call handlers consume
    it when the window they read holds it, but hermes-98 often allocates it
    in a register that no window ever reads (a constructor inlined by the
    compiler, a `typeof` guard in front of the `new`), and it then prints as
    a dead `r3 = CreateThisForNew(r1)`.

    Only a placeholder whose register name is not mentioned by ANY other
    instruction, terminator or region condition of the function is removed:
    when the name is reused for something else the scan cannot tell the two
    lifetimes apart, and the statement stays.
    """

    def run(self) -> None:
        mentions: dict[str, int] = {}
        candidates = []

        for block in self.graph.blocks():
            for instr in block.instructions:
                for held in (instr.value, instr.statement, instr.terminator):
                    _names(held, mentions)

                if (
                        instr.dest_reg is not None
                        and isinstance(instr.value, ThisPlaceholder)
                        and not instr.definition_used
                        and instr.statement is None
                ):
                    candidates.append((block, instr))

            if isinstance(block.terminator, Node):
                _names(block.terminator, mentions)

        if not candidates:
            return

        collector = _RegionCollector()
        collector.visit(self.graph.root)

        for region in collector.regions:
            for attribute in _REGION_EXPRESSION_ATTRIBUTES:
                _names(getattr(region, attribute, None), mentions)

            for case in getattr(region, "cases", ()):
                for test in getattr(case, "tests", None) or ():
                    _names(test, mentions)

        for block, instr in candidates:
            # The placeholder's own value mentions its SOURCE register, not
            # its destination, so a mention of the destination is a reader.
            if mentions.get(f"r{instr.dest_reg}", 0) == 0:
                block.instructions.remove(instr)
                logger.debug("dropped dead this-placeholder r%s", instr.dest_reg)
