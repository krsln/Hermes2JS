"""
Formats decoded functions/instructions into hermes-dec-compatible
`.hasm` text - the format `vendor/hermes-dec` (AGPL, fetched
separately, see `scripts/fetch-hermes-dec.sh`) produces today, and
that `hermes_decompiler`'s frontend (`OpcodeParser`, `OperandPatterns`)
already parses. This is the module that lets `hermes_disassembler`
actually replace that AGPL dependency, per the package docstring's
stated purpose.

Format ground truth: a REAL hermes-dec output fixture already
committed in this repo,
`apps/demo/fixtures/96/sections/section_15042.hasm` - not a guess, not
derived from OpcodeParser's regexes alone (those only constrain the
grammar, not every literal detail like spacing or hex digit count):

    => [Function #15042 "runAllTests" of 30 bytes]: 1 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x0026772c

    Bytecode listing:

    ==> 00000000: <LoadConstUndefined>: <Reg8: 0>
    ==> 00000002: <GetEnvironment>: <Reg8: 1, UInt8: 0>
    ==> 00000009: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 65>  # String: 'apply' (Identifier)
    ==> 0000001c: <Ret>: <Reg8: 0>

Every formatting decision below traces to that example: 8-hex-digit
lowercase addresses (both the function's absolute file offset and each
instruction's offset RELATIVE TO THE FUNCTION START, matching
`==> 00000000:` starting at zero); the function header's exact field
order, labels, and the double space before `@ offset`; operand labels
using the *semantic* tag (`string_id`) instead of the raw encoded type
(`UInt8`) wherever `hermes_disassembler.format.Opcode`'s table carries
one (see `tools/hermes/generate_opcode_tables.py`'s `OPERAND_STRING_ID`
handling); and the string comment's exact shape, including which of
`(Identifier)`/`(String)` to use (from
`StringTable.is_identifier()`).

Confirmed but NOT from that one fixture - separately validated in this
package's own test suite before being relied on here: the jump-target
`# Address: <hex>` comment format is inferred from hermes-dec's general
convention (not present in the one fixture line quoted above, which
has no jump instruction) and given in the SAME relative-to-function
addressing as `==>` lines, per `JumpTarget.py`'s absolute-offset
convention converted back to relative here.

Known gaps, not yet implemented:
- Multiple string_id operands on one instruction (e.g. `CreateRegExp`
  has two) - each gets its own `  # ` segment, per hermes-dec's real
  output for that exact case (confirmed, not guessed).
- Exact `Double` operand text formatting (no fixture example with one).
- RegExp table (`CreateRegExp`'s `# RegExp: ...`-style comment, if any -
  unconfirmed) and the debug tables (`Debug offsets:`'s three raw
  offsets are resolved - see `DebugOffsets.py` - but the source
  location / scope descriptor / textified-callees tables they point
  into aren't parsed).

`bigint_id` operand comments (`BigIntTable.py`) and
`SwitchImm`/`UIntSwitchImm`/`StringSwitchImm` jump-table and
default-target comments (`SwitchTable.py`, `JumpTarget.py`'s
`resolve_operand_jump_target`) are both implemented and validated
directly against real hermes-dec output (`hbc-disassembler`, run
against apps/testy/96 and apps/testy/98 directly, not just read from
source - see those two modules' docstrings) - `UIntSwitchImm`/
`StringSwitchImm` deliberately never get the jump-table comment,
matching a confirmed quirk in real hermes-dec's own output (its
name-matching code only ever checks for the literal string
`"SwitchImm"`). `NewArrayWithBuffer`/`NewObjectWithBuffer`/etc. literal
content comments (`# Array: [...]`, `# Object: {...}`) are also
already implemented (`LiteralBuffer.py`/`ObjectLiteral.py`) - this
bullet used to (wrongly) list them as missing.

Exception handler resolution (`format_function`'s
`  [Exception handlers: ...]` line) and debug offsets resolution
(the `  [Debug offsets: ...]` line, for `has_debug_info=True`
functions) both build on `ExceptionHandlerTable.VERSION_TO_LARGE_HEADER_SIZE`
- see that module's docstring for the full validation story (a real,
previously-undetected bug there, now fixed and validated at scale:
660/660 in bytecode 96, 1082/1082 in bytecode 98, both 100%). Debug
offsets specifically remain UNTESTED against a real `has_debug_info=True`
function in either test fixture - both currently have zero such
functions - see `DebugOffsets.py`'s module docstring.

Pre-existing, separate gap worth knowing about here:
`scripts/split_output_file.py`'s `FUNCTION_HEADER_RE` required a
function-header line to start with `[Function` and didn't match the
`=> [Function...` prefix this module (and real hermes-dec output)
actually produces - already fixed (see that script's own history), so
`format_bundle()`'s output now splits into descriptive `function_N_name`
filenames, not anonymous `section_N` ones.
"""
from __future__ import annotations

