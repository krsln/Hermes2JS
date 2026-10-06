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

from dataclasses import dataclass

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.cfg_passes._generator_dispatch import _operands
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import ArrayExpression, AssignmentExpression, Identifier
from hermes_decompiler.ir.expressions.Collections import ArrayHole, SpreadElement
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

        return items, drop, join, kept_undefined, removed_handlers, cleanup

    def _plan_handlers(self, head: BasicBlock, ctx: "_Ctx", dropped_ids: set[int]):
        """
        Decides which exception handlers go away with the collapsed pattern.

        Returns (removed_handlers, cleanup_blocks) or None when a handler
        cuts through the pattern.

        Three kinds go: the rest loop's own cleanup handler; the iterator
        cleanup handlers (`Catch; ...; IteratorClose it, 1; Throw`) that
        guard an element which can throw (a nested pattern); and, like
        before, a surrounding try merely loses the dropped blocks from its
        range - but only if it covers the whole pattern.
        """
        rest_ids = {b.id for b in ctx.rest_handler_blocks}
        removed: list = []
        remaining: list = []
        chain: dict[int, BasicBlock] = {}

        for handler in self.cfg.exception_handlers:
            hb = handler["handler_block"]
            covered = {b.id for b in handler["try_blocks"]}

            if hb.id in dropped_ids:
                # The rest loop's own cleanup handler: only fine if all it
                # protects goes with it.
                if hb.id not in rest_ids or not covered <= dropped_ids:
                    return None

                removed.append(handler)
                continue

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

        if top and shapes == ["Mov", "IteratorNext", "Mov", "LoadConstUndefined", *expected[3:]]:
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

        taken, fall = branch
        aliases = {flag}
        items: list[_Elem] = []

        if _handlers(fall) == ["Mov"] and _operands(fall.instructions[0]) == [e1, v1]:
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
            cur_block, cur_insts = head, [undef_e, jmp]

        seen: set[int] = set()

        while True:
            if id(cur_block) in seen:
                return None

            seen.add(id(cur_block))
            insts = list(cur_insts)
            peeled = None

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

                sub_start = len(ctx.drop)
                iterators_before = set(ctx.iterators)
                ctx.drop.append(cur_block)
                sub = self._parse(cur_block, len(cur_block.instructions) - len(insts), ctx, top=False)

                if sub is None:
                    return None

                sub_items, sub_join, _ = sub

                # Whatever the nested pattern wrote is no longer the flag.
                for block in ctx.drop[sub_start:]:
                    for instruction in block.instructions:
                        if instruction.dest_reg is not None:
                            aliases.discard(instruction.dest_reg)

                aliases -= ctx.iterators - iterators_before
                items[-1] = _Elem("nested", items=sub_items)
                prev_tmp = None
                cur_block, cur_insts = sub_join, list(sub_join.instructions)
                continue

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
                # `...rest`
                if undef_inst is not None or [i.handler for i in others] != ["NewArray", "LoadConstZero"]:
                    return None

                rest = self._match_rest(cur_block, [*others, jmp_k], it, jump_ops[1], undef_reg)

                if rest is None:
                    return None

                join, rest_drop, rest_reg, rest_result, handler_blocks = rest
                ctx.drop.extend(rest_drop)
                ctx.rest_handler_blocks |= handler_blocks
                items.append(_Elem("rest", rest_reg, rest_result))
                return items, join, kept_undefined

            fall_handlers = _handlers(fall)

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
                aliases = {eh_ops[0]}
                prev_tmp = None
                cur_block, cur_insts = taken, list(taken.instructions)
                continue

            # Element k >= 2.
            ek = _operands(undef_inst)[0]

            if fall_handlers != ["IteratorNext", "Mov", "StrictEq", "LoadConstUndefined", "Mov", "JmpTrue"]:
                return None

            nk, my, eqk, undef_k, mov_f, jmp_n = fall.instructions
            nk_ops, my_ops, eqk_ops = _operands(nk), _operands(my), _operands(eqk)
            f_ops, jn_ops = _operands(mov_f), _operands(jmp_n)

            if len(nk_ops) != 3 or len(my_ops) != 2 or len(eqk_ops) != 3 or len(f_ops) != 2 or len(jn_ops) != 2:
                return None

            vk, nk_it, _ = nk_ops
            y_reg, y_it = my_ops
            flag2, eq_y, eq_u = eqk_ops

            if (
                    nk_it != it or y_it != it or eq_y != y_reg or eq_u != undef_reg
                    or _operands(undef_k) != [ek] or f_ops[0] not in aliases or f_ops[1] != flag2
                    or jn_ops[1] != flag2
            ):
                return None

            inner = _taken_fall(fall)
            if inner is None or inner[0] is not taken:
                return None

            assign = inner[1]

            if _handlers(assign) != ["Mov", "Mov"]:
                return None

            if _operands(assign.instructions[0]) != [ek, vk] or _operands(assign.instructions[1]) != [f_ops[0], flag2]:
                return None

            if _only_successor(assign) is not taken:
                return None

            items.append(_Elem("reg", ek, assign.instructions[0]))
            ctx.drop.extend([*own, fall, assign])
            aliases = {f_ops[0], flag2}
            prev_tmp = ek
            cur_block, cur_insts = taken, list(taken.instructions)

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
        items, drop, join, kept_undefined, removed_handlers, cleanup = match

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
        for leaf in _leaves(items):
            result = leaf.result
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

        head.instructions = head.instructions[:begin_index + 1] + keep + silent
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
        # other just loses the dropped blocks from its range.
        removed_ids = {id(handler) for handler in removed_handlers}
        self.cfg.exception_handlers = [
            handler for handler in self.cfg.exception_handlers
            if id(handler) not in removed_ids and handler["handler_block"].id not in gone_ids
        ]

        for handler in self.cfg.exception_handlers:
            handler["try_blocks"] = [b for b in handler["try_blocks"] if b.id not in dropped_ids]

        for register, definitions in list(self.cfg.reg_definitions.items()):
            self.cfg.reg_definitions[register] = [d for d in definitions if id(d[2]) not in removed]


