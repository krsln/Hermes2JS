"""
Parses the Hermes bytecode string table: the segments between the file
header and the string content itself, and the raw string bytes they
point into.

Segment order and alignment source: facebook/hermes's own MIT-licensed
`include/hermes/BCGen/HBC/BytecodeFileFormat.h`. `SmallFuncHeader`'s
size differs by bytecode version the same way `BytecodeFileHeader`'s
layout does - see `VERSION_TO_SMALL_FUNC_HEADER_SIZE` below and
`BytecodeFileHeader.py`'s module docstring for the pattern this repeats.
Everything else in this module (segment order, alignment, the
`SmallStringTableEntry`/`OverflowStringTableEntry`/`StringKind::Entry`
bit layouts) was confirmed unchanged between the v0.12.0 (bytecode 96)
and cb5bb3342f43d378cc2653e2ac9077a282b97637 (bytecode 98/99) sources -
only the function header struct itself changed shape.
https://github.com/facebook/hermes/blob/cb5bb3342f43d378cc2653e2ac9077a282b97637/include/hermes/BCGen/HBC/BytecodeFileFormat.h

`visitBytecodeSegmentsInOrder()` there is explicitly documented as
"defin[ing] the order of the bytecode file segments" - the six segments
this module walks, in this exact order, right after the 128-byte header:

    1. function headers  (SmallFuncHeader, 16 or 12 bytes each - see
       VERSION_TO_SMALL_FUNC_HEADER_SIZE; version-dependent for the same
       reason BytecodeFileHeader's layout is, see that module)
    2. string kinds       (StringKind::Entry,       4 bytes each)
    3. identifier hashes  (uint32_t,                4 bytes each)
    4. small string table (SmallStringTableEntry,   4 bytes each)  <-- resolved here
    5. overflow string table (OverflowStringTableEntry, 8 bytes each)
    6. string storage     (raw bytes, header.string_storage_size)

Every segment is padded to `BYTECODE_ALIGNMENT = alignof(uint32_t) = 4`
bytes before the next one starts (same file, line ~41). In practice this
padding is a no-op for every segment boundary here - all six segment
sizes above are already multiples of 4 - but it's computed rather than
assumed away, in case that ever changes.

This module only reads segments 1-3 to find the offsets (it doesn't
decode function headers or string kinds into their own structures yet
- `StringKind::Entry`, a run-length-encoded String-vs-Identifier tag
sequence, is decoded here since it's cheap and lives right next to the
string table conceptually, but function headers are skipped as raw
bytes for now; see `hermes_disassembler`'s package docstring for what's
next).

Validated against apps/testy/96 and apps/testy/98: resolving every
string in both bundles' string tables (18615 and 18070 strings
respectively) reproduces exactly what `tools/hermes/dump_bytecode.sh`'s
own "Global String Table:" block shows for the first 15 - including one
hermesc itself truncates in its own text output
(`"__BUNDLE_START_TI"...`) but this module recovers in full
(`__BUNDLE_START_TIME__`), plus zero decode errors and the expected
overflow-entry count (285 for bytecode 96) across the full table - see
`tests/test_hermes_disassembler_string_table.py`.
"""
from __future__ import annotations

import struct
from dataclasses import dataclass

from hermes_disassembler.core.Exceptions import HermesBytecodeError, TruncatedFileError
from hermes_disassembler.format.BytecodeFileHeader import HEADER_SIZE, BytecodeFileHeader

__all__ = [
    "StringTable", "StringTableEntry", "StringKindRun",
    "BYTECODE_ALIGNMENT", "VERSION_TO_SMALL_FUNC_HEADER_SIZE",
    "STRING_KIND_ENTRY_SIZE", "IDENTIFIER_HASH_SIZE",
    "SMALL_STRING_TABLE_ENTRY_SIZE", "OVERFLOW_STRING_TABLE_ENTRY_SIZE",
]

#: hermes/include/hermes/BCGen/HBC/BytecodeFileFormat.h: BYTECODE_ALIGNMENT = alignof(uint32_t)
BYTECODE_ALIGNMENT = 4