from hermes_disassembler.core.Exceptions import HermesBytecodeError
from hermes_disassembler.format.BigIntTable import resolve_bigint
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.Builtins import resolve_builtin
from hermes_disassembler.format.DebugOffsets import resolve_debug_offsets
from hermes_disassembler.format.ExceptionHandlerTable import resolve_exception_handlers
from hermes_disassembler.format.FunctionHeader import FunctionKind, FunctionHeaderEntry
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.JumpTarget import _JUMP_OPERAND_TYPES, resolve_operand_jump_target
from hermes_disassembler.format.LiteralBuffer import _Undefined, decode_literal_buffer
from hermes_disassembler.format.ObjectLiteral import resolve_object_literal
from hermes_disassembler.format.Opcode import Instruction, decode_function, load_opcode_table
from hermes_disassembler.format.StringTable import StringTable
from hermes_disassembler.format.SwitchTable import resolve_switch_table_entries

#: scripts/split_output_file.py's own separator constant, duplicated
#: here rather than imported (that script isn't part of this package
#: and sits outside hermes_disassembler/hermes_decompiler's own
#: dependency graph) - keep in sync if that script's DEFAULT_SEPARATOR
#: ever changes.
SECTION_SEPARATOR = "==============="

__all__ = ["format_instruction", "format_function", "format_bundle", "SECTION_SEPARATOR"]

#: Semantics that replace the operand's raw type in the LABEL position
#: (e.g. "string_id: 20" instead of "UInt32: 20") - these come from
#: BytecodeList.def's own OPERAND_STRING_ID/_FUNCTION_ID/_BIGINT_ID
#: macros, which hermes-dec's own disassembler recognizes the same way.
#: "builtin_id" is NOT in this set: it's this package's own inferred
#: tag (see tools/hermes/generate_opcode_tables.py's _MANUAL_SEMANTICS -
#: BytecodeList.def has no macro for it), and real hermes-dec output
#: keeps the raw type there ("UInt8: 57", not "builtin_id: 57") and
#: only adds a comment - confirmed against real output for
#: GetBuiltinClosure.
_LABEL_SWAPPING_SEMANTICS = frozenset({"string_id", "function_id", "bigint_id"})


def _format_operand(operand_type: str, value: int | float, semantic: str | None) -> str:
    label = semantic if semantic in _LABEL_SWAPPING_SEMANTICS else operand_type
    return f"{label}: {value}"


#: opcode name -> 0-based operand index of (count, buf_idx) for array
#: literal instructions - not a BytecodeList.def-tagged semantic (no
#: OPERAND_*_ID macro covers this), so hand-maintained like builtin_id.
_ARRAY_BUFFER_OPCODES = {
    "NewArrayWithBuffer": (2, 3),
    "NewArrayWithBufferLong": (2, 3),
}

