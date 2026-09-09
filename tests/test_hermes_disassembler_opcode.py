"""
Tests `hermes_disassembler.format.Opcode` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures.

The full-function decode tests reproduce, instruction-by-instruction,
`tools/hermes/dump_bytecode.sh`'s own listing for `clear()` in each
bundle - hardcoded here so this test needs no hermesc install to run.
This is deliberately a whole-function, opcode-by-opcode comparison
rather than a handful of spot checks: an earlier version of the v96
opcode table (generated from the `v0.12.0` git tag instead of the
actual pinned commit) decoded the *first* instruction correctly and
only diverged into garbage from the *second* instruction onward - a
single-instruction smoke test would have missed that entirely. See
`hermes_disassembler/format/Opcode.py`'s module docstring for the full
story.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function, load_opcode_table
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"

# From tools/hermes/dump_bytecode.sh <version> ...'s listing for clear()
# (the (1 params, N registers, ...) variant with no exception handler /
# debug info): (opcode_name, operand_values) in order. Operand values
# that reference the string table are the raw string_table index (not
# the resolved string) except where noted with a separate assertion.
EXPECTED_96 = [
    ("GetGlobalObject", (0,)),
    ("TryGetById", (0, 0, 1, 20)),  # id 20 -> "Map"
    ("GetByIdShort", (1, 0, 2, 206)),  # id 206 -> "prototype"
    ("CreateThis", (1, 1, 0)),
    ("Mov", (2, 1)),
    ("Construct", (0, 0, 1)),
    ("SelectObject", (0, 1, 0)),
    ("GetEnvironment", (1, 0)),
    ("StoreToEnvironment", (1, 1, 0)),
    ("Ret", (0,)),
]
EXPECTED_98 = [
    ("GetGlobalObject", (0,)),
    ("TryGetById", (0, 0, 0, 18)),  # id 18 -> "Map"
    ("CreateThisForNew", (1, 0, 1)),
    ("Mov", (2, 1)),
    ("Construct", (0, 0, 1)),
    ("SelectObject", (0, 1, 0)),
    ("GetParentEnvironment", (1, 0)),
    ("StoreToEnvironment", (1, 1, 0)),
    ("Ret", (0,)),
]


def _load(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, table, resolved


def test_v96_opcode_count():
    assert len(load_opcode_table(96)) == 206


def test_v98_opcode_count():
    assert len(load_opcode_table(98)) == 219


def test_v99_raises_not_generated():
    with pytest.raises(HermesBytecodeError):
        load_opcode_table(99)


def test_clear_decodes_exactly_96():
    data, header, table, resolved = _load("96")
    clear_fn = next(
        e for e in resolved if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == 9)

    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, 96)

    assert [(i.name, i.operands) for i in instructions] == EXPECTED_96
    # every declared byte accounted for, no gap and no overrun
    assert sum(i.size for i in instructions) == clear_fn.bytecode_size_in_bytes
    # spot-check the two string-table operands actually resolve as expected
    assert table.resolve(instructions[1].operands[3]) == "Map"
    assert table.resolve(instructions[2].operands[3]) == "prototype"


def test_clear_decodes_exactly_98():
    data, header, table, resolved = _load("98")
    clear_fn = next(
        e for e in resolved if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == 10)

    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, 98)

    assert [(i.name, i.operands) for i in instructions] == EXPECTED_98
    assert sum(i.size for i in instructions) == clear_fn.bytecode_size_in_bytes
    assert table.resolve(instructions[1].operands[3]) == "Map"


@pytest.mark.parametrize("version,expected_frame_size", [("96", 9), ("98", 10)])
def test_last_instruction_is_ret(version: str, expected_frame_size: int):
    data, header, table, resolved = _load(version)
    clear_fn = next(
        e for e in resolved
        if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == expected_frame_size
    )
    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, int(version))
    assert instructions[-1].name == "Ret"


@pytest.mark.parametrize("version,expected_count", [("96", 15247), ("98", 14267)])
def test_every_function_in_bundle_decodes_cleanly(version: str, expected_count: int):
    """
    Every function header in each bundle - including the ~2.6-3.3% with
    has_exception_handler=True, which earlier (mistaken) investigation
    suspected might need special handling - decodes with decode_function()
    landing exactly on offset + bytecode_size_in_bytes, with no
    HermesBytecodeError. has_exception_handler turned out to need no
    special casing at all: the earlier failure that looked like a
    missing preamble was entirely the v0.12.0-tag opcode table bug (see
    Opcode.py's module docstring) - this test is the regression check
    for that conclusion, across every function, not just the two spot
    checks above.
    """
    data, header, table, resolved = _load(version)
    assert len(resolved) == expected_count

    ok = 0
    for e in resolved:
        decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))  # raises on failure
        ok += 1
    assert ok == expected_count
