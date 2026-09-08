"""
Parses the `Bytecode File Information:` block that `hermesc -dump-bytecode`
prints at the top of its text dump (see `tools/hermes/dump_bytecode.sh`),
so it can be diffed against our own `BytecodeFileHeader.parse()` output.

This is validation tooling, not a data source for the disassembler proper
- see the `hermes_disassembler` package docstring ("Oracle, not source of
truth") for why: hermesc's text dump truncates long string literals and
omits per-instruction byte addresses, so it cannot itself feed a lossless
`.hasm` reconstruction. It CAN, however, confirm the handful of file-level
facts it does print in full - which is exactly what this module extracts.

Only the fields hermesc's dump actually prints are exposed here (a subset
of `BytecodeFileHeader`'s fields - e.g. `fileLength` and
`debugInfoOffset` are never printed by hermesc and so can't be
cross-checked this way).

Example input (see `tools/hermes/dump_bytecode.sh` output):

    Bytecode File Information:
      Bytecode version number: 96
      Source hash: 1d51e04b69e9eff199c798fe7d984872112bdf2c
      Function count: 15247
      String count: 18615
      BigInt count: 0
      String Kind Entry count: 3
      RegExp count: 196
      Segment ID: 0
      CommonJS module count: 0
      CommonJS module count (static): 0
      Function source count: 84
      Bytecode options:
        staticBuiltins: 0
        cjsModulesStaticallyResolved: 0
"""
from __future__ import annotations

import re
from dataclasses import dataclass

__all__ = ["HermescFileInfo", "ORACLE_NOT_PRINTED"]

#: Sentinel: fields BytecodeFileHeader has but hermesc's dump never prints,
#: so HermescFileInfo.diff() must skip them rather than report a false mismatch.
ORACLE_NOT_PRINTED = frozenset({
    "file_length", "global_code_index", "identifier_count",
    "overflow_string_count", "string_storage_size", "bigint_storage_size",
    "regexp_storage_size", "array_buffer_size", "obj_key_buffer_size",
    "obj_value_buffer_size", "debug_info_offset",
})

_FIELD_PATTERNS = {
    "version": re.compile(r"Bytecode version number:\s*(\d+)"),
    "source_hash": re.compile(r"Source hash:\s*([0-9a-fA-F]+)"),
    "function_count": re.compile(r"Function count:\s*(\d+)"),
    "string_count": re.compile(r"String count:\s*(\d+)"),
    "bigint_count": re.compile(r"BigInt count:\s*(\d+)"),
    "string_kind_count": re.compile(r"String Kind Entry count:\s*(\d+)"),
    "regexp_count": re.compile(r"RegExp count:\s*(\d+)"),
    "segment_id": re.compile(r"Segment ID:\s*(\d+)"),
    "cjs_module_count": re.compile(r"CommonJS module count:\s*(\d+)"),
    "function_source_count": re.compile(r"Function source count:\s*(\d+)"),
    "static_builtins": re.compile(r"staticBuiltins:\s*(\d+)"),
    "cjs_modules_statically_resolved": re.compile(r"cjsModulesStaticallyResolved:\s*(\d+)"),
}


@dataclass(frozen=True, slots=True)
class HermescFileInfo:
    """The subset of file-header facts extracted from a hermesc text dump."""

    version: int
    source_hash: str  # hex string, lowercase - compare against header.source_hash.hex()
    function_count: int
    string_count: int
    bigint_count: int
    string_kind_count: int
    regexp_count: int
    segment_id: int
    cjs_module_count: int
    function_source_count: int
    static_builtins: bool
    cjs_modules_statically_resolved: bool

    @classmethod
    def parse(cls, dump_text: str) -> "HermescFileInfo":
        """
        Parse the `Bytecode File Information:` block out of a full
        `hermesc -dump-bytecode` text dump (only the first ~20 lines
        matter; the rest of the dump is ignored).
        """
        values: dict[str, int | str] = {}
        for name, pattern in _FIELD_PATTERNS.items():
            match = pattern.search(dump_text)
            if not match:
                raise ValueError(
                    f"hermesc dump did not contain expected field {name!r} "
                    f"(looked for pattern: {pattern.pattern!r})"
                )
            values[name] = match.group(1)

        return cls(
            version=int(values["version"]),
            source_hash=values["source_hash"].lower(),
            function_count=int(values["function_count"]),
            string_count=int(values["string_count"]),
            bigint_count=int(values["bigint_count"]),
            string_kind_count=int(values["string_kind_count"]),
            regexp_count=int(values["regexp_count"]),
            segment_id=int(values["segment_id"]),
            cjs_module_count=int(values["cjs_module_count"]),
            function_source_count=int(values["function_source_count"]),
            static_builtins=bool(int(values["static_builtins"])),
            cjs_modules_statically_resolved=bool(int(values["cjs_modules_statically_resolved"])),
        )
