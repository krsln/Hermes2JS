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
import re
from collections import deque

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.shared._purity import TRIVIAL_NODE_TYPES
from hermes_decompiler.backend.transforms.shared._structural_key import structural_key
from hermes_decompiler.ir.expressions import Identifier
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
    TerminatorThrow,
)


class SharedReturnDuplicationCfgPass:
    def __init__(self, cfg: CFG, widen: bool = False, statements: bool = False):
        self.cfg = cfg
        # `statements` (with `widen`): the tail may also hold ordinary
        # instructions (`return a === r0` after `r0 = b.v`), not just loads.
        self.statements = widen and statements
        # `widen`: also copy `throw` exits and the closing `return` even when
        # something falls into it (only when every path agrees on the value).
        self.widen = widen

    def run(self) -> int:
        # A copy sits outside every try range. That is exact for an exit that
        # already lies outside them (96/3900: a `for-of` guards its loop, the
        # early `return`s at the top are nowhere near it); an exit inside a
        # protected range, or a handler's own entry, must stay where it is.
        protected = {
            b for handler in self.cfg.exception_handlers
            for b in (*handler.get("try_blocks", ()), handler.get("handler_block"))
            if b is not None
        }

        copied = 0

        for block in list(self.cfg.blocks):
            if block in protected or not self._eligible(block):
                continue

            jumpers = [p for p in block.predecessors if self._jumps_to(p, block)]
            fallers = [p for p in block.predecessors if p not in jumpers]

            if not jumpers:
                continue

            if not fallers:
                # Only jumps reach it (`a === 1 || a === 2` chains ending in
                # `return true`): the last jumper keeps the original.
                if len(jumpers) < 2:
                    continue
                jumpers = jumpers[:-1]

            for pred in jumpers:
                self._give_private_copy(pred, block)
                copied += 1

        if copied:
            self.cfg.duplicated_returns = True

        return copied

    def _eligible(self, block: BasicBlock) -> bool:
        exits = (TerminatorReturn, TerminatorThrow) if self.widen else (TerminatorReturn,)
        if not isinstance(block.terminator, exits):
            return False

        limit = self._MAX_TAIL if self.statements else self._MAX_LEAD + 1
        if len(block.instructions) > limit or len(block.predecessors) < 2:
            return False

        # `r0 = false; return r0` is as much a lone return as `return r0`:
        # only constant loads / copies may lead up to the terminator.
        if not all(
                self._is_plain_load(i) or (self.statements and self._is_copyable(i))
                for i in block.instructions[:-1]
        ):
            return False

        # A widened copy is only exact when the tail reads the same thing on
        # every path into it: `return r0` after `r0 = true` on one path and
        # `r0 = false` on another is not one value, and once each jumper has its
        # own `return` the final one no longer says which it was (96/11046
        # returned `false` for an equal list).
        if (self.widen or self.cfg.exception_handlers) and not self._reads_the_same_on_every_path(block):
            return False

        if self.widen:
            # Also the function's closing `return`, even with a fall-through
            # into it: the jumpers get their own, the original stays.
            return True

        # The function's closing `return` is joined by everything; leave it
        # unless nothing falls into it (decided in `run`).
        return (
                any(other.address > block.address for other in self.cfg.blocks)
                or not any(p not in block.predecessors or not self._jumps_to(p, block) for p in block.predecessors)
        )

    _MAX_LEAD = 2
    _MAX_TAIL = 6

    _REGISTER_NAME = re.compile(r"r(\d+)")

    def _reads_the_same_on_every_path(self, block: BasicBlock) -> bool:
        """Every register the tail reads before writing it has ONE reaching
        value: all paths into the block that define it agree structurally, and no
        path reaches the block with it unset while another sets it."""
        written: set[int] = set()
        exposed: set[int] = set()

        def note(node) -> None:
            if node is None:
                return
            for part in node.walk():
                if isinstance(part, Identifier):
                    match = self._REGISTER_NAME.fullmatch(part.name)
                    if match and int(match.group(1)) not in written:
                        exposed.add(int(match.group(1)))

        for instruction in block.instructions:
            note(instruction.value)
            note(instruction.statement)
            if instruction.dest_reg is not None:
                written.add(instruction.dest_reg)

        terminator = block.terminator
        note(getattr(terminator, "value", None))

        return all(self._single_reaching_value(block, register) for register in exposed)

    @staticmethod
    def _single_reaching_value(block: BasicBlock, register: int) -> bool:
        seen = {block}
        queue = deque(block.predecessors)
        keys: set = set()
        unset = False

        while queue:
            pred = queue.popleft()
            if pred in seen:
                continue
            seen.add(pred)

            definition = next(
                (i for i in reversed(pred.instructions) if i.dest_reg == register and i.value is not None),
                None,
            )

            if definition is not None:
                keys.add(structural_key(definition.value))
                continue

            if not pred.predecessors:
                unset = True
            queue.extend(pred.predecessors)

        return len(keys) <= 1 and not (keys and unset)

    @staticmethod
    def _is_copyable(instruction) -> bool:
        """An ordinary instruction (no control transfer of its own)."""
        return instruction.terminator is None and (instruction.value is not None or instruction.statement is not None)

    @staticmethod
    def _is_plain_load(instruction) -> bool:
        return (
                instruction.terminator is None
                and instruction.value is not None
                and isinstance(instruction.value, TRIVIAL_NODE_TYPES)
        )

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
            # Passes tell writers apart by the identity of the value they
            # hold: a copy sharing the node is folded together with the
            # original (96/12456: `r1 = []` vanished from the copy).
            duplicate.value = copy.deepcopy(instruction.value)
            duplicate.statement = copy.deepcopy(instruction.statement)
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
