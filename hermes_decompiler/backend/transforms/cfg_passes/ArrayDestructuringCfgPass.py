"""
Collapses Hermes's open-coded array-destructuring iterator protocol into
one `[a, b] = source` statement.

`[a, b] = src` compiles (Hermes `IteratorBegin`/`IteratorNext`/
`IteratorClose`, each `IteratorNext` also writing `undefined` into the
iterator register once the iterator is done) to a fixed chain of tiny
blocks. For two elements::

    H:   ...; IteratorBegin it, src
         [Mov t <- src]; IteratorNext v1, it, t
         Mov x <- it; StrictEq f <- (x === undefined)
         LoadConstUndefined e1; JmpTrue f -> H2
    A1:  Mov e1 <- v1
    H2:  LoadConstUndefined e2; JmpTrue f -> CC          # element k >= 2
    N2:  IteratorNext v2, it, t2; Mov y <- it
         StrictEq f2 <- (y === undefined); LoadConstUndefined e2
         Mov f <- f2; JmpTrue f2 -> CC
    A2:  Mov e2 <- v2; Mov f <- f2
    CC:  JmpTrue f -> J                                  # close check
    CL:  IteratorClose it
    J:   ...

Read as a whole this is `e1 = v1 ?? undefined; e2 = ...; close()` - i.e.
exactly array destructuring - but every piece is a separate diamond that
no structurer can read back as one thing, so the output was a pile of
`if (rIt !== undefined)` guards around `rIt.next()`.

Only the flat form is handled: every target is a plain register and
there is no exception handler around the chain. Targets that can throw
(member / nested-pattern targets) and rest elements put a try/catch
around the chain and are left alone.
"""

from __future__ import annotations

import copy
import dataclasses
from dataclasses import dataclass

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.cfg_passes._generator_dispatch import _operands
from hermes_decompiler.backend.transforms.shared._repoint import _repoint_terminator, repoint_node
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import ArrayExpression, AssignmentExpression, CallExpression, Identifier, \
    MemberExpression, NumericLiteral
from hermes_decompiler.ir.expressions.Collections import ArrayHole, ObjectExpression, ObjectProperty, SpreadElement
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.terminators import TerminatorJump

logger = get_logger(__name__)

_JMP_TRUE = ("JmpTrue", "JmpTrueLong")


def _handlers(block: BasicBlock) -> list[str]:
    return [instruction.handler for instruction in block.instructions]


def _taken_fall(block: BasicBlock):
    """(taken, fallthrough) of a conditional block, or None."""
    if len(block.successors) != 2:
        return None

    return block.successors[0], block.successors[1]


def _only_successor(block: BasicBlock) -> BasicBlock | None:
    return block.successors[0] if len(block.successors) == 1 else None


