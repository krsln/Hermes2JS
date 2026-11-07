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
from hermes_decompiler.backend.transforms.shared._absorb import substitute_register
from hermes_decompiler.backend.transforms.shared._purity import TRIVIAL_NODE_TYPES
from hermes_decompiler.backend.transforms.shared._structural_key import structural_key
from hermes_decompiler.ir.expressions import Identifier, Literal
from hermes_decompiler.ir.terminators import (
    TerminatorConditionalBranch,
    TerminatorJump,
    TerminatorReturn,
    TerminatorThrow,
)


class SharedReturnDuplicationCfgPass:
    def __init__(self, cfg: CFG, widen: bool = False, statements: bool = False, own_values: bool = False):
        self.cfg = cfg
        # `statements` (with `widen`): the tail may also hold ordinary
        # instructions (`return a === r0` after `r0 = b.v`), not just loads.
        self.statements = widen and statements
        # `widen`: also copy `throw` exits and the closing `return` even when
        # something falls into it (only when every path agrees on the value).
        self.widen = widen
        # `own_values`: a closing `return` the paths disagree on is still copied for the jumpers that set
        # the value themselves. The last resort: earlier levels solve most of these without it.
        self.own_values = own_values
        self._own_value_only: set[BasicBlock] = set()

    def run(self) -> int:
        # A copy sits outside every try range. That is exact for an exit that
        # already lies outside them (96/3900: a `for-of` guards its loop, the
        # early `return`s at the top are nowhere near it); an exit inside a
        # protected range, or a handler's own entry, must stay where it is.
        # Merged fragments leave gaps the table never protected (96/1324: the `close; return []` exits
        # between the pieces of a for-of's range): a block there is not inside the range.
        ordered = sorted(self.cfg.blocks, key=lambda b: b.address)
        ends = {b: (ordered[i + 1].address if i + 1 < len(ordered) else float("inf")) for i, b in enumerate(ordered)}

        def in_range(block, handler) -> bool:
            fragments = handler.get("fragments")
            return not fragments or any(block.address < e and ends[block] > s for s, e in fragments)

        protected = {
            b for handler in self.cfg.exception_handlers
            for b in (
                *(t for t in handler.get("try_blocks", ()) if in_range(t, handler)),
                handler.get("handler_block"),
            )
            if b is not None
        }

        copied = 0

        for block in list(self.cfg.blocks):
            if block in protected or not self._eligible(block):
                continue

            jumpers = [p for p in block.predecessors if self._jumps_to(p, block)]
            fallers = [p for p in block.predecessors if p not in jumpers]

            if block in self._own_value_only:
                # The paths disagree on the value: only the jumpers that set it themselves get a
                # copy, the original stays for everything else.
                jumpers = [p for p in jumpers if self._sets_what_the_tail_reads(p, block)]
                if len(jumpers) == len(block.predecessors):
                    jumpers = jumpers[:-1]

            if not jumpers:
                continue

            if not fallers and block not in self._own_value_only:
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

        # The last rung only runs for functions every earlier one left with a `goto`: a longer tail
        # (`Object.assign(a, { [k]: v }); return` is seven instructions, 98/10767) is worth its copy there,
        # when only jumps reach it. With a fall-through into it the paths may hold different values for what
        # it reads (98/2844: `r4.decodedBodySize = r5` after `r5 = 0` / `r5 = v`).
        # A fall-through is fine too when the tail reads the same thing on every path into it (98/2930
        # `resolve`: `_y = 1; _z = v; finale(p)` is eight instructions, entered by two jumps and the
        # fall-through of the `typeof then` test).
        if (
                self.statements and self.own_values
                and (
                all(self._jumps_to(p, block) for p in block.predecessors)
                or self._reads_the_same_on_every_path(block)
        )
        ):
            limit = self._MAX_TAIL_LAST_RUNG

        # `throw new RangeError("...")` is ten instructions (`CreateThis`, `Construct`,
        # `SelectObject`, ...) but one statement once printed: a shared one is worth copying.
        if self.statements and isinstance(block.terminator, TerminatorThrow):
            limit = self._MAX_THROW
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
            # Only a jumper that sets the value itself can still get a copy (see `run`).
            if not self.own_values:
                return False

            self._own_value_only.add(block)

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
    _MAX_TAIL_LAST_RUNG = 9
    _MAX_THROW = 16

    _REGISTER_NAME = re.compile(r"r(\d+)")

    def _reads_the_same_on_every_path(self, block: BasicBlock) -> bool:
        """Every register the tail reads before writing it has ONE reaching
        value: all paths into the block that define it agree structurally, and no
        path reaches the block with it unset while another sets it."""
        return all(self._single_reaching_value(block, register) for register in self._exposed_registers(block))

    def _exposed_registers(self, block: BasicBlock) -> set[int]:
        """Registers the tail reads before it writes them."""
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

        note(getattr(block.terminator, "value", None))

        return exposed

    def _sets_what_the_tail_reads(self, pred: BasicBlock, block: BasicBlock) -> bool:
        """The jumper writes every register the tail reads, in its own block: its copy returns ITS
        value whatever the other paths hold (96/7556: `r0 = Number(v); jmp RET`)."""
        exposed = self._exposed_registers(block)

        return bool(exposed) and all(
            any(i.dest_reg == register and i.value is not None for i in pred.instructions)
            for register in exposed
        )

    def _single_reaching_value(self, block: BasicBlock, register: int) -> bool:
        seen = {block}
        queue = deque(block.predecessors)
        keys: set = set()
        constants = True
        unset = False
        inside = set()  # try-range blocks: a throw can come from before their last write

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
                constants = constants and isinstance(definition.value, Literal)
                if pred not in inside:
                    continue

            if not pred.predecessors:
                # A handler has no predecessor, but it runs from inside its try range: the register
                # holds there what the range's blocks (and what leads to them) say (98/13178 `listener`:
                # `r0 = undefined` at the entry, the `catch` tail returns it).
                protected = [
                    t for h in self.cfg.exception_handlers if h.get("handler_block") is pred
                    for t in h.get("try_blocks", ())
                ]
                if protected:
                    queue.extend(protected)
                    inside.update(protected)
                else:
                    unset = True
            queue.extend(pred.predecessors)

        # Several DIFFERENT constants are fine: each jumper's copy returns its own (`r0 = false;
        # if (!c) goto RET` is `return false`) and the closing `return r0` keeps the register's name,
        # which every path that reaches it has set (96/11046 `areDependenciesEqual`).
        return (len(keys) <= 1 or constants) and not (keys and unset)

    def _constant_reaching(self, block: BasicBlock, register: int):
        """The one literal every path into `block` leaves in `register`, else None (same walk as
        `_single_reaching_value`, through a handler into its try range)."""
        seen = {block}
        queue = deque(block.predecessors)
        found = None
        inside = set()

        while queue:
            pred = queue.popleft()
            if pred in seen:
                continue
            seen.add(pred)

            definition = next((i for i in reversed(pred.instructions) if i.dest_reg == register), None)

            if definition is not None:
                # Only a plain constant load counts: a `Mov` join can print a literal it took from one arm
                # (98/2477: `r1 = null` seen through `Mov r1, r2`).
                if not definition.entry.opcode.startswith("LoadConst") or not isinstance(definition.value, Literal):
                    return None
                if found is not None and structural_key(found) != structural_key(definition.value):
                    return None
                found = definition.value
                if pred not in inside:
                    continue

            if not pred.predecessors:
                protected = [
                    t for h in self.cfg.exception_handlers if h.get("handler_block") is pred
                    for t in h.get("try_blocks", ())
                ]
                if not protected:
                    return None
                queue.extend(protected)
                inside.update(protected)
            queue.extend(pred.predecessors)

        return found

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

    @staticmethod
    def _say_the_value(block: BasicBlock, name: str, constant) -> None:
        for instruction in block.instructions:
            instruction.value = substitute_register(instruction.value, name, copy.deepcopy(constant))
            instruction.statement = substitute_register(instruction.statement, name, copy.deepcopy(constant))
            terminator = instruction.terminator
            if terminator is not None and getattr(terminator, "value", None) is not None:
                instruction.terminator = dataclasses.replace(
                    terminator, value=substitute_register(terminator.value, name, copy.deepcopy(constant))
                )
        block.terminator = block.instructions[-1].terminator

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

        if self.cfg.exception_handlers:
            # The register's definition may print nowhere (`r0 = undefined` at the entry): the copy
            # and the original say the value instead of naming it (98/2647: `return r0` after a `catch`).
            for register in self._exposed_registers(block):
                constant = self._constant_reaching(block, register)
                if constant is None:
                    continue
                for target in (clone, block):
                    self._say_the_value(target, f"r{register}", constant)
                clone.terminator = clone.instructions[-1].terminator

        if isinstance(pred.terminator, TerminatorJump):
            # A plain `jmp` to the shared return IS the return: put the copy in the jumper
            # itself (96/6731: the exit of a `try` body, which nothing places a separate
            # block after).
            pred.instructions = [i for i in pred.instructions if i.terminator is not pred.terminator]
            pred.instructions.extend(clone.instructions)
            pred.terminator = clone.terminator
            pred.successors = [s for s in pred.successors if s is not block]
            block.predecessors.remove(pred)

            return

        retargeted = dataclasses.replace(pred.terminator, target=new_address)
        for instruction in pred.instructions:
            if instruction.terminator is pred.terminator:
                instruction.terminator = retargeted
        pred.terminator = retargeted

        pred.successors = [clone if s is block else s for s in pred.successors]
        block.predecessors.remove(pred)
        clone.predecessors.append(pred)
        blocks.append(clone)
