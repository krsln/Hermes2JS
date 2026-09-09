"""
Tests `hermes_disassembler.format.JumpTarget` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.JumpTarget import is_jump_instruction, resolve_jump_target
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
    return data, resolved


def test_non_jump_instruction_returns_none():
    data, resolved = _load("96")
    fn = next(e for e in resolved if e.index == 7)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 96)
    load_param = instructions[0]
    assert load_param.name == "LoadParam"
    assert not is_jump_instruction(load_param, 96)
    assert resolve_jump_target(load_param, 96) is None


def test_guarded_load_module_jump_targets_96():
    """
    apps/testy/96 function index 7 ("guardedLoadModule", a try/catch
    module loader): hand-verified jump targets that established the
    offset formula (offset + first operand) - see JumpTarget.py's
    module docstring.
    """
    data, resolved = _load("96")
    fn = next(e for e in resolved if e.index == 7)
    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 96)
    by_relative_offset = {i.offset - fn.offset: i for i in instructions}

    jmp = by_relative_offset[62]
    assert jmp.name == "Jmp"
    assert resolve_jump_target(jmp, 96) - fn.offset == 87  # lands on LoadConstFalse (try succeeded)

    jmp_true = by_relative_offset[20]
    assert jmp_true.name == "JmpTrue"
    assert resolve_jump_target(jmp_true, 96) - fn.offset == 95

    jmp_false = by_relative_offset[33]
    assert jmp_false.name == "JmpFalse"
    assert resolve_jump_target(jmp_false, 96) - fn.offset == 95  # converges with JmpTrue's target


@pytest.mark.parametrize("version,expected_jump_count", [("96", 26716), ("98", 35178)])
def test_every_jump_in_bundle_lands_on_an_instruction_boundary(version: str, expected_jump_count: int):
    """
    Every jump instruction in every function of the bundle, decoded and
    resolved, lands exactly on another instruction's start offset (or
    exactly at its function's end) - never out of bounds, never
    mid-instruction. This is the mass-validation that confirmed the
    offset formula at scale (26716 / 35178 jumps, all landing exactly)
    rather than trusting the three hand-picked examples above alone.
    """
    data, resolved = _load(version)

    total_jumps = 0
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        starts = {i.offset for i in instructions}
        func_end = e.offset + e.bytecode_size_in_bytes

        for instruction in instructions:
            if not is_jump_instruction(instruction, int(version)):
                continue
            total_jumps += 1
            target = resolve_jump_target(instruction, int(version))
            assert e.offset <= target <= func_end, f"function {e.index}: jump at {instruction.offset} target {target} out of bounds"
            assert target in starts or target == func_end, f"function {e.index}: jump at {instruction.offset} target {target} not on an instruction boundary"

    assert total_jumps == expected_jump_count
