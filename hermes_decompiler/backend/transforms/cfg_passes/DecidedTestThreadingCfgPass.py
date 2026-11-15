"""
Skips a register test the way in already decided.

A tail copy (`SharedTailDuplicationCfgPass`) gives each way in its own run of blocks, and the
second test of the copy tests the very register the first test of the way decided:

    P: if (!r10) goto B;      // falls through here: r10 is truthy
    Q: if (!r11) goto C;
    D: r3 = 1; if (!r10) goto E;   // can only fall through: the copy's own `r10` test

The test is replaced by the jump it must take. The way in is the chain of blocks that each have ONE
predecessor, so the decided test is found without any data-flow: back from the test along the chain until a
conditional branch on the same register, with no write of that register in between.
"""

from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import CFG
from hermes_decompiler.ir.expressions import Identifier, UnaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump


class DecidedTestThreadingCfgPass:
    _MAX_CHAIN = 8

    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        # A catch entry has no predecessor and a try range hides edges: left alone.
        if self.cfg.exception_handlers:
            return 0

        threaded = 0

        for block in list(self.cfg.blocks):
            if self._thread(block):
                threaded += 1

        if threaded:
            self._drop_orphans()

        return threaded

    @staticmethod
    def _register_test(condition):
        """`(register, negated)` for `rN` / `!rN`, else None."""
        negated = False

        if isinstance(condition, UnaryExpression) and getattr(condition.operator, "value", None) == "!":
            negated = True
            condition = condition.operand

        if isinstance(condition, Identifier) and condition.name.startswith("r") and condition.name[1:].isdigit():
            return int(condition.name[1:]), negated

        return None

    def _thread(self, block) -> bool:
        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or len(block.successors) != 2:
            return False

        test = self._register_test(branch.condition)

        if test is None:
            return False

        register, negated = test

        if any(i.dest_reg == register for i in block.instructions):
            return False

        known = self._known_truth(block, register, negated)

        if known is None:
            return False

        taken = next((s for s in block.successors if s.address == branch.target), None)
        other = next((s for s in block.successors if s is not taken), None)

        if taken is None or other is None or taken is other:
            return False

        kept, dead = (taken, other) if known else (other, taken)

        if self._strands_a_reader(block, dead):
            return False

        jump = TerminatorJump(target=kept.address)

        for instruction in block.instructions:
            if instruction.terminator is branch:
                instruction.terminator = jump

        block.terminator = jump
        block.successors = [kept]
        dead.predecessors.remove(block)

        return True

    def _strands_a_reader(self, block, dead) -> bool:
        """Would dropping the edge leave blocks nobody enters, while a block that stays holds a value
        the dropped ones hold too? Such a reader got its value from the dropped path (`r1 = r3` carrying the
        `-1` the dropped arm wrote): the merge that repaired it is gone and the stale value would print."""
        reached = {self.cfg.blocks[0]}
        todo = [self.cfg.blocks[0]]

        while todo:
            current = todo.pop()

            for successor in current.successors:
                if current is block and successor is dead:
                    continue

                if successor not in reached:
                    reached.add(successor)
                    todo.append(successor)

        orphans = [b for b in self.cfg.blocks if b not in reached]

        if not orphans:
            return False

        held = {id(i.value) for b in orphans for i in b.instructions if i.value is not None}

        return any(
            id(i.value) in held for b in self.cfg.blocks if b in reached for i in b.instructions
            if i.value is not None
        )

    def _known_truth(self, block, register: int, negated: bool):
        """Is `rN` (as `block` tests it) known to be true / false on the unique way in?"""
        current = block

        for _ in range(self._MAX_CHAIN):
            if len(current.predecessors) != 1:
                return None

            pred = current.predecessors[0]

            if pred is current:
                return None

            branch = pred.terminator

            if isinstance(branch, TerminatorConditionalBranch):
                test = self._register_test(branch.condition)

                if test is not None and test[0] == register:
                    if pred.successors.count(current) != 1 or len(pred.successors) != 2:
                        return None

                    on_taken = current.address == branch.target
                    pred_true = on_taken  # the branch's own condition holds when it is taken
                    # `pred` tests `rN` as `test[1]`, this block as `negated`.
                    value_true = pred_true != test[1]  # truthiness of rN

                    return value_true != negated

            # Another test, or a plain block: the way in runs on through it when it leaves `rN` alone.
            if any(i.dest_reg == register for i in pred.instructions):
                return None

            current = pred

        return None

    def _drop_orphans(self) -> None:
        blocks = self.cfg.blocks
        entry = blocks[0]
        changed = True

        while changed:
            changed = False

            for block in list(blocks):
                if block is not entry and not block.predecessors:
                    for successor in block.successors:
                        if block in successor.predecessors:
                            successor.predecessors.remove(block)

                    blocks.remove(block)
                    changed = True
