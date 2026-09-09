#!/usr/bin/env python3
"""
Regenerates hermes_disassembler/data/opcodes/<version>.json from
facebook/hermes's own MIT-licensed BytecodeList.def, at the exact git
commit each pinned hermes-compiler npm package (see
tools/hermes/versions.json) was built from - read from that package's
own `gitHead` metadata on the npm registry, never from a human-friendly
release tag.

Why not a tag: the first version of hermes_disassembler's opcode table
was generated from the `v0.12.0` git TAG for bytecode 96, matching
versions.json's `hermes_release: "0.12.0"` label - which turned out to
be a materially different revision than what hermes-compiler@0.14.1
(the actual pinned npm package) was built from: two opcodes
(CreateInnerEnvironment, ThrowIfHasRestrictedGlobalProperty) exist at
the real pinned commit but not at the v0.12.0 tag, which silently
shifted every later opcode's number by 2 and corrupted decoding for
any function using them. Re-derive the exact commit from npm's gitHead
every time - a version label is not a source revision.

Usage:
    python3 tools/hermes/generate_opcode_tables.py <bytecode_version> <npm_version>

    python3 tools/hermes/generate_opcode_tables.py 96 0.14.1
    python3 tools/hermes/generate_opcode_tables.py 98 250829098.0.14

Writes hermes_disassembler/data/opcodes/<bytecode_version>.json.
Prints the resolved commit hash and opcode count - cross-check the
count against a fresh `pip install --break-system-packages` isn't
possible, but DO cross-check decoded output against
tools/hermes/dump_bytecode.sh for a real function before trusting a
newly generated table (see
tests/test_hermes_disassembler_opcode.py for the pattern).
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = REPO_ROOT / "hermes_disassembler" / "data" / "opcodes"

_OPCODE_RE = re.compile(r"^DEFINE_OPCODE_(\d)\((\w+)(?:,\s*(.*))?\)$")
_JUMP_RE = re.compile(r"^DEFINE_JUMP_(\d)\((\w+)\)$")

# DEFINE_JUMP_N(name) macro-expands (see BytecodeList.def itself) to a
# short Addr8 form plus a "...Long" Addr32 form - the .def file's raw
# text never spells these out as DEFINE_OPCODE_N calls, so a naive
# line-by-line parse misses them entirely (and silently shifts every
# later opcode's number). This must be kept in sync with
# BytecodeList.def's own DEFINE_JUMP_1/2/3 macro bodies if Hermes ever
# changes them - diff a freshly fetched .def against the previous one
# before trusting a regenerated table blindly.
_JUMP_TEMPLATES = {
    "1": [(["Addr8"], ""), (["Addr32"], "Long")],
    "2": [(["Addr8", "Reg8"], ""), (["Addr32", "Reg8"], "Long")],
    "3": [(["Addr8", "Reg8", "Reg8"], ""), (["Addr32", "Reg8", "Reg8"], "Long")],
}


def fetch_git_head(npm_version_spec: str) -> str:
    url = f"https://registry.npmjs.org/hermes-compiler/{npm_version_spec}"
    with urllib.request.urlopen(url) as resp:
        data = json.load(resp)
    git_head = data.get("gitHead")
    if not git_head:
        raise RuntimeError(f"no gitHead in npm metadata for hermes-compiler@{npm_version_spec}")
    return git_head


def fetch_bytecode_list_def(commit: str) -> str:
    url = f"https://raw.githubusercontent.com/facebook/hermes/{commit}/include/hermes/BCGen/HBC/BytecodeList.def"
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode("utf-8")


def parse_opcodes(def_text: str) -> list[tuple[str, list[str]]]:
    opcodes: list[tuple[str, list[str]]] = []
    for raw_line in def_text.splitlines():
        line = raw_line.strip()
        m = _OPCODE_RE.match(line)
        if m:
            _n, name, rest = m.groups()
            operands = [o.strip() for o in rest.split(",")] if rest else []
            opcodes.append((name, operands))
            continue
        m2 = _JUMP_RE.match(line)
        if m2:
            n, name = m2.groups()
            for operand_list, suffix in _JUMP_TEMPLATES[n]:
                opcodes.append((name + suffix, list(operand_list)))
    return opcodes


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    bytecode_version, npm_version = sys.argv[1], sys.argv[2]

    commit = fetch_git_head(npm_version)
    def_text = fetch_bytecode_list_def(commit)
    opcodes = parse_opcodes(def_text)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"{bytecode_version}.json"
    out_path.write_text(json.dumps({
        "bytecode_version": int(bytecode_version),
        "npm_version": npm_version,
        "commit": commit,
        "opcodes": [{"name": name, "operands": operands} for name, operands in opcodes],
    }, indent=2) + "\n")

    print(f"bytecode {bytecode_version}: commit={commit} opcode_count={len(opcodes)}")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