#: opcode names for object literal instructions - operand positions
#: differ by version (see ObjectLiteral.py), so extraction happens
#: inside _format_object_buffer_comment rather than a fixed lookup here.
_OBJECT_BUFFER_OPCODES = frozenset({"NewObjectWithBuffer", "NewObjectWithBufferLong"})


def format_instruction(
        data: bytes,
        instruction: Instruction,
        function_offset: int,
        table: StringTable,
        version: int,
        all_functions: tuple[FunctionHeaderEntry, ...] | None = None,
        bc_header: BytecodeFileHeader | None = None,
) -> str:
    """
    Format one instruction as a `==> <rel_offset>: <Name>: <operands>`
    line, with a trailing `  # ...` comment (one per commented operand,
    each with its own `  # ` prefix - see module docstring) for string
    references, function references, builtin references, bigint values,
    array/object literal contents, jump targets, and (`SwitchImm` only -
    see `SwitchTable.py`'s module docstring for why not `UIntSwitchImm`/
    `StringSwitchImm` too) jump tables, where applicable. `data` is the
    full bundle bytes (needed to resolve array literal contents, jump
    tables, and bigint values). `function_offset` is the owning
    function's `FunctionHeaderEntry.offset` (needed to print the
    instruction's offset relative to its function, matching
    hermes-dec's `==> 00000000:`-from-zero convention - see module
    docstring).

    `all_functions` - the full, overflow-resolved function list for this
    bundle (e.g. from `format_bundle`, or
    `FunctionHeaderOverflow.resolve_overflowed_headers`'s return value) -
    is needed to resolve `function_id` operands (e.g. `CreateGenerator`,
    `CreateClosure`) to their target function's own signature. Omit it
    (the default) to format a single function in isolation - `function_id`
    operands are then left without a comment rather than raising, since
    the target function's info genuinely isn't available.

    `bc_header` - the bundle's `BytecodeFileHeader` - is needed to
    resolve `bigint_id` operands (for `header.bigint_count` bounds
    checking - see `BigIntTable.resolve_bigint`). Omit it (the default)
    to leave `bigint_id` operands without a comment, same reasoning as
    `all_functions` above.
    """
    _name, operand_types, semantics = load_opcode_table(version)[instruction.opcode]

    operand_strs = [
        _format_operand(operand_types[i], value, semantics.get(i))
        for i, value in enumerate(instruction.operands)
    ]

    comment_parts: list[str] = []
    for i, value in enumerate(instruction.operands):
        tag = semantics.get(i)
        if tag == "string_id":
            string_value = table.resolve(value)
            kind = "Identifier" if table.is_identifier(value) else "String"
            comment_parts.append(f"String: {string_value!r} ({kind})")
        elif tag == "function_id" and all_functions is not None:
            comment_parts.append(_format_function_reference(all_functions[value], table))
        elif tag == "builtin_id":
            comment_parts.append(f"Built-in function: [#{value} {resolve_builtin(version, value)}]")
        elif tag == "bigint_id" and bc_header is not None:
            comment_parts.append(f"BigInt: {resolve_bigint(data, table, bc_header, value)}")
        elif operand_types[i] in _JUMP_OPERAND_TYPES:
            # Not just DEFINE_JUMP_N's operand-0 case - SwitchImm's/
            # UIntSwitchImm's/StringSwitchImm's default-case Addr32
            # lands here too, at whatever operand index it's at (2 or
            # 3 - see JumpTarget.py's module docstring). Matches real
            # hermes-dec's own per-operand loop exactly: it checks
            # operand TYPE, not instruction identity or operand
            # position, for this specific comment.
            relative_target = resolve_operand_jump_target(instruction, i) - function_offset
            comment_parts.append(f"Address: {relative_target:08x}")
        # function_id with all_functions=None: no comment.

    if instruction.name in _ARRAY_BUFFER_OPCODES:
        comment_parts.append(_format_array_buffer_comment(data, table, version, instruction))

    if instruction.name in _OBJECT_BUFFER_OPCODES:
        comment_parts.append(_format_object_buffer_comment(data, table, version, instruction))

    if instruction.name in ("SwitchImm", "UIntSwitchImm"):
        # StringSwitchImm deliberately excluded - hermes_decompiler's own
        # StringSwitchImm handler doesn't use a jump table at all (its
        # cases come from a separate string-keyed table this package
        # doesn't parse - see SwitchTable.py's module docstring), so
        # there's no consumer for this comment there. UIntSwitchImm IS
        # included here even though real hermes-dec's own disassembly
        # output never prints this comment for it (see SwitchTable.py's
        # module docstring for that confirmed quirk) - unlike that
        # quirk, this isn't just a cosmetic text difference:
        # hermes_decompiler's UIntSwitchImm handler is the SAME class as
        # SwitchImm's (`class UIntSwitchImm(SwitchImm): pass`) and reads
        # `ctx.entry.jump_table`, itself populated by parsing this exact
        # comment (OpcodeEntry.py's `_JUMP_TABLE_RE`) - omitting it here
        # to match hermes-dec's text would silently break every v98
        # switch statement's case reconstruction (empty case_map), not
        # just look different.
        targets = resolve_switch_table_entries(data, instruction, 1, 3, 4)
        entries = ", ".join(f"{t - function_offset:08x}" for t in targets)
        comment_parts.append(f"Jump table: [{entries}]")

    rel_offset = instruction.offset - function_offset
    line = f"==> {rel_offset:08x}: <{instruction.name}>: <{', '.join(operand_strs)}>"
    for part in comment_parts:
        line += f"  # {part}"
    return line


