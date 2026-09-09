from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


@pytest.mark.parametrize("version", ["96", "98"])
def test_data(version, capsys):
    path = APPS_TESTY / version / "index.android.bundle"

    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")

    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)

    with capsys.disabled():
        print()
        print(f"\nHermes {version}")
        print(f"  resolved:   {len(resolved)}")
        print(f"  overflowed: {len(resolved) - len(entries)}")

        print(f"  table.entries:    {len(table.entries)}")
        print(f"  table.storage:    {len(table.storage)}")

        print()
