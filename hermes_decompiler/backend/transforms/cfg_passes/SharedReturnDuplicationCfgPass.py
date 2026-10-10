"""
Gives every jump that lands on a mid-function `return` its own copy of it.

Hermes shares one `return x` block between early exits that sit in
different `if` arms: one reaches it by jumping, another by falling through
into it. Neither arm owns it, so `IfStructurer` hands it to the first
branch and leaves the other test without its exit (`goto label_N`).

    if (!a) goto R;          // R: return p
    ...
    if (b) goto T;           // falls through into R
    R: return p
    T: ...

The jumpers get a private copy placed after the last block; the block the
code falls into keeps its place. Only a lone `return`/`throw` block is
copied, only when it is reached both by a jump and by a fallthrough, and
never in a function with exception handlers (a copy sits outside every
try range).
"""

from __future__ import annotations

import copy
import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
)


class SharedReturnDuplicationCfgPass:
    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        copied = 0

        for block in list(self.cfg.blocks):
            if not self._eligible(block):
                continue

            jumpers = [p for p in block.predecessors if self._jumps_to(p, block)]
            fallers = [p for p in block.predecessors if p not in jumpers]

            if not jumpers or not fallers:
                continue

            for pred in jumpers:
                self._give_private_copy(pred, block)
                copied += 1

        if copied:
            self.cfg.duplicated_returns = True

        return copied

    def _eligible(self, block: BasicBlock) -> bool:
        if not isinstance(block.terminator, TerminatorReturn):
            return False
        if len(block.instructions) != 1 or len(block.predecessors) < 2:
            return False
        # The function's closing `return` is joined by everything; leave it.
        return any(other.address > block.address for other in self.cfg.blocks)

    @staticmethod
    def _jumps_to(pred: BasicBlock, block: BasicBlock) -> bool:
        terminator = pred.terminator
        if isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
            return terminator.target == block.address
        return False

    def _give_private_copy(self, pred: BasicBlock, block: BasicBlock) -> None:
        blocks = self.cfg.blocks
        new_id = max(b.id for b in blocks) + 1
        new_address = max(b.address for b in blocks) + 1

        clone = BasicBlock(new_id, new_address)
        for instruction in block.instructions:
            duplicate = copy.copy(instruction)
            if instruction.terminator is not None:
                duplicate.terminator = copy.copy(instruction.terminator)
            clone.instructions.append(duplicate)
        clone.terminator = clone.instructions[-1].terminator

        retargeted = dataclasses.replace(pred.terminator, target=new_address)
        for instruction in pred.instructions:
            if instruction.terminator is pred.terminator:
                instruction.terminator = retargeted
        pred.terminator = retargeted

        pred.successors = [clone if s is block else s for s in pred.successors]
        block.predecessors.remove(pred)
        clone.predecessors.append(pred)
        blocks.append(clone)
