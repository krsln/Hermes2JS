"""Moves the constant a test loads for the join onto the edge that jumps there.

    B1: r5 = "focus";             if (p === 8)   goto L
    B2: r5 = "windowStateChange"; if (p === 32)  goto L
    B3: r5 = "click";             if (p === 1)   goto L
    E:  <no read of r5>; return
    L:  <reads r5>

The bytecode loads each constant BEFORE its test (the register allocator hoisted it), so on the way to `L` the
register holds the constant of the test that jumped. No `if` can own `L` that way: the printed code showed only
one of the constants. The load belongs to the taken edge:

    B1: if (p === 8) goto E1;  ...  E1: r5 = "focus"; goto L

and the tests become a plain `if / else if` chain with `L` after it.

The load has to be dead on the fall-through path (the next test writes the register first), and nothing in its own
block may read the register. At least two tests of the same join must qualify, with different constants: a lone
`r5 = c; if (t) goto L` is already structured. It runs on the last rung of the retry ladder only, for a function
that still has a `goto`.
"""

from __future__ import annotations

import copy
import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.backend.transforms.shared._repoint import repoint_references
from hermes_decompiler.ir.expressions import Identifier, Literal
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump, TerminatorReturn, \
    TerminatorThrow
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass as _Liveness


class TestConstantSinkCfgPass:
    __test__ = False  # pytest: not a test class

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> bool:
        if self.cfg.exception_handlers:
            return False

        groups: dict = {}

        for block in self.cfg.blocks:
            found = self._candidate(block)

            if found is not None:
                groups.setdefault((found[0].address, found[1].dest_reg), []).append((block, found[1]))

        changed = False

        for (_, register), members in groups.items():
            values = {repr(instruction.value) for _, instruction in members}

            if len(members) < 2 or len(values) < 2:
                continue

            changed = self._sink(members) or changed

        return changed

    def _candidate(self, block: BasicBlock):
        """(join, load) for a test block whose constant can move onto its taken edge."""
        terminator = block.terminator

        if not isinstance(terminator, TerminatorConditionalBranch) or len(block.successors) != 2:
            return None

        taken, fall = block.successors

        if taken.address != terminator.target or taken is fall:
            return None

        loads = [
            i for i in block.instructions
            if i.terminator is None and i.dest_reg is not None and isinstance(i.value, Literal)
            and i.statement is None
        ]

        for load in reversed(loads):
            register = load.dest_reg
            later = block.instructions[block.instructions.index(load) + 1:]

            if any(i.dest_reg == register for i in later if i.terminator is None):
                continue

            if any(self._reads(i, register) for i in later):
                continue

            if not _Liveness._dead_on_entry(fall, register, set()):
                continue

            return taken, load

        return None

    @staticmethod
    def _reads(instruction, register: int) -> bool:
        name = f"r{register}"
        nodes = [
            instruction.value, instruction.statement, getattr(instruction.terminator, "condition", None),
            getattr(instruction.terminator, "value", None),
        ]

        return _Liveness._reads_operand(instruction, register) or any(
            n is not None and _Liveness._mentions(n, name) for n in nodes
        )

    def _sink(self, members: list) -> bool:
        blocks = self.cfg.blocks
        join = members[0][0].successors[0]
        index = blocks.index(join)

        if index == 0:
            return False

        before = blocks[index - 1]

        # The new blocks sit right before the join: what precedes it must not fall into them.
        if not isinstance(before.terminator, (TerminatorJump, TerminatorReturn, TerminatorThrow)):
            return False

        taken_addresses = {b.address for b in blocks}
        addresses = [join.address - len(members) + n for n in range(len(members))]

        if any(a <= before.address or a in taken_addresses for a in addresses):
            return False

        next_id = max(b.id for b in blocks) + 1
        edges = []

        for n, (block, load) in enumerate(members):
            edge = BasicBlock(next_id + n, addresses[n])
            copied = copy.copy(load)
            copied.value = copy.deepcopy(load.value)
            copied.definition_used = False
            edge.instructions.append(copied)

            jump = copy.copy(block.instructions[-1])
            jump.value = None
            jump.statement = None
            jump.dest_reg = None
            jump.terminator = TerminatorJump(target=join.address)
            edge.instructions.append(jump)
            edge.terminator = jump.terminator
            edge.successors = [join]
            edge.predecessors = [block]
            edges.append(edge)

        for (block, load), edge in zip(members, edges):
            block.instructions.remove(load)

            # A reader that took the constant straight from this load (the bytecode order made the last one
            # reach the join) reads the register now: which constant it holds depends on the edge.
            repoint_references(
                self.cfg, None, load.value, Identifier(f"r{load.dest_reg}"),
                min_block_id=0, exclude={e.instructions[0] for e in edges}, structural=False,
            )

            terminator = dataclasses.replace(block.terminator, target=edge.address)
            block.instructions[-1].terminator = terminator
            block.terminator = terminator
            block.successors = [edge if s is join else s for s in block.successors]
            join.predecessors = [edge if p is block else p for p in join.predecessors]

        blocks[index:index] = edges

        return True