class ArrayDestructuringCfgPass:
    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self._env_names: frozenset = frozenset()  # ids of environment slot expressions

    def _environment_stores(self) -> frozenset:
        """Ids of the slot expressions the environment stores write: a member of an environment that a
        `StoreToEnvironment` names is a plain variable slot, whichever register holds the environment
        (98/13030: `r4 = createEnvironment(); ... r4[0] = r6`)."""
        return frozenset(
            id(instr.value.left)
            for block in self.cfg.blocks
            for instr in block.instructions
            if instr.handler == "StoreToEnvironment" and isinstance(instr.value, AssignmentExpression)
        )

    def run(self) -> int:
        applied = 0
        self._env_names = self._environment_stores()

        for block in list(self.cfg.blocks):
            if block not in self.cfg.blocks:
                continue

            for index, instruction in enumerate(block.instructions):
                if instruction.handler != "IteratorBegin":
                    continue

                match = self._match(block, index)

                if match is not None:
                    self._apply(block, index, match)
                    applied += 1

                break

        return applied

    # ------------------------------------------------------------------
    # Recognition
    # ------------------------------------------------------------------

    def _match(self, head: BasicBlock, begin_index: int):
        """
        Returns (items, drop_blocks, join, kept_undefined, removed_handlers,
        cleanup_blocks) or None.

        `items` is the pattern tree: plain targets, holes, nested patterns
        and a trailing rest element (see `_Elem`).
        """
        ctx = _Ctx(head)
        parsed = self._parse(head, begin_index, ctx, top=True)

        if parsed is None:
            return None

        items, join, kept_undefined = parsed

        drop: list[BasicBlock] = []
        seen_ids: set[int] = set()

        for block in ctx.drop:
            if block is not head and block.id not in seen_ids:
                seen_ids.add(block.id)
                drop.append(block)

        dropped_ids = set(seen_ids)

        # The chain must be single-entry: nothing outside it jumps in.
        for block in drop:
            for predecessor in block.predecessors:
                if predecessor is not head and predecessor.id not in dropped_ids:
                    return None

        handlers = self._plan_handlers(head, ctx, dropped_ids)

        if handlers is None:
            return None

        removed_handlers, cleanup = handlers

        leaves = [leaf.reg for leaf in _leaves(items)]

        if len(set(leaves)) != len(leaves):
            return None

        # The temporary an object pattern was read from is not assigned any more: nothing after the
        # pattern may still read it.
        # A register that is still read afterwards (a closure variable also kept in a register) is
        # restored from the environment slot the element was stored into: a slot is a plain variable, so
        # reading it back yields the stored value. Any other target would be read twice, so it declines.
        slots = {item.temp: item.default for item in _targets(items) if _is_env_slot(item.default, self._env_names)}
        restores: dict[int, object] = {}

        # An element stored into an environment slot fetched its value into a register that a LATER element
        # then takes as its own target (98/9949: `[__environment__[0], r5] = x`): that register ends up holding
        # the later element, so there is nothing of the first to restore.
        superseded = {
            item.temp
            for position, item in enumerate(items)
            if item.kind == "target"
            for later in items[position + 1:]
            if later.kind in ("reg", "rest") and later.reg == item.temp
        }

        for temp in _object_temps(items):
            if temp in superseded:
                continue

            if temp in leaves:
                return None

            if not self._dead_after(join, temp, dropped_ids):
                if any(register == temp for register, _ in ctx.slot_copies):
                    continue  # the last property was read into it: restored below like any slot copy

                if temp not in slots:
                    return None

                restores[temp] = slots[temp]

        # The temporaries of an object rest are gone; a register that kept a slot's value is restored from it.
        for register in ctx.scratch:
            if register in leaves or not self._dead_after(join, register, dropped_ids):
                return None

        for register, slot in ctx.slot_copies:
            if register not in leaves and not self._dead_after(join, register, dropped_ids):
                restores[register] = slot

        # A store that read the fetch register itself leaves no copy of the value behind (98/3759).
        # A later slot element that ends up in that very register leaves it holding the later element
        # (98/13030: `[r4[0], r4[1]] = x`, both fetched through r7), restored with its own slot below.
        later_targets = {item.temp for item in items[1:] if item.kind == "target"}

        for register, slot in ctx.fetched:
            if register in later_targets:
                continue

            if register not in leaves and not self._dead_after(join, register, dropped_ids):
                if not _is_env_slot(slot, self._env_names):
                    return None

                restores[register] = slot

        # A moved creation writes its register before the chain: nothing the pattern keeps may live there.
        for created in ctx.hoist:
            kept = {*leaves, *(t for t, _ in ((r, None) for r in _object_temps(items))), *(r for r, _ in ctx.fetched)}
            if created.dest_reg in kept:
                return None

        return items, drop, join, kept_undefined, removed_handlers, cleanup, restores, ctx.hoist

    def _match_object_rest(self, insts, source: int, ctx):
        """`{ a, ...rest }` after the property reads of an object pattern.

            NewObject A; LoadConstNull N; NewObjectWithBufferAndParent B (`Object.setPrototypeOf({keys}, null)`)
            Mov C <- source; CallBuiltin D = copyDataProperties(A, C, B); [Mov X <- D]...; [slot = D]

        Returns ((slot or None, register or None, result instruction or None), the instructions after it) or
        None. The temporaries A, N, B, C are dead after the pattern (checked in `_match`); the registers that
        keep the rest value are restored from the slot, or - without a slot - the rest is the register D."""
        if len(insts) < 5 or [i.handler for i in insts[:5]] != [
            "NewObject", "LoadConstNull", "NewObjectWithBufferAndParent", "Mov", "CallBuiltin"
        ]:
            return None

        new, null, keys, copy_of, call = insts[:5]
        value = call.value

        if not (
                isinstance(value, CallExpression) and isinstance(value.callee, Identifier)
                and value.callee.name == "copyDataProperties" and len(value.arguments) == 3
                and all(isinstance(a, Identifier) for a in value.arguments)
                and [a.name for a in value.arguments] == [f"r{new.dest_reg}", f"r{copy_of.dest_reg}",
                                                          f"r{keys.dest_reg}"]
                and isinstance(copy_of.value, Identifier) and copy_of.value.name == f"r{source}"
                and isinstance(call.dest_reg, int)
        ):
            return None

        rest_reg = call.dest_reg
        copies = []
        later = insts[5:]

        while later and later[0].handler == "Mov" and isinstance(later[0].value, Identifier) \
                and later[0].value.name == f"r{rest_reg}" and isinstance(later[0].dest_reg, int):
            copies.append(later[0].dest_reg)
            later = later[1:]

        scratch = [new.dest_reg, null.dest_reg, keys.dest_reg, copy_of.dest_reg]
        store = _plain_store(later[0], rest_reg) if later else None

        if store is not None and _is_env_slot(store, self._env_names):
            ctx.scratch.extend(scratch)
            ctx.slot_copies.extend((r, store) for r in (rest_reg, *copies))

            return (store, None, None), later[1:]

        if store is None and not copies:
            ctx.scratch.extend(scratch)

            return (None, rest_reg, call), later

        return None

    def _dead_after(self, start: BasicBlock, register: int, dropped_ids: set[int]) -> bool:
        """True if no path from `start` reads `register` before writing it."""
        name = f"r{register}"
        seen: set[int] = set()
        stack = [start]

        while stack:
            block = stack.pop()

            if block.id in seen or block.id in dropped_ids:
                continue

            seen.add(block.id)
            written = False

            for instruction in block.instructions:
                if _reads_name(instruction, name):
                    return False

                if instruction.dest_reg == register:
                    written = True
                    break

            if not written:
                stack.extend(block.successors)

            if block.terminator is not None and _reads_name(block.terminator, name):
                return False

        return True

    def _plan_handlers(self, head: BasicBlock, ctx: "_Ctx", dropped_ids: set[int]):
        """
        Decides which exception handlers go away with the collapsed pattern.

        Returns (removed_handlers, cleanup_blocks) or None when a handler
        cuts through the pattern.

        The iterator cleanup handlers (`Catch; ...; IteratorClose it, 1;
        Throw`) go: they guard whatever can throw between two `next()` calls
        (a nested pattern, a default value, the rest loop). A surrounding try
        merely loses the dropped blocks from its range - but only if it
        covers the whole pattern.
        """
        removed: list = []
        remaining: list = []
        chain: dict[int, BasicBlock] = {}

        for handler in self.cfg.exception_handlers:
            hb = handler["handler_block"]
            covered = {b.id for b in handler["try_blocks"]}

            if hb.id in dropped_ids:
                return None

            if covered and covered <= dropped_ids:
                blocks = _cleanup_chain(hb, ctx.iterators)

                if blocks is not None:
                    removed.append(handler)
                    chain.update({b.id: b for b in blocks})
                    continue

            remaining.append(handler)

        if chain:
            remaining_handler_blocks = {h["handler_block"].id for h in remaining}
            entry = self.cfg.blocks[0] if self.cfg.blocks else None

            # Dead catch blocks that only feed the cleanup (no handler entry
            # points at them any more) go with it.
            for block in self.cfg.blocks:
                if (
                        block.id in dropped_ids or block.id in chain or block is entry
                        or block.id in remaining_handler_blocks or block.predecessors
                        or not block.instructions or block.instructions[0].handler != "Catch"
                        or not _cleanup_vocabulary(block, ctx.iterators)
                ):
                    continue

                if all(s.id in chain for s in block.successors):
                    chain[block.id] = block

            for block in chain.values():
                if any(p.id not in chain for p in block.predecessors):
                    return None

            still: list = []

            for handler in remaining:
                covered = {b.id for b in handler["try_blocks"]}

                if handler["handler_block"].id in chain and covered <= dropped_ids | set(chain):
                    removed.append(handler)
                else:
                    still.append(handler)

            remaining = still

        # A chain inside a try (a for-of body, say) is fine as long as the
        # try covers all of it: the dropped blocks just leave the handler's
        # list. A try that starts or ends inside the chain is not.
        for handler in remaining:
            covered = {b.id for b in handler["try_blocks"]}
            inside = dropped_ids & covered

            if inside and (inside != dropped_ids or head.id not in covered):
                return None

            if not inside and head.id in covered:
                return None

        return removed, list(chain.values())

    def _parse(self, head: BasicBlock, begin_index: int, ctx: "_Ctx", top: bool):
        """
        Parses one pattern whose `IteratorBegin` sits at `head.instructions[begin_index]`.

        Returns (items, join, kept_undefined) or None. Every block that is
        part of the pattern is appended to `ctx.drop` (the top head stays).

        Element k >= 2 starts at a boundary block::

            [Mov target <- previous]          # peeled binding of element k-1
            [LoadConstUndefined ek]           # absent for a hole
            [Mov copy <- done]*; JmpTrue done -> next boundary

        and is followed by either the fetch-and-assign diamond, or (hole)
        just the fetch. The running "done" flag changes register between
        elements, so it is tracked as a set of aliases.
        """
        begin = head.instructions[begin_index]
        begin_ops = _operands(begin)

        if len(begin_ops) != 2:
            return None

        it, src = begin_ops
        ctx.iterators.add(it)
        tail = head.instructions[begin_index + 1:]

        # [Mov t <- src], IteratorNext, Mov x <- it, StrictEq, LoadConstUndefined, JmpTrue
        shapes = [i.handler for i in tail]
        expected = ["Mov", "IteratorNext", "Mov", "StrictEq", "LoadConstUndefined", "JmpTrue"]

        # The `undefined` StrictEq compares against is loaded right here
        # unless an earlier block already holds it; that load outlives the
        # chain (the function's own `return undefined` often reads it).
        kept_undefined = None
        # The load is only the `undefined` the checks compare with; it is no element's initial value.
        shared_undefined = False

        if top and shapes == ["Mov", "IteratorNext", "Mov", "LoadConstUndefined", *expected[3:]]:
            kept_undefined = tail[3]
            tail = tail[:3] + tail[4:]
        elif shapes == ["LoadConstUndefined", "Mov", "IteratorNext", "Mov", "StrictEq", "JmpTrue"]:
            # An element with a default loads its `undefined` first.
            tail = [*tail[1:5], tail[0], tail[5]]
        elif top and shapes == ["LoadConstUndefined", "LoadConstUndefined", "Mov", "IteratorNext", "Mov", "StrictEq",
                                "JmpTrue"]:
            # A later element has a default: the `undefined` the checks compare with is loaded ahead of
            # everything (it outlives the chain, like the mid-check load), then comes element 1's own.
            kept_undefined = tail[0]
            tail = [*tail[2:6], tail[1], tail[6]]
        elif top and shapes == ["IteratorNext", "Mov", "LoadConstUndefined", *expected[3:]]:
            # Both: the source needs no copy, and the `undefined` is loaded in the middle of the check.
            kept_undefined = tail[2]
            tail = [None, *tail[:2], *tail[3:]]
        elif top and shapes == ["IteratorNext", "Mov", "LoadConstUndefined", "StrictEq", "JmpTrue"]:
            # A single element: the one `undefined` is both what the check compares with and the element's
            # own initial value, and the source needs no copy (98/9900).
            kept_undefined = tail[2]
            tail = [None, tail[0], tail[1], tail[3], tail[2], tail[4]]
        elif top and shapes == ["Mov", "IteratorNext", "Mov", "LoadConstUndefined", "StrictEq", "JmpTrue"]:
            # The same one `undefined`, loaded between the fetch and the check, with the source copied first
            # (a leading hole: `[, a, b] = x`, 98/7996).
            kept_undefined = tail[3]
            tail = [tail[0], tail[1], tail[2], tail[4], tail[3], tail[5]]
            shared_undefined = True
        elif shapes == expected[1:]:
            # The fetch reads the source register itself (it already holds it): no `Mov t <- src`.
            tail = [None, *tail]
        elif shapes != expected:
            return None

        mov_t, nxt, mov_x, eq, undef_e, jmp = tail
        t = _operands(mov_t) if mov_t is not None else [src, src]
        n = _operands(nxt)
        x = _operands(mov_x)
        e = _operands(eq)
        u = _operands(undef_e)
        j = _operands(jmp)

        if len(t) != 2 or len(n) != 3 or len(x) != 2 or len(e) != 3 or len(u) != 1 or len(j) != 2:
            return None

        t_reg, t_src = t
        v1, n_it, n_t = n
        x_reg, x_it = x
        flag, eq_x, undef_reg = e
        e1 = u[0]

        if t_src != src or n_it != it or n_t != t_reg or x_it != it or eq_x != x_reg or j[1] != flag:
            return None

        branch = _taken_fall(head)
        if branch is None:
            return None

        taken, fall = branch
        aliases = {flag}
        items: list[_Elem] = []

        if shared_undefined and (_handlers(fall) == ["Mov", "JStrictNotEqual"] or (
                _handlers(fall) == ["Mov"] and _operands(fall.instructions[0]) == [e1, v1])):
            return None

        if _handlers(fall) == ["Mov", "JStrictNotEqual"]:
            # Element 1 with a default: the done path goes straight to the
            # default; otherwise `Mov e1 <- v1; if (v1 !== undefined) skip`.
            mov_ops, cmp_ops = _operands(fall.instructions[0]), _operands(fall.instructions[1])
            cmp_branch = _taken_fall(fall)

            if mov_ops != [e1, v1] or len(cmp_ops) != 3 or cmp_ops[1:] != [v1, undef_reg] or cmp_branch is None:
                return None

            after, default_block = cmp_branch

            if default_block is not taken:
                return None

            default = self._default_value(default_block, e1, after, aliases)

            if default is None:
                return None

            items.append(_Elem("reg", e1, fall.instructions[0], default=default))
            ctx.drop.extend([fall, default_block])
            prev_tmp = e1
            cur_block, cur_insts = after, list(after.instructions)
        elif _handlers(fall) == ["Mov"] and _operands(fall.instructions[0]) == [e1, v1]:
            # A1: Mov e1 <- v1
            if _only_successor(fall) is not taken:
                return None

            items.append(_Elem("reg", e1, fall.instructions[0]))
            ctx.drop.append(fall)
            prev_tmp = e1
            cur_block, cur_insts = taken, list(taken.instructions)
        else:
            # Element 1 is a hole: this block's tail is element 2's head.
            items.append(_Elem("hole"))
            prev_tmp = None
            cur_block, cur_insts = head, [jmp] if shared_undefined else [undef_e, jmp]

        # Element 1's copy `Mov e1 <- v1` may be folded away, the store then reads v1 itself.
        first_value = v1
        seen: set[int] = set()

        while True:
            if id(cur_block) in seen:
                return None

            seen.add(id(cur_block))
            insts = list(cur_insts)
            peeled = None

            # Binding patterns whose targets are all copied at the very end (`[x, y, z] = ...` into outer
            # variables, 98/11846 and 98/13553): the last block holds `Mov target <- tmp` for every element,
            # last element first, and the close block repeats them after the `IteratorClose`.
            if prev_tmp is not None and ctx.peeled_form is not True and not ctx.late:
                late = self._late_copies(insts, items)

                if late is not None:
                    ctx.late = late
                    insts = insts[:len(insts) - 1 - len(late)] + insts[-1:]

                    for leaf, mov in zip([i for i in items if i.kind == "reg"], reversed(late)):
                        leaf.reg = _operands(mov)[0]
                        leaf.result = mov

                    ctx.peeled_form = False

            # Binding patterns (`const [a, b] = x`, `for (const [k, v] of m)`)
            # fill temporaries and copy each into its target at the next
            # element boundary: `Mov target <- tmp` leads that block. All
            # elements must agree on which of the two forms is used.
            if prev_tmp is not None and insts and insts[0].handler == "Mov":
                ops = _operands(insts[0])

                if len(ops) == 2 and ops[1] == prev_tmp and ops[0] != prev_tmp:
                    peeled = insts[0]
                    insts = insts[1:]

            # A nested pattern: the element's value is the new source.
            if prev_tmp is not None and insts and insts[0].handler == "IteratorBegin":
                ops = _operands(insts[0])
                wanted = _operands(peeled)[0] if peeled is not None else prev_tmp

                if len(ops) != 2 or ops[1] != wanted or cur_block is ctx.top:
                    return None

                if peeled is not None:
                    if ctx.peeled_form is False:
                        return None

                    ctx.peeled_form = True

                ctx.drop.append(cur_block)
                sub = self._parse(cur_block, len(cur_block.instructions) - len(insts), ctx, top=False)

                if sub is None:
                    return None

                sub_items, sub_join, _ = sub

                items[-1] = _Elem("nested", items=sub_items)
                prev_tmp = None
                cur_block, cur_insts = sub_join, list(sub_join.instructions)
                continue

            # An object pattern as the element's target (`[{ a, b }, c] = src`): the element value is
            # read by plain property loads before the next fetch, in the order the pattern runs them.
            if peeled is None and prev_tmp is not None and items and items[-1].kind == "reg" \
                    and items[-1].default is None and items[-1].reg == prev_tmp:
                props = []

                while insts:
                    read = _property_read(insts[0], prev_tmp, allow_self=True)

                    if read is None:
                        break

                    leaf = _Elem("reg", insts[0].dest_reg, insts[0])
                    self_read = insts[0].dest_reg == prev_tmp
                    insts = insts[1:]

                    # A closure variable is also kept in its own register: `rA = leaf` sits between the read and the
                    # store of the slot (98/6599). The copy is restored from the slot when something still reads it.
                    copies = 0

                    while copies < len(insts) and insts[copies].handler == "Mov" \
                            and _operands(insts[copies])[1] == leaf.reg \
                            and _operands(insts[copies])[0] not in (leaf.reg, prev_tmp):
                        copies += 1

                    after = insts[copies:]

                    # `{ a: slot }`: the value goes straight into an environment slot (nothing runs on the way).
                    if after and (
                            store := _plain_store(after[0], leaf.reg) or _plain_store_of_read(after[0], prev_tmp, read,
                                                                                              leaf.reg)
                    ) is not None and _is_env_slot(store, self._env_names):
                        leaf.slot = store
                        ctx.slot_copies.append((leaf.reg, store))
                        ctx.slot_copies.extend((_operands(c)[0], store) for c in insts[:copies])
                        insts = after[1:]

                    props.append((read, leaf))

                    # The source register now holds the leaf: nothing can read a further property from it.
                    if self_read:
                        if leaf.slot is None:
                            return None

                        break

                if props:
                    items[-1] = _Elem("object", props=props, temp=prev_tmp)
                    prev_tmp = None
                    matched_rest = self._match_object_rest(insts, items[-1].temp, ctx)

                    if matched_rest is not None:
                        items[-1].rest, insts = matched_rest
                else:
                    # A constant key loaded just for the store is inlined into it, so its load is dead.
                    lead = 0

                    creates = []

                    while lead < len(insts) and (
                            (insts[lead].handler in _KEY_LOADS and insts[lead].definition_used)
                            or (insts[lead].handler in _ENV_CREATES and not ctx.hoist and not creates
                                and _is_env_creation(insts[lead]))
                    ):
                        if insts[lead].handler in _ENV_CREATES:
                            creates.append(insts[lead])

                        lead += 1

                    if lead < len(insts) and (store := _plain_store(insts[lead], prev_tmp, first_value)) is not None \
                            and not any(_reads_name(insts[lead], f"r{c.dest_reg}") for c in creates):
                        # The environment the slot belongs to is created right before its first store; it moves
                        # in front of the pattern (an allocation: nothing observable runs in between).
                        ctx.hoist.extend(creates)
                        # `[..., slot] = src`: the element is stored into a slot that needs no evaluation.
                        items[-1] = _Elem("target", items=None, default=store, temp=prev_tmp)

                        if insts[lead].value.right.name == f"r{first_value}":
                            ctx.fetched.append((first_value, store))

                        insts = insts[lead + 1:]
                        prev_tmp = None

            if prev_tmp is not None:
                if ctx.peeled_form is None:
                    ctx.peeled_form = peeled is not None
                elif ctx.peeled_form != (peeled is not None):
                    return None

                if peeled is not None:
                    items[-1].reg = _operands(peeled)[0]
                    items[-1].result = peeled

            if not insts or insts[-1].handler not in _JMP_TRUE:
                return None

            jmp_k = insts[-1]
            jump_ops = _operands(jmp_k)

            if len(jump_ops) != 2:
                return None

            undef_inst = None
            others = []

            for instruction in insts[:-1]:
                ops = _operands(instruction)

                if instruction.handler == "Mov" and len(ops) == 2 and ops[1] in aliases:
                    aliases.add(ops[0])
                elif instruction.handler == "LoadConstUndefined" and undef_inst is None:
                    undef_inst = instruction
                else:
                    others.append(instruction)

            if jump_ops[1] not in aliases:
                return None

            branch = _taken_fall(cur_block)
            if branch is None:
                return None

            taken, fall = branch
            own = [] if cur_block is ctx.top else [cur_block]

            if others:
                # `...rest`; the loop's `+ 1` may be hoisted into a register here.
                shape = [i.handler for i in others]

                if shape == ["NewArray", "LoadConstUInt8", "LoadConstZero"] and _operands(others[1])[1:] == [1]:
                    others = [others[0], others[2]]
                elif shape != ["NewArray", "LoadConstZero"]:
                    return None

                if undef_inst is not None:
                    return None

                rest = self._match_rest(cur_block, [*others, jmp_k], it, jump_ops[1], undef_reg)

                if rest is None:
                    return None

                join, rest_drop, rest_reg, rest_result = rest
                ctx.drop.extend(rest_drop)
                items.append(_Elem("rest", rest_reg, rest_result))
                return items, join, kept_undefined

            fall_handlers = _handlers(fall)

            if ctx.late and undef_inst is None:
                # The close block repeats the copies after the close: `IteratorClose it; Mov...; [Jmp]`.
                body = fall.instructions

                if (
                        len(body) >= 1 + len(ctx.late) and body[0].handler == "IteratorClose"
                        and _operands(body[0])[:1] == [it]
                        and all(a.handler == "Mov" and _operands(a) == _operands(b)
                                for a, b in zip(body[1:1 + len(ctx.late)], ctx.late))
                        and all(i.handler.startswith("Jmp") for i in body[1 + len(ctx.late):])
                        and _only_successor(fall) is taken
                ):
                    ctx.drop.extend([*own, fall])
                    return items, taken, kept_undefined

                return None

            if undef_inst is None and fall_handlers in (["IteratorClose"], ["Mov", "IteratorClose"]):
                # Close check: JmpTrue f -> J ; fall -> [Mov tmp <- it] IteratorClose -> J.
                close = fall.instructions[-1]
                close_ops = _operands(close)

                if fall_handlers == ["Mov"] + ["IteratorClose"]:
                    mov_ops = _operands(fall.instructions[0])

                    if len(mov_ops) != 2 or mov_ops[1] != it or close_ops[:1] != [mov_ops[0]]:
                        return None
                elif close_ops[:1] != [it]:
                    return None

                if _only_successor(fall) is not taken:
                    return None

                ctx.drop.extend([*own, fall])
                return items, taken, kept_undefined

            if undef_inst is None:
                # Hole: just the fetch, falling into the next boundary.
                if fall_handlers not in (["IteratorNext", "Mov", "StrictEq"],
                                         ["Mov", "IteratorNext", "Mov", "StrictEq"]):
                    return None

                fetch = list(fall.instructions)

                if fall_handlers[0] == "Mov":
                    if len(_operands(fetch[0])) != 2:
                        return None

                    fetch = fetch[1:]

                nh_ops, mh_ops, eh_ops = (_operands(i) for i in fetch)

                if len(nh_ops) != 3 or len(mh_ops) != 2 or len(eh_ops) != 3:
                    return None

                if nh_ops[1] != it or mh_ops[1] != it or eh_ops[1] != mh_ops[0] or eh_ops[2] != undef_reg:
                    return None

                # The skipped path must leave the new flag register set.
                if eh_ops[0] not in aliases or _only_successor(fall) is not taken:
                    return None

                items.append(_Elem("hole"))
                ctx.drop.extend([*own, fall])
                aliases.add(eh_ops[0])
                prev_tmp = None
                cur_block, cur_insts = taken, list(taken.instructions)
                continue

            # Element k >= 2.
            ek = _operands(undef_inst)[0]
            first_value = None

            # Fetch: [Mov t <- src] Next vk; Mov y <- it; StrictEq f2 <- y === undefined;
            #        [LoadConstUndefined ek]; Mov f <- f2; JmpTrue f -> X
            core = list(fall.instructions)

            if core and core[0].handler == "Mov" and _operands(core[0])[1:] == [src]:
                core = core[1:]

            if [i.handler for i in core] == ["IteratorNext", "Mov", "StrictEq", "LoadConstUndefined", "Mov", "JmpTrue"]:
                if _operands(core[3]) != [ek]:
                    return None

                core = core[:3] + core[4:]

            if [i.handler for i in core] != ["IteratorNext", "Mov", "StrictEq", "Mov", "JmpTrue"]:
                return None

            nk, my, eqk, mov_f, jmp_n = core
            nk_ops, my_ops, eqk_ops = _operands(nk), _operands(my), _operands(eqk)
            f_ops, jn_ops = _operands(mov_f), _operands(jmp_n)

            if len(nk_ops) != 3 or len(my_ops) != 2 or len(eqk_ops) != 3 or len(f_ops) != 2 or len(jn_ops) != 2:
                return None

            vk, nk_it, _ = nk_ops
            y_reg, y_it = my_ops
            flag2, eq_y, eq_u = eqk_ops

            if nk_it != it or y_it != it or eq_y != y_reg or eq_u != undef_reg or f_ops[1] != flag2:
                return None

            aliases.update((flag2, f_ops[0]))

            if jn_ops[1] not in aliases:
                return None

            inner = _taken_fall(fall)
            if inner is None:
                return None

            done_target, assign = inner

            if _handlers(assign) != ["Mov", "Mov"]:
                return None

            assign_ops = _operands(assign.instructions[1])

            if _operands(assign.instructions[0]) != [ek, vk] or len(assign_ops) != 2 or assign_ops[1] != flag2:
                return None

            aliases.add(assign_ops[0])
            default = None
            extra: list[BasicBlock] = []
            after = taken

            if done_target is taken:
                # No default: every path meets at the next boundary.
                if _only_successor(assign) is not taken:
                    return None
            else:
                # With a default the done path goes straight to it, the others
                # compare the value first:  Cmp: Mov tmp <- ek; JStrictNotEqual tmp, undefined -> A
                compare = taken

                if _only_successor(assign) is not compare:
                    return None

                after_default = self._compare_block(compare, ek, undef_reg, aliases)

                if after_default is None:
                    return None

                after, default_block = after_default

                if default_block is not done_target:
                    return None

                default = self._default_value(default_block, ek, after, aliases)

                if default is None:
                    return None

                extra = [compare, default_block]

            items.append(_Elem("reg", ek, assign.instructions[0], default=default))
            ctx.drop.extend([*own, fall, assign, *extra])
            prev_tmp = ek
            cur_block, cur_insts = after, list(after.instructions)

    @staticmethod
    def _late_copies(insts, items):
        """The `Mov target <- tmp` run in front of the closing jump when it holds one copy per element, the last
        element first, into registers that are no element's temporary; else None."""
        regs = [i for i in items if i.kind == "reg" and i.default is None]

        if len(regs) < 2 or len(regs) != len([i for i in items if i.kind != "hole"]) or len(insts) < len(regs) + 1:
            return None

        if insts[-1].handler not in _JMP_TRUE:
            return None

        run = insts[len(insts) - 1 - len(regs):-1]
        temps = {i.reg for i in regs}
        targets = []

        for mov, leaf in zip(run, reversed(regs)):
            ops = _operands(mov)

            if mov.handler != "Mov" or len(ops) != 2 or ops[1] != leaf.reg or ops[0] in temps:
                return None

            targets.append(ops[0])

        if len(set(targets)) != len(targets):
            return None

        return run

    def _compare_block(self, block: BasicBlock, ek: int, undef_reg: int, flags: set[int]):
        """
        `Mov tmp <- ek; [flag copies]; JStrictNotEqual tmp, undefined -> A`:
        returns (A, default_block) or None.
        """
        if not block.instructions or block.instructions[-1].handler != "JStrictNotEqual":
            return None

        tmp = None

        for instruction in block.instructions[:-1]:
            ops = _operands(instruction)

            if instruction.handler != "Mov" or len(ops) != 2:
                return None

            if ops[1] in flags:
                flags.add(ops[0])
            elif ops[1] == ek and tmp is None:
                tmp = ops[0]
            else:
                return None

        cmp_ops = _operands(block.instructions[-1])
        branch = _taken_fall(block)

        if tmp is None or len(cmp_ops) != 3 or cmp_ops[1:] != [tmp, undef_reg] or branch is None:
            return None

        return branch

    def _default_value(self, block: BasicBlock, ek: int, after: BasicBlock, flags: set[int]):
        """
        The default expression computed by `block` into `ek` (flag copies
        and the closing `Jmp` aside), or None when the block does anything
        else than compute that value.
        """
        if _only_successor(block) is not after:
            return None

        computed = []

        for instruction in block.instructions:
            ops = _operands(instruction)

            if instruction.handler == "Jmp":
                continue

            if instruction.handler == "Mov" and len(ops) == 2 and ops[1] in flags:
                flags.add(ops[0])
                continue

            computed.append(instruction)

        if not computed or computed[-1].dest_reg != ek or computed[-1].value is None:
            return None

        for instruction in computed[:-1]:
            if not instruction.definition_used or instruction.statement is not None:
                return None

        if computed[-1].statement is not None:
            return None

        return computed[-1].value

    def _match_rest(self, start: BasicBlock, insts, it: int, flag: int, undef_reg: int):
        """`...rest` after the last element.

            start: NewArray rest; LoadConstZero idx; JmpTrue f -> X
            LH:    Mov t <- src; IteratorNext v, it, t; Mov y <- it
                   StrictEq f2 <- (y === undefined); Mov j <- idx; JmpTrue f2 -> X
            LB:    PutByValStrict rest[j] = v; AddN idx = j + 1; Jmp LH

        Returns (join, blocks_to_drop, rest_reg, rest_result).
        """
        new_array, load_zero, jump = insts
        rest_reg = _operands(new_array)[0]
        idx = _operands(load_zero)[0]
        jump_ops = _operands(jump)

        if len(jump_ops) != 2 or jump_ops[1] != flag:
            return None

        branch = _taken_fall(start)
        if branch is None:
            return None

        exit_block, header = branch

        if handlers_of(header) != ["Mov", "IteratorNext", "Mov", "StrictEq", "Mov", "JmpTrue"]:
            return None

        mov_t, nxt, mov_y, eq, mov_j, jmp = header.instructions
        t, n, y, e, j, jm = (_operands(i) for i in (mov_t, nxt, mov_y, eq, mov_j, jmp))

        if any(len(ops) != want for ops, want in ((t, 2), (n, 3), (y, 2), (e, 3), (j, 2), (jm, 2))):
            return None

        value, n_it, n_t = n
        f2 = e[0]

        if n_it != it or n_t != t[0] or y[1] != it or e[1] != y[0] or e[2] != undef_reg:
            return None

        if j[1] != idx or jm[1] != f2:
            return None

        header_branch = _taken_fall(header)
        if header_branch is None or header_branch[0] is not exit_block:
            return None

        body = header_branch[1]

        if handlers_of(body) != ["PutByValStrict", "AddN", "Jmp"]:
            return None

        put, add, _jump = body.instructions

        if _operands(put) != [rest_reg, j[0], value]:
            return None

        add_ops = _operands(add)

        if len(add_ops) < 2 or add_ops[0] != idx or add_ops[1] != j[0] or _only_successor(body) is not header:
            return None

        # The handler that protects the loop body (`Catch; ...; IteratorClose it, 1;
        # Throw`) is iterator cleanup like any other: `_plan_handlers` removes it.
        return exit_block, [start, header, body], rest_reg, new_array

    # ------------------------------------------------------------------
    # Rewrite
    # ------------------------------------------------------------------

    def _apply(self, head: BasicBlock, begin_index: int, match) -> None:
        items, drop, join, kept_undefined, removed_handlers, cleanup, restores, hoist = match

        begin = head.instructions[begin_index]
        source = begin.value.arguments[0]

        pattern = AssignmentExpression(
            left=_pattern_expression(items),
            operator=AssignmentOperator.ASSIGN,
            right=source,
        )

        # The IteratorBegin result carries the single printed statement.
        begin.dest_reg = None
        begin.value = pattern
        begin.definition_used = False

        # Each element keeps a silent definition (`rN = rN` prints nothing)
        # so reaching-definition lookups still see the register written here.
        silent = []
        copies: list[tuple[object, int]] = []
        for leaf in _leaves(items):
            result = leaf.result

            # What the frontend read through `Mov e <- v` is the fetched register's own node (98/9900:
            # `return r2 === r1` printed `r3 === r1`); the register the element lands in is what is read now.
            if isinstance(result.value, Identifier) and result.value.name != f"r{leaf.reg}":
                copies.append((result.value, leaf.reg))

            result.dest_reg = leaf.reg
            result.value = Identifier(name=f"r{leaf.reg}")
            result.definition_used = False
            silent.append(result)

        gone = [*drop, *cleanup]
        removed = {id(instruction) for block in gone for instruction in block.instructions}
        removed.update(id(i) for i in head.instructions[begin_index + 1:])
        removed -= {id(result) for result in silent}

        keep = [kept_undefined] if kept_undefined is not None else []
        removed -= {id(result) for result in keep}

        # `rN = <slot>` for a register that outlives the pattern (see `_match`).
        restored = []
        for register, slot in restores.items():
            copy_ = copy.copy(begin)
            copy_.dest_reg = register
            copy_.value = slot
            copy_.definition_used = False
            restored.append(copy_)

        hoisted_ids = {id(i) for i in hoist}
        removed -= hoisted_ids
        before = head.instructions[:begin_index]
        # (A creation that overwrites the register the source is read from runs after the pattern: 98/5651.)
        if any(_mentions_register(source, created.dest_reg) for created in hoist):
            head.instructions = before + [begin] + hoist + keep + silent + restored
        else:
            head.instructions = before + hoist + [begin] + keep + silent + restored
        head.terminator = TerminatorJump(target=join.address)

        for successor in list(head.successors):
            if head in successor.predecessors:
                successor.predecessors.remove(head)

        head.successors = [join]
        join.predecessors = [p for p in join.predecessors if p not in drop]

        if head not in join.predecessors:
            join.predecessors.append(head)

        gone_ids = {block.id for block in gone}
        dropped_ids = {block.id for block in drop}
        self.cfg.blocks = [block for block in self.cfg.blocks if block.id not in gone_ids]

        # Handlers that guarded only the pattern (the rest loop's cleanup,
        # the iterator-close cleanup of a nested pattern) go with it; any
        # other just loses the dropped blocks from its range (and the cleanup
        # blocks too: a surrounding try covers those as well, and a block
        # left in its list is gone from the CFG - dominators then fail on it).
        removed_ids = {id(handler) for handler in removed_handlers}
        self.cfg.exception_handlers = [
            handler for handler in self.cfg.exception_handlers
            if id(handler) not in removed_ids and handler["handler_block"].id not in gone_ids
        ]

        for handler in self.cfg.exception_handlers:
            handler["try_blocks"] = [b for b in handler["try_blocks"] if b.id not in gone_ids]

        for register, definitions in list(self.cfg.reg_definitions.items()):
            self.cfg.reg_definitions[register] = [d for d in definitions if id(d[2]) not in removed]

        self._read_the_targets(copies, {id(begin), *(id(r) for r in silent)})

    def _read_the_targets(self, copies, own: set[int]) -> None:
        """Reads that hold the very node of a dropped `Mov e <- v` now read `e`."""
        for old, register in copies:
            new = Identifier(name=f"r{register}")

            for block in self.cfg.blocks:
                for instruction in block.instructions:
                    if id(instruction) in own:
                        continue

                    for field in ("value", "statement"):
                        node = getattr(instruction, field, None)

                        if node is not None:
                            replaced, changed = repoint_node(node, old, new, structural=False)

                            if changed:
                                setattr(instruction, field, replaced)

                if block.terminator is not None:
                    block.terminator = _repoint_terminator(block.terminator, old, new, structural=False)


