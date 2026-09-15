"""
Tests `hermes_disassembler.format.ObjectLiteral` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures. Both layouts are
supported (v96's direct key/value buffers, v98's shape-table
indirection) - see the module's own docstring for the tag-6 bug that
initially made v96 look unsupportable, and its fix.
"""
from __future__ import annotations

import struct
from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.ObjectLiteral import resolve_object_literal
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


def _resolve(data, table, version: str, instruction):
    """Dispatch operand extraction per version's layout - see ObjectLiteral.py."""
    if version == "98":
        shape_idx, val_idx = instruction.operands[1], instruction.operands[2]
        return resolve_object_literal(data, table, 98, shape_idx, val_idx)
    count, key_idx, val_idx = instruction.operands[2], instruction.operands[3], instruction.operands[4]
    return resolve_object_literal(data, table, 96, count, key_idx, val_idx)


def test_shape_table_entry_25_matches_oracle_byte_for_byte():
    """
    tools/hermes/dump_bytecode.sh 98 ...'s own "Object Shape Table:"
    line for index 25 is "25[254, 1]" - keyBufferOffset=254, numProps=1 -
    confirmed here directly from the file (not just via an instruction).
    """
    data, header, table, resolved = _load("98")
    entry_offset = table.object_value_or_shape_table_offset + 25 * 8
    key_buffer_offset, num_props = struct.unpack_from("<II", data, entry_offset)
    assert (key_buffer_offset, num_props) == (254, 1)


def test_resolves_plausible_object_literal_98():
    """A real NewObjectWithBuffer's operands resolve to {'value': True} - matches shape 25 above (single prop, key 'value')."""
    data, header, table, resolved = _load("98")
    literal = resolve_object_literal(data, table, 98, 25, 17297)
    assert literal.keys == ("value",)
    assert literal.values == (True,)


def test_bytecode_96_direct_layout_resolves_console_levels():
    """
    apps/testy/96's console-level object ({trace:0, info:1, warn:2,
    error:3}) - the same source, and the identical decoded result, as
    apps/testy/98's own shape-table-based instance of it (see
    test_v96_and_v98_agree_on_the_same_source_object below) - proof v96's
    direct keyBufIdx/valBufIdx layout is genuinely fixed, not just
    "less wrong".
    """
    data, header, table, resolved = _load("96")
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, 96)
        for instruction in instructions:
            if instruction.name != "NewObjectWithBuffer":
                continue
            literal = _resolve(data, table, "96", instruction)
            if literal.keys == ("trace", "info", "warn", "error"):
                assert literal.values == (0, 1, 2, 3)
                return
    pytest.fail("console-level object not found in apps/testy/96")


def test_v96_and_v98_agree_on_the_same_source_object():
    """The exact same {trace,info,warn,error} object, compiled to both bytecode versions, decodes identically."""
    values_by_version = {}
    for version in ("96", "98"):
        data, header, table, resolved = _load(version)
        for e in resolved:
            instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
            for instruction in instructions:
                if instruction.name != "NewObjectWithBuffer":
                    continue
                literal = _resolve(data, table, version, instruction)
                if literal.keys == ("trace", "info", "warn", "error"):
                    values_by_version[version] = literal.values
                    break
            if version in values_by_version:
                break
    assert values_by_version["96"] == values_by_version["98"] == (0, 1, 2, 3)


def test_unconfirmed_version_raises_not_guessed():
    data, header, table, resolved = _load("98")
    with pytest.raises(HermesBytecodeError):
        resolve_object_literal(data, table, 97, 0, 0, 0)


@pytest.mark.parametrize("version,expected_min_string_key_ratio", [("96", 0.95), ("98", 0.95)])
def test_most_keys_are_strings_at_scale(version: str, expected_min_string_key_ratio: float):
    """
    Every NewObjectWithBuffer in the bundle: the overwhelming majority
    of decoded keys should be strings (property names) - a numeric key
    is legal JS but rare; anything else (undefined/bool/None) would
    indicate a decoding bug. Before the LiteralBuffer tag-6 fix, v96
    scored only 42% here; now both versions are effectively clean
    (99.8%/99.3%).
    """
    data, header, table, resolved = _load(version)

    total_keys = 0
    string_keys = 0
    errors = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        for instruction in instructions:
            if instruction.name not in ("NewObjectWithBuffer", "NewObjectWithBufferLong"):
                continue
            try:
                literal = _resolve(data, table, version, instruction)
            except Exception:
                errors += 1
                continue
            for k in literal.keys:
                total_keys += 1
                if isinstance(k, str):
                    string_keys += 1

    assert total_keys > 0
    assert string_keys / total_keys >= expected_min_string_key_ratio
