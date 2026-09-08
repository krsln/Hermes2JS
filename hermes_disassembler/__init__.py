"""
hermes_disassembler: reads raw Hermes bytecode (HBC) files directly.

Purpose
-------
`hermes_decompiler/` consumes a hermes-dec-style `.hasm` text listing (see
`hermes_decompiler.frontend.parsing.OpcodeParser`): one line per
instruction, each carrying an absolute byte address and fully-resolved
string literals. Today that listing is produced by `vendor/hermes-dec`
(P1sec/hermes-dec), an external tool licensed AGPL-3.0 and fetched
separately (see `scripts/fetch-hermes-dec.sh`) - not shipped in this repo.

`hermes_disassembler/` is the MIT-licensed, in-repo replacement: it reads
a compiled `.bundle` file's raw HBC bytecode and will (eventually) emit
the same hermes-dec-compatible `.hasm` shape that
`scripts/split_output_file.py` and `hermes_decompiler/` already expect,
so the rest of the pipeline (README's Step 2/3) does not need to change.

Ground truth for the binary layout comes from facebook/hermes's own
public, MIT-licensed sources (`BytecodeFileFormat.h`, `BytecodeList.def`)
- never from vendor/hermes-dec's Python source, which is AGPL and must
not leak into this package even as "reference".

Non-goal (for now): full instruction-stream decoding. See
`format/BytecodeFileHeader.py` for the first working slice (the fixed
128-byte file header) and its module docstring for what's next.

Oracle, not source of truth
----------------------------
`tools/hermes/` (the pinned, official `hermesc` binaries) is used under
`oracle/` to cross-check *structural* facts this package computes
(function count, string count, bytecode version, ...) against hermesc's
own `-dump-bytecode` text output. It is validation tooling, not an input
to the disassembler: hermesc's textual dump elides long string literals
(truncates with "...") and omits per-instruction byte addresses, so it
cannot itself serve as the source for a lossless `.hasm` reconstruction.
"""
