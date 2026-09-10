#!/usr/bin/env python3
"""
Regenerates hermes_disassembler/data/builtins/<version>.json from
facebook/hermes's own MIT-licensed
include/hermes/FrontEndDefs/Builtins.def, at the exact commit each
pinned hermes-compiler npm package was built from (see
tools/hermes/generate_opcode_tables.py for why a commit, not a tag).

Builtins.def's own comment warns "DO NOT FORGET TO INCREASE THE
BYTECODE FILE FORMAT VERSION IF YOU MODIFY THIS FILE" - i.e. this list
is bytecode-version-specific, exactly like BytecodeList.def, and NOT
shared across versions: v96 and v98 (at their respective pinned
commits) differ - v96 has no "normal builtins" category at all
(NORMAL_OBJECT/NORMAL_METHOD are entirely absent), so its numbering
starts differently. Never reuse one version's table for another.

Numbering: each NORMAL_METHOD/BUILTIN_METHOD/PRIVATE_BUILTIN/JS_BUILTIN
line consumes the next sequential index (0-based), in file declaration
order - NORMAL_OBJECT/BUILTIN_OBJECT/MARK_FIRST_*_BUILTIN lines are
markers only and consume no index. Confirmed against a real bundle:
apps/testy/98's GetBuiltinClosure with operand 57 names a function
that, called immediately after, behaves like (and per hermes-dec's own
output, IS labeled) "spawnAsync" - index 57 in this file's parse is
exactly `JS_BUILTIN(spawnAsync)`.

Usage:
    python3 tools/hermes/generate_builtins_table.py <bytecode_version> <npm_version>

Writes hermes_disassembler/data/builtins/<bytecode_version>.json.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "hermes_disassembler" / "data" / "builtins"

_ENTRY_PATTERNS = [
    (re.compile(r"^NORMAL_METHOD\((\w+),\s*(\w+)\)$"), lambda m: f"{m.group(1)}.{m.group(2)}"),
    (re.compile(r"^BUILTIN_METHOD\((\w+),\s*(\w+)\)$"), lambda m: f"{m.group(1)}.{m.group(2)}"),
    (re.compile(r"^PRIVATE_BUILTIN\((\w+)\)$"), lambda m: f"HermesBuiltin_{m.group(1)}"),
    (re.compile(r"^JS_BUILTIN\((\w+)\)$"), lambda m: m.group(1)),
]


def fetch_git_head(npm_version_spec: str) -> str:
    url = f"https://registry.npmjs.org/hermes-compiler/{npm_version_spec}"
    with urllib.request.urlopen(url) as resp:
        data = json.load(resp)
    git_head = data.get("gitHead")
    if not git_head:
        raise RuntimeError(f"no gitHead in npm metadata for hermes-compiler@{npm_version_spec}")
    return git_head


def fetch_builtins_def(commit: str) -> str:
    url = f"https://raw.githubusercontent.com/facebook/hermes/{commit}/include/hermes/FrontEndDefs/Builtins.def"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def parse_builtins(def_text: str) -> list[str]:
    names: list[str] = []
    for raw_line in def_text.splitlines():
        line = raw_line.strip()
        for pattern, name_fn in _ENTRY_PATTERNS:
            m = pattern.match(line)
            if m:
                names.append(name_fn(m))
                break
    return names


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    bytecode_version, npm_version = sys.argv[1], sys.argv[2]

    commit = fetch_git_head(npm_version)
    def_text = fetch_builtins_def(commit)
    names = parse_builtins(def_text)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{bytecode_version}.json"
    out_path.write_text(json.dumps({
        "bytecode_version": int(bytecode_version),
        "npm_version": npm_version,
        "commit": commit,
        "builtins": names,
    }, indent=2) + "\n")

    print(f"bytecode {bytecode_version}: commit={commit} builtin_count={len(names)}")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
