"""Find edges of the CFG that the final region tree no longer has (a silent drop).

usage: python3 scripts/audit/drop_scan.py <sections-in> <out-dir> <jsonl>
       python3 scripts/audit/drop_scan.py --report <jsonl>     (goto-free candidates)

For every function the adopted attempt's (region tree, CFG) pair is checked: each CFG edge
u -> v between blocks of the tree must still be a path in the tree's own flow graph (an
over-approximation: loops let every member reach the body entry and the exit, a `try` body
reaches its catch). A lost edge is a path the decompiled code can no longer take.
"""
import json
import sys
from pathlib import Path

if len(sys.argv) == 3 and sys.argv[1] == "--report":
    records = [json.loads(line) for line in Path(sys.argv[2]).read_text().splitlines() if line.strip()]
    found = [r for r in records if r["gotos"] == 0 and any(k[2] == "edge lost" for k in r["lost"])]
    print(f"{len(found)} goto-free functions with a lost edge")
    for r in found:
        print(r["fn"], [k for k in r["lost"] if k[2] == "edge lost"][:3])
    sys.exit(0)

if len(sys.argv) != 4:
    sys.exit(__doc__)

sections, out_dir, jsonl = sys.argv[1:4]
repo = str(Path(__file__).resolve().parent.parent.parent)
sys.path.insert(0, repo)

from hermes_decompiler.backend.analysis.cfg import BasicBlock  # noqa: E402
from hermes_decompiler.backend.regions import (  # noqa: E402
    IfRegion, LoopRegion, SequenceRegion, SwitchRegion, TryRegion,
)
from hermes_decompiler.backend.runtime.HermesAnalysis import HermesAnalysis  # noqa: E402
from hermes_decompiler.backend.transforms.StructuralAnalyzer import StructuralAnalyzer  # noqa: E402
from hermes_decompiler.ir.statements import BreakStatement, ContinueStatement  # noqa: E402
from hermes_decompiler.ir.terminators import TerminatorReturn, TerminatorThrow  # noqa: E402
from hermes_decompiler.pipeline.stages import CodeGenerationStage  # noqa: E402

records = []
current = {"fn": None, "pending": None, "by_lines": {}}


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
            if v not in r and not _bare_undefined_return(v):
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


original = StructuralAnalyzer._audit_unstructured_blocks


def audit(root, graph, cfg):
    try:
        current["pending"] = {"lost": scan(root, cfg), "unknown": None}
    except Unknown as e:
        current["pending"] = {"lost": [], "unknown": str(e)}
    except RecursionError:
        current["pending"] = {"lost": [], "unknown": "recursion"}
    return original(root, graph, cfg)


StructuralAnalyzer._audit_unstructured_blocks = staticmethod(audit)

_run = CodeGenerationStage.run


def _run_tagged(self, context):
    current["fn"] = f"{context.function_id}:{context.function_name}"
    current["by_lines"] = {}
    return _run(self, context)


CodeGenerationStage.run = _run_tagged

_gen = HermesAnalysis._generate_js


def _gen_tagged(self, verbose, raw, creator_facts, duplicate_returns):
    current["pending"] = None
    result = _gen(self, verbose, raw, creator_facts, duplicate_returns)
    if current["pending"] is not None:
        current["by_lines"][id(result[0])] = (duplicate_returns, current["pending"])
    return result


HermesAnalysis._generate_js = _gen_tagged

_warn = HermesAnalysis._warn_if_invalid_js


def _warn_tagged(self, lines, reason):
    level, found = current["by_lines"].get(id(lines), (None, None))
    if found is not None:
        records.append({"fn": current["fn"], "level": level, "lost": found["lost"][:6],
                        "n": len(found["lost"]), "unknown": found["unknown"],
                        "gotos": sum("goto label" in l for l in lines)})
    return _warn(self, lines, reason)


HermesAnalysis._warn_if_invalid_js = _warn_tagged

sys.argv = ["decompile_sections.py", "-i", sections, "-o", out_dir, "--no-verbose", "--no-raw", "--log-level", "CRITICAL"]
sys.path.insert(0, str(Path(repo) / "scripts"))
import runpy  # noqa: E402

try:
    runpy.run_path(str(Path(repo) / "scripts" / "decompile_sections.py"), run_name="__main__")
finally:
    Path(jsonl).write_text("\n".join(json.dumps(r) for r in records))
