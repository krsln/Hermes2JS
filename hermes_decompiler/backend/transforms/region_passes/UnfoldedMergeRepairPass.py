from __future__ import annotations

import re

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, IfRegion
from hermes_decompiler.backend.transforms.shared import (
    has_side_effects, repoint_references, reclaim_definition, TRIVIAL_NODE_TYPES, prints_definition,
    substitute_register,
)
from hermes_decompiler.backend.transforms.shared._repoint import _reads_register_by_name
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import ConditionalExpression, Identifier, ThisPlaceholder
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow
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


def _always_assigns(body, register: int) -> bool:
    """Does every path through `body` that reaches the code after it write `rN`
    (whatever the value)? A path that returns or throws never reaches it."""
    if body is None:
        return False

    if isinstance(body, IfRegion):
        return (
                body.else_body is not None
                and _always_assigns(body.then_body, register)
                and _always_assigns(body.else_body, register)
        )

    if isinstance(body, BasicBlock):
        return (
                isinstance(body.terminator, (TerminatorReturn, TerminatorThrow))
                or any(i.dest_reg == register and i.value is not None for i in body.instructions)
        )

    for child in reversed(getattr(body, "children", ())):
        if isinstance(child, IfRegion):
            if _always_assigns(child, register):
                return True

            continue

        if isinstance(child, BasicBlock):
            if _always_assigns(child, register):
                return True

            continue

        # A loop / try / switch: whether it runs, or finishes, is not known here.
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
        self._made: set[int] = set()  # ids of the replacement identifiers this pass created

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

            reaching: set[int] = set()

            for write in reversed(arm_instructions):
                # The first write met walking backwards is the arm's LAST write
                # of that register: the one that reaches the code after the `if`.
                is_last = write.dest_reg is not None and write.dest_reg not in reaching

                if write.dest_reg is not None:
                    reaching.add(write.dest_reg)

                self._repair_write(if_region, write, arm_set, other_blocks, arm_blocks, is_last)

    def _repair_write(self, if_region, write, arm_set, region_blocks, arm_blocks, is_last=False) -> None:
        if write.dest_reg is None or write.value is None:
            return

        if not write.definition_used:
            # The arm's write already prints. A reader after the `if` normally
            # names the register and needs nothing repointed - unless a fold
            # handed it a COPY of the arm's value (`r5 = c ? a : b` folded inside
            # the arm, the `Add` after the `if` repointed to the same ternary):
            # on the path that skips the arm it reads the wrong thing.
            #
            # The OTHER path of the phi still needs its value: the default that
            # was current before the `if` and that the `if`'s own condition may
            # have consumed inline.
            self._reprint_default_for_printed_write(if_region, write, region_blocks)
            self._repoint_copies_of_printed_write(write, arm_set, region_blocks, arm_blocks, is_last)
            return

        # `this` placeholders have no surface syntax; nothing to name.
        if isinstance(write.value, ThisPlaceholder):
            return

        # The code after the `if` names the register (`r2.call(...)`) rather than
        # holding a copy of this value, and this is the write that reaches it on
        # this arm's path: the statement has to print, whatever else inlined the
        # value inside the arm (`r3[12] = y`). Nothing is repointed - the reader
        # already says `rN`.
        if is_last and not has_side_effects(write.value) and self._named_after_the_if(write, region_blocks):
            write.definition_used = False
            self._index = None
            logger.debug("unfolded merge: r%s written in an arm is named after the if", write.dest_reg)
            return

        # The same node object defined by several instructions (constant loads
        # share one literal, a parameter load its `param1`) cannot tell whose
        # value a reader holds. A holder of ANOTHER opcode is a reader (`Mov r11,
        # r5` carrying the arm's value) and is exactly what gets repointed.
        # An object an earlier repair of this pass created (`Identifier r0`
        # handed to every reader it repointed) is shared on purpose.
        if id(write.value) not in self._made:
            holders = [
                i for b in self.cfg.blocks for i in b.instructions
                if i.value is write.value and i.entry.opcode == write.entry.opcode
            ]

            if len(holders) > 1:
                # The extra holders being `Mov`s that read this register are
                # the readers of the join value; only THEY take the register
                # (a global repoint would also hit every other register the
                # value was copied into). Anything else is ambiguous.
                readers = [i for i in holders if i is not write and self._is_reader_mov_of(i, write)]
                # The `Mov` that handed the write its value (`Mov r13, r10` ...
                # `Mov r14, r13`) holds the same node because the write COPIED
                # it: it is the write's source, not an unrelated owner (96/4846).
                feeders = [i for i in holders if i is not write and self._is_source_mov_of(i, write)]

                if len(holders) - len(readers) - len(feeders) > 1 or not readers:
                    return

                self._repoint_reader_movs(write, if_region, region_blocks, arm_blocks)
                return

        # Every path writes the same thing: no phi, the inlined copy is right.
        if (
                if_region.else_body is not None
                and _always_writes(if_region.then_body, write.dest_reg, write.value)
                and _always_writes(if_region.else_body, write.dest_reg, write.value)
        ):
            return

        # A write run twice (printed and inlined) would repeat its effect. The
        # repoint below MOVES the effect: the arm prints it and the reader
        # names the register, so it runs once - and only on the path that
        # takes the arm (`x = c ? new A(a) : a`, `AnimatedAddition` 96/5146).
        # Only the arm's last write of the register reaches the reader.
        if has_side_effects(write.value) and not is_last:
            return

        if not self._read_after_the_if(write, region_blocks):
            return

        replacement = Identifier(name=f"r{write.dest_reg}")
        old_value = write.value
        self._made.add(id(replacement))

        repoint_references(
            self.cfg, self.graph.root, old_value, replacement,
            min_block_id=min(b.id for b in arm_blocks),
            exclude=arm_set,
        )

        self._index = None
        write.definition_used = False
        logger.debug("unfolded merge: r%s written in one arm is read after the if", write.dest_reg)

        self._reprint_default(if_region, write)

    def _default_prints(self, write, region_blocks) -> bool:
        """Is the register assigned on the path that skips the arm? The copy is
        a pure value that needs no register; the register read in its place
        only has one when an earlier definition outside the `if` prints."""
        earlier = [
            i for blk in self.cfg.blocks if blk not in region_blocks for i in blk.instructions
            if i.address < write.address and i.dest_reg == write.dest_reg and i.value is not None
        ]

        return bool(earlier) and prints_definition(max(earlier, key=lambda i: i.address))

    def _repoint_copies_of_printed_write(self, write, arm_set, region_blocks, arm_blocks, is_last) -> None:
        """Readers outside the `if` that hold the printed arm write's value
        itself read `rN` instead (see `_repair_write`). Only a pure value that is
        the arm's last write of the register, and only a non-trivial one: a bare
        literal or identifier is shared by unrelated readers."""
        if (
                not is_last
                or isinstance(write.value, ThisPlaceholder)
                or has_side_effects(write.value)
                or not self._read_after_the_if(write, region_blocks)
                or not self._default_prints(write, region_blocks)
        ):
            return

        if isinstance(write.value, TRIVIAL_NODE_TYPES):
            self._repoint_movs_of_printed_write(write, arm_blocks, region_blocks)
            self._repoint_alias_readers_of_printed_write(write, arm_blocks, region_blocks)
            return

        # Only readers OUTSIDE the `if`: the sibling arm holds the very same value
        # object (`guard.call(.., r0.message)` next to `r18 = r0.message`) and runs
        # on a path where the register was never written.
        repoint_references(
            self.cfg, self.graph.root, write.value, Identifier(name=f"r{write.dest_reg}"),
            min_block_id=min(b.id for b in arm_blocks),
            exclude={i for blk in region_blocks for i in blk.instructions},
            structural=False,
        )

        self._index = None
        logger.debug("unfolded merge: copies of printed r%s after the if read the register", write.dest_reg)

    _MOV_SOURCE_RE = re.compile(r"Reg(?:8|32):\s*\d+,\s*Reg(?:8|32):\s*(\d+)")

    def _repoint_reader_movs(self, write, if_region, region_blocks, arm_blocks) -> None:
        if (not isinstance(write.value, (*TRIVIAL_NODE_TYPES, ConditionalExpression)) or has_side_effects(write.value)
                or not self._read_after_the_if(write, region_blocks)):
            return

        self._repoint_movs_of_printed_write(write, arm_blocks, region_blocks)

        self._index = None
        write.definition_used = False
        logger.debug("unfolded merge: r%s read by Mov after the if", write.dest_reg)
        self._reprint_default(if_region, write)

    def _is_reader_mov_of(self, instruction, write) -> bool:
        """A `Mov rX, rN` (X != N) holding the write's value is its reader."""
        if instruction is write or instruction.dest_reg == write.dest_reg:
            return False

        if instruction.entry.opcode not in ("Mov", "MovLong"):
            return False

        source = self._MOV_SOURCE_RE.match(instruction.entry.args)

        return source is not None and int(source.group(1)) == write.dest_reg

    def _is_source_mov_of(self, instruction, write) -> bool:
        """`instruction` is a `Mov` that wrote the register `write` (a `Mov`)
        copies from."""
        if write.entry.opcode not in ("Mov", "MovLong") or instruction.entry.opcode not in ("Mov", "MovLong"):
            return False

        source = self._MOV_SOURCE_RE.match(write.entry.args)

        return source is not None and instruction.dest_reg == int(source.group(1))

    def _repoint_movs_of_printed_write(self, write, arm_blocks, region_blocks) -> None:
        """A bare identifier/literal is shared by unrelated readers, so only a
        `Mov` that reads this very register and holds the arm's value takes the
        register: `r3 = 2; if (c) { r3 = r4 }; r8 = r3` printed `r8 = r4`."""
        inside = {i for blk in region_blocks for i in blk.instructions}
        minimum = min(b.id for b in arm_blocks)
        changed = False

        for block in self.cfg.blocks:
            if block.id < minimum:
                continue

            for instruction in block.instructions:
                if instruction in inside or instruction.value is not write.value:
                    continue

                if instruction.entry.opcode not in ("Mov", "MovLong"):
                    continue

                source = self._MOV_SOURCE_RE.match(instruction.entry.args)

                if source is None or int(source.group(1)) != write.dest_reg:
                    continue

                instruction.value = Identifier(name=f"r{write.dest_reg}")
                changed = True

        if changed:
            self._index = None
            logger.debug("unfolded merge: Mov of printed r%s after the if reads the register", write.dest_reg)

    _REGISTER_NAME_RE = re.compile(r"r\d+")
    _OPERAND_REGISTER_RE = re.compile(r"Reg(?:8|32):\s*(\d+)")

    def _repoint_alias_readers_of_printed_write(self, write, arm_blocks, region_blocks) -> None:
        """`Mov r2, r4` printed in an arm (`r2 = r4`) hands the register alias `r4`
        to whatever reads `r2` next - a store (`r0.baseState = r2`), a call
        argument. Read after the `if` that is the arm's value alone, and on the
        paths that skip the arm `r2` holds something else (`useReducer` 96/2215).

        The readers are found by the bytecode, not by the node they hold: every
        read of the alias gets a copy of its own, and a node shared between
        several arms' writes cannot say whose it is. An instruction that has
        this register as an operand, runs before the register is written again
        and does not also read the alias's own register (that `r4` could be a
        genuine read of it) reads the register."""
        value = write.value

        if not isinstance(value, Identifier) or not self._REGISTER_NAME_RE.fullmatch(value.name):
            return

        if value.name == f"r{write.dest_reg}":
            return

        source = int(value.name[1:])
        inside = {i for blk in region_blocks for i in blk.instructions}

        # The alias travels on through copies (`Mov r18, r17` hands `r17`'s value
        # to `r18`), and a reader of THAT copy reads `r18`, not this register. Only
        # what runs before this register is written again can be its reader.
        limit = min(
            (
                i.address for blk in self.cfg.blocks for i in blk.instructions
                if i.address > write.address and i.dest_reg == write.dest_reg and i not in inside
                   and i.value is not None
            ),
            default=None,
        )

        replacement = Identifier(name=f"r{write.dest_reg}")
        minimum = min(b.id for b in arm_blocks)
        changed = False

        for block in self.cfg.blocks:
            if block.id < minimum:
                continue

            for instruction in block.instructions:
                if (
                        instruction in inside
                        or instruction.address <= write.address
                        or (limit is not None and instruction.address >= limit)
                        or instruction.dest_reg == write.dest_reg
                ):
                    continue

                operands = {int(n) for n in self._OPERAND_REGISTER_RE.findall(instruction.entry.args)}

                if write.dest_reg not in operands or source in operands:
                    continue

                if instruction.value is not None:
                    new_value = substitute_register(instruction.value, value.name, replacement)

                    if new_value is not instruction.value:
                        instruction.value = new_value
                        changed = True

                if instruction.statement is not None:
                    new_statement = substitute_register(instruction.statement, value.name, replacement)

                    if new_statement is not instruction.statement:
                        instruction.statement = new_statement
                        changed = True

        if changed:
            self._index = None
            logger.debug("unfolded merge: readers of the alias of printed r%s after the if read the register",
                         write.dest_reg)

    def _named_after_the_if(self, write, region_blocks) -> bool:
        """Does code after the `if` read `write`'s register BY NAME, before
        anything writes it again?"""
        end = max(
            (i.address for blk in region_blocks for i in blk.instructions),
            default=write.address,
        )

        return _reads_register_by_name(self.cfg, write.dest_reg, end, root=self.graph.root)

    def _reprint_default_for_printed_write(self, if_region, write, region_blocks) -> None:
        """`rN = d; if (c) { rN = v }; ...rN...` where `rN = v` prints: when `c`
        keeps the arm from running, the code after the `if` reads `d`, so
        `rN = d` has to print. It does not when the `if`'s condition inlined
        `d` (a constant compared against) and flagged it `definition_used`.

        Left alone when every path through the `if` writes the register (no
        path keeps the default), when nothing after the `if` names it, and
        when the default already prints."""
        register = write.dest_reg

        if isinstance(write.value, ThisPlaceholder):
            return

        if not self._named_after_the_if(write, region_blocks):
            return

        self._reprint_unprinted_default(if_region, write)

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

        # A parameter load (`r1 = param1`) shares its `param1` node with every
        # other reader of the parameter, so "is something else still holding
        # it" is always yes and `reclaim_definition` never prints it: the
        # skipping path then reads an `r1` nothing assigned. Print it - unless
        # every path overwrites the register anyway.
        if default.entry.opcode.startswith("LoadParam"):
            if not (
                    if_region.else_body is not None
                    and _always_assigns(if_region.then_body, write.dest_reg)
                    and _always_assigns(if_region.else_body, write.dest_reg)
            ):
                default.definition_used = False
                self._index = None

            return

        if reclaim_definition(
                self.cfg, self.graph.root, default, default.value, write,
                ignore_blocks=set(_blocks_of(if_region.then_body)) | set(_blocks_of(if_region.else_body)),
                ignore_regions={if_region},
        ):
            return

        # Still held by something else - the `if`'s own condition, as a rule
        # (`r0 = this.context; if (r0) { r0 = x }; return !!r0`). A pure value
        # is free to evaluate twice, and the path that skips the arm reads
        # the register.
        if (
                not has_side_effects(default.value)
                and not isinstance(write.value, TRIVIAL_NODE_TYPES)
                and self._condition_holds(if_region, default.value)
        ):
            default.definition_used = False

    @staticmethod
    def _condition_holds(if_region, value) -> bool:
        """Is `value` (this very node) part of the `if`'s own condition?"""
        condition = if_region.condition

        return isinstance(condition, Node) and any(node is value for node in condition.walk())

    def _reprint_unprinted_default(self, if_region, write) -> None:
        """The definition that was current before the `if` - for an arm write
        that already prints - when nothing prints it.

        That is the LATEST earlier definition of the register outside the `if`:
        when it already prints there is nothing to do - an older definition
        that happens to be unprinted is dead, and printing it would add a
        statement nothing reads. Nothing is repointed on this path, so a
        condition that inlined the default keeps its copy; only the path that
        skips the arm needs the register assigned."""
        # Every path through the `if` writes the register: no path keeps the
        # default, so it is dead.
        if _always_assigns(if_region.then_body, write.dest_reg) and _always_assigns(if_region.else_body,
                                                                                    write.dest_reg):
            return

        region_blocks = set(_blocks_of(if_region.then_body)) | set(_blocks_of(if_region.else_body))

        earlier = [
            i for blk in self.cfg.blocks if blk not in region_blocks for i in blk.instructions
            if i.address < write.address and i.dest_reg == write.dest_reg and i.value is not None
        ]

        if not earlier:
            return

        default = max(earlier, key=lambda i: i.address)

        if not default.definition_used or isinstance(default.value, ThisPlaceholder):
            return

        # A literal or a plain name is free to evaluate twice, so printing it as
        # well as leaving the copies other readers hold cannot change anything;
        # `reclaim_definition` would refuse because the condition it was folded
        # into (`r4 = param1 > 100`) still holds the very same node.
        if isinstance(default.value, TRIVIAL_NODE_TYPES):
            default.definition_used = False
            return

        reclaim_definition(
            self.cfg, self.graph.root, default, default.value, write,
            ignore_blocks=region_blocks,
            ignore_regions={if_region},
        )