@dataclass(slots=True)
class _Elem:
    """One slot of a destructuring pattern."""

    kind: str  # "reg" | "hole" | "nested" | "rest"
    reg: int | None = None
    result: object = None
    items: list | None = None


class _Ctx:
    """State shared by a pattern and the patterns nested in it."""

    def __init__(self, head: BasicBlock):
        self.top = head
        self.drop: list[BasicBlock] = []
        self.iterators: set[int] = set()
        self.peeled_form: bool | None = None
        self.rest_handler_blocks: set[BasicBlock] = set()


def _leaves(items):
    for item in items:
        if item.kind == "nested":
            yield from _leaves(item.items)
        elif item.kind in ("reg", "rest"):
            yield item


def _pattern_expression(items) -> ArrayExpression:
    elements = []

    for item in items:
        if item.kind == "hole":
            elements.append(ArrayHole())
        elif item.kind == "nested":
            elements.append(_pattern_expression(item.items))
        elif item.kind == "rest":
            elements.append(SpreadElement(argument=Identifier(name=f"r{item.reg}")))
        else:
            elements.append(Identifier(name=f"r{item.reg}"))

    return ArrayExpression(elements=tuple(elements))


_CLEANUP_HANDLERS = {"Catch", "Mov", "Jmp", "JmpTrue", "JmpTrueLong", "LoadConstUndefined", "IteratorClose", "Throw"}


def _cleanup_vocabulary(block: BasicBlock, iterators: set[int]) -> bool:
    for instruction in block.instructions:
        if instruction.handler not in _CLEANUP_HANDLERS:
            return False

        if instruction.handler == "IteratorClose" and _operands(instruction)[:1] and _operands(instruction)[
            0] not in iterators:
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