@dataclass(slots=True)
class _Elem:
    """One slot of a destructuring pattern."""

    kind: str  # "reg" | "hole" | "nested" | "rest" | "object"
    reg: int | None = None
    result: object = None
    items: list | None = None
    default: object = None  # `[a = 0]`: the default value expression
    props: list | None = None  # "object": (property name, leaf `_Elem`) in the order the reads run
    temp: int | None = None  # "object": the register the element value was fetched into
    slot: object = None  # "reg" leaf of an object pattern stored straight into an environment slot
    rest: object = None  # "object": `...rest` of the pattern: (target expression or None, register or None, result)


class _Ctx:
    """State shared by a pattern and the patterns nested in it."""

    def __init__(self, head: BasicBlock):
        self.top = head
        self.drop: list[BasicBlock] = []
        self.iterators: set[int] = set()
        self.peeled_form: bool | None = None
        self.late: list = []  # the closing run of `Mov target <- tmp` copies (see `_late_copies`)
        self.hoist: list = []  # environment creations that move in front of the pattern
        self.scratch: list[int] = []  # registers an object-rest sequence wrote: dead after the pattern
        self.slot_copies: list[tuple[int, object]] = []  # (register holding the value of a slot, the slot)
        self.fetched: list[
            tuple[int, object]] = []  # fetch registers a slot store read directly, no copy of them is kept


