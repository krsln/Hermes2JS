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

from hermes_decompiler.backend.analysis.flow_audit import Unknown, scan  # noqa: E402
from hermes_decompiler.backend.runtime.HermesAnalysis import HermesAnalysis  # noqa: E402
from hermes_decompiler.backend.transforms.StructuralAnalyzer import StructuralAnalyzer  # noqa: E402
from hermes_decompiler.pipeline.stages import CodeGenerationStage  # noqa: E402

records = []
current = {"fn": None, "pending": None, "by_lines": {}}

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