#: SmallFuncHeader size, in bytes - version-dependent, like BytecodeFileHeader
#: (see hermes_disassembler.format.BytecodeFileHeader for why). Confirmed via
#: static_assert in facebook/hermes source at the same commits used there:
#:   - bytecode 96 (v0.12.0): native C bitfields, 4 uint32_t "words" ->
#:     static_assert(32 % sizeof(SmallFuncHeader) == 0, ...) -> 16 bytes.
#:   - bytecode 98/99 (cb5bb334...): BitField<> template, 2 uint32_t words +
#:     3 uint8_t bytes + 1 flags byte ->
#:     static_assert(sizeof(SmallFuncHeader) == 12, ...) -> 12 bytes.
#: Only the total size matters here (the function-headers segment is only
#: skipped over, not decoded field-by-field yet - see module docstring),
#: so the internal bitfield differences between 98 and 99
#: (WriteCacheSize 6-vs-7 bits, NumCacheNewObject present-vs-absent) don't
#: matter for this module even though they change FUNC_HEADER_FIELDS.
VERSION_TO_SMALL_FUNC_HEADER_SIZE: dict[int, int] = {96: 16, 98: 12, 99: 12}

#: StringKind::Entry: a single uint32_t (top bit = kind, low 31 bits = count)
STRING_KIND_ENTRY_SIZE = 4

#: identifierHashes: Array<uint32_t>
IDENTIFIER_HASH_SIZE = 4

#: SmallStringTableEntry: a single uint32_t bitfield (IsUTF16:1, Offset:23, Length:8)
SMALL_STRING_TABLE_ENTRY_SIZE = 4

#: OverflowStringTableEntry: two uint32_t (offset, length)
OVERFLOW_STRING_TABLE_ENTRY_SIZE = 8

#: SmallStringTableEntry.Length sentinel meaning "look this index up in the
#: overflow table instead" (INVALID_LENGTH = (1 << 8) - 1)
_OVERFLOW_LENGTH_SENTINEL = 0xFF


def _align_up(offset: int, alignment: int = BYTECODE_ALIGNMENT) -> int:
    remainder = offset % alignment
    return offset if remainder == 0 else offset + (alignment - remainder)


@dataclass(frozen=True, slots=True)
class StringTableEntry:
    """
    One resolved string table entry: where its bytes live in string
    storage, and how to decode them - not the decoded string itself
    (call `StringTable.resolve(index)` for that; this is the metadata
    `resolve()` uses, exposed separately since hermesc's own text dump
    reports it too, for cross-checking - see module docstring).
    """

    is_utf16: bool
    offset: int  # byte offset into string storage
    length: int  # in UTF-16 code units if is_utf16, else bytes
    is_overflowed: bool  # True if this index's real offset/length came from the overflow table


@dataclass(frozen=True, slots=True)
class StringKindRun:
    """One run-length-encoded `StringKind::Entry`: `count` consecutive string-table indices, all of the same kind."""

    is_identifier: bool
    count: int


