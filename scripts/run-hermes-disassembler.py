#!/usr/bin/env python3
"""
Disassembles a Hermes bytecode `.bundle` into a hermes-dec-compatible
`output.hasm`, using `hermes_disassembler` (this repo's MIT-licensed,
in-repo disassembler) instead of `vendor/hermes-dec` (AGPL, fetched
separately - see `vendor/fetch-hermes-dec.sh` and `vendor/run-hermes-dec.sh`,
which this script mirrors the interface of on purpose: same positional
bundle argument, same `<bundle-dir>/output/output.hasm` default output
location, so either tool drops into the existing README/USAGE.md
pipeline - `scripts/split_output_file.py`, `hermes_decompiler/` -
unchanged).

Unlike run-hermes-dec.sh, this script does not need a bytecode version
argument: `BytecodeFileHeader.parse()` reads it directly from the
bundle's own header.

Usage:
    python3 scripts/run-hermes-disassembler.py <bundle-path> [output-path]

    python3 scripts/run-hermes-disassembler.py apps/testy/96/index.android.bundle
    python3 scripts/run-hermes-disassembler.py apps/testy/96/index.android.bundle apps/testy/96/output
    python3 scripts/run-hermes-disassembler.py apps/testy/96/index.android.bundle apps/testy/96/output/custom.hasm

[output-path] may be a directory (an `output.hasm` is created inside
it, creating the directory if needed - matching run-hermes-dec.sh's
convention) or an exact file path ending in `.hasm`. If omitted,
defaults to `<bundle-dir>/output/output.hasm`, exactly like
run-hermes-dec.sh.

Exits non-zero with a clear message (not a traceback) for a missing
input file or an unsupported bytecode version - see
`hermes_disassembler.format.BytecodeFileHeader.VERSION_TO_LAYOUT` and
`hermes_disassembler.format.Opcode.load_opcode_table` for which
versions are currently supported (96 and 98 as of this writing; 99 is
missing an opcode table, and no version past what those two modules
confirm should be assumed to work - see their module docstrings).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.emit.HasmWriter import format_bundle
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.StringTable import StringTable


def resolve_output_path(bundle_path: Path, output_arg: str | None) -> Path:
    if output_arg is None:
        return bundle_path.parent / "output" / "output.hasm"
    output_path = Path(output_arg)
    if output_path.suffix == ".hasm":
        return output_path
    return output_path / "output.hasm"


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv

    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 1

    if len(argv) > 2:
        print("❌ Too many arguments.", file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 1

    bundle_path = Path(argv[0]).resolve()
    if not bundle_path.is_file():
        print(f"❌ Bundle not found:\n   {bundle_path}", file=sys.stderr)
        return 1

    output_path = resolve_output_path(bundle_path, argv[1] if len(argv) > 1 else None)

    print("🔍 Reading bundle...")
    data = bundle_path.read_bytes()

    try:
        header = BytecodeFileHeader.parse(data)
        print(
            f"   bytecode version: {header.version}  ({header.function_count} functions, {header.string_count} strings)")

        table = StringTable.parse(data, header)

        print("🔍 Disassembling...")
        t0 = time.time()
        text = format_bundle(data, header, table, header.version)
        elapsed = time.time() - t0
    except HermesBytecodeError as exc:
        print(f"❌ {exc}", file=sys.stderr)
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text)

    print(f"✅ Done in {elapsed:.1f}s.")
    print(f"📁 Output: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