def _format_object_buffer_comment(data: bytes, table: StringTable, version: int, instruction: Instruction) -> str:
    """
    `# Object: {'a': 1, 'b': 2, 'c': 3}` for a `NewObjectWithBuffer`/
    `NewObjectWithBufferLong` instruction (see `ObjectLiteral.py` for
    the two different operand layouts this dispatches between).
    """
    try:
        if version in (98, 99):
            shape_idx, val_idx = instruction.operands[1], instruction.operands[2]
            literal = resolve_object_literal(data, table, version, shape_idx, val_idx)
        elif version == 96:
            count, key_idx, val_idx = instruction.operands[2], instruction.operands[3], instruction.operands[4]
            literal = resolve_object_literal(data, table, version, count, key_idx, val_idx)
        else:
            raise HermesBytecodeError(f"no object literal layout known for bytecode {version}")
    except (HermesBytecodeError, ValueError, IndexError) as exc:
        return f"Object: <unresolved: {exc}>"
    pairs = ", ".join(f"{_js_repr(k)}: {_js_repr(v)}" for k, v in zip(literal.keys, literal.values))
    return f"Object: {{{pairs}}}"


def _js_repr(value) -> str:
    """
    Render one decoded literal value the way hermes-dec's own
    `SLPArray.to_strings()` does: `null`/`true`/`false`/`undefined`
    (JS spelling, not Python's `None`/`True`/`False`) for those tags,
    `repr()` for strings (matches hermes-dec's own `repr(string_table[...])`),
    and plain `str()` for numbers.
    """
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is _Undefined:
        return "undefined"
    if isinstance(value, str):
        return repr(value)
    return str(value)


def _format_array_buffer_comment(data: bytes, table: StringTable, version: int, instruction: Instruction) -> str:
    """
    `# Array: [1, 0, 2]` for a `NewArrayWithBuffer`/`NewArrayWithBufferLong`
    instruction - decodes its literal buffer contents (see
    `LiteralBuffer.decode_literal_buffer`). Falls back to a
    `<unresolved: ...>` placeholder instead of raising, so one bad
    array doesn't abort formatting the rest of the bundle.
    """
    count_index, buf_idx_index = _ARRAY_BUFFER_OPCODES[instruction.name]
    count = instruction.operands[count_index]
    buf_idx = instruction.operands[buf_idx_index]
    try:
        values = decode_literal_buffer(data, table.literal_value_buffer_offset + buf_idx, count, version, table)
    except (HermesBytecodeError, ValueError, IndexError) as exc:
        return f"Array: <unresolved: {exc}>"
    return f"Array: [{', '.join(_js_repr(v) for v in values)}]"


