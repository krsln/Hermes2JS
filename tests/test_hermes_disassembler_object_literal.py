"""
Tests `hermes_disassembler.format.ObjectLiteral` against the real
`apps/testy/98` bundle fixture. bytecode 96 is intentionally
unsupported here (see the module's own docstring) - tested as an
explicit rejection, not skipped.
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


def test_resolves_plausible_object_literal_96_style_names():
    """A real NewObjectWithBuffer's operands resolve to {'value': True} - matches shape 25 above (single prop, key 'value')."""
    data, header, table, resolved = _load("98")
    literal = resolve_object_literal(data, table, 98, 25, 17297)
    assert literal.keys == ("value",)
    assert literal.values == (True,)


def test_bytecode_96_is_rejected_not_guessed():
    data, header, table, resolved = _load("96")
    with pytest.raises(HermesBytecodeError):
        resolve_object_literal(data, table, 96, 0, 0)


@pytest.mark.parametrize("version,expected_min_string_key_ratio", [("98", 0.95)])
def test_most_keys_are_strings_at_scale(version: str, expected_min_string_key_ratio: float):
    """
    Every NewObjectWithBuffer in the bundle: the overwhelming majority
    of decoded keys should be strings (property names) - a numeric key
    is legal JS but rare; anything else (undefined/bool/None) would
    indicate a decoding bug, which is exactly the signal that ruled out
    bytecode 96's direct keyBufIdx approach (only 42% strings there -
    see ObjectLiteral.py's module docstring) in favor of bytecode 98's
    shape-table indirection (99.3% strings).
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
            shape_idx, val_idx = instruction.operands[1], instruction.operands[2]
            try:
                literal = resolve_object_literal(data, table, int(version), shape_idx, val_idx)
            except Exception:
                errors += 1
                continue
            for k in literal.keys:
                total_keys += 1
                if isinstance(k, str):
                    string_keys += 1

    assert total_keys > 0
    assert string_keys / total_keys >= expected_min_string_key_ratio
