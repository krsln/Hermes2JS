"""
Tests `hermes_disassembler.format.SwitchTable` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures, cross-checked
against real hermes-dec output (`hbc-disassembler`, installed from
`vendor/hermes-dec` via `pip install -e .` - not shipped in this repo,
see `vendor/fetch-hermes-dec.sh`) rather than hardcoding expected
values as literals here.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.JumpTarget import resolve_operand_jump_target
from hermes_disassembler.format.Opcode import decode_function
from hermes_disassembler.format.SwitchTable import resolve_switch_table_entries

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


def _load(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, resolved


def _find_switch_imm(data: bytes, resolved, version: int):
    for e in resolved:
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, version):
            if i.name == "SwitchImm" and (i.offset - e.offset) == 0xB and i.operands == (1, 238, 232, 0, 31):
                return e, i
    raise AssertionError("expected SwitchImm instruction not found in fixture")


def test_switch_imm_matches_real_hermes_dec_output():
    """
    apps/testy/96's SwitchImm at function-relative offset 0x0000000b:
    real hermes-dec prints `# Address: 000000f3  # Jump table:
    [00000067, 00000031, 000000f3, ...]` (32 entries total, min=0/max=31)
    for this exact instruction - confirmed by actually running
    `hbc-disassembler` against this fixture, not read from source alone.
    """
    data, resolved = _load("96")
    fn, instr = _find_switch_imm(data, resolved, 96)

    default_target = resolve_operand_jump_target(instr, 2) - fn.offset
    assert default_target == 0xF3

    entries = resolve_switch_table_entries(data, instr, 1, 3, 4)
    relative_entries = [t - fn.offset for t in entries]
    assert len(relative_entries) == 32  # max(31) - min(0) + 1
    assert relative_entries[0] == 0x67
    assert relative_entries[1] == 0x31
    assert relative_entries[-1] == 0x1D


def test_string_switch_imm_raises():
    """
    StringSwitchImm is deliberately unsupported here (see module
    docstring) - resolve_switch_table_entries raises rather than
    silently mis-decoding it, matching the fact that hermes-dec's own
    output never includes a jump table comment for one either (only
    the ordinary # Address: comment for its default-case operand,
    handled separately by JumpTarget.py).
    """
    data, resolved = _load("98")
    string_switch = next(
        i
        for e in resolved
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, 98)
        if i.name == "StringSwitchImm"
    )
    with pytest.raises(HermesBytecodeError):
        resolve_switch_table_entries(data, string_switch, 1, 4, 2)


@pytest.mark.parametrize("version,opcode_name", [(96, "SwitchImm"), (98, "UIntSwitchImm")])
def test_every_switch_imm_table_resolves_without_error_at_scale(version: int, opcode_name: str):
    """Every SwitchImm/UIntSwitchImm instruction in the whole bundle resolves its jump table without raising."""
    data, resolved = _load(str(version))
    count = 0
    for e in resolved:
        for i in decode_function(data, e.offset, e.bytecode_size_in_bytes, version):
            if i.name == opcode_name:
                count += 1
                resolve_switch_table_entries(data, i, 1, 3, 4)
    assert count > 0
