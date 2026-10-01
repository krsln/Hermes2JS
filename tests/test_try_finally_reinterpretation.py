"""
Tests for `_FinallyAttacher.maybe_reinterpret_as_finally` and the
`ForEachRegionPass` iterator-close recognition that depends on it.

A handler `catch (e) { B; throw e }` and a `finally { B }` compile to the
same handler table and handler block; only the try body differs (Hermes
inlines a copy of a `finally` body at every normal exit). Rewriting a real
catch-and-rethrow as `finally` runs B on the success path - it must only
happen with evidence that the source was a `finally`.
"""

from __future__ import annotations

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures"

# hermesc 250829098.0.14 (bytecode 98), compiled from:
#
#   function rethrowWithLog(x) {
#     try { console.log("try-body"); mayThrow(x); }
#     catch (e) { console.log("caught-and-logged"); throw e; }
#     console.log("after");
#   }
RETHROW_WITH_LOG = r"""
=> [Function #2 "rethrowWithLog" of 85 bytes]: 2 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x000001d1
  [Exception handlers: [start=0x0, end=0x25, target=0x3b] ]
  [Debug offsets: source_locs=0x38, scope_desc_data=0x226]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <GetGlobalObject>: <Reg8: 1>
==> 00000005: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 0000000b: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 00000010: <LoadConstString>: <Reg8: 0, string_id: 5>  # String: 'try-body' (String)
==> 00000014: <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
==> 00000019: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 10>  # String: 'mayThrow' (Identifier)
==> 0000001e: <LoadConstUndefined>: <Reg8: 0>
==> 00000020: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 3>
==> 00000025: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 0000002b: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 00000030: <LoadConstString>: <Reg8: 1, string_id: 0>  # String: 'after' (String)
==> 00000034: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000039: <Ret>: <Reg8: 0>
==> 0000003b: <Catch>: <Reg8: 0>
==> 0000003d: <GetGlobalObject>: <Reg8: 1>
==> 0000003f: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 9>  # String: 'console' (Identifier)
==> 00000045: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 7>  # String: 'log' (Identifier)
==> 0000004a: <LoadConstString>: <Reg8: 1, string_id: 1>  # String: 'caught-and-logged' (String)
==> 0000004e: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000053: <Throw>: <Reg8: 0>


"""