def _property_read(instruction, source: int, allow_self: bool = False):
    """`rD = rSource.name` (a plain property load of the element value into a new register), as its name.

    `allow_self`: the last property of a pattern may be read into the source register itself."""
    value = instruction.value

    if (
            not isinstance(value, MemberExpression)
            or value.computed
            or value.optional
            or value.receiver is not None
            or not isinstance(value.obj, Identifier)
            or value.obj.name != f"r{source}"
            or not isinstance(value.prop, Identifier)
            or not value.prop.name.isidentifier()
            or not isinstance(instruction.dest_reg, int)
            or (instruction.dest_reg == source and not allow_self)
    ):
        return None

    return value.prop.name


def _plain_store(instruction, source: int, alias: int | None = None):
    """`slot = rSource` where the slot is a member of a register or of the environment reached by a constant
    key, so that no code runs when the target is evaluated: returns the target expression."""
    value = instruction.value

    if (
            not isinstance(value, AssignmentExpression)
            or value.operator != AssignmentOperator.ASSIGN
            or not isinstance(value.right, Identifier)
            or value.right.name not in (f"r{source}", f"r{alias}")
            or instruction.dest_reg is not None
    ):
        return None

    left = value.left

    if (
            not isinstance(left, MemberExpression)
            or left.optional
            or left.receiver is not None
            or not isinstance(left.obj, Identifier)
            or left.obj.name in (f"r{source}", f"r{alias}")
    ):
        return None

    if left.computed and not isinstance(left.prop, NumericLiteral):
        return None

    if not left.computed and not isinstance(left.prop, Identifier):
        return None

    return left


