"""
Tests `hermes_disassembler.format.FunctionHeader` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures. Expected
(name, param_count) signatures were captured once from
`tools/hermes/dump_bytecode.sh <version> ...`'s function listing -
hardcoded here so this test needs no hermesc install to run.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import (
    FuncKind,
    ProhibitInvoke,
    parse_function_headers,
)
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
    return data, header, table, entries


def _signatures(entries, table) -> set[tuple[str, int]]:
    found = set()
    for e in entries:
        if e.is_overflowed:
            continue
        try:
            name = table.resolve(e.function_name)
        except Exception:
            continue
        found.add((name, e.param_count))
    return found


def test_entry_count_matches_header_96():
    _, header, _, entries = _load("96")
    assert len(entries) == header.function_count


def test_known_signatures_found_96():
    # from tools/hermes/dump_bytecode.sh 96 ...: Function<clear>(1 params...),
    # Function<define>(4 params...), Function<metroRequire>(3 params...),
    # Function<metroImportDefault>(3 params...)
    _, _, table, entries = _load("96")
    signatures = _signatures(entries, table)
    for target in [("clear", 1), ("define", 4), ("metroRequire", 3), ("metroImportDefault", 3)]:
        assert target in signatures


def test_known_signature_found_98():
    # Most bytecode-98 functions overflow (FunctionName is only 8 bits there
    # - see module docstring), so this checks a signature that survives:
    # Function<get>(1 params...), confirmed present in the oracle dump.
    _, _, table, entries = _load("98")
    signatures = _signatures(entries, table)
    assert ("get", 1) in signatures


def test_v96_overflow_is_rare():
    _, header, _, entries = _load("96")
    overflow_count = sum(1 for e in entries if e.is_overflowed)
    assert overflow_count == 3  # see module docstring


def test_v98_overflow_is_common_due_to_8bit_function_name():
    _, header, _, entries = _load("98")
    overflow_count = sum(1 for e in entries if e.is_overflowed)
    # not a bug - LAYOUT_V98's FunctionName field is only 8 bits (max 255),
    # see module docstring. Assert the majority overflow to catch any future
    # regression that would make this either 0 or 100%.
    assert 0.5 * header.function_count < overflow_count < header.function_count


def test_overflowed_entries_have_no_other_fields():
    _, _, _, entries = _load("96")
    overflowed = [e for e in entries if e.is_overflowed]
    assert overflowed  # sanity: there are some to check
    for e in overflowed:
        assert e.offset is None
        assert e.param_count is None
        assert e.function_name is None


def test_flags_decode_as_enums():
    _, _, _, entries = _load("96")
    for e in entries:
        if e.is_overflowed:
            continue
        assert isinstance(e.prohibit_invoke, ProhibitInvoke)
        assert isinstance(e.kind, FuncKind)
        assert e.kind == FuncKind.NORMAL  # LAYOUT_V96 has no Kind bits