def render(hasm: str, index: int) -> str:
    context = Decompiler.build_context(hasm, index)
    out = Decompiler.render(context, verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def render_fixture(version: str, index: int, name: str) -> str:
    hasm = (FIXTURES / version / "sections" / f"function_{index}_{name}.hasm").read_text()

    return render(hasm, index)


def test_catch_that_logs_and_rethrows_is_not_rewritten_as_finally():
    out = render(RETHROW_WITH_LOG, 2)

    assert "finally" not in out
    assert "catch" in out

    lines = [line.strip() for line in out.split("\n")]
    catch_at = next(i for i, line in enumerate(lines) if line.startswith("} catch"))

    # The logging belongs to the catch, not to the try body.
    assert any("caught-and-logged" in line for line in lines[catch_at:])
    assert not any("caught-and-logged" in line for line in lines[:catch_at])

    # KNOWN LIMITATION, deliberately not asserted either way: the code
    # after the try statement ("after") currently lands INSIDE the try
    # body, because the last protected block also holds unprotected
    # instructions and only LEADING unprotected content is split off.


def test_real_try_finally_with_inlined_copy_still_becomes_finally():
    out = render_fixture("98", 9466, "tryFinallyNormalCompletionTest")

    assert "} finally {" in out
    assert "catch" not in out
    # The inlined normal-exit copy was stripped: the finally body appears once.
    assert out.count("finally-block") == 1


def test_try_body_with_no_normal_exit_still_becomes_finally():
    # try always throws, catch always throws: no copy can exist, and
    # `catch { B; throw e }` is equivalent to `finally { B }` here.
    out = render_fixture("96", 15079, "tryCatchRethrowDifferentTest")

    assert "} finally {" in out


def test_for_of_iterator_close_catch_is_unwrapped_into_plain_for_of():
    # The iterator close reaches the structurer as a catch-and-rethrow;
    # ForEachRegionPass recognises that shape and drops the scaffolding.
    out = render_fixture("96", 15092, "forOfTest")

    assert "for (const" in out
    assert "try" not in out
    assert ".return()" not in out


# ---------------------------------------------------------------------------
# Inlined copy placed AFTER the try (a loop's `break` and its normal end
# converge on one block, so Hermes emits the finally body once, there).
# ---------------------------------------------------------------------------


def test_finally_copy_after_the_try_is_recovered_as_a_real_finally():
    # try { for (...) { if (items[i] === 0) break; ... } } finally { F }
    out = render_fixture("98", 9472, "tryFinallyLoopBreakTest")

    assert "} finally {" in out
    assert "catch" not in out

    # F runs once, in the finally clause - the copy after the try is gone -
    # and the code that followed it is still there, after the try.
    assert out.count("finally-block") == 1
    assert out.index("finally-block") < out.index("/end")


# hermesc 250829098.0.14 (bytecode 98), compiled from:
#
#   function sharedTail(x, y) {
#     if (y) {
#       try { console.log("a"); mayThrow(x); }
#       catch (e) { console.log("dup"); throw e; }
#     }
#     console.log("dup");
#     console.log("rest");
#   }
#
# The code after the try starts with the same statement as the catch body,
# but that block is also reachable when `y` is false, i.e. without passing
# through the try: its first statement is not a finally copy.
SHARED_TAIL = r"""
=> [Function #2 "sharedTail" of 115 bytes]: 3 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x000001f2
  [Exception handlers: [start=0x6, end=0x2b, target=0x59] ]
  [Debug offsets: source_locs=0x44, scope_desc_data=0x265]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 0, UInt8: 2>
==> 00000003: <JmpFalse>: <Addr8: 40, Reg8: 0>  # Address: 0000002b
==> 00000006: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000009: <GetGlobalObject>: <Reg8: 0>
==> 0000000b: <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000011: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000016: <LoadConstString>: <Reg8: 1, string_id: 2>  # String: 'a' (String)
==> 0000001a: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 4, Reg8: 1>
==> 0000001f: <GetByIdShort>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 9>  # String: 'mayThrow' (Identifier)
==> 00000024: <LoadConstUndefined>: <Reg8: 0>
==> 00000026: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 0, Reg8: 2>
==> 0000002b: <GetGlobalObject>: <Reg8: 0>
==> 0000002d: <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000033: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000038: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000003c: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000041: <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000047: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 0000004c: <LoadConstString>: <Reg8: 0, string_id: 4>  # String: 'rest' (String)
==> 00000050: <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
==> 00000055: <LoadConstUndefined>: <Reg8: 0>
==> 00000057: <Ret>: <Reg8: 0>
==> 00000059: <Catch>: <Reg8: 0>
==> 0000005b: <GetGlobalObject>: <Reg8: 1>
==> 0000005d: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000063: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000068: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000006c: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000071: <Throw>: <Reg8: 0>


"""

# ... and:
#
#   function returnInside(x) {
#     try { if (x) { return 1; } console.log("a"); mayThrow(x); }
#     catch (e) { console.log("dup"); throw e; }
#     console.log("dup");
#     console.log("rest");
#   }
#
# A `return` in the try body carries its own inlined copy inside the try;
# the trailing-copy rule does not model that and must decline.
RETURN_INSIDE = r"""
=> [Function #3 "returnInside" of 113 bytes]: 2 params, frame size=14, strict=0, exc handler=1, debug info=1  @ offset 0x00000265
  [Exception handlers: [start=0x0, end=0x28, target=0x57] ]
  [Debug offsets: source_locs=0x7f, scope_desc_data=0x2d6]

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <JmpTrue>: <Addr8: 79, Reg8: 3>  # Address: 00000052
==> 00000006: <GetGlobalObject>: <Reg8: 1>
==> 00000008: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 2, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000013: <LoadConstString>: <Reg8: 0, string_id: 2>  # String: 'a' (String)
==> 00000017: <Call2>: <Reg8: 0, Reg8: 2, Reg8: 4, Reg8: 0>
==> 0000001c: <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 9>  # String: 'mayThrow' (Identifier)
==> 00000021: <LoadConstUndefined>: <Reg8: 0>
==> 00000023: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 3>
==> 00000028: <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 0000002e: <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000033: <LoadConstString>: <Reg8: 2, string_id: 3>  # String: 'dup' (String)
==> 00000037: <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
==> 0000003c: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000042: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000047: <LoadConstString>: <Reg8: 1, string_id: 4>  # String: 'rest' (String)
==> 0000004b: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 00000050: <Ret>: <Reg8: 0>
==> 00000052: <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
==> 00000055: <Ret>: <Reg8: 0>
==> 00000057: <Catch>: <Reg8: 0>
==> 00000059: <GetGlobalObject>: <Reg8: 1>
==> 0000005b: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 7>  # String: 'console' (Identifier)
==> 00000061: <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 5>  # String: 'log' (Identifier)
==> 00000066: <LoadConstString>: <Reg8: 1, string_id: 3>  # String: 'dup' (String)
==> 0000006a: <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
==> 0000006f: <Throw>: <Reg8: 0>


"""


def test_trailing_copy_is_not_stripped_when_the_block_is_reachable_from_outside_the_try():
    out = render(SHARED_TAIL, 2)

    assert "finally" not in out
    assert "} catch" in out
    # Both statements survive: the one in the catch and the one after.
    assert out.count('"dup"') == 2


def test_trailing_copy_rule_declines_a_try_body_containing_a_return():
    out = render(RETURN_INSIDE, 3)

    assert "finally" not in out
    assert "} catch" in out