def _format_function_reference(target: FunctionHeaderEntry, table: StringTable) -> str:
    """
    `# Function: [#N name of B bytes]: P params @ offset 0xHEX` for a
    `function_id` operand's comment.

    Known gap: hermes-dec shows a synthesized `?anon_<n>_<description>`
    name for functions it considers anonymous (observed in real output,
    e.g. `?anon_0_generatorWithLoopTest`), not the plain string-table
    name this uses - that heuristic isn't reverse-engineered here (it
    likely depends on debug info this package doesn't parse yet - see
    `hermes_disassembler`'s package docstring). Index, byte size, param
    count, and offset are the real, structurally-verified fields here;
    only the cosmetic name may not match hermes-dec byte-for-byte for
    an anonymous function.
    """
    name = table.resolve(target.function_name)
    return (
        f"Function: [#{target.index} {name} of {target.bytecode_size_in_bytes} bytes]: "
        f"{target.param_count} params @ offset 0x{target.offset:08x}"
    )


def format_function(
        data: bytes,
        header: FunctionHeaderEntry,
        instructions: tuple[Instruction, ...],
        table: StringTable,
        version: int,
        all_functions: tuple[FunctionHeaderEntry, ...] | None = None,
        bc_header: BytecodeFileHeader | None = None,
) -> str:
    """
    Format a complete function block matching hermes-dec's shape:
    the `=> [Function #N "name" of B bytes]: ...` header line (using
    "Generator function"/"Async function" instead of "Function" per
    `header.kind` - previously hardcoded to "Function" regardless of
    kind, an unnoticed bug affecting 192 of apps/testy/98's functions;
    see `_FUNC_KIND_LABEL` above), plus a `  [Exception handlers: ...]`
    line when `header.has_exception_handler` and a
    `  [Debug offsets: ...]` line when `header.has_debug_info` (neither
    fixture has a real example of the latter - see `DebugOffsets.py`'s
    module docstring), a `Bytecode listing:` label, then one
    `format_instruction()` line per instruction - see module docstring
    for the exact fixture this reproduces. `data` is the full bundle
    bytes (needed to resolve the exception handler table and debug
    offsets). `all_functions` and `bc_header` are passed through to
    `format_instruction` for `function_id`/`bigint_id` resolution
    respectively.
    """
    name = table.resolve(header.function_name)
    #: hermes-dec's own header-line label per FunctionKind - see FunctionHeader.py.
    function_kind_label = {
        None: 'Function',
        FunctionKind.NORMAL: 'Function',
        FunctionKind.GENERATOR: 'Generator function',
        FunctionKind.ASYNC: 'Async function',
    }[header.kind]
    header_line = (
        f'=> [{function_kind_label} #{header.index} "{name}" of {header.bytecode_size_in_bytes} bytes]: '
        f"{header.param_count} params, frame size={header.frame_size}, "
        f"strict={int(header.strict_mode)}, exc handler={int(header.has_exception_handler)}, "
        f"debug info={int(header.has_debug_info)}  @ offset 0x{header.offset:08x}"
    )

    lines = [header_line]
    if header.has_exception_handler:
        lines.append(_format_exception_handlers_line(data, header, version))
    if header.has_debug_info:
        lines.append(_format_debug_offsets_line(data, header, version))
    lines += ["", "Bytecode listing:", ""]
    lines.extend(
        format_instruction(data, i, header.offset, table, version, all_functions, bc_header) for i in instructions
    )

    return "\n".join(lines)


