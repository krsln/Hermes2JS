"""
Tests `hermes_disassembler.format.BytecodeFileHeader` against the real
`apps/testy/96` and `apps/testy/98` bundle fixtures already committed in
this repo. Expected values were cross-checked once against
`tools/hermes/dump_bytecode.sh <version> ...`'s own "Bytecode File
Information" block (see `BytecodeFileHeader.py`'s module docstring) -
hardcoded here so this test needs no hermesc install to run.

See `test_hermes_disassembler_oracle.py` for the live cross-check against
hermesc itself (skipped when the compiler isn't installed).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_disassembler.core.Exceptions import (
    InvalidMagicError,
    TruncatedFileError,
    UnsupportedBytecodeVersionError,
)
from hermes_disassembler.format.BytecodeFileHeader import (
    HEADER_SIZE,
    LAYOUT_V96,
    LAYOUT_V98,
    MAGIC,
    BytecodeFileHeader,
)

APPS_TESTY = Path(__file__).resolve().parent.parent / "apps" / "testy"


def _bundle(version: str) -> bytes:
    path = APPS_TESTY / version / "index.android.bundle"
    if not path.is_file():
        pytest.skip(f"fixture not found: {path}")
    return path.read_bytes()


@pytest.fixture(scope="module")
def bundle_96_bytes() -> bytes:
    return _bundle("96")


@pytest.fixture(scope="module")
def bundle_98_bytes() -> bytes:
    return _bundle("98")


def test_header_size_is_128_bytes():
    assert HEADER_SIZE == 128


def test_parses_real_bundle_96_legacy_layout(bundle_96_bytes: bytes):
    header = BytecodeFileHeader.parse(bundle_96_bytes)

    assert header.layout is LAYOUT_V96
    assert header.version == 96
    assert header.source_hash.hex() == "1d51e04b69e9eff199c798fe7d984872112bdf2c"
    assert header.file_length == len(bundle_96_bytes)
    assert header.function_count == 15247
    assert header.string_count == 18615
    assert header.string_kind_count == 3
    assert header.identifier_count == 11707
    assert header.overflow_string_count == 285
    assert header.bigint_count == 0
    assert header.regexp_count == 196
    assert header.segment_id == 0
    assert header.cjs_module_count == 0
    assert header.function_source_count == 84
    assert header.options.static_builtins is False
    assert header.options.cjs_modules_statically_resolved is False
    # v96-only fields present, v98-only fields absent:
    assert header.array_buffer_size is not None
    assert header.num_string_switch_imms is None


def test_parses_real_bundle_98_stringswitch_layout(bundle_98_bytes: bytes):
    header = BytecodeFileHeader.parse(bundle_98_bytes)

    assert header.layout is LAYOUT_V98
    assert header.version == 98
    assert header.source_hash.hex() == "0c1ff7241f4ebcf41ad75a2a9ae7d9f9cc2e34aa"
    assert header.file_length == len(bundle_98_bytes)
    assert header.function_count == 14267
    assert header.string_count == 18070
    assert header.string_kind_count == 3
    assert header.bigint_count == 0
    assert header.regexp_count == 199
    assert header.num_string_switch_imms == 7
    assert header.segment_id == 0  # was misread as 7 under the v96 layout - see module docstring
    assert header.cjs_module_count == 0
    assert header.function_source_count == 90
    assert header.options.static_builtins is False
    # v98-only fields present, v96-only fields absent:
    assert header.literal_value_buffer_size is not None
    assert header.array_buffer_size is None


def test_rejects_bad_magic():
    junk = b"\x00" * HEADER_SIZE
    with pytest.raises(InvalidMagicError) as exc_info:
        BytecodeFileHeader.parse(junk)
    assert exc_info.value.expected == MAGIC


def test_rejects_truncated_input():
    with pytest.raises(TruncatedFileError):
        BytecodeFileHeader.parse(b"\x00" * 10)


def test_rejects_unconfirmed_version():
    import struct
    # valid magic, version 97 (no confirmed layout - see versions.json: no npm hermesc exists for it)
    junk = struct.pack("<QI", MAGIC, 97) + b"\x00" * (HEADER_SIZE - 12)
    with pytest.raises(UnsupportedBytecodeVersionError) as exc_info:
        BytecodeFileHeader.parse(junk)
    assert exc_info.value.version == 97