@dataclass(frozen=True, slots=True)
class StringTable:
    """
    A parsed Hermes string table: entry metadata for every string (in
    table-index order) plus the raw storage bytes they point into.

    Construct via `StringTable.parse(data, header)`, not directly.
    """

    entries: tuple[StringTableEntry, ...]
    storage: bytes
    string_kinds: tuple[StringKindRun, ...]

    def is_identifier(self, index: int) -> bool:
        """
        True if string table entry `index` is tagged `StringKind::Identifier`
        rather than plain `StringKind::String` (see `string_kinds`' module
        docstring). Walks the run-length-encoded `string_kinds` list, which
        covers indices `[0, string_count)` in order with no gaps - an
        `index` beyond that range raises `IndexError`, same as `resolve()`.
        """
        remaining = index
        for run in self.string_kinds:
            if remaining < run.count:
                return run.is_identifier
            remaining -= run.count
        raise IndexError(f"string index {index} not covered by string_kinds runs")

    def resolve(self, index: int) -> str:
        """
        Decode string table entry `index` to a `str`.

        Raises `IndexError` for an out-of-range index, and
        `HermesBytecodeError` if the entry's byte range falls outside
        `storage` (a truncated or corrupt bundle).
        """
        entry = self.entries[index]
        end = entry.offset + entry.length * (2 if entry.is_utf16 else 1)
        if end > len(self.storage):
            raise HermesBytecodeError(
                f"string table entry {index}: byte range "
                f"[{entry.offset}:{end}) exceeds string storage size {len(self.storage)}"
            )
        raw = self.storage[entry.offset:end]
        return raw.decode("utf-16-le") if entry.is_utf16 else raw.decode("ascii")

    @classmethod
    def parse(cls, data: bytes, header: BytecodeFileHeader) -> "StringTable":
        """
        Parse the string table segments that follow `header` in `data`
        (the full bundle bytes). `header` must already be
        `BytecodeFileHeader.parse(data)` for the same `data`.
        """
        offset = HEADER_SIZE

        # 1. function headers - skipped as raw bytes for now (see module docstring)
        small_func_header_size = VERSION_TO_SMALL_FUNC_HEADER_SIZE.get(header.version)
        if small_func_header_size is None:
            raise HermesBytecodeError(
                f"no confirmed SmallFuncHeader size for bytecode version {header.version} "
                f"(known: {sorted(VERSION_TO_SMALL_FUNC_HEADER_SIZE)}) - don't guess, "
                f"confirm against a real bundle first (see module docstring)"
            )
        offset += header.function_count * small_func_header_size
        offset = _align_up(offset)

        # 2. string kinds
        kinds_end = offset + header.string_kind_count * STRING_KIND_ENTRY_SIZE
        _require(data, kinds_end, "string kinds table")
        string_kinds = tuple(
            _parse_string_kind_entry(
                struct.unpack_from("<I", data, offset + i * STRING_KIND_ENTRY_SIZE)[0]
            )
            for i in range(header.string_kind_count)
        )
        offset = _align_up(kinds_end)

        # 3. identifier hashes - skipped (not needed to resolve strings; kept
        # here only to advance `offset` past this segment correctly)
        offset += header.identifier_count * IDENTIFIER_HASH_SIZE
        offset = _align_up(offset)

        # 4. small string table
        small_table_end = offset + header.string_count * SMALL_STRING_TABLE_ENTRY_SIZE
        _require(data, small_table_end, "small string table")
        raw_small_entries = struct.unpack_from(f"<{header.string_count}I", data, offset)
        offset = _align_up(small_table_end)

        # 5. overflow string table
        overflow_end = offset + header.overflow_string_count * OVERFLOW_STRING_TABLE_ENTRY_SIZE
        _require(data, overflow_end, "overflow string table")
        overflow_entries = [
            struct.unpack_from("<II", data, offset + i * OVERFLOW_STRING_TABLE_ENTRY_SIZE)
            for i in range(header.overflow_string_count)
        ]
        offset = _align_up(overflow_end)

        # 6. string storage
        storage_end = offset + header.string_storage_size
        _require(data, storage_end, "string storage")
        storage = data[offset:storage_end]

        entries = tuple(
            _resolve_entry(raw, overflow_entries) for raw in raw_small_entries
        )

        return cls(entries=entries, storage=storage, string_kinds=string_kinds)


def _require(data: bytes, needed_end: int, what: str) -> None:
    if len(data) < needed_end:
        raise TruncatedFileError(what, needed_end, len(data))


def _parse_string_kind_entry(datum: int) -> StringKindRun:
    # StringKind.h: CountBits = 31; Kind::Identifier = 1u << 31
    return StringKindRun(is_identifier=bool(datum & 0x8000_0000), count=datum & 0x7FFF_FFFF)


def _resolve_entry(
        raw: int, overflow_entries: list[tuple[int, int]]
) -> StringTableEntry:
    # SmallStringTableEntry bitfield, LSB first (matches BytecodeOptions -
    # empirically confirmed via BytecodeFileHeader's oracle cross-check):
    #   bit 0       IsUTF16
    #   bits 1-23   Offset (23 bits)
    #   bits 24-31  Length (8 bits)
    is_utf16 = bool(raw & 0x1)
    small_offset = (raw >> 1) & 0x7F_FFFF
    small_length = (raw >> 24) & 0xFF

    if small_length == _OVERFLOW_LENGTH_SENTINEL:
        offset, length = overflow_entries[small_offset]
        return StringTableEntry(is_utf16=is_utf16, offset=offset, length=length, is_overflowed=True)

    return StringTableEntry(
        is_utf16=is_utf16, offset=small_offset, length=small_length, is_overflowed=False
    )
