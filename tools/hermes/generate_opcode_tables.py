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

Semantics: operands tagged `string_id`/`function_id`/`bigint_id` come
from BytecodeList.def's own `OPERAND_STRING_ID`/`_FUNCTION_ID`/
`_BIGINT_ID` macros. `builtin_id` (GetBuiltinClosure/CallBuiltin/
CallBuiltinLong's builtin-number operand) has no such macro - confirmed
by reading each opcode's own doc comment ("Arg2 is the builtin
number") rather than a machine-checkable annotation - so it's a small,
hand-maintained override list (`_MANUAL_SEMANTICS` below) instead.
Verify against a real bundle before trusting a newly added entry there,
same discipline as everything else in this file.

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
_SEMANTIC_RE = re.compile(r"^OPERAND_(STRING|FUNCTION|BIGINT)_ID\((\w+),\s*(\d+)\)$")
_SEMANTIC_TAG = {"STRING": "string_id", "FUNCTION": "function_id", "BIGINT": "bigint_id"}

# BytecodeList.def has no OPERAND_*_ID-style macro for builtin-number
# operands - confirmed by reading each opcode's own doc comment ("Arg2
# is the builtin number") rather than a machine-checkable annotation,
# so this list is hand-maintained. 0-based operand index.
_MANUAL_SEMANTICS: dict[str, dict[int, str]] = {
    "GetBuiltinClosure": {1: "builtin_id"},
    "CallBuiltin": {1: "builtin_id"},
    "CallBuiltinLong": {1: "builtin_id"},
}

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


def parse_opcodes(def_text: str) -> list[tuple[str, list[str], dict[int, str]]]:
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

    # Second pass: OPERAND_STRING_ID(name, argnum) / _FUNCTION_ID / _BIGINT_ID
    # lines reference an opcode by name with a 1-based argument index -
    # e.g. `OPERAND_STRING_ID(GetByIdShort, 4)` means GetByIdShort's 4th
    # operand (a plain UInt8 by raw type) is a string-table index, and
    # hermes-dec's text format shows it as `string_id: N` instead of
    # `UInt8: N`. Collect these by name, then attach to every matching
    # opcode entry (a name can appear more than once only for the
    # Jmp/JmpLong pairs generated above, none of which take these
    # annotations, so a name->tags dict is unambiguous here).
    semantics_by_name: dict[str, dict[int, str]] = {
        name: dict(tags) for name, tags in _MANUAL_SEMANTICS.items()
    }
    for raw_line in def_text.splitlines():
        line = raw_line.strip()
        m = _SEMANTIC_RE.match(line)
        if m:
            kind, name, argnum = m.groups()
            semantics_by_name.setdefault(name, {})[int(argnum) - 1] = _SEMANTIC_TAG[kind]

    return [
        (name, operands, semantics_by_name.get(name, {}))
        for name, operands in opcodes
    ]


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
        "opcodes": [
            {
                "name": name,
                "operands": operands,
                # keys are stringified 0-based operand indices (JSON has no int keys);
                # value is "string_id" | "function_id" | "bigint_id". Absent entirely
                # for opcodes with no such operand - most opcodes.
                **({"semantics": {str(i): tag for i, tag in semantics.items()}} if semantics else {}),
            }
            for name, operands, semantics in opcodes
        ],
    }, indent=2) + "\n")

    print(f"bytecode {bytecode_version}: commit={commit} opcode_count={len(opcodes)}")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
