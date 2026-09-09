"""
Tests `scripts/split_output_file.py`'s `FUNCTION_HEADER_RE`.

Regression test for a pre-existing bug: the regex required a function
header line to start with `[Function`, but real hermes-dec output (and
`hermes_disassembler.emit.HasmWriter`'s output, built to match it)
actually prefixes that line with `=> ` - confirmed against
`apps/demo/fixtures/96/sections/section_15042.hasm`, a real hermes-dec
fixture already committed in this repo. Before the fix, every function
in a hermes-dec dump fell back to anonymous `section_N` naming instead
of the descriptive `function_N_name` the code is clearly meant to
produce (`Section.base_filename()`) - visible in that same fixture
file's own name, `section_15042.hasm` rather than
`function_15042_runAllTests.hasm`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE = REPO_ROOT / "apps" / "demo" / "fixtures" / "96" / "sections" / "section_15042.hasm"


@pytest.fixture(scope="module")
def split_output_file():
    scripts_dir = str(REPO_ROOT / "scripts")
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import split_output_file as module  # noqa: PLC0415
    return module


def test_matches_real_hermes_dec_prefixed_line(split_output_file):
    if not FIXTURE.is_file():
        pytest.skip(f"fixture not found: {FIXTURE}")
    first_line = FIXTURE.read_text().splitlines()[1]  # line 0 is a leading blank line, see fixture
    assert first_line.startswith("=> [Function")

    match = split_output_file.FUNCTION_HEADER_RE.match(first_line)
    assert match is not None
    assert match.group("number") == "15042"
    assert match.group("name") == "runAllTests"


def test_still_matches_bare_form_without_prefix(split_output_file):
    """Backward compatibility: a line with no '=> ' prefix must still match."""
    match = split_output_file.FUNCTION_HEADER_RE.match('[Function #7 "foo" of 10 bytes]')
    assert match is not None
    assert match.group("number") == "7"
    assert match.group("name") == "foo"


def test_section_is_recognized_as_a_function(split_output_file, tmp_path):
    """
    End-to-end: a hermes-dec-style dump containing an '=> [Function...'
    line, split via the real iter_sections(), is recognized as a
    function section (not an anonymous one) and named accordingly.
    """
    text = (
        '=> [Function #3 "clear" of 5 bytes]: 1 params, frame size=1, '
        "strict=0, exc handler=0, debug info=0  @ offset 0x00000000\n"
        "\n"
        "Bytecode listing:\n"
        "\n"
        "==> 00000000: <Ret>: <Reg8: 0>\n"
    )
    hasm_path = tmp_path / "output.hasm"
    hasm_path.write_text(text)

    sections = list(split_output_file.iter_sections(hasm_path, split_output_file.DEFAULT_SEPARATOR))
    assert len(sections) == 1
    assert sections[0].is_function
    assert sections[0].base_filename() == "function_3_clear"
