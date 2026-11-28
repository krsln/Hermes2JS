"""Array and object destructuring recovered from iterator scaffolds and register copies.

Merged from: test_array_pattern_defaults_with_long_jump_cleanup, test_array_pattern_object_element_kept_in_registers, test_array_pattern_object_element_with_rest, test_destructuring_before_a_moved_environment, test_destructuring_cleanup_in_try, test_destructuring_copied_to_targets_at_the_end, test_destructuring_default_close_copy, test_destructuring_element_targets, test_destructuring_hoisted_undefined, test_destructuring_into_a_created_environment, test_destructuring_slot_then_register, test_destructuring_with_a_dead_cleanup_catch, test_destructuring_with_leading_holes, test_destructuring_with_two_leading_holes, test_single_element_destructuring.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# array_pattern_defaults_with_long_jump_cleanup
#
# An array pattern with default values whose cleanup handlers reach the shared close by a long jump (F-278).
#
# `const [a = "", b = "", c = ""] = text.split("/")` wraps each default in a try range whose handler is
# `Catch; JmpLong CLOSE` (the shared `IteratorClose; Throw` is too far for a short `Jmp`). The cleanup vocabulary knew
# `Jmp` but not `JmpLong`, so the handler was a "real catch", the pattern kept its iterator protocol and the
# function a `goto` (98/7643 `resolveBlurhashString`).
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_defaults_pattern_is_one_statement():
    hasm = (_DATA / "array_pattern_defaults_with_long_jump_cleanup_98_7643.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7643, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert '[r11 = "", r10 = "", r7 = ""] = r6;' in out
    assert "GetIterator" not in out


# ----------------------------------------------------------------------------------------------------
# array_pattern_object_element_kept_in_registers
#
# An object-pattern element whose leaves are also kept in registers stays one pattern (F-279).
#
# `const [{ nextScreenId, tabPath }, x] = useNextScreenId()` where the names are captured by a closure and read
# locally too: each property is read, copied into the variable's own register (`r4 = leaf`) and stored into its
# environment slot, and the last read goes into the source register itself (`r5 = r5.tabPath`). The pattern stores
# into the slots; the registers that are still read afterwards are restored from them (98/6599 `LinkWithPreview`).
# ----------------------------------------------------------------------------------------------------

def test_the_object_element_is_a_pattern_and_the_local_copies_are_restored():
    hasm = (_DATA / "array_pattern_object_element_kept_in_registers_98_6599.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6599, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "[{ nextScreenId: __environment__[8], tabPath: __environment__[9] }, __environment__[10]] = r13;" in out
    assert "r4 = __environment__[8];" in out
    assert "r8 = __environment__[9];" in out


# ----------------------------------------------------------------------------------------------------
# array_pattern_object_element_with_rest
#
# An object pattern with a `...rest` as an element of an array pattern collapses into one destructuring.
#
# `const [a, { if: b, ...rest }] = param` stores each property straight into an environment slot and builds the
# rest with `copyDataProperties`; the iterator cleanup `try` around it kept the function full of `goto`
# (98/10811). `ArrayDestructuringCfgPass` now reads `{ if: slot, ...slot }` as the element, and the register that
# kept the rest value is restored from its slot.
# ----------------------------------------------------------------------------------------------------

def test_object_element_with_rest_is_one_pattern():
    hasm = (_DATA / "array_pattern_object_element_with_rest_98_10811.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10811, strict=False), verbose=False, raw=False)

    assert "[__environment__[0], { if: __environment__[1], ...__environment__[2] }] = param1;" in out
    assert "r4 = __environment__[2];" in out
    assert "goto" not in out
    assert "GetIterator" not in out


# ----------------------------------------------------------------------------------------------------
# destructuring_before_a_moved_environment
#
# A destructuring whose environment creation was moved in front of it (98/5651 `useThenable`).
#
# `const [x] = useState(p)` where `x` lives in the closure environment: Hermes creates the environment in the middle of
# the chain (`CreateTopLevelEnvironment r3` between the element and its close check) into the register that also holds
# the source (`r3 = r4; ... GetIterator(r3)`). `ArrayDestructuringCfgPass` moves such a creation in front of the
# pattern and gave up when the source read the created register, so the first pattern stayed open-coded with its
# `if (rIt !== undefined)` guards. The creation now runs after the pattern in that case.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    hasm = (_DATA / "destructuring_before_a_moved_environment_98_5651.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_all_three_patterns_are_printed():
    out = _render()

    assert "[__environment__[0]] = r3;" in out
    assert "[r2, __environment__[2]] = r9;" in out
    assert "[__environment__[3]] = r5;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_cleanup_in_try
#
# `ArrayDestructuringCfgPass` collapses a destructuring pattern and removes its
# iterator-cleanup blocks from the CFG. A surrounding `try` (here the `for...of`
# over the iterator) lists those blocks in its range too; they were only
# removed from the handlers that guard the pattern itself, so the surrounding
# handler kept CFG-less blocks, and the dominator analysis died with a
# `KeyError` (98/5649 `extractPathFromURL`: "Code generation failed").
# ----------------------------------------------------------------------------------------------------

_HASM = """
=> [Function #5649 "extractPathFromURL" of 548 bytes]: 3 params, frame size=39, strict=1, exc handler=1, debug info=0  @ offset 0x001b9054
  [Exception handlers: [start=0x188, end=0x18c, target=0x192] [start=0x4c, end=0x213, target=0x21b] ]

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 20, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 16, UInt8: 2>
==> 00000006: <LoadConstUndefined>: <Reg8: 0>
==> 00000008: <LoadConstUndefined>: <Reg8: 19>
==> 0000000a: <LoadConstUndefined>: <Reg8: 1>
==> 0000000c: <LoadConstUndefined>: <Reg8: 18>
==> 0000000e: <LoadConstUndefined>: <Reg8: 17>
==> 00000010: <LoadConstUndefined>: <Reg8: 3>
==> 00000012: <LoadParam>: <Reg8: 15, UInt8: 1>
==> 00000015: <IteratorBegin>: <Reg8: 2, Reg8: 15>
==> 00000018: <LoadConstString>: <Reg8: 14, string_id: 1865>  # String: '?' (String)
==> 0000001c: <GetGlobalObject>: <Reg8: 13>
==> 0000001e: <LoadConstString>: <Reg8: 12, string_id: 503>  # String: '/' (String)
==> 00000022: <LoadConstString>: <Reg8: 5, string_id: 6457>  # String: '' (Identifier)
==> 00000026: <LoadConstUInt8>: <Reg8: 10, UInt8: 1>
==> 00000029: <LoadConstString>: <Reg8: 9, string_id: 1693>  # String: '^' (String)
==> 0000002d: <LoadConstString>: <Reg8: 8, string_id: 840>  # String: '.' (String)
==> 00000031: <LoadConstString>: <Reg8: 7, string_id: 1900>  # String: '\\.' (String)
==> 00000035: <LoadConstString>: <Reg8: 6, string_id: 1168>  # String: '(/)*' (String)
==> 00000039: <LoadConstNull>: <Reg8: 4>
==> 0000003b: <Mov>: <Reg8: 21, Reg8: 15>
==> 0000003e: <IteratorNext>: <Reg8: 23, Reg8: 2, Reg8: 21>
==> 00000042: <Mov>: <Reg8: 21, Reg8: 2>
==> 00000045: <JStrictEqualLong>: <Addr32: 477, Reg8: 21, Reg8: 0>  # Address: 00000222
==> 0000004c: <Mov>: <Reg8: 19, Reg8: 23>
==> 0000004f: <GetByIdShort>: <Reg8: 22, Reg8: 23, UInt8: 0, string_id: 180>  # String: 'match' (Identifier)
==> 00000054: <CreateRegExp>: <Reg8: 21, string_id: 4591, string_id: 6457, UInt32: 90>  # String: '^[^:]+:' (String)  # String: '' (Identifier)
==> 00000062: <Call2>: <Reg8: 21, Reg8: 22, Reg8: 23, Reg8: 21>
==> 00000067: <Eq>: <Reg8: 22, Reg8: 21, Reg8: 4>
==> 0000006b: <LoadConstUndefined>: <Reg8: 24>
==> 0000006d: <JmpTrue>: <Addr8: 7, Reg8: 22>  # Address: 00000074
==> 00000070: <GetByIndex>: <Reg8: 24, Reg8: 21, UInt8: 0>
==> 00000074: <JNotEqual>: <Addr8: 7, Reg8: 24, Reg8: 4>  # Address: 0000007b
==> 00000078: <Mov>: <Reg8: 24, Reg8: 5>
==> 0000007b: <Mov>: <Reg8: 25, Reg8: 19>
==> 0000007e: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 00000083: <TryGetById>: <Reg8: 27, Reg8: 13, UInt8: 2, string_id: 29>  # String: 'RegExp' (Identifier)
==> 00000089: <LoadFromEnvironment>: <Reg8: 21, Reg8: 20, UInt8: 0>
==> 0000008d: <GetByIdShort>: <Reg8: 22, Reg8: 21, UInt8: 3, string_id: 115>  # String: 'default' (Identifier)
==> 00000092: <Call2>: <Reg8: 26, Reg8: 22, Reg8: 0, Reg8: 24>
==> 00000097: <TryGetById>: <Reg8: 22, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 0000009d: <GetByIdShort>: <Reg8: 22, Reg8: 22, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000000a2: <Call2>: <Reg8: 30, Reg8: 22, Reg8: 9, Reg8: 26>
==> 000000a7: <CreateThisForNew>: <Reg8: 26, Reg8: 27, UInt8: 6>
==> 000000ab: <Mov>: <Reg8: 31, Reg8: 26>
==> 000000ae: <Construct>: <Reg8: 22, Reg8: 27, UInt8: 2>
==> 000000b2: <SelectObject>: <Reg8: 22, Reg8: 26, Reg8: 22>
==> 000000b6: <Call3>: <Reg8: 25, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 5>
==> 000000bc: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000000c1: <CreateRegExp>: <Reg8: 22, string_id: 1678, string_id: 6578, UInt32: 11>  # String: '\\/+' (String)  # String: 'g' (Identifier)
==> 000000cf: <Call3>: <Reg8: 25, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 12>
==> 000000d5: <GetByIdShort>: <Reg8: 23, Reg8: 25, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000000da: <CreateRegExp>: <Reg8: 22, string_id: 1676, string_id: 6457, UInt32: 86>  # String: '^\\/' (String)  # String: '' (Identifier)
==> 000000e8: <Call3>: <Reg8: 22, Reg8: 23, Reg8: 25, Reg8: 22, Reg8: 5>
==> 000000ee: <TryGetById>: <Reg8: 23, Reg8: 13, UInt8: 2, string_id: 29>  # String: 'RegExp' (Identifier)
==> 000000f4: <GetByIdShort>: <Reg8: 21, Reg8: 21, UInt8: 3, string_id: 115>  # String: 'default' (Identifier)
==> 000000f9: <Call2>: <Reg8: 24, Reg8: 21, Reg8: 0, Reg8: 24>
==> 000000fe: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 7, string_id: 230>  # String: 'split' (Identifier)
==> 00000103: <Call2>: <Reg8: 25, Reg8: 21, Reg8: 22, Reg8: 8>
==> 00000108: <GetByIdShort>: <Reg8: 22, Reg8: 25, UInt8: 8, string_id: 126>  # String: 'map' (Identifier)
==> 0000010d: <CreateClosure>: <Reg8: 21, Reg8: 20, function_id: 10986>  # Function: [#10986  of 36 bytes]: 2 params @ offset 0x002215b5
==> 00000112: <Call2>: <Reg8: 22, Reg8: 22, Reg8: 25, Reg8: 21>
==> 00000117: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 9, string_id: 167>  # String: 'join' (Identifier)
==> 0000011c: <Call2>: <Reg8: 22, Reg8: 21, Reg8: 22, Reg8: 7>
==> 00000121: <TryGetById>: <Reg8: 21, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 00000127: <GetByIdShort>: <Reg8: 21, Reg8: 21, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 0000012c: <Call4>: <Reg8: 30, Reg8: 21, Reg8: 9, Reg8: 24, Reg8: 6, Reg8: 22>
==> 00000133: <CreateThisForNew>: <Reg8: 22, Reg8: 23, UInt8: 6>
==> 00000137: <Mov>: <Reg8: 31, Reg8: 22>
==> 0000013a: <Construct>: <Reg8: 21, Reg8: 23, UInt8: 2>
==> 0000013e: <SelectObject>: <Reg8: 1, Reg8: 22, Reg8: 21>
==> 00000142: <GetByIdShort>: <Reg8: 21, Reg8: 16, UInt8: 7, string_id: 230>  # String: 'split' (Identifier)
==> 00000147: <Call2>: <Reg8: 21, Reg8: 21, Reg8: 16, Reg8: 14>
==> 0000014c: <Mov>: <Reg8: 25, Reg8: 21>
==> 0000014f: <IteratorBegin>: <Reg8: 23, Reg8: 25>
==> 00000152: <Mov>: <Reg8: 21, Reg8: 25>
==> 00000155: <IteratorNext>: <Reg8: 22, Reg8: 23, Reg8: 21>
==> 00000159: <Mov>: <Reg8: 21, Reg8: 23>
==> 0000015c: <StrictEq>: <Reg8: 24, Reg8: 21, Reg8: 0>
==> 00000160: <LoadConstUndefined>: <Reg8: 21>
==> 00000162: <JmpTrue>: <Addr8: 6, Reg8: 24>  # Address: 00000168
==> 00000165: <Mov>: <Reg8: 21, Reg8: 22>
==> 00000168: <Mov>: <Reg8: 18, Reg8: 21>
==> 0000016b: <NewArray>: <Reg8: 21, UInt16: 0>
==> 0000016f: <LoadConstZero>: <Reg8: 22>
==> 00000171: <JmpTrue>: <Addr8: 43, Reg8: 24>  # Address: 0000019c
==> 00000174: <Mov>: <Reg8: 24, Reg8: 25>
==> 00000177: <IteratorNext>: <Reg8: 27, Reg8: 23, Reg8: 24>
==> 0000017b: <Mov>: <Reg8: 24, Reg8: 23>
==> 0000017e: <StrictEq>: <Reg8: 24, Reg8: 24, Reg8: 0>
==> 00000182: <Mov>: <Reg8: 26, Reg8: 22>
==> 00000185: <JmpTrue>: <Addr8: 23, Reg8: 24>  # Address: 0000019c
==> 00000188: <PutByValStrict>: <Reg8: 21, Reg8: 26, Reg8: 27>
==> 0000018c: <AddN>: <Reg8: 22, Reg8: 26, Reg8: 10>
==> 00000190: <Jmp>: <Addr8: -28>  # Address: 00000174
==> 00000192: <Catch>: <Reg8: 22>
==> 00000194: <JmpTrue>: <Addr8: 6, Reg8: 24>  # Address: 0000019a
==> 00000197: <IteratorClose>: <Reg8: 23, UInt8: 1>
==> 0000019a: <Throw>: <Reg8: 22>
==> 0000019c: <Mov>: <Reg8: 17, Reg8: 21>
==> 0000019f: <Mov>: <Reg8: 24, Reg8: 18>
==> 000001a2: <GetByIdShort>: <Reg8: 23, Reg8: 24, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 000001a7: <CreateRegExp>: <Reg8: 22, string_id: 1678, string_id: 6578, UInt32: 11>  # String: '\\/+' (String)  # String: 'g' (Identifier)
==> 000001b5: <Call3>: <Reg8: 23, Reg8: 23, Reg8: 24, Reg8: 22, Reg8: 12>
==> 000001bb: <GetByIdShort>: <Reg8: 22, Reg8: 23, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000001c0: <GetByIdShort>: <Reg8: 24, Reg8: 21, UInt8: 10, string_id: 177>  # String: 'length' (Identifier)
==> 000001c5: <Mov>: <Reg8: 21, Reg8: 5>
==> 000001c8: <JmpFalse>: <Addr8: 32, Reg8: 24>  # Address: 000001e8
==> 000001cb: <Mov>: <Reg8: 25, Reg8: 17>
==> 000001ce: <GetByIdShort>: <Reg8: 24, Reg8: 25, UInt8: 9, string_id: 167>  # String: 'join' (Identifier)
==> 000001d3: <Call2>: <Reg8: 25, Reg8: 24, Reg8: 25, Reg8: 14>
==> 000001d8: <TryGetById>: <Reg8: 24, Reg8: 13, UInt8: 4, string_id: 10>  # String: 'HermesInternal' (Identifier)
==> 000001de: <GetByIdShort>: <Reg8: 24, Reg8: 24, UInt8: 5, string_id: 105>  # String: 'concat' (Identifier)
==> 000001e3: <Call2>: <Reg8: 21, Reg8: 24, Reg8: 14, Reg8: 25>
==> 000001e8: <Call2>: <Reg8: 23, Reg8: 22, Reg8: 23, Reg8: 21>
==> 000001ed: <Mov>: <Reg8: 3, Reg8: 23>
==> 000001f0: <Mov>: <Reg8: 22, Reg8: 1>
==> 000001f3: <GetByIdShort>: <Reg8: 21, Reg8: 22, UInt8: 11, string_id: 47>  # String: 'test' (Identifier)
==> 000001f8: <Call2>: <Reg8: 21, Reg8: 21, Reg8: 22, Reg8: 23>
==> 000001fd: <JmpTrue>: <Addr8: 8, Reg8: 21>  # Address: 00000205
==> 00000200: <JmpLong>: <Addr32: -453>  # Address: 0000003b
==> 00000205: <Mov>: <Reg8: 4, Reg8: 3>
==> 00000208: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 217>  # String: 'replace' (Identifier)
==> 0000020d: <Call3>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 5>
==> 00000213: <Mov>: <Reg8: 3, Reg8: 2>
==> 00000216: <IteratorClose>: <Reg8: 3, UInt8: 0>
==> 00000219: <Ret>: <Reg8: 1>
==> 0000021b: <Catch>: <Reg8: 1>
==> 0000021d: <IteratorClose>: <Reg8: 2, UInt8: 1>
==> 00000220: <Throw>: <Reg8: 1>
==> 00000222: <Ret>: <Reg8: 0>
"""


def test_a_surrounding_try_does_not_keep_the_removed_cleanup_blocks():
    out = Decompiler.render(Decompiler.build_context(_HASM, 5649), verbose=False)

    assert "function extractPathFromURL(" in out


# ----------------------------------------------------------------------------------------------------
# destructuring_copied_to_targets_at_the_end
#
# `[x, y, z] = src` into outer variables, the targets copied once at the end (98/13553; 98/11846 `HSVtoRGB`).
#
# The element registers are temporaries; the last block copies every one into its target (last element first) and the
# close block repeats those copies after `IteratorClose`. The pass knew the binding form that copies each target at the
# next element's boundary and mixed the first copy up with such a boundary copy, so the open-coded `next()` ladder stayed.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "destructuring_copied_to_targets_at_the_end_98_13553.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_targets_are_the_pattern():
    out = _render_2()

    assert "[r7, r6, r5] = r11;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_2(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_default_close_copy
#
# `for (const [key, value = ""] of entries)`: the default's guard closes a copy of the iterator (F-214, 98/5707).
#
# The handler around the default value is `Catch ex; JmpTrue done; Mov r20 <- it; IteratorClose r20, 1; Throw ex`. It
# closes a register that was copied from the iterator, which the cleanup check did not accept: the handler stayed, it
# cut through the pattern, and the whole destructuring printed as the open-coded iterator protocol with a `goto`.
# ----------------------------------------------------------------------------------------------------

def test_the_default_value_pattern_is_one_destructuring():
    hasm = (_DATA / "destructuring_default_close_copy_98_5707.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 5707, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert '[r14, r13 = ""] = r19;' in code
    assert "GetIterator" not in code


# ----------------------------------------------------------------------------------------------------
# destructuring_element_targets
#
# Iterator destructuring whose element targets run code (F-215, 98/10423 `VirtualCollectionSpacer`, 98/10166).
#
#     const [{ SpacerView }, setX] = useState(...)
#
# Hermes reads the element's properties between two fetches and stores the last element into a slot, all behind a
# cleanup handler. The pass knew register targets only, so these stayed an open-coded iterator state machine. The
# property reads and the store are targets of the pattern now, and the pattern keeps the order JavaScript runs them
# in (fetch, bind, fetch): nothing is moved across a `next()`. The target is recognised by the IR shape of the binding
# code (a plain property load of the element register, a store of it into a slot that needs no evaluation), not by
# opcode names.
# ----------------------------------------------------------------------------------------------------

def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_an_object_pattern_element_and_a_slot_store_are_one_destructuring():
    code = _code("destructuring_object_target_98_10423.hasm", 10423)

    assert "[{ SpacerView: r0 }, __environment__[2]] = r10;" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_a_hole_followed_by_a_slot_store():
    code = _code("destructuring_hole_store_98_10166.hasm", 10166)

    assert "[, __environment__[1]] = r9;" in code
    assert ".next()" not in code


def test_member_targets_with_constant_keys_in_a_per_element_try():
    # 98/11908 `maybeSwapComponents`: `[a[0], a[1]] = src`. The element value is stored straight from the fetch
    # register (the copy was folded away) and the key loads are dead; every store sits in its own try range whose
    # handler only closes the iterator.
    code = _code("destructuring_member_targets_98_11908.hasm", 11908)

    assert "[r0[0], r0[1]] = r5;" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_a_register_read_after_the_pattern_is_restored_from_its_slot():
    # 98/5806: `const [a, b] = useState(...)` where `a` is a closure variable that is also kept in a register
    # (`r8`) and read later. The pattern stores into the slot; the register is read back from it.
    code = _code("destructuring_slot_restore_98_5806.hasm", 5806)

    assert "[__environment__[3], __environment__[4]] = r11;" in code
    assert "r8 = __environment__[3];" in code
    assert "goto" not in code
    assert ".next()" not in code


def test_fetch_that_reads_the_source_register_without_a_copy():
    # 98/10000: `const [key] = args`: the source already sits in the register `IteratorNext` reads, so
    # there is no `Mov t <- src` before the first fetch.
    code = _code("destructuring_no_source_copy_98_10000.hasm", 10000)

    assert "[r3] = r2;" in code
    assert ".next()" not in code


def test_environment_created_between_the_fetch_and_the_first_store():
    # 98/10817: parameter destructuring into a fresh environment. `CreateFunctionEnvironment` sits in the
    # element block, right before the store into its slot; the allocation moves in front of the pattern.
    code = _code("destructuring_env_creation_98_10817.hasm", 10817)

    assert "[__environment__[0], r11] = param1;" in code
    assert "r8 = __environment__[0];" in code
    assert ".next()" not in code


def test_no_source_copy_and_the_undefined_loaded_inside_the_check():
    # 98/10001: `const [key] = args` where the first block is `IteratorNext; Mov; LoadConstUndefined; StrictEq;
    # LoadConstUndefined; JmpTrue` (the shape of F-234 with the `undefined` loaded in the middle of the check).
    code = _code("destructuring_no_copy_late_undefined_98_10001.hasm", 10001)

    assert "[r2] = r1;" in code
    assert ".next()" not in code


# ----------------------------------------------------------------------------------------------------
# destructuring_hoisted_undefined
#
# `const [uri, scale = "1x"] = x.split(" ")`: the `undefined` the checks compare with is loaded ahead of the chain (F-215, 98/10271).
#
# A default on a LATER element makes the compiler load `undefined` once, before element 1's own `LoadConstUndefined`
# and its fetch: the head block read `LoadConstUndefined; LoadConstUndefined; Mov; IteratorNext; Mov; StrictEq; JmpTrue`,
# a shape the pass did not know, so the iterator protocol stayed open-coded with a `goto`.
# ----------------------------------------------------------------------------------------------------

def test_the_default_on_the_second_element_is_one_pattern():
    hasm = (_DATA / "destructuring_hoisted_undefined_98_10271.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10271, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert '[r5, r6 = "1x"] = r4;' in code
    assert "goto" not in code
    assert "GetIterator" not in code


# ----------------------------------------------------------------------------------------------------
# destructuring_into_a_created_environment
#
# Array destructuring whose elements go into the slots of an environment made by `createEnvironment()` (98/13030).
#
# The slots (`r4[0]`, `r4[1]`) are those of a `StoreToEnvironment`, plain variables like the members of the function's
# own `__environment__`, but the pass only knew the latter, so the open-coded `next()` ladder stayed. The two
# registers the elements went through are read afterwards; each is restored from ITS slot (the first element's fetch
# register is also the second element's register and must not be restored from the first slot).
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    hasm = (_DATA / "destructuring_into_a_created_environment_98_13030.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_slots_are_a_pattern_and_each_register_is_restored_from_its_own_slot():
    out = _render_3()

    assert "[r4[0], r4[1]] = r9;" in out
    assert "r6 = r4[0];" in out
    assert "r7 = r4[1];" in out
    assert "GetIterator" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_3(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_3(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_slot_then_register
#
# `const [a, b] = x` where `a` lives in the closure environment and `b` in a register (98/9949).
#
# Element 1 is stored into an environment slot through a scratch register (`r5`), and element 2 then takes that same
# register as its own target. `ArrayDestructuringCfgPass._match` refused any pattern whose scratch register was also a
# leaf. A scratch register that a later element takes over holds the later element afterwards, so there is nothing of
# the first one to restore and the pattern is printed.
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    hasm = (_DATA / "destructuring_slot_then_register_98_9949.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_pattern_is_printed():
    out = _render_4()

    assert "[__environment__[0], r5] = param1;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out
    assert "r5 = r5.map(function_12722);" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_4(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_4(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_with_a_dead_cleanup_catch
#
# A destructuring pattern in a function with no exception handler table leaves no dead cleanup code behind (98/11141).
#
# `[, r2] = param1` compiles to the open-coded iterator chain plus a `Catch; IteratorClose it, 1; Throw` block at the
# end. The function has no handler entry, so the block has no predecessor and no handler: nothing removed it with the
# pattern, and it printed after the `return` (`r1.return(); throw caughtException;`).
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "destructuring_with_a_dead_cleanup_catch_98_11141.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 11141, strict=False), verbose=False, raw=False)


def test_the_cleanup_block_is_gone():
    out = _render_5()

    assert "[, r2] = param1;" in out
    assert "return r2 != null;" in out
    assert ".return()" not in out
    assert "caughtException" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_5(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_5(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_with_leading_holes
#
# `[, , a, b, c, d] = x` with the first elements skipped is recognised as a pattern (98/7996 `C`).
#
# With the source copied first (`Mov t <- src`), the `undefined` the done checks compare with is loaded between the
# fetch and the check, ahead of the `StrictEq` (a shape the pass only knew without the copy, for a single element). It
# is no element's initial value, so only a pattern whose first element is a hole can use it; the open-coded
# `next()`/`=== undefined` ladder was left otherwise.
# ----------------------------------------------------------------------------------------------------

def _render_6() -> str:
    hasm = (_DATA / "destructuring_with_leading_holes_98_7996.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_holes_stay_holes_in_the_pattern():
    out = _render_6()

    assert "[, , r9, r8, r7, r6] = r10;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_6(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_6(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# destructuring_with_two_leading_holes
#
# `[, , a, b] = x` is recognised as a pattern when the first hole copies the check's result into the shared flag
# register (98/13555).
#
# A leading hole has no initial value to load after the `StrictEq`; Hermes copies the result into the flag register the
# later checks use (`Mov r4 <- r2`) instead of the `LoadConstUndefined` the pass expected, so the head block was
# parsed as something else and the open-coded `next()` ladder stayed.
# ----------------------------------------------------------------------------------------------------

def _render_7() -> str:
    hasm = (_DATA / "destructuring_with_two_leading_holes_98_13555.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 13555, strict=False), verbose=False, raw=False)


def test_the_holes_stay_holes_in_the_pattern_2():
    out = _render_7()

    assert "[, , r5, r6] = r7;" in out
    assert "[r11, r10] = r5;" in out
    assert "GetIterator" not in out
    assert ".next()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_7(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_7(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# single_element_destructuring
#
# `const [a] = x` with one element prints as a pattern, and what reads `a` afterwards reads `a` (98/9900).
#
# For one element Hermes loads a single `undefined` that serves as the value the done check compares with and as the
# element's initial value, and fetches from the source register itself: `IteratorNext, Mov, LoadConstUndefined,
# StrictEq, JmpTrue`. `ArrayDestructuringCfgPass._parse` knew the shapes with a separate load and left this one as
# `GetIterator(..)` with `if (rIt !== undefined)` guards. Matching it exposed a second thing: the frontend had read
# `a` through the dropped `Mov a <- v` as the fetched register `v`, so `return a === b` printed `return r3 === r1`.
# The reads that hold that very node now read the target register.
# ----------------------------------------------------------------------------------------------------

def _render_8() -> str:
    hasm = (_DATA / "single_element_destructuring_98_9900.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_pattern_is_printed_2():
    out = _render_8()

    assert "[r2] = param1;" in out
    assert "GetIterator" not in out
    assert ".return()" not in out


def test_the_element_is_read_from_its_own_register():
    out = _render_8()

    assert "return r2 === r1;" in out
    assert "r3" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_8(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_8(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
