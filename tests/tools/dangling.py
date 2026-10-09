"""
Dangling-register measurement: registers (rN) that are read but never defined
(or read before their first definition). Acts as a correctness proxy for the
decompiler output.

python dangling.py [output.json] [repo_root]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Repo / path setup
# ---------------------------------------------------------------------------

def get_repo_root() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return os.getcwd()


REPO = Path(sys.argv[2] if len(sys.argv) > 2 else get_repo_root()).resolve()
sys.path.insert(0, str(REPO))

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.frontend.batch_pipeline import BatchContext, BatchPipeline
from hermes_decompiler.frontend.batch_pipeline.stages import (
    ClassEnvironmentTableStage,
    CreatorTableStage,
    EnvironmentOriginTableStage,
    PrivateNameTableStage,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT = REPO / "apps" / "demo" / "fixtures"
FN_RE = re.compile(r"^function_(\d+)_(.+)\.hasm$")
REG_RE = re.compile(r"\br\d+\b")

# Patterns that introduce a definition of a register
DEF_PATTERNS = [
    re.compile(r"(\br\d+\b)\s*(?:[-+*/%&|^]|\*\*|<<|>>>?|\?\?|&&|\|\|)?=(?!=)"),
    re.compile(r"\b(?:const|let|var)\s+(\br\d+\b)"),
    re.compile(r"\bcatch\s*\(\s*(\br\d+\b)"),
    re.compile(r"(?:\+\+|--)(\br\d+\b)"),
    re.compile(r"(\br\d+\b)(?:\+\+|--)"),
]

# Patterns that introduce multiple definitions (destructuring, params, …)
GROUP_DEF_PATTERNS = [
    re.compile(r"\b(?:const|let|var)\s+[\[{]([^\]}]*)[\]}]"),
    # Destructuring assignment statement: `[a, b] = src`, and the nested /
    # holey / defaulted / rest forms `[[a, b], , [, c]] = src`,
    # `[a = 0, ...b] = src`. The pattern runs from the opening bracket to the
    # LAST `]`/`}` that is followed by `=` on the line (lazy, so the first such
    # one); a class that excluded `]` stopped at the first inner bracket and
    # left the nested targets looking undefined.
    re.compile(r"(?m)^\s*[\[{]([^\n]*?)[\]}]\s*=(?![=>])"),
    re.compile(r"\bfunction\b[^(\n]*\(([^)]*)\)"),
    re.compile(r"\(([^()]*)\)\s*=>"),
]

# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

# Comments and string literals are matched by ONE alternation, left to right,
# so whichever starts first wins. Stripping comments in a separate earlier pass
# treated the `//` inside a string ("https://...") as a line comment, deleted
# the rest of the line including the closing quote, and the orphaned `"` then
# swallowed code up to the next quote - hiding real definitions and producing
# false "never defined" / "read before defined" results.
#
# '...' and "..." cannot contain a raw newline in JS, so they never span
# lines; a stray quote can no longer run on into later statements. Template
# literals can span lines.
_COMMENT_OR_STRING_RE = re.compile(
    r"""
      /\*.*?\*/                      # block comment
    | //[^\n]*                       # line comment
    | "(?:\\.|[^"\\\n])*"            # double-quoted string
    | '(?:\\.|[^'\\\n])*'            # single-quoted string
    | `(?:\\.|[^`\\])*`              # template literal
    """,
    re.S | re.X,
)


def strip_comments_and_strings(js: str) -> str:
    """Remove comments and replace string/template literals with empty strings."""
    return _COMMENT_OR_STRING_RE.sub(
        lambda m: '""' if m.group(0)[0] in "\"'`" else "",
        js,
    )


def analyze(js: str) -> tuple[set[str], set[str]]:
    """
    Return (never_defined, read_before_def).

    - never_defined: registers that appear but have no definition site
    - read_before_def: registers whose first use occurs before their first definition
    """
    js = strip_comments_and_strings(js)

    # Neutralise the update expression of for-loops so we don't count them as uses
    js = re.sub(
        r"(for\s*\([^;\n]*;[^;\n]*;)([^\n]*)(\)\s*\{)",
        lambda m: m.group(1) + REG_RE.sub(lambda x: "_" * len(x.group(0)), m.group(2)) + m.group(3),
        js,
    )

    all_regs = set(REG_RE.findall(js))
    first_def: dict[str, int] = {}
    first_use: dict[str, int] = {}

    for pat in DEF_PATTERNS:
        for m in pat.finditer(js):
            reg = m.group(1)
            first_def[reg] = min(first_def.get(reg, 10 ** 12), m.start(1))

    for pat in GROUP_DEF_PATTERNS:
        for m in pat.finditer(js):
            for r in REG_RE.finditer(m.group(1)):
                reg = r.group(0)
                pos = m.start(1) + r.start()
                first_def[reg] = min(first_def.get(reg, 10 ** 12), pos)

    for m in REG_RE.finditer(js):
        reg = m.group(0)
        first_use.setdefault(reg, m.start())

    never_defined = {r for r in all_regs if r not in first_def}
    read_before_def = {
        r for r in all_regs
        if first_def.get(r, 10 ** 12) > first_use.get(r, 10 ** 12)
    }

    return never_defined, read_before_def


