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

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.cfg_passes._generator_dispatch import _operands
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import ArrayExpression, AssignmentExpression, Identifier
from hermes_decompiler.ir.expressions.Collections import SpreadElement
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
    # Recognition
    # ------------------------------------------------------------------

    def _match(self, head: BasicBlock, begin_index: int):
        """
        Returns (targets, drop_blocks, join, element_results) or None.

        `targets` are the element registers in order; `element_results` the
        `Mov e_k <- v_k` results (kept as silent definitions of e_k).
        """
        begin = head.instructions[begin_index]
        begin_ops = _operands(begin)

        if len(begin_ops) != 2:
            return None

        it, src = begin_ops
        tail = head.instructions[begin_index + 1:]

        # [Mov t <- src], IteratorNext, Mov x <- it, StrictEq, LoadConstUndefined, JmpTrue
        shapes = [i.handler for i in tail]
        expected = ["Mov", "IteratorNext", "Mov", "StrictEq", "LoadConstUndefined", "JmpTrue"]

        # The `undefined` StrictEq compares against is loaded right here
        # unless an earlier block already holds it; that load outlives the
        # chain (the function's own `return undefined` often reads it).
        kept_undefined = None

        if shapes == ["Mov", "IteratorNext", "Mov", "LoadConstUndefined", *expected[3:]]:
            kept_undefined = tail[3]
            tail = tail[:3] + tail[4:]
        elif shapes != expected:
            return None

        mov_t, nxt, mov_x, eq, undef_e, jmp = tail
        t = _operands(mov_t)
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

        taken, assign_block = branch

        # A1: Mov e1 <- v1
        if _handlers(assign_block) != ["Mov"] or _operands(assign_block.instructions[0]) != [e1, v1]:
            return None

        if _only_successor(assign_block) is not taken:
            return None

        targets = [e1]
        element_results = [assign_block.instructions[0]]
        drop = [assign_block]
        undef_defs: list = []
        flags = {flag}
        current = taken

        # Binding patterns (`for (const [k, v] of m)`) fill temporaries and
        # copy each into its target at the next element boundary:
        # `Mov target <- tmp` leads the following head / close-check block.
        # All elements must agree on which of the two forms is used.
        peeled_form: bool | None = None
        previous_tmp = e1
        rest = None

        while True:
            insts = list(current.instructions)
            peeled = None

            if insts and insts[0].handler == "Mov":
                ops = _operands(insts[0])

                if len(ops) == 2 and ops[1] == previous_tmp and ops[0] != previous_tmp:
                    peeled = insts[0]
                    insts = insts[1:]

            if peeled_form is None:
                peeled_form = peeled is not None
            elif peeled_form != (peeled is not None):
                return None

            if peeled is not None:
                targets[-1] = _operands(peeled)[0]
                element_results[-1] = peeled

            handlers = [i.handler for i in insts]

            if handlers == ["LoadConstUndefined", "JmpTrue"]:
                # Element k >= 2.
                ek = _operands(insts[0])[0]
                jump_ops = _operands(insts[1])

                if len(jump_ops) != 2 or jump_ops[1] != flag:
                    return None

                branch = _taken_fall(current)
                if branch is None:
                    return None

                close_check, next_block = branch

                if handlers_of(next_block) != [
                    "IteratorNext", "Mov", "StrictEq", "LoadConstUndefined", "Mov", "JmpTrue",
                ]:
                    return None

                nk, my, eqk, undef_k, mov_f, jmp_k = next_block.instructions
                nk_ops, my_ops, eqk_ops = _operands(nk), _operands(my), _operands(eqk)
                f_ops, jk_ops = _operands(mov_f), _operands(jmp_k)

                if len(nk_ops) != 3 or len(my_ops) != 2 or len(eqk_ops) != 3 or len(f_ops) != 2 or len(jk_ops) != 2:
                    return None

                vk, nk_it, _ = nk_ops
                y_reg, y_it = my_ops
                flag2, eq_y, eq_u = eqk_ops

                if (
                        nk_it != it or y_it != it or eq_y != y_reg or eq_u != undef_reg
                        or _operands(undef_k) != [ek] or f_ops != [flag, flag2] or jk_ops[1] != flag2
                ):
                    return None

                branch = _taken_fall(next_block)
                if branch is None or branch[0] is not close_check:
                    return None

                assign = branch[1]

                if handlers_of(assign) != ["Mov", "Mov"]:
                    return None

                if _operands(assign.instructions[0]) != [ek, vk] or _operands(assign.instructions[1]) != [flag, flag2]:
                    return None

                targets.append(ek)
                element_results.append(assign.instructions[0])
                previous_tmp = ek
                drop.extend([current, next_block, assign])
                flags.add(flag2)
                following = _only_successor(assign)

                if following is None:
                    return None

                # Every head's early-out must agree with the chain's own exit.
                current = following
                chain_exit = close_check

                if current is not chain_exit and handlers_of(current)[-2:] != ["LoadConstUndefined", "JmpTrue"]:
                    return None

                continue

            if handlers == ["NewArray", "LoadConstZero", "JmpTrue"]:
                rest = self._match_rest(current, insts, it, flag, undef_reg)

                if rest is None:
                    return None

                break

            if handlers == ["JmpTrue"]:
                close_check = current
                close_insts = insts
                break

            return None

        if rest is not None:
            join, rest_drop, rest_reg, rest_result, handler_blocks = rest
            drop.extend(rest_drop)
            targets.append(rest_reg)
            element_results.append(rest_result)
        else:
            # Close check: JmpTrue f -> J ; fall -> IteratorClose it -> J.
            jump_ops = _operands(close_insts[0])
            branch = _taken_fall(close_check)

            if len(jump_ops) != 2 or jump_ops[1] != flag or branch is None:
                return None

            join, close_block = branch

            if handlers_of(close_block) != ["IteratorClose"]:
                return None

            if _operands(close_block.instructions[0])[:1] != [it] or _only_successor(close_block) is not join:
                return None

            drop.extend([close_check, close_block])
            handler_blocks = set()

        # The chain must be single-entry: nothing outside it jumps in, and
        # nothing in it is covered by an exception handler.
        dropped_ids = {block.id for block in drop}

        for block in drop:
            for predecessor in block.predecessors:
                if predecessor is not head and predecessor.id not in dropped_ids:
                    return None

        # A chain inside a try (a for-of body, say) is fine as long as the
        # try covers all of it: the dropped blocks just leave the handler's
        # list. A try that starts or ends inside the chain is not.
        for handler in self.cfg.exception_handlers:
            covered = {b.id for b in handler["try_blocks"]}

            if handler["handler_block"].id in dropped_ids:
                # The rest loop's own cleanup handler: only fine if all it
                # protects goes with it.
                if handler["handler_block"].id not in {b.id for b in handler_blocks} or not covered <= dropped_ids:
                    return None

                continue

            inside = dropped_ids & covered

            if inside and (inside != dropped_ids or head.id not in covered):
                return None

            if not inside and head.id in covered:
                return None

        if len(set(targets)) != len(targets):
            return None

        return targets, drop, join, element_results, kept_undefined, rest is not None

    def _match_rest(self, start: BasicBlock, insts, it: int, flag: int, undef_reg: int):
        """`...rest` after the last element.

            start: NewArray rest; LoadConstZero idx; JmpTrue f -> X
            LH:    Mov t <- src; IteratorNext v, it, t; Mov y <- it
                   StrictEq f2 <- (y === undefined); Mov j <- idx; JmpTrue f2 -> X
            LB:    PutByValStrict rest[j] = v; AddN idx = j + 1; Jmp LH
            handler (protects LB): Catch ex; JmpTrue f2 -> T
                   IteratorClose it; T: Throw ex

        Returns (join, blocks_to_drop, rest_reg, rest_result, handler_blocks).
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

        # The cleanup handler that protects the loop body.
        handler = next(
            (h for h in self.cfg.exception_handlers if [b.id for b in h["try_blocks"]] == [body.id]),
            None,
        )

        if handler is None:
            return None

        hb = handler["handler_block"]

        if handlers_of(hb) != ["Catch", "JmpTrue"]:
            return None

        catch_reg = hb.instructions[0].dest_reg
        hb_branch = _taken_fall(hb)

        if hb_branch is None or _operands(hb.instructions[1])[1:] != [f2]:
            return None

        throw_block, close_block = hb_branch

        if handlers_of(close_block) != ["IteratorClose"] or _operands(close_block.instructions[0])[:1] != [it]:
            return None

        if _only_successor(close_block) is not throw_block or handlers_of(throw_block) != ["Throw"]:
            return None

        if _operands(throw_block.instructions[0]) != [catch_reg]:
            return None

        return (
            exit_block,
            [start, header, body, hb, close_block, throw_block],
            rest_reg,
            new_array,
            {hb, close_block, throw_block},
        )

    # ------------------------------------------------------------------
    # Rewrite
    # ------------------------------------------------------------------

    def _apply(self, head: BasicBlock, begin_index: int, match) -> None:
        targets, drop, join, element_results, kept_undefined, has_rest = match

        begin = head.instructions[begin_index]
        source = begin.value.arguments[0]

        elements = [Identifier(name=f"r{reg}") for reg in targets]

        if has_rest:
            elements[-1] = SpreadElement(argument=elements[-1])

        pattern = AssignmentExpression(
            left=ArrayExpression(elements=tuple(elements)),
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
        for reg, result in zip(targets, element_results):
            result.dest_reg = reg
            result.value = Identifier(name=f"r{reg}")
            result.definition_used = False
            silent.append(result)

        removed = {id(instruction) for block in drop for instruction in block.instructions}
        removed.update(id(i) for i in head.instructions[begin_index + 1:])
        removed -= {id(result) for result in silent}

        keep = [kept_undefined] if kept_undefined is not None else []
        removed -= {id(result) for result in keep}

        head.instructions = head.instructions[:begin_index + 1] + keep + silent
        head.terminator = TerminatorJump(target=join.address)

        for successor in list(head.successors):
            if head in successor.predecessors:
                successor.predecessors.remove(head)

        head.successors = [join]
        join.predecessors = [p for p in join.predecessors if p not in drop]

        if head not in join.predecessors:
            join.predecessors.append(head)

        dropped_ids = {block.id for block in drop}
        self.cfg.blocks = [block for block in self.cfg.blocks if block.id not in dropped_ids]

        # A handler whose own block was dropped (the rest loop's cleanup) goes
        # with it; any other just loses the dropped blocks from its range.
        self.cfg.exception_handlers = [
            handler for handler in self.cfg.exception_handlers if handler["handler_block"].id not in dropped_ids
        ]

        for handler in self.cfg.exception_handlers:
            handler["try_blocks"] = [b for b in handler["try_blocks"] if b.id not in dropped_ids]

        for register, definitions in list(self.cfg.reg_definitions.items()):
            self.cfg.reg_definitions[register] = [d for d in definitions if id(d[2]) not in removed]


def handlers_of(block: BasicBlock) -> list[str]:
    return _handlers(block)