def _plain_store_of_read(instruction, source: int, name: str, leaf_register: int):
    """`slot = rSource.name` where the property load was inlined into the store: the store of that leaf."""
    value = instruction.value

    if not isinstance(value, AssignmentExpression) or not isinstance(value.right, MemberExpression):
        return None

    right = value.right

    if (
            right.computed or right.optional or right.receiver is not None
            or not isinstance(right.obj, Identifier) or right.obj.name != f"r{source}"
            or not isinstance(right.prop, Identifier) or right.prop.name != name
    ):
        return None

    probe = copy.copy(instruction)
    probe.value = dataclasses.replace(value, right=Identifier(name=f"r{leaf_register}"))

    return _plain_store(probe, leaf_register)


def _mentions_register(expression, register: int) -> bool:
    return any(isinstance(n, Identifier) and n.name == f"r{register}" for n in expression.walk())


def _reads_name(node, name: str) -> bool:
    for part in (getattr(node, "value", None), getattr(node, "statement", None)):
        if part is not None and any(isinstance(n, Identifier) and n.name == name for n in part.walk()):
            return True

    return False


def _is_env_creation(instruction) -> bool:
    value = instruction.value

    return isinstance(value, Identifier) and value.name == "__environment__" and isinstance(instruction.dest_reg, int)


