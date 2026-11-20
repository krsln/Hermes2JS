"""Sends an edge that carries a constant straight to the way a lone register test decides it.

    B: r7 = a(x); r5 = r7 > 0; r0 = true; if (r5) goto J     // J has other entries: r0 = h(x) > 0
    J: if (!r0) goto END;                                      // a lone test of r0
    BODY: ...

The `r0 = true` the bytecode loads before the jump is only there for the test at `J`. On this edge the test is
decided, so the jump goes to `BODY` and the load is dropped (`r0` has to be dead on entry to `BODY` and on B's
fall-through). `J` keeps its other entries; `BODY` now has one more way in, which the tail-copy passes and the `if`
structurer see as an ordinary shared tail instead of a value no test can own (96/155 `Pe`: three arms
`r0 = true; if (r5) goto J`).
"""

from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import CFG
from hermes_decompiler.ir.expressions import Identifier, Literal, UnaryExpression
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch
from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass as _Liveness


class ConstantEdgeThreadingCfgPass:
    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        threaded = 0
        joins = []

        for block in list(self.cfg.blocks):
            join = self._thread(block)

            if join is not None:
                threaded += 1
                joins.append(join)

        # A join left with the one block that falls into it is that block's own test again.
        for join in joins:
            self._fuse(join)

        return threaded

    def _fuse(self, join) -> None:
        if len(join.predecessors) != 1 or join not in self.cfg.blocks:
            return

        pred = join.predecessors[0]

        if pred.terminator is not None or pred.successors != [join] or pred is join:
            return

        if any(i.terminator is not None for i in pred.instructions):
            return

        pred.instructions.extend(join.instructions)
        pred.terminator = join.terminator
        pred.successors = list(join.successors)

        for successor in join.successors:
            successor.predecessors = [pred if p is join else p for p in successor.predecessors]

        self.cfg.blocks.remove(join)

    @staticmethod
    def _register_test(condition):
        negated = False

        if isinstance(condition, UnaryExpression) and getattr(condition.operator, "value", None) == "!":
            negated = True
            condition = condition.operand

        if isinstance(condition, Identifier) and condition.name.startswith("r") and condition.name[1:].isdigit():
            return int(condition.name[1:]), negated

        return None

    def _thread(self, block):
        terminator = block.terminator

        if not isinstance(terminator, TerminatorConditionalBranch) or len(block.successors) != 2:
            return None

        join, fall = block.successors

        if join.address != terminator.target or join is fall:
            return None

        # A lone test of one register with other ways in.
        if len(join.predecessors) < 2 or len(join.instructions) != 1:
            return None

        join_branch = join.terminator

        if not isinstance(join_branch, TerminatorConditionalBranch) or len(join.successors) != 2:
            return None

        test = self._register_test(join_branch.condition)

        if test is None:
            return None

        register, negated = test
        loads = [
            i for i in block.instructions
            if i.terminator is None and i.dest_reg == register and isinstance(i.value, Literal) and i.statement is None
        ]

        if not loads:
            return None

        load = loads[-1]
        later = block.instructions[block.instructions.index(load) + 1:]

        if any(i.dest_reg == register for i in later if i.terminator is None):
            return None

        if any(self._reads(i, register) for i in later):
            return None

        if not _Liveness._dead_on_entry(fall, register, set()):
            return None

        taken_of_join = next((s for s in join.successors if s.address == join_branch.target), None)
        fall_of_join = next((s for s in join.successors if s is not taken_of_join), None)

        if taken_of_join is None or fall_of_join is None or taken_of_join is fall_of_join:
            return None

        truthy = bool(load.value.value)
        condition_holds = truthy != negated
        decided = taken_of_join if condition_holds else fall_of_join

        if decided in (block, join) or not _Liveness._dead_on_entry(decided, register, set()):
            return None

        block.instructions.remove(load)

        retargeted = dataclasses.replace(terminator, target=decided.address)
        block.instructions[-1].terminator = retargeted
        block.terminator = retargeted
        block.successors = [decided if s is join else s for s in block.successors]
        join.predecessors.remove(block)
        decided.predecessors.append(block)

        return join

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
