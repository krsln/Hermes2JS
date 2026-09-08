"""
Parses the fixed-size `BytecodeFileHeader` at the start of every Hermes
bytecode (.bundle) file.

Layout source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/HBC/BytecodeFileFormat.h`. The struct has changed
shape across releases, so this module tracks two confirmed layouts
rather than assuming one universal format:

  LAYOUT_V96 ("legacy"): confirmed against tag v0.12.0 - the
  `hermes_release` `tools/hermes/versions.json` pins for bytecode 96:
  https://github.com/facebook/hermes/blob/v0.12.0/include/hermes/BCGen/HBC/BytecodeFileFormat.h
  Fields: ...regExpStorageSize, arrayBufferSize, objKeyBufferSize,
  objValueBufferSize, segmentID... - 19 uint32 fields, padding[19].

  LAYOUT_V98 ("stringswitch"): confirmed against the exact git commit
  the pinned `hermes-compiler@250829098.0.14` (bytecode 98) AND
  `hermes-compiler@260318099.0.0` (bytecode 99) npm packages were built
  from (commit hash read from each package's own `gitHead` metadata on
  the npm registry - as precise as it gets short of hermesc's source):
  https://github.com/facebook/hermes/blob/cb5bb3342f43d378cc2653e2ac9077a282b97637/include/hermes/BCGen/HBC/BytecodeFileFormat.h
  `arrayBufferSize` was renamed `literalValueBufferSize`,
  `objValueBufferSize` was replaced by `objShapeTableCount`, and a new
  `numStringSwitchImms` field was inserted right before `segmentID` -
  20 uint32 fields, padding[15] (still 128 bytes total).

Both were validated byte-for-byte against a real committed bundle
(apps/testy/96 and apps/testy/98) via `hermes_disassembler/oracle/` -
see `tests/test_hermes_disassembler_oracle.py`. LAYOUT_V96 was the
original guess and initially passed for 96; LAYOUT_V98 exists because
that same guess, applied to a 98 bundle, mis-decoded `segment_id` as 7
instead of 0 - the oracle's "StringSwitchImm count: 7" line was the
tell. Moral: don't add a third bytecode version here without running
that oracle test against a real bundle for it first.

`BytecodeFileHeader` is documented as cache-line-tuned and a multiple
of 32 bytes (`static_assert(sizeof(BytecodeFileHeader) % 32 == 0,
...)`); both layouts are exactly 128 bytes.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass
from typing import Optional

from hermes_disassembler.core.Exceptions import (
    InvalidMagicError,
    TruncatedFileError,
    UnsupportedBytecodeVersionError,
)

__all__ = [
    "BytecodeFileHeader", "BytecodeOptions", "HeaderLayout",
    "MAGIC", "HEADER_SIZE", "LAYOUT_V96", "LAYOUT_V98", "VERSION_TO_LAYOUT",
]

#: "Hermes" in ancient Greek encoded in UTF-16BE and truncated to 8 bytes.
#: (hermes/include/hermes/BCGen/HBC/BytecodeFileFormat.h)
MAGIC = 0x1F1903C103BC1FC6

HEADER_SIZE = 128  # both layouts; asserted per-layout below


@dataclass(frozen=True, slots=True)
class HeaderLayout:
    """One confirmed `BytecodeFileHeader` binary layout (see module docstring)."""

    name: str
    struct_format: str  # full struct.unpack format for the whole 128-byte header
    uint32_field_names: tuple[str, ...]  # in on-disk order, fileLength..debugInfoOffset

    def __post_init__(self):
        size = struct.calcsize(self.struct_format)
        assert size == HEADER_SIZE, f"{self.name}: expected {HEADER_SIZE} bytes, got {size}"


# '<'    little-endian, no alignment padding (matches LLVM_PACKED_START)
# Q      uint64_t magic
# I      uint32_t version
# 20s    uint8_t sourceHash[20]                  (SHA1_NUM_BYTES)
# nI     the uint32_t fields fileLength..debugInfoOffset (n = 19 or 20)
# B      BytecodeOptions (1-byte bitfield)
# ms     uint8_t padding[m]
LAYOUT_V96 = HeaderLayout(
    name="v96_legacy",
    struct_format="<QI20s19IB19s",
    uint32_field_names=(
        "file_length", "global_code_index", "function_count", "string_kind_count",
        "identifier_count", "string_count", "overflow_string_count", "string_storage_size",
        "bigint_count", "bigint_storage_size", "regexp_count", "regexp_storage_size",
        "array_buffer_size", "obj_key_buffer_size", "obj_value_buffer_size",
        "segment_id", "cjs_module_count", "function_source_count", "debug_info_offset",
    ),
)

LAYOUT_V98 = HeaderLayout(
    name="v98_stringswitch",
    struct_format="<QI20s20IB15s",
    uint32_field_names=(
        "file_length", "global_code_index", "function_count", "string_kind_count",
        "identifier_count", "string_count", "overflow_string_count", "string_storage_size",
        "bigint_count", "bigint_storage_size", "regexp_count", "regexp_storage_size",
        "literal_value_buffer_size", "obj_key_buffer_size", "obj_shape_table_count",
        "num_string_switch_imms", "segment_id", "cjs_module_count",
        "function_source_count", "debug_info_offset",
    ),
)

#: Bytecode version -> confirmed layout. 97 is intentionally absent (see
#: tools/hermes/versions.json: no npm-installable hermesc exists for it).
#: 99 shares LAYOUT_V98 - confirmed identical BytecodeFileHeader struct at
#: its own pinned commit, see module docstring.
VERSION_TO_LAYOUT: dict[int, HeaderLayout] = {
    96: LAYOUT_V96,
    98: LAYOUT_V98,
    99: LAYOUT_V98,
}

_MAGIC_VERSION_FORMAT = "<QI"  # just enough to read version and pick a layout
_MAGIC_VERSION_SIZE = struct.calcsize(_MAGIC_VERSION_FORMAT)


@dataclass(frozen=True, slots=True)
class BytecodeOptions:
    """The 1-byte `BytecodeOptions` bitfield (bit 0 = LSB)."""

    static_builtins: bool
    cjs_modules_statically_resolved: bool
    has_async: bool
    raw: int

    @classmethod
    def from_byte(cls, value: int) -> "BytecodeOptions":
        return cls(
            static_builtins=bool(value & 0b001),
            cjs_modules_statically_resolved=bool(value & 0b010),
            has_async=bool(value & 0b100),
            raw=value,
        )


@dataclass(frozen=True, slots=True)
class BytecodeFileHeader:
    """
    Decoded `BytecodeFileHeader` (see module docstring for source layouts).

    Fields only present in one layout are `None` under the other - e.g.
    `array_buffer_size`/`obj_value_buffer_size` are `None` for a
    LAYOUT_V98 file, and `literal_value_buffer_size`/
    `obj_shape_table_count`/`num_string_switch_imms` are `None` for a
    LAYOUT_V96 file. Check `layout.name` if this matters to a caller.
    """

    version: int
    layout: HeaderLayout
    source_hash: bytes  # 20 raw bytes; format as hex for display, e.g. source_hash.hex()
    file_length: int
    global_code_index: int
    function_count: int
    string_kind_count: int
    identifier_count: int
    string_count: int
    overflow_string_count: int
    string_storage_size: int
    bigint_count: int
    bigint_storage_size: int
    regexp_count: int
    regexp_storage_size: int
    obj_key_buffer_size: int
    segment_id: int
    cjs_module_count: int
    function_source_count: int
    debug_info_offset: int
    options: BytecodeOptions
    # LAYOUT_V96-only:
    array_buffer_size: Optional[int] = None
    obj_value_buffer_size: Optional[int] = None
    # LAYOUT_V98-only:
    literal_value_buffer_size: Optional[int] = None
    obj_shape_table_count: Optional[int] = None
    num_string_switch_imms: Optional[int] = None

    @classmethod
    def parse(cls, data: bytes) -> "BytecodeFileHeader":
        """
        Parse a `BytecodeFileHeader` from the first `HEADER_SIZE` bytes of
        `data` (a full bundle's contents, or at least its first 128 bytes).

        Raises `InvalidMagicError` if `data` doesn't start with the Hermes
        magic number, `TruncatedFileError` if fewer than `HEADER_SIZE`
        bytes are available, and `UnsupportedBytecodeVersionError` if the
        version has no confirmed layout in `VERSION_TO_LAYOUT` (parsing an
        unconfirmed version's fields would silently misalign, as bytecode
        98 did under the version-96 layout - see module docstring).
        """
        if len(data) < _MAGIC_VERSION_SIZE:
            raise TruncatedFileError("BytecodeFileHeader", HEADER_SIZE, len(data))

        magic, version = struct.unpack_from(_MAGIC_VERSION_FORMAT, data, 0)
        if magic != MAGIC:
            raise InvalidMagicError(found=magic, expected=MAGIC)

        layout = VERSION_TO_LAYOUT.get(version)
        if layout is None:
            raise UnsupportedBytecodeVersionError(version, tuple(sorted(VERSION_TO_LAYOUT)))

        if len(data) < HEADER_SIZE:
            raise TruncatedFileError("BytecodeFileHeader", HEADER_SIZE, len(data))

        _magic, _version, source_hash, *uint32_fields, options_byte, _padding = (
            struct.unpack(layout.struct_format, data[:HEADER_SIZE])
        )

        fields = dict(zip(layout.uint32_field_names, uint32_fields))

        return cls(
            version=version,
            layout=layout,
            source_hash=source_hash,
            options=BytecodeOptions.from_byte(options_byte),
            **fields,
        )
