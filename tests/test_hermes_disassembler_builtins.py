"""
Tests `hermes_disassembler.format.Builtins` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures.

`GetBuiltinClosure`/`CallBuiltin`/`CallBuiltinLong`'s builtin-number
operand (tagged `builtin_id` by `Opcode.load_opcode_table`, always at
operand index 1 for these three opcodes) is resolved here for every
such instruction in both bundles, not just the one spot-checked
example already cited in `Builtins.py`'s own module docstring - see
`test_every_builtin_reference_resolves_at_scale` below for why that
matters (the same "don't trust a single spot check" lesson `Opcode.py`
and `StringTable.py`'s own test suites already apply).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.Builtins import load_builtins_table, resolve_builtin
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"

#: opcodes whose builtin_id-tagged operand is at this fixed index (see
#: Opcode.py's semantics table for CallBuiltin/CallBuiltinLong/GetBuiltinClosure -
#: all three carry it at operand index 1).
_BUILTIN_OPERAND_INDEX = 1
_BUILTIN_OPCODES = ("GetBuiltinClosure", "CallBuiltin", "CallBuiltinLong")


def _load(version: str):
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    data = path.read_bytes()
    header = BytecodeFileHeader.parse(data)
    entries = parse_function_headers(data, header)
    resolved = resolve_overflowed_headers(data, header, entries)
    return data, header, resolved


def _iter_builtin_refs(data: bytes, resolved, version: int):
    """Yield (function_index, instruction_name, builtin_index) for every builtin-referencing instruction in the bundle."""
    for e in resolved:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, version)
        for i in instructions:
            if i.name in _BUILTIN_OPCODES:
                yield e.index, i.name, i.operands[_BUILTIN_OPERAND_INDEX]


def test_v96_builtins_table_size():
    assert len(load_builtins_table(96)) == 53


def test_v98_builtins_table_size():
    assert len(load_builtins_table(98)) == 59


def test_v99_raises_not_generated():
    with pytest.raises(HermesBytecodeError):
        load_builtins_table(99)


def test_getbuiltinclosure_57_resolves_to_spawnasync_98():
    """
    The exact spot check cited in Builtins.py's own module docstring:
    apps/testy/98's GetBuiltinClosure with operand 57 resolves to
    "spawnAsync", matching real hermes-dec output's own
    `# Built-in function: [#57 spawnAsync]` comment for the same
    instruction.
    """
    assert resolve_builtin(98, 57) == "spawnAsync"


def test_out_of_range_index_raises_indexerror():
    table_size = len(load_builtins_table(96))
    with pytest.raises(IndexError):
        resolve_builtin(96, table_size)


@pytest.mark.parametrize(
    "version,expected_count,expected_unique_names",
    [(96, 1314, 5), (98, 2546, 10)],
)
def test_every_builtin_reference_resolves_at_scale(version: int, expected_count: int, expected_unique_names: int):
    """
    Every `GetBuiltinClosure`/`CallBuiltin`/`CallBuiltinLong` instruction
    in each full bundle resolves its builtin_id operand without error -
    not just the single "operand 57 -> spawnAsync" example the module
    docstring cites. Exact counts pinned here as a regression check:
    a shift in these numbers would mean either the opcode table or the
    builtins table changed under us.
    """
    data, header, resolved = _load(str(version))
    refs = list(_iter_builtin_refs(data, resolved, version))
    assert len(refs) == expected_count

    names = {resolve_builtin(version, idx) for _fn, _name, idx in refs}
    assert len(names) == expected_unique_names


def test_getbuiltinclosure_57_found_in_real_bundle_98():
    """
    Confirms the docstring's spot-check instruction actually exists in
    the fixture (rather than `test_getbuiltinclosure_57_resolves_to_spawnasync_98`
    only checking the table in isolation) - i.e. some real function in
    apps/testy/98 has a `GetBuiltinClosure` whose builtin_id operand is
    literally 57.
    """
    data, header, resolved = _load("98")
    refs = list(_iter_builtin_refs(data, resolved, 98))
    assert any(name == "GetBuiltinClosure" and idx == 57 for _fn, name, idx in refs)
