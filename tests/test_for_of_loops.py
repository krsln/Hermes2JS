"""`for (... of ...)` / `for (... in ...)` recognition: scaffold removal, closes, breaks, nesting.

Merged from: test_constant_for_end_edge_before_for_of, test_for_header_bound, test_for_in_property_list_guard, test_for_of_break_through_a_copy, test_for_of_break_with_a_several_block_body, test_for_of_close_through_a_copy, test_for_of_dead_iterator_copy, test_for_of_guarded_body, test_for_of_in_a_loop_with_a_latch, test_for_of_in_an_if_chain_in_a_for_of, test_for_of_inline_close, test_for_of_param_iterable, test_for_of_return_through_a_reused_copy, test_for_of_with_its_done_test_in_the_body, test_for_of_without_scaffold, test_nested_for_of_in_a_for_of, test_yield_inside_a_for_of_that_closes_its_iterator.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# constant_for_end_edge_before_for_of
#
# A later `for-of`'s handler does not stop a constant from moving onto the edge into END (96/11000).
#
#     typeof a === "object" && a !== null && a.value === undefined  ->  END: Object.keys(a) ... for (const k of keys)
#
# The last test reads `r5 = undefined`, and END (the `for-of`'s `r7 === r5` exit test) reads it too, so the test takes the
# value and END gets its own copy. The `for-of` has an iterator-close handler that reads `r2`, which the test block
# also writes; but `IteratorBegin` in END writes `r2` before the protected range starts, so the handler never sees the
# test's value. The guard looked at every handler and gave up, leaving two `goto`s.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_three_tests_are_one_condition_before_the_for_of():
    hasm = (_DATA / "constant_for_end_edge_before_for_of_96_11000.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11000, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    # Since F-297 the copy `r3 = param1` is folded into the test (it is dead for both exits).
    assert 'if (r2 === "object" && (param1 !== null && param1.value === undefined)) {' in out


# ----------------------------------------------------------------------------------------------------
# for_header_bound
#
# A `for` header runs before the first iteration (`decode`, 96/7575):
#
#     r1 = r1.length; if (1 < r1) { for (...; r2 < r1.length; ) { ...; r1 = r1.length } }
#
# The bottom-tested loop reloads its bound (`r1 = r1.length`) right before the
# compare, and the bound was folded into the condition. But the entry guard had
# already replaced `r1` by that same length, so the header's first test read
# `r1.length` of a NUMBER (`undefined`) and the loop never ran. The reload stays
# a statement and the condition reads the register.
# ----------------------------------------------------------------------------------------------------

_DECODE = r"""

