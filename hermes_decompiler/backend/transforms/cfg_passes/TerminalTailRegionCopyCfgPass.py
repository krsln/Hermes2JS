"""Gives the jumpers of a shared tail that only ever returns or throws their own copy of it.

    if (!X) goto T;            // jumper
    A;
    if (c) goto TAIL;          // faller's test: skips T
    T: ... return ...          // reached by the jumper AND by falling out of the test above
    TAIL: ... return ...

Neither `if (X)` arm owns `T`, and `TAIL` is entered from inside the arm, so the structurers keep one of the ways
into `T` as a raw `goto` (`SharedTailDuplicationCfgPass` copies only a tail that runs on into `END`). A tail that
never runs on, a closed forward region of blocks ending in `return`/`throw`, can simply be copied behind the last
block for the jumpers (98/2330 and 96/7888 `anonymous`); the test that falls into it keeps the original.
"""

from __future__ import annotations

import copy
import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
    TerminatorThrow,
)


class TerminalTailRegionCopyCfgPass:
    _MAX_BLOCKS = 24
    _MAX_INSTRUCTIONS = 150

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        copied = 0

        for tail in list(self.cfg.blocks):
            found = self._candidate(tail)

            if found is not None:
                self._copy(*found)
                copied += 1

        return copied

    def _candidate(self, tail: BasicBlock):
        blocks = self.cfg.blocks

        if len(tail.predecessors) < 2 or tail not in blocks:
            return None

        index = blocks.index(tail)

        if index == 0:
            return None

        faller = blocks[index - 1]
        branch = faller.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or faller not in tail.predecessors:
            return None
        if branch.target <= tail.address or tail.successors == []:
            return None

        jumpers = [p for p in tail.predecessors if p is not faller]

        for pred in jumpers:
            terminator = pred.terminator

            if not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                return None
            if terminator.target != tail.address or pred.address >= tail.address:
                return None

        region = self._closed_region(tail)

        if region is None or faller in region or len(region) < 3:
            return None

        return tail, region, jumpers

    def _closed_region(self, tail: BasicBlock):
        region: dict[BasicBlock, None] = {}
        stack = [tail]

        while stack:
            block = stack.pop()

            if block in region:
                continue

            region[block] = None

            if len(region) > self._MAX_BLOCKS:
                return None

            terminator = block.terminator

            if terminator is not None and not isinstance(
                    terminator, (TerminatorJump, TerminatorConditionalBranch, TerminatorReturn, TerminatorThrow)
            ):
                return None
            if any(i.terminator is not None and i.terminator is not terminator for i in block.instructions):
                return None

            for successor in block.successors:
                # A back edge to the loop head the tail sits in is a way out too (`continue`, 98/2330).
                if successor.address < tail.address and successor not in region:
                    continue

                stack.append(successor)

        for block in region:
            if block is not tail and any(p not in region for p in block.predecessors):
                return None

        if sum(len(b.instructions) for b in region) > self._MAX_INSTRUCTIONS:
            return None

        # Every way out is a return, a throw or a back edge: nothing in the region runs on into the code behind it.
        if any(not block.successors and block.terminator is None for block in region):
            return None

        ordered = [b for b in self.cfg.blocks if b in region]

        # A fall-through successor has to stay right behind its block in the copy.
        for position, block in enumerate(ordered):
            terminator = block.terminator
            falls = terminator is None or isinstance(terminator, TerminatorConditionalBranch)

            if falls and block.successors:
                fall = next((s for s in block.successors if not self._jump_target(block, s)), None)

                if fall is not None and (position + 1 >= len(ordered) or ordered[position + 1] is not fall):
                    return None

        return ordered

    @staticmethod
    def _jump_target(block: BasicBlock, successor: BasicBlock) -> bool:
        terminator = block.terminator

        return isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)) and (
                terminator.target == successor.address
        )

    def _copy(self, tail: BasicBlock, region: list, jumpers: list) -> None:
        blocks = self.cfg.blocks
        next_id = max(b.id for b in blocks) + 1
        next_address = max(b.address for b in blocks) + 1
        clones: dict[BasicBlock, BasicBlock] = {}

        for offset, block in enumerate(region):
            clone = BasicBlock(next_id + offset, next_address + offset)

            for instruction in block.instructions:
                duplicate = copy.copy(instruction)
                duplicate.value = copy.deepcopy(instruction.value)
                duplicate.statement = copy.deepcopy(instruction.statement)

                if instruction.terminator is not None:
                    duplicate.terminator = copy.copy(instruction.terminator)

                clone.instructions.append(duplicate)

            if block.terminator is not None and block.instructions and (
                    block.instructions[-1].terminator is block.terminator
            ):
                clone.terminator = clone.instructions[-1].terminator
            else:
                clone.terminator = copy.copy(block.terminator)

            clones[block] = clone

        for block, clone in clones.items():
            terminator = clone.terminator

            if isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                target = next((s for s in block.successors if s.address == terminator.target), None)

                if target is not None and target in clones:
                    retargeted = dataclasses.replace(terminator, target=clones[target].address)

                    for instruction in clone.instructions:
                        if instruction.terminator is terminator:
                            instruction.terminator = retargeted

                    clone.terminator = retargeted

            clone.successors = [clones.get(s, s) for s in block.successors]

            for successor in clone.successors:
                successor.predecessors.append(clone)

        entry = clones[tail]

        for pred in jumpers:
            retargeted = dataclasses.replace(pred.terminator, target=entry.address)

            for instruction in pred.instructions:
                if instruction.terminator is pred.terminator:
                    instruction.terminator = retargeted

            pred.terminator = retargeted
            pred.successors = [entry if s is tail else s for s in pred.successors]
            tail.predecessors.remove(pred)
            entry.predecessors.append(pred)

        blocks.extend(clones[b] for b in region)
