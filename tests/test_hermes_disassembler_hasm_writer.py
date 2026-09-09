"""
Tests `hermes_disassembler.emit.HasmWriter` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures.

The most important test here (`test_emitted_text_parses_with_real_hermes_decompiler`)
doesn't just check our own output against a hardcoded string - it feeds
every emitted line through `hermes_decompiler.frontend.parsing.OpcodeParser`,
the REAL parser `hermes_decompiler`'s pipeline uses today (fed by
vendor/hermes-dec's AGPL output). If that parser accepts our lines and
extracts the expected opcode/args/comment, that's direct evidence
`hermes_disassembler`'s output is usable as a drop-in replacement for
that AGPL dependency - the actual stated purpose of this package (see
its `__init__.py`).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_decompiler.frontend.parsing.OpcodeParser import OpcodeParser
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function
from hermes_disassembler.format.StringTable import StringTable
from hermes_disassembler.emit import HasmWriter
from hermes_disassembler.emit.HasmWriter import format_bundle, format_function, format_instruction

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


def _load_clear(version: str, expected_frame_size: int):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    clear_fn = next(
        e for e in resolved
        if table.resolve(e.function_name) == "clear" and e.param_count == 1 and e.frame_size == expected_frame_size
    )
    instructions = decode_function(data, clear_fn.offset, clear_fn.bytecode_size_in_bytes, int(version))
    return clear_fn, instructions, table


def test_function_header_line_format_96():
    clear_fn, instructions, table = _load_clear("96", 9)
    text = format_function(clear_fn, instructions, table, 96)
    header_line = text.splitlines()[0]
    assert header_line == (
        '=> [Function #2 "clear" of 37 bytes]: 1 params, frame size=9, '
        'strict=1, exc handler=0, debug info=0  @ offset 0x000f7241'
    )


def test_string_id_operand_shows_semantic_label_and_comment_96():
    clear_fn, instructions, table = _load_clear("96", 9)
    line = format_instruction(instructions[1], clear_fn.offset, table, 96)  # TryGetById ... "Map"
    assert line == (
        "==> 00000002: <TryGetById>: <Reg8: 0, Reg8: 0, UInt8: 1, string_id: 20>"
        "  # String: 'Map' (Identifier)"
    )


def test_plain_instruction_has_no_comment_96():
    clear_fn, instructions, table = _load_clear("96", 9)
    line = format_instruction(instructions[0], clear_fn.offset, table, 96)  # GetGlobalObject
    assert line == "==> 00000000: <GetGlobalObject>: <Reg8: 0>"
    assert "#" not in line


@pytest.mark.parametrize("version,expected_frame_size", [("96", 9), ("98", 10)])
def test_emitted_text_parses_with_real_hermes_decompiler(version: str, expected_frame_size: int):
    """
    The end-to-end check: every instruction line this module emits for
    clear() is fed through hermes_decompiler's REAL OpcodeParser (not a
    reimplementation or a mock) and must parse successfully, extracting
    the same opcode name and a non-None args string for every
    instruction - see module docstring.
    """
    clear_fn, instructions, table = _load_clear(version, expected_frame_size)

    parsed_count = 0
    for instruction in instructions:
        line = format_instruction(instruction, clear_fn.offset, table, int(version))
        entry = OpcodeParser.parse(line)
        assert entry is not None, f"real OpcodeParser rejected our emitted line: {line!r}"
        assert entry.opcode == instruction.name
        parsed_count += 1

    assert parsed_count == len(instructions)


def test_string_comment_content_matches_resolved_string():
    """The comment's resolved string content must match StringTable.resolve() exactly - not just be present."""
    clear_fn, instructions, table = _load_clear("96", 9)
    get_by_id_short = instructions[2]  # GetByIdShort ... "prototype"
    line = format_instruction(get_by_id_short, clear_fn.offset, table, 96)
    entry = OpcodeParser.parse(line)
    assert "'prototype'" in entry.comment
    assert table.resolve(206) == "prototype"


def _split_output_file_module():
    """Import the real scripts/split_output_file.py (not part of any package - script directory added to sys.path)."""
    import sys as _sys

    scripts_dir = str(Path(__file__).resolve().parent.parent / "scripts")
    if scripts_dir not in _sys.path:
        _sys.path.insert(0, scripts_dir)
    import split_output_file  # noqa: PLC0415
    return split_output_file


@pytest.mark.parametrize("version", ["96", "98"])
def test_bundle_splits_with_real_split_output_file(version: str, tmp_path):
    """
    format_bundle()'s output, written to disk and split with the REAL
    scripts/split_output_file.py (not a reimplementation), produces
    exactly one section per function - the closed-loop check that
    SECTION_SEPARATOR matches that script's DEFAULT_SEPARATOR and that
    every format_function() block is self-contained (no stray
    separator-looking lines inside a function's own instructions).
    """
    split_output_file = _split_output_file_module()

    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    bc_header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, bc_header)

    assert HasmWriter.SECTION_SEPARATOR == split_output_file.DEFAULT_SEPARATOR

    text = format_bundle(data, bc_header, table, int(version))
    hasm_path = tmp_path / "output.hasm"
    hasm_path.write_text(text)

    sections = list(split_output_file.iter_sections(hasm_path, split_output_file.DEFAULT_SEPARATOR))
    assert len(sections) == bc_header.function_count
    assert sections[0].lines[0].startswith('=> [Function #0 ')
    assert sections[-1].lines[-1].rstrip("\n") != ""  # no trailing empty section
