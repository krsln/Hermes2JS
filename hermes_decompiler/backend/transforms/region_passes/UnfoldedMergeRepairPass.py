from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, IfRegion
from hermes_decompiler.backend.transforms.shared import (
    has_side_effects, repoint_references, reclaim_definition,
)
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier, ThisPlaceholder
from ._base import RegionPass

logger = get_logger(__name__)


class _BlockCollector(RegionVisitor):
    """Every BasicBlock below a region (BasicBlock is a leaf: `generic_visit`)."""

    def __init__(self) -> None:
        self.blocks: list[BasicBlock] = []

    def generic_visit(self, node) -> None:
        if isinstance(node, BasicBlock):
            self.blocks.append(node)
            return

        super().generic_visit(node)


class _IfCollector(RegionVisitor):
    def __init__(self) -> None:
        self.ifs: list[IfRegion] = []

    def visit_IfRegion(self, node: IfRegion) -> None:
        self.ifs.append(node)
        super().visit_IfRegion(node)


def _always_writes(body, register: int, value) -> bool:
    """Does every path through `body` end with `rN = <value equal to value>`?"""
    if body is None:
        return False

    if isinstance(body, IfRegion):
        return (
                body.else_body is not None
                and _always_writes(body.then_body, register, value)
                and _always_writes(body.else_body, register, value)
        )

    if isinstance(body, BasicBlock):
        written = None

        for instr in body.instructions:
            if instr.dest_reg == register and instr.value is not None:
                written = instr

        return written is not None and written.value.structurally_equal(value)

    for child in reversed(getattr(body, "children", ())):
        if isinstance(child, IfRegion):
            if _always_writes(child, register, value):
                return True

            continue

        if isinstance(child, BasicBlock):
            if any(i.dest_reg == register for i in child.instructions):
                return _always_writes(child, register, value)

            continue

        return False

    return False


def _blocks_of(body) -> list[BasicBlock]:
    if body is None:
        return []

    collector = _BlockCollector()
    collector.visit(body)

    return collector.blocks


class UnfoldedMergeRepairPass(RegionPass):
    """A value written in only ONE arm of an `if` is not a value the code
    after the `if` may inline.

    The frontend analysis is linear: it never sees a control-flow merge. For
    `if (r3 == null) { r3 = r2[3] }` followed by a read of `r3`, the reader
    inlines `r2[3]` (the arm's write) and flags the arm instruction
    `definition_used`, so the arm prints nothing - `if (r3 == null) { }` -
    and the read claims the value unconditionally. Whether it is `r3` as it
    was or `r2[3]` depends on the path taken: a phi.

    The fold passes remove such arms when they can express the merge as one
    expression (`||`, `?:`, `??=`). For every arm they LEFT, this pass
    undoes the inlining that crossed the merge: the readers outside the `if`
    get `rN` back, the arm's write is printed again, and the definition
    that was current before the `if` (flagged used by the `if`'s own
    condition) is printed too when nothing else reads it.

    A reader INSIDE the same arm, after the write, is not a merge read and
    keeps its inlined value.
    """

    def run(self) -> None:
        self._index = None

        collector = _IfCollector()
        collector.visit(self.graph.root)

        # Inner `if`s first: their repair changes what an outer arm holds.
        for if_region in reversed(collector.ifs):
            self._repair(if_region)

    def _repair(self, if_region: IfRegion) -> None:
        for body in (if_region.then_body, if_region.else_body):
            arm_blocks = _blocks_of(body)

            if not arm_blocks:
                continue

            arm_instructions = [i for blk in arm_blocks for i in blk.instructions]
            other_blocks = set(_blocks_of(if_region.then_body)) | set(_blocks_of(if_region.else_body))
            arm_set = set(arm_instructions)

            for write in reversed(arm_instructions):
                self._repair_write(if_region, write, arm_set, other_blocks, arm_blocks)

    def _repair_write(self, if_region, write, arm_set, region_blocks, arm_blocks) -> None:
        if write.dest_reg is None or not write.definition_used or write.value is None:
            return

        # `this` placeholders have no surface syntax; nothing to name.
        if isinstance(write.value, ThisPlaceholder):
            return

        # The same node object defined by several instructions (constant
        # loads share one literal) cannot tell whose value a reader holds.
        if sum(1 for b in self.cfg.blocks for i in b.instructions if i.value is write.value) > 1:
            return

        # Every path writes the same thing: no phi, the inlined copy is right.
        if (
                if_region.else_body is not None
                and _always_writes(if_region.then_body, write.dest_reg, write.value)
                and _always_writes(if_region.else_body, write.dest_reg, write.value)
        ):
            return

        # A write run twice (printed and inlined) would repeat its effect.
        if has_side_effects(write.value):
            return

        if not self._read_after_the_if(write, region_blocks):
            return

        replacement = Identifier(name=f"r{write.dest_reg}")
        old_value = write.value

        repoint_references(
            self.cfg, self.graph.root, old_value, replacement,
            min_block_id=min(b.id for b in arm_blocks),
            exclude=arm_set,
        )

        self._index = None
        write.definition_used = False
        logger.debug("unfolded merge: r%s written in one arm is read after the if", write.dest_reg)

        self._reprint_default(if_region, write)

    def _holders(self) -> dict[int, set]:
        """id(node) -> the blocks holding that node in a value, statement or
        terminator. Built once; dropped after a repair rewrites nodes."""
        if self._index is None:
            index: dict[int, set] = {}

            def walk(node, block) -> None:
                index.setdefault(id(node), set()).add(block)

                for child in node.children:
                    if isinstance(child, Node):
                        walk(child, block)

            for block in self.cfg.blocks:
                for instr in block.instructions:
                    for held in (instr.value, instr.statement, instr.terminator):
                        if isinstance(held, Node):
                            walk(held, block)

                if isinstance(block.terminator, Node):
                    walk(block.terminator, block)

            self._index = index

        return self._index

    def _read_after_the_if(self, write, region_blocks) -> bool:
        """Is a copy of `write.value` held by something outside the `if`?"""
        holders = self._holders().get(id(write.value), ())

        return any(block not in region_blocks for block in holders)

    def _reprint_default(self, if_region, write) -> None:
        """Print the definition that was current before the `if` (the other
        path of the phi), unless something else still consumes it inline."""
        head = [
            i for blk in self.cfg.blocks for i in blk.instructions
            if i.address < write.address and i.dest_reg == write.dest_reg
               and i.definition_used and i.value is not None
        ]

        if not head:
            return

        default = max(head, key=lambda i: i.address)

        if isinstance(default.value, ThisPlaceholder):
            return

        reclaim_definition(
            self.cfg, self.graph.root, default, default.value, write,
            ignore_blocks=set(_blocks_of(if_region.then_body)) | set(_blocks_of(if_region.else_body)),
            ignore_regions={if_region},
        )
