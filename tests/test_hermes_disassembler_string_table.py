"""
Tests `hermes_disassembler.format.StringTable` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures. Expected values
(first 15 strings, overflow/utf16 counts) were captured once from
`tools/hermes/dump_bytecode.sh <version> ...`'s "Global String Table:"
block - hardcoded here so this test needs no hermesc install to run.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.StringTable import StringTable

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"

# First 15 entries of "Global String Table:" from a real hermesc dump, in order.
EXPECTED_FIRST_15 = {
    "96": [
        "$$typeof", "type", "_state", "state", "Animated", "isArray", "Array",
        "y", "Boolean", "ComplexAnimationBuilder", "r", "ReanimatedError",
        "Error", "H", "HermesInternal",
    ],
    "98": [
        "$$typeof", "type", "isArray", "Array", "y", "Boolean",
        "ComplexAnimationBuilder", "r", "TypeError", "Error", "HermesInternal",
        "has", "hasOwnProperty", "data", "width",
    ],
}


def _load(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    return header, StringTable.parse(data, header)


@pytest.mark.parametrize("version", ["96", "98"])
def test_string_count_matches_header(version: str):
    header, table = _load(version)
    assert len(table.entries) == header.string_count
    assert len(table.storage) == header.string_storage_size


@pytest.mark.parametrize("version", sorted(EXPECTED_FIRST_15))
def test_first_15_strings_match_oracle(version: str):
    _, table = _load(version)
    for i, expected in enumerate(EXPECTED_FIRST_15[version]):
        assert table.resolve(i) == expected, f"i{i}"


def test_recovers_string_hermesc_truncates_in_its_own_dump():
    """
    hermesc's own `-dump-bytecode` text output shows this string as
    `"__BUNDLE_START_TI"...` (truncated at ~18 chars, see
    BytecodeFileHeader.py's module docstring for background on that
    limitation) - this module reads it from string storage directly, so
    it should come back whole.
    """
    _, table = _load("96")
    matches = [
        table.resolve(i)
        for i in range(len(table.entries))
        if table.resolve(i).startswith("__BUNDLE_START_TI")
    ]
    assert matches == ["__BUNDLE_START_TIME__"]


@pytest.mark.parametrize("version", ["96", "98"])
def test_every_string_resolves_without_error(version: str):
    _, table = _load(version)
    for i in range(len(table.entries)):
        table.resolve(i)  # raises on failure


def test_overflow_entry_count_matches_header_96():
    header, table = _load("96")
    overflow_count = sum(1 for e in table.entries if e.is_overflowed)
    assert overflow_count == header.overflow_string_count == 285


def test_utf16_entries_decode_cleanly_96():
    _, table = _load("96")
    utf16_indices = [i for i, e in enumerate(table.entries) if e.is_utf16]
    assert len(utf16_indices) == 24
    for i in utf16_indices:
        assert isinstance(table.resolve(i), str)