=> [Function #7575 "decode" of 157 bytes]: 2 params, frame size=19, strict=1, exc handler=1, debug info=0  @ offset 0x001b4c67
  [Exception handlers: [start=0x9, end=0x19, target=0x1b] ]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 1>
==> 00000003: <LoadConstUndefined>: <Reg8: 5>
==> 00000005: <LoadConstUndefined>: <Reg8: 6>
==> 00000007: <LoadConstUndefined>: <Reg8: 7>
==> 00000009: <GetGlobalObject>: <Reg8: 1>
==> 0000000b: <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 10229>  # String: 'decodeURIComponent' (Identifier)
==> 00000011: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000014: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 1>
==> 00000019: <Ret>: <Reg8: 1>
==> 0000001b: <Catch>: <Reg8: 1>
==> 0000001d: <Mov>: <Reg8: 8, Reg8: 0>
==> 00000020: <GetByIdShort>: <Reg8: 3, Reg8: 8, UInt8: 2, string_id: 171>  # String: 'match' (Identifier)
==> 00000025: <GetEnvironment>: <Reg8: 4, UInt8: 0>
==> 00000028: <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 0>
==> 0000002c: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 8, Reg8: 2>
==> 00000031: <Mov>: <Reg8: 1, Reg8: 2>
==> 00000034: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 0000003b
==> 00000037: <NewArray>: <Reg8: 1, UInt16: 0>
==> 0000003b: <Mov>: <Reg8: 6, Reg8: 1>
==> 0000003e: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000041: <Mov>: <Reg8: 7, Reg8: 2>
==> 00000044: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000049: <LoadConstString>: <Reg8: 3, string_id: 7163>  # String: '' (Identifier)
==> 0000004d: <JNotLess>: <Addr8: 78, Reg8: 2, Reg8: 1>  # Address: 0000009b
==> 00000051: <LoadFromEnvironment>: <Reg8: 8, Reg8: 4, UInt8: 2>
==> 00000055: <Mov>: <Reg8: 2, Reg8: 6>
==> 00000058: <Mov>: <Reg8: 1, Reg8: 7>
==> 0000005b: <Call3>: <Reg8: 2, Reg8: 8, Reg8: 5, Reg8: 2, Reg8: 1>
==> 00000061: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 165>  # String: 'join' (Identifier)
==> 00000066: <Call2>: <Reg8: 9, Reg8: 1, Reg8: 2, Reg8: 3>
==> 0000006b: <Mov>: <Reg8: 0, Reg8: 9>
==> 0000006e: <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 171>  # String: 'match' (Identifier)
==> 00000073: <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 0>
==> 00000077: <Call2>: <Reg8: 2, Reg8: 8, Reg8: 9, Reg8: 2>
==> 0000007c: <Mov>: <Reg8: 1, Reg8: 2>
==> 0000007f: <JmpTrue>: <Addr8: 7, Reg8: 2>  # Address: 00000086
==> 00000082: <NewArray>: <Reg8: 1, UInt16: 0>
==> 00000086: <Mov>: <Reg8: 6, Reg8: 1>
==> 00000089: <Mov>: <Reg8: 2, Reg8: 7>
==> 0000008c: <Inc>: <Reg8: 2, Reg8: 2>
==> 0000008f: <Mov>: <Reg8: 7, Reg8: 2>
==> 00000092: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 169>  # String: 'length' (Identifier)
==> 00000097: <JLess>: <Addr8: -70, Reg8: 2, Reg8: 1>  # Address: 00000051
==> 0000009b: <Ret>: <Reg8: 0>
"""


def _render() -> str:
    context = Decompiler.build_context(_DECODE, 7575, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_header_does_not_read_length_of_a_length():
    js = _render()

    assert "r2 < r1.length" not in js
    assert "r2 < r1;" in js
    assert js.index("r1 = r1.length;\n        }") > js.index("r7 = r2;")


# ----------------------------------------------------------------------------------------------------
# for_in_property_list_guard
#
# `for (k in obj)` is printed without Hermes' null guard around it (96/5107 `addAnimatedValuesListenersToProps`).
#
#     GetPNameList r6, r5, ...      # `undefined` for a null/undefined object
#     JmpUndefined r6 -> exit       # the guard
#     GetNextPName r2, r6, ...      # the loop
#
# printed `r6 = HermesPropertyIterator(r5); if (r6 !== undefined) { for (const r2 in r5) { ... } }`. A for-in over
# null/undefined runs zero times, so the guard and the list's own definition say nothing the loop does not. They stay
# when later code still reads the list register.
# ----------------------------------------------------------------------------------------------------

_HEADER = (
    '=> [Function #5107 "addAnimatedValuesListenersToProps" of 52 bytes]: 3 params, frame size=20, strict=1, '
    'exc handler=0, debug info=0  @ offset 0x0017d8a9'
)

_BODY = """
Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 8, UInt8: 1>
==> 00000003: <LoadParam>: <Reg8: 7, UInt8: 2>
==> 00000006: <Mov>: <Reg8: 5, Reg8: 8>
==> 00000009: <GetEnvironment>: <Reg8: 1, UInt8: 0>
==> 0000000c: <LoadConstUndefined>: <Reg8: 0>
==> 0000000e: <GetPNameList>: <Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 00000013: <JmpUndefined>: <Addr8: 31, Reg8: 6>  # Address: 00000032
==> 00000016: <GetNextPName>: <Reg8: 2, Reg8: 6, Reg8: 5, Reg8: 4, Reg8: 3>
==> 0000001c: <JmpUndefined>: <Addr8: 22, Reg8: 2>  # Address: 00000032
==> 0000001f: <Mov>: <Reg8: 9, Reg8: 2>
==> 00000022: <GetByVal>: <Reg8: 10, Reg8: 8, Reg8: 9>
==> 00000026: <LoadFromEnvironment>: <Reg8: 9, Reg8: 1, UInt8: 11>
==> 0000002a: <Call3>: <Reg8: 9, Reg8: 9, Reg8: 0, Reg8: 10, Reg8: 7>
==> 00000030: <Jmp>: <Addr8: -26>  # Address: 00000016
==> 00000032: <Ret>: <Reg8: {returned}>
"""


def _render_2(returned: int) -> str:
    hasm = f"\n{_HEADER}\n{_BODY.format(returned=returned)}"

    return Decompiler.render(Decompiler.build_context(hasm, 5107, strict=False), verbose=False, raw=False)


def test_the_null_guard_and_the_property_list_are_not_printed():
    code = _render_2(returned=0)

    assert "for (const r2 in r5) {" in code
    assert "HermesPropertyIterator" not in code
    assert "!== undefined" not in code
    assert "goto" not in code


def test_the_guard_stays_when_the_property_list_is_read_after_the_loop():
    code = _render_2(returned=6)

    assert "HermesPropertyIterator(r5)" in code
    assert "if (r6 !== undefined) {" in code


# ----------------------------------------------------------------------------------------------------
# for_of_break_through_a_copy
#
# A `break` out of a `for-of` leaves no copy of the iterator behind either (98/5913 `convertRedirect`).
#
# Hermes closes the iterator on the way out through a scratch register (`r4 = r5; r5.return(); break;`). The loop's
# own close covers the `break`, so `_strip_inline_closes` drops the close; the copy stayed, read the iterator register
# by name, and kept `r5 = GetIterator(r7)` alive in front of the loop. The copy goes with the close when nothing that
# is still printed reads its register.
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    hasm = (_DATA / "for_of_break_through_a_copy_98_5913.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_iterator_setup_is_gone():
    out = _render_3()

    assert "of r7)" in out
    assert "GetIterator" not in out
    assert "break;" in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_3(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_break_with_a_several_block_body
#
# A `break` out of a `for-of` whose arm is several blocks long stays inside the loop (98/11038 `getStateForAction`).
#
# `for (r14 of routes) { if (key === key) { <several blocks, an if/else inside>; break; } ... }`: Hermes lays the arm out
# behind the loop and ends it with a jump to the loop's own merge. Only a one-block arm was moved into the loop; a longer
# one stayed behind it, where the loop's normal end (the iterator is done) ran it too - the printed code did the work of
# the arm for a list without a match. The arm now becomes the `if` body and each end that rejoins the merge a `break`.
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    hasm = (_DATA / "for_of_break_with_a_several_block_body_98_11038.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_arm_is_the_if_body_and_ends_in_a_break():
    out = _render_4()
    lines = [line.strip() for line in out.splitlines()]

    start = next(i for i, line in enumerate(lines) if line.startswith("for (let r14 of r10)"))
    body = lines[start:start + 30]

    assert "if (r16 === r14) {" in body
    assert "break;" in body
    assert body.index("break;") > body.index("if (r16 === r14) {")
    assert "GetIterator" not in out
    assert "label_1810" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_4(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_close_through_a_copy
#
# The close of a `for-of` that leaves through a `return` prints nothing, copy included (98/13334 `findInMenu`).
#
# Hermes closes the iterator on every way out of the loop, reading it through a scratch register (`r11 = r2;
# r11.return(); return r8;`). The loop's own close already covers the `return`, so `_strip_inline_closes` drops the
# close; it kept the copy (`r11 = r2;`) and the `GetIterator(..)` setup that the copy still read. It now takes the pair
# before a `return` as well as before a `break`, and a copy left alone before a `return` when nothing after reads it.
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "for_of_close_through_a_copy_98_13334.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_copy_or_setup_of_the_iterator_is_left():
    out = _render_5()

    assert "for (let r10 of r6)" in out
    assert "GetIterator" not in out
    assert "r11 = r2" not in out
    assert ".return()" not in out
    assert "return r8;" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_3(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_5(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_dead_iterator_copy
#
# The `GetIterator` setup in front of a for-of is dropped although the loop header copies the iterator (F-235).
#
# The header's done check copies the iterator (`Mov y <- it`); the copy is inlined into its uses and prints
# nothing, but its operand still names the iterator register, and the dead-setup check counted that as a read.
# `r1 = GetIterator(r2);` stayed in front of every such `for (x of xs)`.
#
#     98/4310  `anyInCell`
# ----------------------------------------------------------------------------------------------------

def test_an_inlined_copy_of_the_iterator_is_not_a_read():
    hasm = (_DATA / "for_of_dead_iterator_copy_98_4310.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4310, strict=False), verbose=False, raw=False)

    assert "for (let r4 of r2) {" in out
    assert "GetIterator" not in out


# ----------------------------------------------------------------------------------------------------
# for_of_guarded_body
#
# A `for-of` whose try covers only the loop body (F-166).
#
#     while (!done) { r = it.next(); try { body } finally { it.return() } }
#
# Two things kept it a `while`/`try` pile, or a `goto`:
#
#   * `LoopBreakStructurer` found the loop's merge only through the latches. A top-tested loop's latch just
#     jumps back, so `if (c) { r0 = x; it.return(); break; }` stayed outside the loop behind `goto label_67`.
#     The header's own exit now counts when the header is the guard.
#   * `ForEachRegionPass._try_recognize_for_of_with_inner_try` refused a `finally`, which is how the close
#     scaffold looks once a `break`/`return` copied it. It only needs to be the iterator close.
#
#     96/10789  `checkIfScreenWasChanged`
#     96/13412  `findInMenu`
# ----------------------------------------------------------------------------------------------------

def _render_6(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_break_out_of_a_guarded_body_stays_in_the_for_of():
    out = _render_6("for_of_break_in_guarded_try_96_10789.hasm", 10789)

    assert "goto" not in out
    assert "for (const r8 of r5) {" in out
    assert "r0 = r8;\n            break;" in out
    assert "finally" not in out and "while" not in out


def test_a_return_in_a_guarded_body_leaves_no_finally_close():
    out = _render_6("for_of_return_in_guarded_try_96_13412.hasm", 13412)

    assert "for (let r9 of r6) {" in out
    assert "finally" not in out and "GetIterator" not in out and ".return()" not in out


# ----------------------------------------------------------------------------------------------------
# for_of_in_a_loop_with_a_latch
#
# Two `for-of` loops in the arms of an `if`, inside a `for (; cond; ...)` loop whose body ends in code (96/10225).
#
# Each inner loop's `IteratorClose` handler covers only the block that ends the inner loop's body (the call and the
# jump back). `_scan_loop_body_protected_extent` took "a latch at the start of the range" to mean the try wraps the
# whole loop, so both `try`s went around the whole `if`, and the loops stayed `while (true)` over `GetIterator(..)`
# with a `finally { r9.return() }`. A plain jump-back block that is not the first of its body can start the range.
# The done test of each inner loop then lands on the outer loop's latch (`r1 = r7; r2 = r8;`), which is also what a
# `for-of` falls into, so `_enclosing_loop_it_ends` stops looking for trailing code at that latch.
# ----------------------------------------------------------------------------------------------------

def _render_7() -> str:
    hasm = (_DATA / "for_of_in_a_loop_with_a_latch_96_10225.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_both_inner_loops_are_for_of():
    out = _render_7()

    assert "for (const r13 of r1)" in out
    assert "for (const r14 of r1)" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out


def test_no_try_or_done_test_is_left():
    out = _render_7()

    assert "try" not in out
    assert "finally" not in out
    assert ".return()" not in out
    assert "continue loop_2" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_4(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_7(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_in_an_if_chain_in_a_for_of
#
# A `for-of` behind a chain of `if`s inside another `for-of` keeps its own close handler (98/8056 `filterCSSAndStyleProperties`).
#
# The inner loop's protected range starts inside it and ends with a `continue` trampoline block (a lone `JmpLong`) that
# lies in the outer loop's region, outside the `if` chain that holds the rest of the range. The descent into the chain
# wanted every protected block inside it, gave up, and wrapped BOTH handlers around the outer loop - `try { try {
# for ... } catch (e) { r19.return(); throw e } } catch (e) { r7.return(); throw e }` - which kept both
# `GetIterator` lines. A jump-only block no longer blocks the descent.
# ----------------------------------------------------------------------------------------------------

def _render_8() -> str:
    hasm = (_DATA / "for_of_in_an_if_chain_in_a_for_of_98_8056.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 8056, strict=False), verbose=False, raw=False)


def test_both_loops_are_plain_for_of_loops():
    out = _render_8()

    assert "for (const [r17, r16] of r11)" in out
    assert "for (const [r14, r13] of r18)" in out
    assert "GetIterator" not in out
    assert ".return()" not in out
    assert "try {" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_5(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_8(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_inline_close
#
# The iterator close Hermes copies onto a for-of's exits is dropped (F-167).
#
# `for (x of xs)` already closes the iterator on `break` and `return`, so
#
#     r2.return(); break;           r1.return(); return true;
#
# only repeat what the loop says. Left behind they also kept the `GetIterator` setup alive.
#
#     96/13887  `matchAgainstConfigs`  (break)
#     96/10836  `inlinePropsHasChanged`  (return)
# ----------------------------------------------------------------------------------------------------

def _render_9(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_close_before_a_break_is_dropped():
    out = _render_9("for_of_inline_close_break_96_13887.hasm", 13887)

    assert "for (const r10 of r5) {" in out
    assert ".return()" not in out and "GetIterator" not in out
    assert "if (r9 === 1) {\n                break;" in out


def test_a_close_before_a_return_is_dropped():
    out = _render_9("for_of_inline_close_return_96_10836.hasm", 10836)

    assert "for (const r7 of r2) {" in out
    assert ".return()" not in out and "GetIterator" not in out
    assert "if (r6 !== r5) {\n                return true;" in out


# ----------------------------------------------------------------------------------------------------
# for_of_param_iterable
#
# A `for (x of param)` whose iterable is a parameter is a for-of (F-191).
#
# Hermes primes a scratch register from the iterable right before `IteratorNext` (`r8 = r4`). With the iterable
# a parameter the copy folds into `r8 = param2`, which `_is_plain_register_copy` did not take for the priming `Mov`,
# so the header did not match, the loop stayed a `while` and printed the exit test BEFORE the statements that set
# what it reads:
#
#     while (!(r9 === undefined)) { r8 = r2.next(); r9 = r2; try { ... } catch { r2.return(); throw e } }
#
# (`r9` is unset on the first check: the loop never ran.)
#
# Two more things showed once the loop was recognized (98/5425 `matchAgainstConfigs`, whose body is a call and a
# chain of tests with two `continue` edges):
#
#   - the body's last block was a COPY of a latch (`loop.latches` held the original), its `goto` to the header
#     stayed: `RedundantJumpRegionPass` also clears a trailing jump to the header at the end of the body;
#   - the close on `break` reads the iterator through a scratch copy (`r8 = r2; r8.return(); break;`).
#
#     98/7122 `cloneSet`   98/5425 `matchAgainstConfigs`
# ----------------------------------------------------------------------------------------------------

def _render_10(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_parameter_iterable_is_a_for_of():
    out = _render_10("for_of_param_iterable_98_7122.hasm", 7122)

    assert "for (const r8 of r4) {" in out
    assert "while" not in out and "caughtException" not in out and ".next()" not in out and ".return()" not in out


def test_the_back_edge_copy_and_the_close_on_break_are_scaffolding():
    out = _render_10("for_of_param_iterable_98_5425.hasm", 5425)

    # the body reuses r8 for the call result (`r8 = _loop.call(0, r8)`): a `let`, a `const` cannot be assigned (F-192)
    assert "for (let r8 of r4) {" in out
    assert "goto" not in out
    assert ".return()" not in out
    assert "break;" in out


# ----------------------------------------------------------------------------------------------------
# for_of_return_through_a_reused_copy
#
# A `return` out of a `for-of` leaves no iterator copy when the copy's register is reused for the value (98/8004 `deepEqual`).
#
# Hermes closes the iterator before `return false` through the register that then holds the value (`r8 = r1;
# r8.return(); r8 = false; return r8;`). The copy was kept because the `return` names `r8`, and it kept
# `r1 = GetIterator(r0)` alive. A copy that is written again before anything reads it holds nothing and goes.
# ----------------------------------------------------------------------------------------------------

def _render_11() -> str:
    hasm = (_DATA / "for_of_return_through_a_reused_copy_98_8004.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_iterator_setup_is_gone_2():
    out = _render_11()

    assert "of r0)" in out
    assert "GetIterator" not in out
    assert "return false;" in out
    assert ".return()" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_6(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_11(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_with_its_done_test_in_the_body
#
# A `for-of` whose done test stayed in the loop body prints as a `for-of` (96/3625 `generateValues`).
#
# `for (const s of m.values()) for (const x of s) yield x;`: the inner loop has no exception handler and ends in the
# outer loop's latch, so its `IteratorNext` test is not the loop's condition but `if (rN === undefined) continue outer;`
# at the top of the body. The bare for-of recognition only knew the loop condition; it now also takes this body test
# (when the loop is the last thing of the outer body) and drops it, as `_drop_exit_test` does for the other variants.
# ----------------------------------------------------------------------------------------------------

def _render_12() -> str:
    hasm = (_DATA / "for_of_in_a_generator_loop_96_3625.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_inner_loop_is_a_for_of():
    out = _render_12()

    assert "for (const r4 of r6)" in out
    assert "yield r4;" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out
    assert "continue loop_2" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_7(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_12(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# for_of_without_scaffold
#
# A for-of whose iterator-close handler covers only the body, or none at all (96/5140 `anonymous`).
#
# `IteratorNext; Mov; JStrictEqual it undefined -> exit` heads the loop and the handler range (0x1c-0x24) starts at
# the `if` that is the body: the `if`'s test block was no longer a child of any sequence, so
# `RegionGraph.lowest_common_sequence` found no common sequence with the handler's block, the `try` was never built
# and the loop stayed `while (!(r5 === undefined)) { r4 = r2.next(); r5 = r2; ... }` (the test reads a register the
# body sets AFTER the test) with the close handler left as dead `r2.return(); throw caughtException;` behind it.
# Without any handler the loop was left the same way: `ForEachRegionPass` only recognized a loop inside a `try`.
# ----------------------------------------------------------------------------------------------------

def _render_13(name):
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 5140, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_handler_over_the_body_only_is_a_for_of():
    code = _render_13("for_of_inner_try_96_5140.hasm")

    assert "for (let r4 of r3)" in code
    assert "next()" not in code
    assert "caughtException" not in code


def test_for_of_without_a_handler_is_a_for_of():
    code = _render_13("for_of_no_handler_96_5140.hasm")

    assert "for (let r4 of r3)" in code
    assert "next()" not in code
    assert "undefined" not in code


# ----------------------------------------------------------------------------------------------------
# nested_for_of_in_a_for_of
#
# A `for-of` inside the body of another `for-of` prints as a `for-of` (96/10393 `dfs`).
#
# The inner loop's protected range (`IteratorClose` on a throw) lies inside the inner loop's body, but the outer
# loop's body holds the inner loop behind an `if`. `_find_loop_nested_home` stopped at the first loop it met, put the
# `try` around the whole `if`, and the inner loop stayed a `while (true)` over `GetIterator(..)` with the close printed
# as a `finally`. Two changes: the home search goes down to the deepest loop that holds every protected block, and the
# done test of the inner loop (`if (rN === undefined) continue outer;`, the exit jumps to the outer latch) is dropped
# when the loop is the last thing of the outer body: a `for-of` ends by itself.
# ----------------------------------------------------------------------------------------------------

def _render_14() -> str:
    hasm = (_DATA / "nested_for_of_in_a_for_of_96_10393.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_both_loops_are_for_of():
    out = _render_14()

    assert "for (let r9 of r2)" in out
    assert "for (const r11 of r7)" in out
    assert "GetIterator" not in out
    assert "while (true)" not in out


def test_no_close_or_done_test_is_left():
    out = _render_14()

    assert "finally" not in out
    assert ".return()" not in out
    assert "continue loop_1" not in out
    assert "=== undefined" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_8(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_14(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# yield_inside_a_for_of_that_closes_its_iterator
#
# `yield x` inside `for (... of ...)` folds although its return arm closes the iterators (96/3625 `generateValues`).
#
# The compiler lays the yield out as a lone `SaveGenerator` (the value was computed in the block before) and a return
# guard whose arm is `IteratorClose` + `Ret`. The guard was not recognised, so the suspend printed as `r4 = await yield;`
# (not valid JavaScript) and the yielded value was nowhere in the output.
# ----------------------------------------------------------------------------------------------------

def _render_15() -> str:
    hasm = (_DATA / "yield_inside_a_for_of_that_closes_its_iterator_96_3625.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_or_resume_flag_is_printed():
    out = _render_15()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out


def test_the_value_is_yielded():
    assert "            yield r4;\n" in _render_15()
