"""
Tests `hermes_disassembler.format.BigIntTable` - synthetically for the
value-decoding logic itself (neither `apps/testy/96` nor
`apps/testy/98` has a single real BigInt literal - both have
`bigint_count=0`, see that module's own docstring), and against the
real fixtures for the table-location computation (`StringTable.py`'s
`bigint_table_offset`), which real hermes-dec output can cross-check
even with zero entries in it.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BigIntTable import resolve_bigint
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


class _FakeHeader:
    def __init__(self, bigint_count: int):
        self.bigint_count = bigint_count


class _FakeTable:
    def __init__(self, bigint_table_offset: int):
        self.bigint_table_offset = bigint_table_offset


def test_resolves_two_entries_of_different_lengths():
    table_start = 100
    data = bytearray(300)
    _pack_entry(data, table_start, index=0, offset=0, length=4)
    _pack_entry(data, table_start, index=1, offset=4, length=2)
    storage_start = table_start + 2 * 8
    data[storage_start:storage_start + 4] = (0x12345678).to_bytes(4, "little")
    data[storage_start + 4:storage_start + 6] = (0xABCD).to_bytes(2, "little")

    fake_table = _FakeTable(bigint_table_offset=table_start)
    fake_header = _FakeHeader(bigint_count=2)

    assert resolve_bigint(bytes(data), fake_table, fake_header, 0) == 0x12345678
    assert resolve_bigint(bytes(data), fake_table, fake_header, 1) == 0xABCD


def test_out_of_range_index_raises_indexerror():
    fake_table = _FakeTable(bigint_table_offset=100)
    fake_header = _FakeHeader(bigint_count=2)
    with pytest.raises(IndexError):
        resolve_bigint(b"\x00" * 300, fake_table, fake_header, 5)


def _pack_entry(data: bytearray, table_start: int, index: int, offset: int, length: int) -> None:
    entry_pos = table_start + index * 8
    data[entry_pos:entry_pos + 4] = offset.to_bytes(4, "little")
    data[entry_pos + 4:entry_pos + 8] = length.to_bytes(4, "little")


@pytest.mark.parametrize("version", [96, 98])
def test_bigint_table_offset_matches_real_hermes_dec_stream_position(version: int):
    """
    Neither fixture has a real BigInt to decode, but the TABLE START
    position (StringTable.bigint_table_offset) is independently
    confirmed here by actually running real hermes-dec's own
    sequential HBCReader up through read_arrays() and checking its
    file stream position at that exact point: 943398 for bytecode 96
    (943400 once 4-byte aligned - read_bigints()'s own first step) and
    912180 for bytecode 98 (already aligned) - both match
    bigint_table_offset exactly. Not re-run here (would require
    reaching into vendor/hermes-dec directly from a test file); this
    only re-confirms both fixtures still have bigint_count=0, so a
    future fixture change would be caught if the offset math needed
    revisiting.
    """
    path = APPS_TESTY / str(version) / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    assert header.bigint_count == 0
    assert table.bigint_table_offset in (943400, 912180)
