"""`StringSwitchImm` comes out as a `switch` (F-219).

Its case strings and targets sit in a table of the bytecode file that real hermes-dec never prints, so the decompiler
used to get a switch with no cases and printed every case body in a row. The disassembler now writes
`# String switch table: [["to top", "00000072"], ...]` and the decompiler reads it.

    98/2184  `getDirectionForKeyword`: twelve strings on eight bodies (two spellings per corner)
    98/2140  `getNativeComponentAttributes`: the cases jump to the `if` behind the switch, which the structurer had
             built before, so the test block of that `if` is the merge
"""

from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function
from hermes_disassembler.format.StringTable import StringTable
from hermes_disassembler.format.SwitchTable import resolve_string_switch_entries

_DATA = Path(__file__).parent / "data"
_BUNDLE = Path(__file__).resolve().parent.parent / "apps" / "testy" / "98" / "index.android.bundle"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_table_is_read_from_the_bundle():
    if not _BUNDLE.is_file():
        pytest.skip(f"fixture not found: {_BUNDLE}")

    data = _BUNDLE.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    resolved = resolve_overflowed_headers(data, header, parse_function_headers(data, header))

    for entry in resolved:
        for instruction in decode_function(data, entry.offset, entry.bytecode_size_in_bytes, header.version):
            if instruction.name == "StringSwitchImm" and instruction.operands == (1, 3, 86, 82, 12):
                cases = [(table.resolve(s), target - entry.offset) for s, target in
                         resolve_string_switch_entries(data, instruction)]

                assert len(cases) == 12
                assert cases[0] == ("to top", 0x72)
                assert dict(cases)["to top right"] == dict(cases)["to right top"] == 0x52
                return

    raise AssertionError("the StringSwitchImm of 98/2184 was not found")


def test_the_cases_are_strings_and_spellings_share_a_body():
    out = _render("string_switch_98_2184.hasm", 2184)

    assert "switch (r1) {" in out
    assert '            case "to bottom left":\n            case "to left bottom":\n' in out
    assert '            case "to top":\n' in out
    assert "Raw TerminatorSwitch" not in out
    assert "goto" not in out


def test_a_switch_whose_merge_is_the_test_of_an_if():
    out = _render("string_switch_merge_98_2140.hasm", 2140)

    assert 'case "CGColor":' in out
    assert "goto" not in out
