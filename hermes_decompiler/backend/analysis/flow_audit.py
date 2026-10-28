"""Edges of the CFG that the final region tree no longer has (a silent drop).

Each CFG edge u -> v between blocks of the tree must still be a path in the tree's own flow graph
(an over-approximation: loops let every member reach the body entry and the exit, a `try` body
reaches its catch). A lost edge is a path the decompiled code can no longer take.

`scripts/audit/drop_scan.py` reports it per function; `HermesAnalysis.generate_js` uses the count
to try the shared-return/-tail copies on a function that printed no `goto` but lost a path.
The check is an approximation: a flagged function can still be right (a bare `return undefined`
arm falls off the end, a `Catch` edge), so a count is a reason to TRY another attempt, never a verdict.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopRegion, SequenceRegion, SwitchRegion, TryRegion
from hermes_decompiler.ir.statements import BreakStatement, ContinueStatement
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow

__all__ = ["Unknown", "scan", "count_lost_edges"]


class Unknown(Exception):
    pass


def synthetic_kind(block):
    for i in block.instructions:
        if isinstance(i.statement, BreakStatement):
            return "break"
        if isinstance(i.statement, ContinueStatement):
            return "continue"
    return None


def scan(root, cfg):
    edges = {}
    nodes = set()
    satellites = set()
    loops = []

    def add(u, vs):
        edges.setdefault(u, set()).update(vs)

    def flow(node, cont, ctx):
        """Entry blocks of `node`; `cont` is where control goes when it completes."""
        if isinstance(node, BasicBlock):
            nodes.add(node)
            kind = synthetic_kind(node) if node.address < 0 else None
            if kind == "break":
                add(node, ctx["break"] if ctx["break"] is not None else cont)
            elif kind == "continue":
                add(node, ctx["continue"] if ctx["continue"] is not None else cont)
            else:
                term = node.terminator
                if isinstance(term, (TerminatorReturn, TerminatorThrow)):
                    pass
                elif term is None:
                    add(node, cont)
                else:
                    raise Unknown(type(term).__name__)
            return {node}
        if isinstance(node, SequenceRegion):
            current_cont = cont
            for child in reversed(node.children):
                current_cont = flow(child, current_cont, ctx)
            return set(current_cont)
        if isinstance(node, IfRegion):
            then = flow(node.then_body, cont, ctx) if node.then_body is not None else set(cont)
            other = flow(node.else_body, cont, ctx) if node.else_body is not None else set(cont)
            return then | other
        if isinstance(node, LoopRegion):
            for attr in ("header_block", "condition_block", "update_block", "continue_target", "break_target"):
                block = getattr(node, attr, None)
                if isinstance(block, BasicBlock):
                    satellites.add(block)
            first = flow(node.body, set(cont), {"break": set(cont), "continue": set(cont)})
            entries = set(first)
            inner = {"break": set(cont), "continue": entries}
            entries = flow(node.body, entries | set(cont), inner)
            loops.append((node, entries))
            return entries | set(cont)
        if isinstance(node, TryRegion):
            if node.finally_ is not None:
                raise Unknown("finally")
            body = flow(node.try_body, cont, ctx)
            catch = set()
            if node.catch is not None:
                catch = flow(node.catch.body, cont, ctx)
            for block in node.try_body.covered_blocks:
                add(block, catch)
            return body
        if isinstance(node, SwitchRegion):
            entries = set()
            next_entries = set(cont)
            inner = dict(ctx)
            inner["break"] = set(cont)
            default = flow(node.default_body, cont, inner) if node.default_body is not None else set(cont)
            next_entries = default | set(cont)
            for case in reversed(node.cases):
                got = flow(case.body, next_entries | set(cont), inner)
                entries |= got
                next_entries = got
            return entries | default
        raise Unknown(type(node).__name__)

    flow(root, set(), {"break": None, "continue": None})

    for loop, entries in loops:
        exits = set()
        for b in loop.body.covered_blocks:
            for s in b.successors:
                exits.add(s)
        for block in loop.body.covered_blocks:
            if block in nodes:
                add(block, entries)
        for sat in satellites:
            add(sat, entries)

    def reach(start):
        seen = set()
        stack = list(edges.get(start, ()))
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(edges.get(cur, ()))
        return seen

    lost = []
    for u in nodes:
        if u.address < 0:
            continue
        r = None
        for v in u.successors:
            if v in satellites or v in nodes and v.address < 0:
                continue
            if v not in nodes:
                # An uncovered block: only a problem when it holds a statement or an exit.
                if v.instructions and (v.terminator is not None or any(i.statement is not None for i in v.instructions)):
                    lost.append((u.address, v.address, "block missing"))
                continue
            if r is None:
                r = reach(u)
            if v not in r and not _bare_undefined_return(v) and not _returns_undefined_register(v, cfg):
                lost.append((u.address, v.address, "edge lost"))
    return lost


def _bare_undefined_return(block):
    """`return undefined`: what falling off the end of the function does anyway."""
    if not isinstance(block.terminator, TerminatorReturn) or block.successors:
        return False
    return all(
        i.statement is None and (i.value is None or type(i.value).__name__ in ("UndefinedLiteral", "Undefined"))
        for i in block.instructions
    ) and len(block.instructions) <= 2


def count_lost_edges(root, cfg) -> int:
    """Number of lost `edge lost` paths; 0 when the tree has a shape the scan does not model."""
    try:
        return sum(1 for entry in scan(root, cfg) if entry[2] == "edge lost")
    except (Unknown, RecursionError):
        return 0


def _returns_undefined_register(block, cfg) -> bool:
    """`return r0` where nothing ever sets `r0` to anything but `undefined` (96/7599, 96/7236): falling off
    the end of the function is the same result."""
    terminator = block.terminator
    if not isinstance(terminator, TerminatorReturn) or block.successors:
        return False

    value = terminator.value
    if type(value).__name__ == "UndefinedLiteral":
        return True
    if type(value).__name__ != "Identifier":
        return False

    found = False
    for other in cfg.blocks:
        for i in other.instructions:
            if i.dest_reg is None or f"r{i.dest_reg}" != value.name:
                continue
            if type(i.value).__name__ != "UndefinedLiteral":
                return False
            found = True

    return found