def build_batch_tables(sections_dir: Path) -> Any:
    sections = [
        (int(FN_RE.match(p.name).group(1)), p.read_text(encoding="utf-8"))
        for p in sorted(sections_dir.glob("function_*.hasm"))
        if FN_RE.match(p.name)
    ]
    pipeline = BatchPipeline([
        CreatorTableStage(),
        EnvironmentOriginTableStage(),
        PrivateNameTableStage(),
        ClassEnvironmentTableStage(),
    ])
    return pipeline.run(BatchContext(sections=sections)).to_batch_tables()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT = SCRIPT_DIR / "dangling.json"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure dangling registers in decompiled Hermes bytecode fixtures."
    )
    parser.add_argument(
        "output",
        nargs="?",
        default=str(DEFAULT_OUTPUT),
        help=f"Output JSON file (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "repo",
        nargs="?",
        default=None,
        help="Repository root (default: auto-detect via git)",
    )
    args = parser.parse_args()

    global REPO, ROOT
    if args.repo:
        REPO = Path(args.repo).resolve()
        sys.path.insert(0, str(REPO))
        ROOT = REPO / "apps" / "demo" / "fixtures"

    results: dict[str, dict] = {}
    errors: dict[str, str] = {}

    fixture_dirs = sorted(
        p for p in ROOT.iterdir()
        if p.is_dir() and (p / "sections").is_dir()
    )

    if not fixture_dirs:
        print(f"No fixture directories found under {ROOT}", file=sys.stderr)
        sys.exit(1)

    for fx in fixture_dirs:
        sections_dir = fx / "sections"
        try:
            batch_tables = build_batch_tables(sections_dir)
        except Exception as e:
            errors[fx.name] = f"batch_tables: {e!r}"[:200]
            continue

        fixture_result: dict[str, dict] = {}

        for hasm_path in sorted(sections_dir.glob("function_*.hasm")):
            m = FN_RE.match(hasm_path.name)
            if not m:
                continue

            func_id = int(m.group(1))
            func_name = m.group(2)
            key = f"{func_id}_{func_name}"

            try:
                source = hasm_path.read_text(encoding="utf-8")
                ctx = Decompiler.build_context(
                    source, func_id, strict=False, batch_tables=batch_tables
                )
                js = Decompiler.render(ctx, verbose=True, raw=False)
            except Exception as e:
                errors[f"{fx.name}/{func_id}"] = repr(e)[:200]
                continue

            never, order = analyze(js)
            fixture_result[key] = {
                "never_defined": sorted(never),
                "read_before_def": sorted(order - never),
            }

        results[fx.name] = fixture_result

    # ---- Summary (English) -------------------------------------------------
    print("=== Dangling-register summary ===")
    for fx_name, res in results.items():
        never_count = sum(len(v["never_defined"]) for v in res.values())
        order_count = sum(len(v["read_before_def"]) for v in res.values())
        never_funcs = sum(1 for v in res.values() if v["never_defined"])
        order_funcs = sum(1 for v in res.values() if v["read_before_def"])

        print(
            f"{fx_name}: "
            f"functions={len(res)}  "
            f"never_defined={never_count} (in {never_funcs} funcs)  "
            f"read_before_def={order_count} (in {order_funcs} funcs)"
        )

    print(f"errors: {len(errors)}")
    if errors:
        for k, v in list(errors.items())[:10]:
            print(f"  {k}: {v}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

    # ---- Write JSON --------------------------------------------------------
    # out_path = Path(args.output).resolve()
    # out_path.parent.mkdir(parents=True, exist_ok=True)  # güvenlik için
    # with out_path.open("w", encoding="utf-8") as f:
    #     json.dump({"results": results, "errors": errors}, f, indent=2)
    #
    # print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
