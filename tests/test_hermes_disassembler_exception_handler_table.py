"""
Tests `hermes_disassembler.format.ExceptionHandlerTable` against the
real `apps/testy/96` and `apps/testy/98` bundle fixtures.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.ExceptionHandlerTable import ExceptionHandler, resolve_exception_handlers
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function

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


def test_non_overflowed_handler_matches_instruction_boundaries_exactly():
    """
    apps/testy/96 function index 7 (guardedLoadModule): the exact
    hand-verified case that established the non-overflowed formula
    (info_offset points directly at the table, no large-header prefix) -
    see ExceptionHandlerTable.py's module docstring.
    """
    data, resolved = _load("96")
    guarded_load_module = next(e for e in resolved if e.index == 7)
    assert not guarded_load_module.was_large_header

    handlers = resolve_exception_handlers(data, guarded_load_module, 96)
    assert handlers == (ExceptionHandler(start=42, end=62, target=64),)

    instructions = decode_function(
        data, guarded_load_module.offset, guarded_load_module.bytecode_size_in_bytes, 96
    )
    starts = {i.offset - guarded_load_module.offset for i in instructions}
    assert handlers[0].start in starts
    assert handlers[0].target in starts


def test_overflowed_handler_matches_instruction_boundaries_exactly():
    """
    apps/testy/98 function index 1: the exact hand-verified case that
    established the overflowed formula (table follows the 37-byte large
    header, aligned to 4 bytes) - see ExceptionHandlerTable.py's module
    docstring and FunctionHeaderOverflow.py's for why 37, not
    hermes-dec's own (buggy, one byte short) 36, is correct for v98.
    """
    data, resolved = _load("98")
    fn = next(e for e in resolved if e.index == 1)
    assert fn.was_large_header

    handlers = resolve_exception_handlers(data, fn, 98)
    assert len(handlers) == 1
    assert handlers[0].start == 3
    assert handlers[0].end == 42
    assert handlers[0].target == 42

    instructions = decode_function(data, fn.offset, fn.bytecode_size_in_bytes, 98)
    starts = {i.offset - fn.offset for i in instructions}
    assert handlers[0].start in starts
    assert handlers[0].target in starts


def test_no_exception_handler_returns_empty_tuple():
    data, resolved = _load("96")
    clear_fn = next(e for e in resolved if e.index == 2)
    assert not clear_fn.has_exception_handler
    assert resolve_exception_handlers(data, clear_fn, 96) == ()


def test_overflowed_global_function_has_no_exception_handler():
    """
    Regression test for the bug FunctionHeaderOverflow.py's module
    docstring describes at length: apps/testy/96 function index 0
    ("global") was previously misdetected as `has_exception_handler=True`
    (from misreading its flags byte 6 bytes past its real position,
    under the old flat `LARGE_HEADER_SIZE=37`), with a handler table
    that never landed on real instruction boundaries. With the corrected
    31-byte v96 large-header size, it correctly decodes to
    `has_exception_handler=False` - matching
    `tools/hermes/dump_bytecode.sh`'s own real hermesc oracle output,
    which has no "Exception Handlers:" block anywhere in that
    function's ~7500-line listing (not re-run here; this only checks
    this package's own decoding, not the oracle itself).
    """
    data, resolved = _load("96")
    global_fn = next(e for e in resolved if e.index == 0)
    assert global_fn.was_large_header
    assert not global_fn.has_exception_handler
    assert resolve_exception_handlers(data, global_fn, 96) == ()


@pytest.mark.parametrize("version,expected_min_plausible_ratio", [("96", 1.0), ("98", 1.0)])
def test_most_handlers_land_on_instruction_boundaries_at_scale(version: str, expected_min_plausible_ratio: float):
    """
    Every has_exception_handler function's resolved table, across the
    whole bundle: each handler's start/target should land exactly on
    another instruction's offset within the same function. Both
    versions now hit 100% (660/660 in bytecode 96, 1082/1082 in
    bytecode 98) - bytecode 96 previously needed a 0.9 tolerance for
    one misdetected function (see
    test_overflowed_global_function_has_no_exception_handler above for
    what that was and why it no longer applies).
    """
    data, resolved = _load(version)
    eh_functions = [e for e in resolved if e.has_exception_handler]
    assert eh_functions  # sanity: both fixtures have some

    total = 0
    plausible = 0
    for e in eh_functions:
        instructions = decode_function(data, e.offset, e.bytecode_size_in_bytes, int(version))
        starts = {i.offset - e.offset for i in instructions}
        handlers = resolve_exception_handlers(data, e, int(version))
        for h in handlers:
            total += 1
            if h.start in starts and h.target in starts:
                plausible += 1

    assert total > 0
    assert plausible / total >= expected_min_plausible_ratio