def _targets(items):
    for item in items:
        if item.kind == "nested":
            yield from _targets(item.items)
        elif item.kind == "target":
            yield item


def _is_env_slot(expression, environments: frozenset = frozenset()) -> bool:
    return (
            isinstance(expression, MemberExpression)
            and expression.computed
            and not expression.optional
            and isinstance(expression.obj, Identifier)
            and (expression.obj.name == "__environment__" or id(expression) in environments)
            and isinstance(expression.prop, NumericLiteral)
    )


def _object_temps(items):
    for item in items:
        if item.kind == "nested":
            yield from _object_temps(item.items)
        elif item.kind in ("object", "target"):
            yield item.temp


def _leaves(items):
    for item in items:
        if item.kind == "nested":
            yield from _leaves(item.items)
        elif item.kind == "object":
            for _, leaf in item.props:
                if leaf.slot is None:
                    yield leaf

            if item.rest is not None and item.rest[1] is not None:
                yield _Elem("reg", item.rest[1], item.rest[2])
        elif item.kind in ("reg", "rest"):
            yield item


def _pattern_expression(items) -> ArrayExpression:
    elements = []

    for item in items:
        if item.kind == "hole":
            elements.append(ArrayHole())
        elif item.kind == "nested":
            elements.append(_pattern_expression(item.items))
        elif item.kind == "target":
            elements.append(item.default)
        elif item.kind == "object":
            properties = [
                ObjectProperty(key=Identifier(name=name), value=leaf.slot or Identifier(name=f"r{leaf.reg}"))
                for name, leaf in item.props
            ]

            if item.rest is not None:
                slot, register, _ = item.rest
                properties.append(SpreadElement(argument=slot or Identifier(name=f"r{register}")))

            elements.append(ObjectExpression(properties=tuple(properties)))
        elif item.kind == "rest":
            elements.append(SpreadElement(argument=Identifier(name=f"r{item.reg}")))
        elif item.default is not None:
            elements.append(AssignmentExpression(
                left=Identifier(name=f"r{item.reg}"), operator=AssignmentOperator.ASSIGN, right=item.default,
            ))
        else:
            elements.append(Identifier(name=f"r{item.reg}"))

    return ArrayExpression(elements=tuple(elements))