def _format_exception_handlers_line(data: bytes, header: FunctionHeaderEntry, version: int) -> str:
    """
    `  [Exception handlers: [start=0xHEX, end=0xHEX, target=0xHEX] ...]`
    - confirmed format for a single handler against real hermes-dec
    output; the separator between multiple handlers is NOT confirmed
    (no multi-handler real example seen) - space-separated here as a
    reasonable guess.

    Falls back to a clearly-marked `<unresolved: ...>` placeholder
    instead of raising when resolution fails, so that one function's
    unresolved edge case doesn't abort `format_bundle()` for an entire
    otherwise-healthy bundle - though as of `ExceptionHandlerTable.py`'s
    `VERSION_TO_LARGE_HEADER_SIZE` fix, no such case is currently known
    in either test fixture (both resolve 100% cleanly at scale).
    """
    try:
        handlers = resolve_exception_handlers(data, header, version)
    except HermesBytecodeError as exc:
        return f"  [Exception handlers: <unresolved: {exc}>]"

    entries = " ".join(
        f"[start=0x{h.start:x}, end=0x{h.end:x}, target=0x{h.target:x}]" for h in handlers
    )
    return f"  [Exception handlers: {entries} ]"


def _format_debug_offsets_line(data: bytes, header: FunctionHeaderEntry, version: int) -> str:
    """
    `  [Debug offsets: source_locs=0xHEX, scope_desc_data=0xHEX]` -
    matches real hermes-dec's own disassembler print exactly (it reads
    a third field, `textifiedCallees`, but never prints it - see
    `DebugOffsets.py`'s module docstring - so neither do we).

    Falls back to a clearly-marked `<unresolved: ...>` placeholder on
    the same class of error `_format_exception_handlers_line` does,
    for the same reason. Untested against a real `has_debug_info=True`
    function in either test fixture - see `DebugOffsets.py`'s module
    docstring for why neither currently has one.
    """
    try:
        offsets = resolve_debug_offsets(data, header, version)
    except HermesBytecodeError as exc:
        return f"  [Debug offsets: <unresolved: {exc}>]"

    return f"  [Debug offsets: source_locs=0x{offsets.source_locations:x}, scope_desc_data=0x{offsets.scope_desc_data:x}]"


def format_bundle(data: bytes, bc_header: BytecodeFileHeader, table: StringTable, version: int) -> str:
    """
    Decode and format every function in `data` into one hermes-dec-style
    multi-function `.hasm` text: each function's `format_function()`
    block, each followed by `SECTION_SEPARATOR` on its own line - the
    exact boundary `scripts/split_output_file.py`'s `iter_sections()`
    scans for (see module docstring's "Pre-existing, separate gap" note
    re: function-name extraction specifically, which is unaffected
    here). The separator follows EVERY function, including the last one
    - confirmed against real hermes-dec's own `hbc_disassembler.py`
    source (`disassemble_function`'s trailing `print(); print();
    print('='*15); print()` calls run unconditionally after every
    function, not specially skipped for the final one) and against a
    full-file diff of its actual output for apps/testy/96: without a
    trailing separator, this function's own output was missing exactly
    that one occurrence at the very end of the file.

    This resolves overflowed function headers itself (via
    `FunctionHeaderOverflow.resolve_overflowed_headers`) - callers don't
    need to do that step separately first.
    """
    from hermes_disassembler.format.FunctionHeader import parse_function_headers

    entries = parse_function_headers(data, bc_header)
    resolved = resolve_overflowed_headers(data, bc_header, entries)

    blocks = []
    for entry in resolved:
        instructions = decode_function(data, entry.offset, entry.bytecode_size_in_bytes, version)
        blocks.append(format_function(data, entry, instructions, table, version, resolved, bc_header))

    return f"\n\n\n{SECTION_SEPARATOR}\n\n".join(blocks) + f"\n\n\n{SECTION_SEPARATOR}\n\n"
