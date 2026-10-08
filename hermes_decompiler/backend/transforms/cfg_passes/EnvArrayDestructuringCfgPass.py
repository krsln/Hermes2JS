"""
Collapses array destructuring whose targets live in environment slots.

A destructuring pattern in a generator/async function whose bindings are
captured (`const [a, b] = await Promise.all(...)` with `a`/`b` read from a
closure, or simply kept in the function's environment) cannot use
registers for its elements. Hermes then emits the same iterator protocol
as `ArrayDestructuringCfgPass` handles, but every element goes through
two environment temporaries - `Q` (the `next` method, restored before
each `IteratorNext`) and `S` (the fetched value) - and is stored into its
target slot with `StoreToEnvironment`::

    H:  [StoreToEnvironment E,Q,o]; [Mov src <- o]; IteratorBegin it, src
        StoreToEnvironment E,Q,src; LoadConstUndefined u; StoreNPToEnvironment E,S,u
        Mov f <- it; IteratorNext v, f, src; Mov x <- f
        StrictEq flag <- (x === u); JmpTrue flag -> J1
    A1: StoreToEnvironment E,S,v
    Jk: LoadFromEnvironment rX,E,T; LoadFromEnvironment rV,E,S
        StoreToEnvironment rX,idx_k,rV                 # target_k = value
        [LoadConstUndefined u]; StoreNPToEnvironment E,S,u   # not the last
        [Mov copy <- x]*; JmpTrue flag -> J(k+1)
    Nk: LoadFromEnvironment nm,E,Q; Mov y <- x; IteratorNext v, y, nm
        StrictEq flag2 <- (y === u); [Mov copy]*; JmpTrue flag2 -> Jk
    Ak: StoreToEnvironment E,S,v; [Mov copy]*
    last Jn ends `JmpTrue flag -> exit`, falling into `IteratorClose it, 0`.

That is `[target_1, target_2, ...] = src`. Only the flat form is handled
(no holes, defaults, nested patterns or rest) and only when nothing else
in the function touches the temporaries `Q` and `S`.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.cfg_passes._generator_dispatch import _operands
from hermes_decompiler.backend.transforms.cfg_passes.ArrayDestructuringCfgPass import (
    ArrayDestructuringCfgPass, _Ctx, _handlers, _only_successor, _taken_fall,
)
from hermes_decompiler.backend.transforms.shared._repoint import _reads_register_by_name
from hermes_decompiler.ir.expressions import ArrayExpression, AssignmentExpression
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.terminators import TerminatorJump

_JMP_TRUE = ("JmpTrue", "JmpTrueLong")
_ENV_OPS = ("LoadFromEnvironment", "StoreToEnvironment", "StoreNPToEnvironment")


class EnvArrayDestructuringCfgPass:
    def __init__(self, cfg: CFG):
        self.cfg = cfg

    def run(self) -> int:
        applied = 0

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

    def _match(self, head: BasicBlock, bi: int):
        begin = head.instructions[bi]
        ops = _operands(begin)

        if len(ops) != 2:
            return None

        it, src = ops
        tail = head.instructions[bi + 1:]

        if [i.handler for i in tail[:7]] != [
            "StoreToEnvironment", "LoadConstUndefined", "StoreNPToEnvironment",
            "Mov", "IteratorNext", "Mov", "StrictEq",
        ] or len(tail) != 8 or tail[-1].handler not in _JMP_TRUE:
            return None

        save, undef, init, mov_f, nxt, mov_x, eq, jmp = tail
        save_ops, undef_ops, init_ops = _operands(save), _operands(undef), _operands(init)
        f_ops, n_ops, x_ops, e_ops, j_ops = (
            _operands(mov_f), _operands(nxt), _operands(mov_x), _operands(eq), _operands(jmp)
        )

        if not (
                len(save_ops) == 3 and len(init_ops) == 3 and len(undef_ops) == 1 and len(f_ops) == 2
                and len(n_ops) == 3 and len(x_ops) == 2 and len(e_ops) == 3 and len(j_ops) == 2
        ):
            return None

        env, slot_q, saved = save_ops
        u = undef_ops[0]
        env2, slot_s, init_value = init_ops
        f, f_it = f_ops
        v, n_it, n_t = n_ops
        x, x_f = x_ops
        flag, eq_x, eq_u = e_ops

        if (
                env2 != env or init_value != u or f_it != it or n_it != f or n_t != saved
                or saved != src or x_f != f or eq_x != x or eq_u != u or j_ops[1] != flag
                or slot_q == slot_s
        ):
            return None

        # The iterable is first saved into Q too (`Mov src <- o` precedes the begin).
        drop_before = []
        before = head.instructions[:bi]

        if before and before[-1].handler == "Mov":
            mv = _operands(before[-1])

            if len(mv) == 2 and mv[0] == src and len(before) >= 2 and before[-2].handler == "StoreToEnvironment":
                st = _operands(before[-2])

                if len(st) == 3 and st[0] == env and st[1] == slot_q and st[2] == mv[1]:
                    drop_before = [before[-2]]

        branch = _taken_fall(head)

        if branch is None:
            return None

        taken, fall = branch
        a1_ops = _operands(fall.instructions[0]) if _handlers(fall) == ["StoreToEnvironment"] else None

        if a1_ops != [env, slot_s, v] or _only_successor(fall) is not taken:
            return None

        drop = [fall]
        flags = {flag}
        iters = {x, f, it}
        written = {it, src, u, f, v, x, flag}
        targets = []
        cur = taken
        undefined = u
        slot_t = None
        seen: set[int] = set()

        while True:
            if id(cur) in seen:
                return None

            seen.add(id(cur))
            insts = list(cur.instructions)

            if len(insts) < 4 or [i.handler for i in insts[:3]] != [
                "LoadFromEnvironment", "LoadFromEnvironment", "StoreToEnvironment"
            ] or insts[-1].handler not in _JMP_TRUE:
                return None

            l1, l2, st = (_operands(i) for i in insts[:3])

            if (
                    len(l1) != 3 or len(l2) != 3 or len(st) != 3 or l1[1] != env2 and False
                    or l2[1] != env or l2[2] != slot_s or st[0] != l1[0] or st[2] != l2[0]
            ):
                return None

            if slot_t is None:
                slot_t = l1[2]
            elif l1[2] != slot_t or l1[1] != env:
                return None

            store = insts[2]

            if (
                    not isinstance(store.value, AssignmentExpression)
                    or store.value.operator != AssignmentOperator.ASSIGN
            ):
                return None

            targets.append(store.value.left)
            written.update({l1[0], l2[0]})
            drop.append(cur)
            reset = False

            for instruction in insts[3:-1]:
                o = _operands(instruction)

                if instruction.handler == "LoadConstUndefined" and len(o) == 1:
                    undefined = o[0]
                    written.add(o[0])
                elif (
                        instruction.handler == "StoreNPToEnvironment" and len(o) == 3
                        and o[0] == env and o[1] == slot_s and o[2] == undefined and not reset
                ):
                    reset = True
                elif instruction.handler == "Mov" and len(o) == 2 and (o[1] in flags or o[1] in iters):
                    (flags if o[1] in flags else iters).add(o[0])
                    written.add(o[0])
                else:
                    return None

            jump = _operands(insts[-1])

            if len(jump) != 2 or jump[1] not in flags:
                return None

            branch = _taken_fall(cur)

            if branch is None:
                return None

            taken, fall = branch

            if not reset:
                # Last element: done -> exit, otherwise `IteratorClose`.
                if _handlers(fall) != ["IteratorClose"] or _only_successor(fall) is not taken:
                    return None

                close = _operands(fall.instructions[0])

                if len(close) != 2 or close[0] not in iters:
                    return None

                drop.append(fall)
                join = taken
                break

            # N: fetch the next element.
            nb = fall
            n_insts = list(nb.instructions)
            expected = ["LoadFromEnvironment", "Mov", "IteratorNext", "StrictEq"]

            if [i.handler for i in n_insts[:4]] != expected or n_insts[-1].handler not in _JMP_TRUE:
                return None

            ld, mv, nx, se = (_operands(i) for i in n_insts[:4])

            if (
                    len(ld) != 3 or ld[1] != env or ld[2] != slot_q or len(mv) != 2 or mv[1] not in iters
                    or len(nx) != 3 or nx[1] != mv[0] or nx[2] != ld[0] or len(se) != 3
                    or se[1] != mv[0] or se[2] != undefined
            ):
                return None

            iters.add(mv[0])
            flags = {se[0]}
            iters_extra = set()
            written.update({ld[0], mv[0], nx[0], se[0]})

            if se[0] == undefined:
                undefined = None

            for instruction in n_insts[4:-1]:
                o = _operands(instruction)

                if instruction.handler == "Mov" and len(o) == 2 and (o[1] in flags or o[1] in iters):
                    (flags if o[1] in flags else iters).add(o[0])
                    written.add(o[0])
                else:
                    return None

            n_jump = _operands(n_insts[-1])

            if len(n_jump) != 2 or n_jump[1] not in flags:
                return None

            n_branch = _taken_fall(nb)

            if n_branch is None or n_branch[0] is not taken:
                return None

            ab = n_branch[1]
            a_insts = list(ab.instructions)

            if not a_insts or a_insts[0].handler != "StoreToEnvironment" or _only_successor(ab) is not taken:
                return None

            a_ops = _operands(a_insts[0])

            if a_ops != [env, slot_s, nx[0]]:
                return None

            for instruction in a_insts[1:]:
                o = _operands(instruction)

                if instruction.handler == "Mov" and len(o) == 2 and (o[1] in flags or o[1] in iters):
                    (flags if o[1] in flags else iters).add(o[0])
                    written.add(o[0])
                else:
                    return None

            drop.extend([nb, ab])
            cur = taken
            del iters_extra

        dropped_ids = {b.id for b in drop}

        for block in drop:
            for predecessor in block.predecessors:
                if predecessor is not head and predecessor.id not in dropped_ids:
                    return None

        # Nothing else may touch the temporaries.
        dropped_instructions = {id(i) for b in drop for i in b.instructions}
        dropped_instructions.update(id(i) for i in tail)
        dropped_instructions.update(id(i) for i in drop_before)

        for block in self.cfg.blocks:
            for instruction in block.instructions:
                if id(instruction) in dropped_instructions or instruction.handler not in _ENV_OPS:
                    continue

                o = _operands(instruction)
                env_reg, slot = (o[1], o[2]) if instruction.handler == "LoadFromEnvironment" else (o[0], o[1])

                if env_reg == env and slot in (slot_q, slot_s):
                    return None

        # The temporaries must be dead after the pattern.
        last = max(
            [i.entry.address for b in drop for i in b.instructions] + [i.entry.address for i in tail],
        )

        for register in written:
            if _reads_register_by_name(self.cfg, register, last):
                return None

        ctx = _Ctx(head)
        ctx.iterators.add(it)
        handlers = ArrayDestructuringCfgPass(self.cfg)._plan_handlers(head, ctx, dropped_ids)

        if handlers is None:
            return None

        removed_handlers, cleanup = handlers

        if cleanup:
            return None

        return targets, drop, join, drop_before, removed_handlers

    # ------------------------------------------------------------------

    def _apply(self, head: BasicBlock, bi: int, match) -> None:
        targets, drop, join, drop_before, removed_handlers = match

        begin = head.instructions[bi]
        source = begin.value.arguments[0]

        pattern = AssignmentExpression(
            left=ArrayExpression(elements=tuple(targets)),
            operator=AssignmentOperator.ASSIGN,
            right=source,
        )

        begin.dest_reg = None
        begin.value = pattern
        begin.definition_used = False

        removed = {id(i) for block in drop for i in block.instructions}
        removed.update(id(i) for i in head.instructions[bi + 1:])
        removed.update(id(i) for i in drop_before)

        drop_before_ids = {id(i) for i in drop_before}
        head.instructions = [i for i in head.instructions[:bi + 1] if id(i) not in drop_before_ids]
        head.terminator = TerminatorJump(target=join.address)

        for successor in list(head.successors):
            if head in successor.predecessors:
                successor.predecessors.remove(head)

        head.successors = [join]
        join.predecessors = [p for p in join.predecessors if p not in drop]

        if head not in join.predecessors:
            join.predecessors.append(head)

        gone_ids = {block.id for block in drop}
        self.cfg.blocks = [block for block in self.cfg.blocks if block.id not in gone_ids]

        removed_ids = {id(handler) for handler in removed_handlers}
        self.cfg.exception_handlers = [
            handler for handler in self.cfg.exception_handlers
            if id(handler) not in removed_ids and handler["handler_block"].id not in gone_ids
        ]

        for handler in self.cfg.exception_handlers:
            handler["try_blocks"] = [b for b in handler["try_blocks"] if b.id not in gone_ids]

        for register, definitions in list(self.cfg.reg_definitions.items()):
            self.cfg.reg_definitions[register] = [d for d in definitions if id(d[2]) not in removed]