_ENV_CREATES = frozenset({"CreateFunctionEnvironment", "CreateTopLevelEnvironment"})

_KEY_LOADS = frozenset({"LoadConstUInt8", "LoadConstZero", "LoadConstInt"})

_CLEANUP_HANDLERS = {"Catch", "Mov", "Jmp", "JmpLong", "JmpTrue", "JmpTrueLong", "LoadConstUndefined", "IteratorClose",
                     "Throw"}


def _cleanup_vocabulary(block: BasicBlock, iterators: set[int]) -> bool:
    # `Mov r20 <- it; IteratorClose r20, 1` closes a copy of the iterator (98/5707): the copy is the iterator.
    closable = set(iterators)

    for instruction in block.instructions:
        if instruction.handler not in _CLEANUP_HANDLERS:
            return False

        if instruction.handler == "Mov":
            operands = _operands(instruction)

            if len(operands) == 2 and operands[1] in iterators:
                closable.add(operands[0])

        if instruction.handler == "IteratorClose" and _operands(instruction)[:1] and _operands(instruction)[
            0] not in closable:
            return False

    return True


def _cleanup_chain(handler_block: BasicBlock, iterators: set[int]):
    """
    The blocks of an iterator-cleanup handler (`Catch ex; [flag copy]; ...
    JmpTrue done -> T; IteratorClose it, 1; T: Throw ex`), or None when the
    handler does anything else (a real `catch` block).
    """
    chain: dict[int, BasicBlock] = {}
    stack = [handler_block]

    while stack:
        block = stack.pop()

        if block.id in chain:
            continue

        if not _cleanup_vocabulary(block, iterators):
            return None

        chain[block.id] = block
        stack.extend(block.successors)

    closes = any(i.handler == "IteratorClose" for b in chain.values() for i in b.instructions)
    throws = any(i.handler == "Throw" for b in chain.values() for i in b.instructions)

    return list(chain.values()) if closes and throws else None


def handlers_of(block: BasicBlock) -> list[str]:
    return _handlers(block)
