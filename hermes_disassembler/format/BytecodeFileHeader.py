"""
Parses the fixed-size `BytecodeFileHeader` at the start of every Hermes
bytecode (.bundle) file.

Layout source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/HBC/BytecodeFileFormat.h` (confirmed here against
tag v0.12.0, the release `tools/hermes/versions.json` pins to bytecode
version 96):
https://github.com/facebook/hermes/blob/v0.12.0/include/hermes/BCGen/HBC/BytecodeFileFormat.h

Validated byte-for-byte against apps/testy/96/index.android.bundle: every
field this module decodes (functionCount=15247, stringCount=18615,
sourceHash, bigIntCount=0, regExpCount=196, functionSourceCount=84,
fileLength == actual file size, options=0) matches
`tools/hermes/dump_bytecode.sh 96 ...`'s own "Bytecode File Information"
block exactly - see `hermes_disassembler/oracle/` for that cross-check
made repeatable.

`BytecodeFileHeader` is documented as cache-line-tuned and a multiple of
32 bytes (`static_assert(sizeof(BytecodeFileHeader) % 32 == 0, ...)`);
this layout is exactly 128 bytes.

Known gap: only confirmed for bytecode version 96 (hermes_release
0.12.0) so far. Bytecode 98 (hermes_release 1.0.0, per versions.json) is
NOT yet confirmed to share this exact layout - the struct has changed
shape across Hermes releases before (e.g. `hasAsync` was added to
`BytecodeOptions` at some point). Verify against a 98 bundle before
trusting this for that version; see `SUPPORTED_VERSIONS` below.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import InvalidMagicError, TruncatedFileError

__all__ = ["BytecodeFileHeader", "BytecodeOptions", "MAGIC", "HEADER_SIZE", "SUPPORTED_VERSIONS"]

#: "Hermes" in ancient Greek encoded in UTF-16BE and truncated to 8 bytes.
#: (hermes/include/hermes/BCGen/HBC/BytecodeFileFormat.h)
MAGIC = 0x1F1903C103BC1FC6

#: Bytecode versions this exact 128-byte layout has been confirmed against
#: a real bundle for (see module docstring). Parsing a header for a version
#: outside this set still works (the layout hasn't changed since 96 as far
#: as documented), but hasn't been byte-verified here yet.
SUPPORTED_VERSIONS = (96,)

# '<'    little-endian, no alignment padding (matches LLVM_PACKED_START)
# Q      uint64_t magic
# I      uint32_t version
# 20s    uint8_t sourceHash[20]                  (SHA1_NUM_BYTES)
# 19I    the 19 uint32_t fields fileLength..debugInfoOffset
# B      BytecodeOptions (1-byte bitfield)
# 19s    uint8_t padding[19]
_STRUCT_FORMAT = "<QI20s19IB19s"
HEADER_SIZE = struct.calcsize(_STRUCT_FORMAT)
assert HEADER_SIZE == 128, f"expected 128-byte header, got {HEADER_SIZE}"

_UINT32_FIELD_NAMES = (
    "file_length",
    "global_code_index",
    "function_count",
    "string_kind_count",
    "identifier_count",
    "string_count",
    "overflow_string_count",
    "string_storage_size",
    "bigint_count",
    "bigint_storage_size",
    "regexp_count",
    "regexp_storage_size",
    "array_buffer_size",
    "obj_key_buffer_size",
    "obj_value_buffer_size",
    "segment_id",
    "cjs_module_count",
    "function_source_count",
    "debug_info_offset",
)


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
    """Decoded `BytecodeFileHeader` (see module docstring for the source layout)."""

    version: int
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
    array_buffer_size: int
    obj_key_buffer_size: int
    obj_value_buffer_size: int
    segment_id: int
    cjs_module_count: int
    function_source_count: int
    debug_info_offset: int
    options: BytecodeOptions

    @classmethod
    def parse(cls, data: bytes) -> "BytecodeFileHeader":
        """
        Parse a `BytecodeFileHeader` from the first `HEADER_SIZE` bytes of
        `data` (a full bundle's contents, or at least its first 128 bytes).

        Raises `InvalidMagicError` if `data` doesn't start with the Hermes
        magic number, and `TruncatedFileError` if fewer than `HEADER_SIZE`
        bytes are available.
        """
        if len(data) < HEADER_SIZE:
            raise TruncatedFileError("BytecodeFileHeader", HEADER_SIZE, len(data))

        magic, version, source_hash, *uint32_fields, options_byte, _padding = (
            struct.unpack(_STRUCT_FORMAT, data[:HEADER_SIZE])
        )

        if magic != MAGIC:
            raise InvalidMagicError(found=magic, expected=MAGIC)

        fields = dict(zip(_UINT32_FIELD_NAMES, uint32_fields))

        return cls(
            version=version,
            source_hash=source_hash,
            options=BytecodeOptions.from_byte(options_byte),
            **fields,
        )
