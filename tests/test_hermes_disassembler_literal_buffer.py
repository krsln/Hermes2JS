"""
Tests `hermes_disassembler.format.LiteralBuffer` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.LiteralBuffer import decode_literal_buffer
from hermes_disassembler.format.Opcode import decode_function
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


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


def test_decodes_byte_verified_single_element_array_96():
    """
    Hand-verified byte-for-byte: offset base+3 is 0x71 (IntegerTag,
    run length 1), payload 01 00 00 00 = 1 - see LiteralBuffer.py's
    module docstring.
    """
    data, header, table, resolved = _load("96")
    values = decode_literal_buffer(data, table.literal_value_buffer_offset + 3, 1, table)
    assert values == (1,)


def test_decodes_byte_verified_three_element_array_96():
    """Same hand-verified region: offset base+8 is 3 consecutive Integer tag+run, values 2, 578, 1478."""
    data, header, table, resolved = _load("96")
    values = decode_literal_buffer(data, table.literal_value_buffer_offset + 8, 3, table)
    assert values == (2, 578, 1478)


def test_matches_oracle_array_buffer_dump_sequence_96():
    """
    Reproduces the exact start of tools/hermes/dump_bytecode.sh's own
    "Array Buffer:" section (a raw sequential walk from byte 0 - NOT
    per-instruction order, see module docstring): String(1914),
    Integer(1), Integer(2), Integer(578), Integer(1478).
    """
    data, header, table, resolved = _load("96")
    base = table.literal_value_buffer_offset
    # decode the first 5 values by walking from byte 0 (mimicking the
    # oracle's own raw sequential dump, not any single instruction's view)
    values = decode_literal_buffer(data, base, 5, table)
    assert values == (table.resolve(1914), 1, 2, 578, 1478)


@pytest.mark.parametrize("version,expected_min_success_ratio", [("96", 0.98), ("98", 1.0)])
def test_every_array_instruction_decodes_at_scale(version: str, expected_min_success_ratio: float):
    """
    Every NewArrayWithBuffer/NewArrayWithBufferLong instruction in the
    bundle, decoded via its own buf_idx: 100% succeed in bytecode 98;
    bytecode 96 has a small (~1%) known-bad slice - see LiteralBuffer.py's
    module docstring for why this isn't chased further, and
    HasmWriter.py for the graceful fallback that covers it in practice.
    """
    data, header, table, resolved = _load(version)

    total = 0
    ok = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        for instruction in instructions:
            if instruction.name not in ("NewArrayWithBuffer", "NewArrayWithBufferLong"):
                continue
            total += 1
            _reg, _hint, count, buf_idx = instruction.operands
            try:
                decode_literal_buffer(data, table.literal_value_buffer_offset + buf_idx, count, table)
                ok += 1
            except Exception:
                pass

    assert total > 0
    assert ok / total >= expected_min_success_ratio
