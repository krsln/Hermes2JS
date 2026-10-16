"""
Gives the test that skips a shared tail its own copy of it.

Hermes lays out `c ? x : y` / `a && b ? x : y` so that one small block is
reached both by jumps from several tests and by falling through the last
test, which jumps over it:

    if (!a) goto T;          // jumper
    if (!b) goto T;          // jumper
    ...
    if (c) goto END;         // P: skips T when c holds
    T: r0 = typeof a         // reached by the jumpers and by P's fall-through
    END: return r0

Neither arm owns `T`, so the structurers hand it to one test and the other
test loses its exit (a dropped `if`, or a raw `goto`). The block P falls
into gets a private copy placed right behind it; the jumpers keep the
original. Only a short run of plain instructions is copied, and never in a
function with exception handlers (a copy sits outside every try range).
"""

from __future__ import annotations

import copy

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump


class SharedTailDuplicationCfgPass:
    _MAX_INSTRUCTIONS = 12

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        copied = 0

        for tail in list(self.cfg.blocks):
            faller = self._faller_that_skips(tail)

            if faller is not None:
                self._give_private_copy(faller, tail)
                copied += 1

        return copied

    def _faller_that_skips(self, tail: BasicBlock) -> BasicBlock | None:
        if len(tail.instructions) > self._MAX_INSTRUCTIONS or len(tail.predecessors) < 2:
            return None
        if tail.terminator is not None and not isinstance(tail.terminator, TerminatorJump):
            return None
        if len(tail.successors) != 1 or tail.successors[0].address <= tail.address:
            return None
        if any(i.terminator is not None and i.terminator is not tail.terminator for i in tail.instructions):
            return None

        blocks = self.cfg.blocks
        index = blocks.index(tail)

        if index == 0:
            return None

        faller = blocks[index - 1]
        branch = faller.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or faller not in tail.predecessors:
            return None
        if branch.target != tail.successors[0].address or branch.target <= faller.address:
            return None
        if faller.address >= tail.address - 1:
            return None

        # Every other way in is a forward jump onto the tail.
        for pred in tail.predecessors:
            if pred is faller:
                continue
            terminator = pred.terminator
            if not isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                return None
            if terminator.target != tail.address or terminator.target <= pred.address:
                return None

        return faller

    def _give_private_copy(self, faller: BasicBlock, tail: BasicBlock) -> None:
        blocks = self.cfg.blocks
        end = tail.successors[0]

        clone = BasicBlock(max(b.id for b in blocks) + 1, tail.address - 1)

        for instruction in tail.instructions:
            duplicate = copy.copy(instruction)
            # Passes tell writers apart by the identity of the value they hold.
            duplicate.value = copy.deepcopy(instruction.value)
            duplicate.statement = copy.deepcopy(instruction.statement)
            if instruction.terminator is not None:
                duplicate.terminator = copy.copy(instruction.terminator)
            clone.instructions.append(duplicate)

        if tail.instructions and tail.instructions[-1].terminator is tail.terminator:
            clone.terminator = clone.instructions[-1].terminator
        else:
            clone.terminator = TerminatorJump(target=end.address)

        faller.successors = [clone if s is tail else s for s in faller.successors]
        tail.predecessors.remove(faller)
        clone.predecessors.append(faller)
        clone.successors.append(end)
        end.predecessors.append(clone)

        blocks.insert(blocks.index(tail), clone)
