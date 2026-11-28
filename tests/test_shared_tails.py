"""Shared tails and shared returns/throws: duplication, relocation, labels, jumpers.

Merged from: test_continue_stubs_behind_a_shared_tail, test_if_tail_merge_jumped_throw, test_if_tail_merge_tested_return, test_jump_only_shared_return, test_jump_to_shared_return_after_try, test_large_shared_tail, test_long_shared_return, test_long_tail_with_fall_in, test_own_value_return, test_return_and_update_reorder, test_second_jumper_copy, test_second_jumper_exit, test_shared_constant_return, test_shared_return_exit, test_shared_return_labels, test_shared_return_try_exit, test_shared_return_widened, test_shared_tail_conditions, test_shared_tail_each_way, test_shared_tail_foreign_leaf, test_shared_tail_inside_try, test_shared_tail_jumpers, test_shared_tail_other_way, test_shared_tail_region_copy_values, test_shared_tail_that_only_returns_gets_a_copy_for_the_jumpers, test_shared_tail_with_try, test_shared_throw_exits_keep_the_original_for_the_earlier_jumper, test_shared_throw_size, test_tail_copy_register_leak, test_terminal_tail_copy_on_the_plain_layout, test_terminal_tail_relocated_in_function_with_handlers, test_terminal_tail_relocation.
"""

import re
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.cfg_passes import SharedTailDuplicationCfgPass


# ----------------------------------------------------------------------------------------------------
# continue_stubs_behind_a_shared_tail
#
# Stores that end in `continue`, laid out behind a tail two tests fall into (98/8045 `parseSingleTransitionShorthand`).
#
# `if (isTimeUnit(t)) { if (duration === undefined) <store>; else if (delay === undefined) <store> }` followed by the
# `timingFunction` code: the compiler put the two stores AFTER that code, so the second test jumped forward past it
# and the structurer left `goto label_245`. The last retry moves such a stub behind its test and reads the tail as
# the code after the `if`, which every other path of the arm also reaches.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "continue_stubs_behind_a_shared_tail_98_8045.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_no_goto_is_left():
    assert "goto" not in _render()


def test_the_timing_function_code_follows_the_time_unit_branch():
    out = _render()
    time_unit = out.split("if (r12) {")[1]
    arm, after = time_unit.split("r12 = r0.transitionTimingFunction;")[0], time_unit.split("r12 = r0.transitionTimingFunction;")[1]

    # the duration and delay stores sit in the arm; the timing code comes once, behind it (both paths reach it)
    assert "r0.transitionDuration = r11;" in arm and "r0.transitionDelay = r11;" in arm
    assert out.count("r12 = r0.transitionTimingFunction;") == 1
    assert "r0.transitionTimingFunction = r11;" in after


# ----------------------------------------------------------------------------------------------------
# if_tail_merge_jumped_throw
#
# `IfTailMergeRegionPass` leaves a `throw` that something jumps to where it is (F-209, 98/2798 `mark`).
#
# An arm's last block that other code JUMPS to is not the arm's end just because it is the last item: the
# pass hoisted its trailing `throw r3` into one `throw` after the `if`, so the jumper printed
# `r3 = new TypeError(...)` and fell on into the code behind it. Twenty-one files (96 and 98) printed a
# `throw` as an assignment this way (`BottomTabBar`, `commitRoot`, `createChild`, ...).
# ----------------------------------------------------------------------------------------------------

def _code() -> str:
    hasm = (_DATA / "if_tail_merge_jumped_throw_98_2798.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2798, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_each_error_is_thrown_where_it_is_made():
    code = _code()

    assert code.count("throw new TypeError(") == 4
    assert "r3 = new TypeError" not in code


def test_no_throw_is_left_for_the_end_of_the_function():
    assert "throw r3;" not in _code()


# ----------------------------------------------------------------------------------------------------
# if_tail_merge_tested_return
#
# `IfTailMergeRegionPass` keeps a `return` that a test (still unresolved, ending its sequence) jumps to (F-210,
# 96/13834 `getInitialURL`).
#
# `if (r3 === "web") { ...; if (r1) goto HREF }` runs on into the native-platform code when `r1` is false; the
# `HREF` block (`r0 = window.location; return r0.href`) was merged into the one `return r0` after the `if`, so the
# test printed `if (r1) { r0 = ...href }` and the true case ran on into the native code instead of returning.
# ----------------------------------------------------------------------------------------------------

def _code_2() -> str:
    hasm = (_DATA / "if_tail_merge_tested_return_96_13834.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13834, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_href_case_returns_where_the_test_is():
    code = _code_2()

    assert "goto" not in code
    assert "if (r1) {\n                r0 = window.location;\n                return r0.href;\n            }" in code


# ----------------------------------------------------------------------------------------------------
# jump_only_shared_return
#
# A constant `return` reached only by jumps (`a === 1 || a === 2 ... return true`,
# 98/8021) is copied per jumper, the last one keeping the original, so no
# `goto label_N` is left. Nested tail merges of the resulting `return r0` must
# still resolve `r0` along every arm (98/2190: all-`true` arms once collapsed the
# whole function to `return true`).
# ----------------------------------------------------------------------------------------------------

_IS_TRANSITION_PROP = """
=> [Function #8021 "isTransitionProp" of 59 bytes]: 2 params, frame size=3, strict=1, exc handler=0, debug info=0  @ offset 0x001e7794

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <LoadConstString>: <Reg8: 1, string_id: 14389>  # String: 'transitionProperty' (Identifier)
==> 00000007: <JStrictEqual>: <Addr8: 48, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000000b: <LoadConstString>: <Reg8: 1, string_id: 14259>  # String: 'transitionDuration' (Identifier)
==> 0000000f: <JStrictEqual>: <Addr8: 40, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000013: <LoadConstString>: <Reg8: 1, string_id: 13592>  # String: 'transitionTimingFunction' (Identifier)
==> 00000017: <JStrictEqual>: <Addr8: 32, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000001b: <LoadConstString>: <Reg8: 1, string_id: 14254>  # String: 'transitionDelay' (Identifier)
==> 0000001f: <JStrictEqual>: <Addr8: 24, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000023: <LoadConstString>: <Reg8: 1, string_id: 14249>  # String: 'transitionBehavior' (Identifier)
==> 00000027: <JStrictEqual>: <Addr8: 16, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 0000002b: <LoadConstString>: <Reg8: 1, string_id: 6760>  # String: 'transition' (Identifier)
==> 0000002f: <JStrictEqual>: <Addr8: 8, Reg8: 1, Reg8: 2>  # Address: 00000037
==> 00000033: <LoadConstFalse>: <Reg8: 0>
==> 00000035: <Ret>: <Reg8: 0>
==> 00000037: <LoadConstTrue>: <Reg8: 0>
==> 00000039: <Ret>: <Reg8: 0>


"""

_IS_VALID_POSITION = """
=> [Function #2190 "isValidPosition" of 53 bytes]: 2 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x00161b72

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 2, UInt8: 1>
==> 00000003: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 135>  # String: 'endsWith' (Identifier)
==> 00000008: <LoadConstString>: <Reg8: 1, string_id: 307>  # String: 'px' (String)
==> 0000000c: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
==> 00000011: <JmpTrue>: <Addr8: 32, Reg8: 1>  # Address: 00000031
==> 00000014: <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 0, string_id: 135>  # String: 'endsWith' (Identifier)
==> 00000019: <LoadConstString>: <Reg8: 1, string_id: 856>  # String: '%' (String)
==> 0000001d: <Call2>: <Reg8: 1, Reg8: 3, Reg8: 2, Reg8: 1>
==> 00000022: <JmpTrue>: <Addr8: 15, Reg8: 1>  # Address: 00000031
==> 00000025: <LoadConstString>: <Reg8: 1, string_id: 810>  # String: '0' (String)
==> 00000029: <JStrictEqual>: <Addr8: 8, Reg8: 2, Reg8: 1>  # Address: 00000031
==> 0000002d: <LoadConstFalse>: <Reg8: 0>
==> 0000002f: <Ret>: <Reg8: 0>
==> 00000031: <LoadConstTrue>: <Reg8: 0>
==> 00000033: <Ret>: <Reg8: 0>


"""


def _js(hasm, index):
    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_jump_only_constant_return_has_no_goto():
    js = _js(_IS_TRANSITION_PROP, 8021)

    assert "goto" not in js
    # six labels of one body are one condition (a `switch` needs two bodies);
    # every label is tested and the false path is kept
    assert js.count(" === param1") == 6
    assert "r0 = true;" in js
    assert "r0 = false;" in js
    assert js.strip().endswith("return r0;\n}")


def test_nested_merged_returns_keep_the_false_path():
    js = _js(_IS_VALID_POSITION, 2190)

    assert "r0 = false;" in js
    assert js.strip().endswith("return r0;\n}")


# ----------------------------------------------------------------------------------------------------
# jump_to_shared_return_after_try
#
# A plain `jmp` to a shared `return` takes the return along (F-158).
#
# The exit of a `try` body is a `jmp` over the catch to the closing `return`. The private copy was a separate
# block that nothing placed after the `try`, so a `goto` stayed.
#
#     96/6731  `ensureNativeModulesAreInstalled`
# ----------------------------------------------------------------------------------------------------

def test_the_exit_of_a_try_body_returns_in_place():
    hasm = (_DATA / "jump_to_shared_return_after_try_96_6731.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6731, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.index("} catch") < out.index("return undefined;")


# ----------------------------------------------------------------------------------------------------
# large_shared_tail
#
# A shared tail too big for the small copy limit is copied on the last rung (F-217, 98/6570).
#
#     if (!a) goto T;  ...  r1 = false; if (c) goto J;  T: <several tests>;  J: return r1
#
# `T` is the first test's target and the fall-through of the last test, whose other exit skips it: no `if` owns it.
# `SharedTailDuplicationCfgPass` gives the skipping test its own copy, but `T` is longer than the usual limit (12
# instructions / 4 blocks); the last retry rung raises it, so the earlier rungs keep the shapes they already built.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "large_shared_tail_98_6570.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6570, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_long_shared_tail_gets_a_private_copy():
    code = _render_2()

    assert "goto" not in code
    assert code.count("param1.preventDefault()") == 1


def test_the_large_limit_is_the_last_rung_only():
    small = SharedTailDuplicationCfgPass(None, regions=True, per_predecessor=True)
    large = SharedTailDuplicationCfgPass(None, regions=True, per_predecessor=True, large=True)

    assert small.max_instructions == 12 and small.max_region_blocks == 4
    assert large.max_instructions > 12 and large.max_region_blocks > 4


# ----------------------------------------------------------------------------------------------------
# long_shared_return
#
# On the last rung of the retry ladder a longer shared `return` is copied for the jumps that reach it (F-189).
#
#     if (!a) goto T; ...; if (b) goto T; throw ...; T: Object.assign(x, { [k]: v }); return r0
#
# `T` is seven instructions, one over the limit of the rungs before, and only jumps reach it: the second test kept
# `goto label_195`. The last rung (it only runs for functions every earlier one left with a `goto`) copies a tail
# up to nine instructions when nothing falls into it.
#
# Not for a tail something falls into (98/2844 `rawToPerformanceEntry`: `r4.decodedBodySize = r5; return new r6(r4)`
# after `r5 = 0` on one path and `r5 = v` on the other; the copy printed `= 0` on both).
#
#     98/10767 `anonymous` (react-navigation)   98/2844 `rawToPerformanceEntry`
# ----------------------------------------------------------------------------------------------------

def _render_3(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_long_tail_the_guard_jumps_to_follows_the_if():
    out = _render_3("long_shared_return_98_10767.hasm", 10767)

    assert "goto" not in out
    assert out.count("r0 = Object.assign(param1, r0);") == 1
    assert "if (!r0) {" in out


def test_a_tail_something_falls_into_keeps_its_own_values():
    out = _render_3("long_shared_return_98_2844.hasm", 2844)

    assert "r4.decodedBodySize = 0;" not in out


# ----------------------------------------------------------------------------------------------------
# long_tail_with_fall_in
#
# A tail of up to nine instructions that a fall-through enters as well is copied when it reads the same on every
# path (F-218, 98/2930 `resolve`).
#
#     if (!a) goto T;  if (typeof a !== "object" ...) goto T;  ...  if (typeof then === "function") goto BIND;
#     T: _y = 1; _z = v; finale(p); return           (eight instructions: two jumps and the fall-through enter it)
#
# The last rung copies a tail longer than six instructions only when jumps alone reach it: with a fall-through the
# paths may hold different values for what the tail reads (98/2844). `_reads_the_same_on_every_path` says whether they
# do; here nothing the tail reads is written differently, so the fall-through counts too. The `goto` for the
# `typeof then` test is gone and the `_y = 1` tail is the `else` of it.
# ----------------------------------------------------------------------------------------------------

def test_the_fulfil_tail_is_the_else_of_the_typeof_test():
    hasm = (_DATA / "long_tail_with_fall_in_98_2930.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2930, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert '} else if (typeof r7 === "function") {' in code
    assert "} else {\n                param1._y = 1;\n                param1._z = param2;" in code


# ----------------------------------------------------------------------------------------------------
# own_value_return
#
# A closing `return` the paths disagree on is copied for the jumpers that set the value themselves (F-162).
#
#     r0 = Number(v); jmp RET      RET: return r0      (other paths reach RET with other values of r0)
#
# The copy of that jumper returns ITS value (`r0 = Number(v); return r0`) whatever the others hold; the original
# `return` stays for them. Used only by the last retry level.
#
#     96/7556  `parseValue`: three tests of the `parseNumbers` arm jump onto the code the first test skips to.
#     96/9896  `getReduceMotionFromConfig`: `!p || p === System` with the loads in the middle block.
# ----------------------------------------------------------------------------------------------------

def _render_4(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_number_that_parses_returns_before_the_boolean_tests():
    out = _render_4("own_value_return_96_7556.hasm", 7556)

    assert "goto" not in out
    assert out.index("r0 = Number.call(undefined, param1);") < out.index("param2.parseBooleans")
    assert out.count("return r0;") == 2


def test_the_loads_of_an_or_chain_stay_in_front_of_its_second_test():
    out = _render_4("own_value_return_96_9896.hasm", 9896)

    assert "goto" not in out
    assert "return param1 === r0.Always;" in out
    assert out.rstrip().endswith("return r1.value;\n}")


# ----------------------------------------------------------------------------------------------------
# return_and_update_reorder
#
# `decode` (96/7575): a `Inc r2, r2` whose result a later `Mov r7, r2` reads, and a
# `return r0` that `Mov r0, r9` (inside the loop) and `LoadParam r0` both reach.
#
# * The update was pulled into the `for` header, i.e. moved after the `Mov` that
#   stores the incremented value (`r7 = r2` then stored the OLD counter).
# * `ReturnValueResolutionPass` walked back from `return r0`, never saw the path
#   through the handler (no predecessor edge), found only `Mov r0, r9` and printed
#   `return r9`, skipping the zero-iteration path where `r0` is the parameter.
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


def _render_5() -> str:
    context = Decompiler.build_context(_DECODE, 7575, strict=False)

    return Decompiler.render(context, verbose=False, raw=False)


def test_update_is_not_moved_past_a_reader_of_the_incremented_value():
    js = _render_5()

    # The increment stays ahead of the statement that stores it.
    assert js.index("r2 = r2 + 1;") < js.index("r7 = r2;")


def test_return_names_a_register_some_paths_never_rewrote():
    js = _render_5()

    assert "return r9;" not in js
    assert "return r0;" in js
    assert "r0 = r9;" in js


# ----------------------------------------------------------------------------------------------------
# second_jumper_copy
#
# Two tests jumping to one short tail: the later one gets its own copy, on the last rung (F-194).
#
#     if (kind !== 1) goto T; r4 = env[1]; if (r4 === undefined) goto T; ...; T: x; END:
#
# `A || B` would be the natural reading, but `B` reads `r4`, set by a statement of the else arm in front of it, so
# the test cannot move up into the condition (F-185 does that only when nothing prints in front of it) and the tail
# is not a lone `return` (`SharedReturnDuplicationCfgPass`). `_copy_for_the_second_jumper` gives the later test a copy
# of the tail (up to six instructions, only jumps reach it, it runs on into `END`) and leaves the original to the
# first one. Only on the last rung, `per_predecessor`: on a function that structures without it the copy would break
# an `||` chain apart.
#
#     98/13588 `get` (reanimated mutables)   98/5905 `getNavigationConfig`
# ----------------------------------------------------------------------------------------------------

def _render_6(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_test_that_jumps_to_the_tail_has_its_own_copy():
    out = _render_6("second_jumper_copy_98_13588.hasm", 13588)

    assert "goto" not in out
    # F-203 folds the load into the test, so the tail is no longer copied: one `||` condition
    assert out.count("r3 = r4.getSync();") == 1
    assert "if (r3 !== 1 || r2[1] === undefined) {" in out


def test_a_navigation_config_with_two_tests_to_one_tail_has_no_goto():
    out = _render_6("second_jumper_copy_98_5905.hasm", 5905)

    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# second_jumper_exit
#
# Two tests that jump to one short tail ending in `return`/`throw`: the later one gets its own copy (F-196).
#
#     for (x of xs) { if (A) goto B; if (C) goto B; }   return;   B: position = "absolute"; return
#
# F-194 copied a tail that runs on into a join. The break path of a for-of that sets something and leaves ends in
# its own `return`: the loop's natural exit is a different, bare `return` block, the break path sits right behind
# the loop and the structurers took IT for the loop's exit, so the natural exit printed the `position` line too
# (98/8693 `maybeModifyStyleForKeyframe`: a list without `originX`/`originY` got `position = "absolute"`), and a
# `goto` stayed. The tail (up to six instructions, exactly two forward conditional ways in, nothing falls into it)
# now gets a copy ending in the same `return`/`throw` for the later test, on the last rung only.
#
#     98/8693 `maybeModifyStyleForKeyframe`   98/11911 `transformOrigin` (`r6 < 1 || r7.length > 3` -> `throw`)
# ----------------------------------------------------------------------------------------------------

def _render_7(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_natural_exit_of_the_loop_does_not_set_the_position():
    out = _render_7("second_jumper_exit_98_8693.hasm", 8693)

    assert "goto" not in out
    # only the break paths set it, each leaves the function right away; nothing behind the loop does
    # (F-216: both tests are one `||` now, so the one break path is written once)
    assert out.count('if (r7 || "originY" in r6) {\n                param1.style.position = "absolute";\n                return undefined;\n            }') == 1
    assert out.count('param1.style.position = "absolute";') == 1


def test_a_throw_tail_two_tests_jump_to_is_copied():
    out = _render_7("second_jumper_exit_98_11911.hasm", 11911)

    assert "goto" not in out
    assert out.count("throw new Error(r19);") >= 3


# ----------------------------------------------------------------------------------------------------
# shared_constant_return
#
# A shared `r0 = false; return r0` block (the `typeof a === ... || x === null`
# guard shape, 98/2336 and 98/5366) is copied per jumper like a bare `return`,
# so no `goto label_N` is left behind. When the arms then end in the same
# `return rN` with different values (98/5366, 98/4378), the merged return stays
# `return rN` and every arm prints its own `rN = ...`.
# ----------------------------------------------------------------------------------------------------

_IS_IGNORED = """
=> [Function #2336 "isIgnored" of 40 bytes]: 2 params, frame size=13, strict=1, exc handler=0, debug info=0  @ offset 0x001655dd

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 3, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 14, Reg8: 3, UInt16: 253>  # Address: 00000011
==> 0000000b: <LoadConstNull>: <Reg8: 0>
==> 0000000d: <JNotEqual>: <Addr8: 8, Reg8: 3, Reg8: 0>  # Address: 00000015
==> 00000011: <LoadConstFalse>: <Reg8: 0>
==> 00000013: <Ret>: <Reg8: 0>
==> 00000015: <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
==> 00000018: <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
==> 0000001c: <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 0, string_id: 11>  # String: 'has' (Identifier)
==> 00000021: <Call2>: <Reg8: 1, Reg8: 1, Reg8: 2, Reg8: 3>
==> 00000026: <Ret>: <Reg8: 1>


"""

_IS_PLAIN_OBJECT = """
=> [Function #5366 "isPlainObject" of 57 bytes]: 2 params, frame size=14, strict=1, exc handler=0, debug info=0  @ offset 0x001b1899

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 4, UInt8: 1>
==> 00000003: <JmpTypeOfIs>: <Addr32: 14, Reg8: 4, UInt16: 253>  # Address: 00000011
==> 0000000b: <LoadConstNull>: <Reg8: 0>
==> 0000000d: <JStrictNotEqual>: <Addr8: 8, Reg8: 4, Reg8: 0>  # Address: 00000015
==> 00000011: <LoadConstFalse>: <Reg8: 0>
==> 00000013: <Ret>: <Reg8: 0>
==> 00000015: <GetGlobalObject>: <Reg8: 1>
==> 00000017: <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 23>  # String: 'Object' (Identifier)
==> 0000001d: <GetById>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 6472>  # String: 'getPrototypeOf' (Identifier)
==> 00000023: <Call2>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 4>
==> 00000028: <TryGetById>: <Reg8: 1, Reg8: 1, UInt8: 0, string_id: 23>  # String: 'Object' (Identifier)
==> 0000002e: <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 2, string_id: 212>  # String: 'prototype' (Identifier)
==> 00000033: <StrictEq>: <Reg8: 0, Reg8: 2, Reg8: 1>
==> 00000037: <Ret>: <Reg8: 0>


"""

_ARE_INPUTS_EQUAL = """
=> [Function #4378 "areInputsEqual" of 113 bytes]: 3 params, frame size=22, strict=1, exc handler=0, debug info=0  @ offset 0x001a1d77

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 10, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 9, UInt8: 1>
==> 00000006: <LoadParam>: <Reg8: 8, UInt8: 2>
==> 00000009: <GetByIdShort>: <Reg8: 11, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000000e: <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000013: <JStrictNotEqual>: <Addr8: 90, Reg8: 11, Reg8: 7>  # Address: 0000006d
==> 00000017: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 0000001c: <LoadConstZero>: <Reg8: 0>
==> 0000001e: <Less>: <Reg8: 3, Reg8: 0, Reg8: 7>
==> 00000022: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 00000025: <LoadConstTrue>: <Reg8: 4>
==> 00000027: <LoadConstUndefined>: <Reg8: 5>
==> 00000029: <LoadConstFalse>: <Reg8: 6>
==> 0000002b: <JmpFalse>: <Addr8: 64, Reg8: 3>  # Address: 0000006b
==> 0000002e: <GetByVal>: <Reg8: 12, Reg8: 9, Reg8: 0>
==> 00000032: <GetByVal>: <Reg8: 11, Reg8: 8, Reg8: 0>
==> 00000036: <Mov>: <Reg8: 1, Reg8: 0>
==> 00000039: <LoadConstTrue>: <Reg8: 3>
==> 0000003b: <JStrictEqual>: <Addr8: 30, Reg8: 12, Reg8: 11>  # Address: 00000059
==> 0000003f: <LoadFromEnvironment>: <Reg8: 7, Reg8: 10, UInt8: 0>
==> 00000043: <Call2>: <Reg8: 12, Reg8: 7, Reg8: 5, Reg8: 12>
==> 00000048: <LoadConstFalse>: <Reg8: 3>
==> 0000004a: <JmpFalse>: <Addr8: 15, Reg8: 12>  # Address: 00000059
==> 0000004d: <Call2>: <Reg8: 7, Reg8: 7, Reg8: 5, Reg8: 11>
==> 00000052: <LoadConstFalse>: <Reg8: 3>
==> 00000054: <JmpFalse>: <Addr8: 5, Reg8: 7>  # Address: 00000059
==> 00000057: <LoadConstTrue>: <Reg8: 3>
==> 00000059: <JmpTrue>: <Addr8: 5, Reg8: 3>  # Address: 0000005e
==> 0000005c: <Ret>: <Reg8: 6>
==> 0000005e: <AddN>: <Reg8: 0, Reg8: 1, Reg8: 2>
==> 00000062: <GetByIdShort>: <Reg8: 7, Reg8: 9, UInt8: 0, string_id: 177>  # String: 'length' (Identifier)
==> 00000067: <JLess>: <Addr8: -57, Reg8: 0, Reg8: 7>  # Address: 0000002e
==> 0000006b: <Ret>: <Reg8: 4>
==> 0000006d: <LoadConstFalse>: <Reg8: 4>
==> 0000006f: <Ret>: <Reg8: 4>


"""




def test_constant_return_shared_by_a_guard_chain_has_no_goto():
    js = _js(_IS_IGNORED, 2336)

    assert "goto" not in js
    # One `return false` for the whole guard (`!(a && b)` folded to one test),
    # not one per jumper: both exits are the same constant.
    assert js.count("return false;") == 1
    assert "return r1;" in js


def test_arms_returning_different_values_keep_the_register_return():
    js = _js(_IS_PLAIN_OBJECT, 5366)

    assert "goto" not in js
    assert js.count("r0 = false;") == 1
    assert "r0 = r2 === Object.prototype;" in js
    assert re.search(r"return r0;\n}$", js.strip())


def test_constant_defined_before_the_if_is_printed_when_return_is_merged():
    js = _js(_ARE_INPUTS_EQUAL, 4378)

    assert "r4 = false;" in js
    assert "r4 = true;" in js
    assert js.strip().endswith("return r4;\n}")


# ----------------------------------------------------------------------------------------------------
# shared_return_exit
#
# One `return` block shared by two early exits in different `if` arms, with an
# `||`-style join behind them (`maybeSwapComponents`, 96/9150):
#
#     if (!(p[0] in A)) return p;            // jumps to the shared `return p`
#     if (p[1] !== undefined && !(p[1] in B)) return p;   // falls into it
#     ...swap...
#
# The block belonged to the first branch only; the second test lost its exit
# and the swap code ended up under `r5 === undefined` alone.
# `SharedReturnDuplicationCfgPass` gives each jumper its own copy and
# `_DominanceIfBuilder` treats the shared `||` target as the join.
# ----------------------------------------------------------------------------------------------------

_HASM = """
=> [Function #9150 "maybeSwapComponents" of 107 bytes]: 2 params, frame size=16, strict=1, exc handler=0, debug info=0  @ offset 0x001d6a13

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 1>
==> 00000003: <LoadConstZero>: <Reg8: 4>
==> 00000005: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 4>
==> 00000009: <GetEnvironment>: <Reg8: 0, UInt8: 0>
==> 0000000c: <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
==> 00000010: <IsIn>: <Reg8: 2, Reg8: 3, Reg8: 2>
==> 00000014: <JmpFalse>: <Addr8: 31, Reg8: 2>  # Address: 00000033
==> 00000017: <LoadConstUInt8>: <Reg8: 2, UInt8: 1>
==> 0000001a: <GetByVal>: <Reg8: 5, Reg8: 1, Reg8: 2>
==> 0000001e: <LoadConstUndefined>: <Reg8: 3>
==> 00000020: <JStrictEqual>: <Addr8: 21, Reg8: 5, Reg8: 3>  # Address: 00000035
==> 00000024: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 2>
==> 00000028: <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 1>
==> 0000002c: <IsIn>: <Reg8: 0, Reg8: 3, Reg8: 0>
==> 00000030: <JmpTrue>: <Addr8: 5, Reg8: 0>  # Address: 00000035
==> 00000033: <Ret>: <Reg8: 1>
==> 00000035: <NewArray>: <Reg8: 0, UInt16: 0>
==> 00000039: <Mov>: <Reg8: 8, Reg8: 0>
==> 0000003c: <Mov>: <Reg8: 7, Reg8: 1>
==> 0000003f: <LoadConstZero>: <Reg8: 6>
==> 00000041: <CallBuiltin>: <Reg8: 1, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
==> 00000045: <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 2>
==> 00000049: <NewArray>: <Reg8: 1, UInt16: 2>
==> 0000004d: <PutOwnByIndex>: <Reg8: 1, Reg8: 3, UInt8: 0>
==> 00000051: <GetByVal>: <Reg8: 3, Reg8: 0, Reg8: 4>
==> 00000055: <PutOwnByIndex>: <Reg8: 1, Reg8: 3, UInt8: 1>
==> 00000059: <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 4>
==> 0000005d: <PutByVal>: <Reg8: 0, Reg8: 4, Reg8: 3>
==> 00000061: <GetByVal>: <Reg8: 1, Reg8: 1, Reg8: 2>
==> 00000065: <PutByVal>: <Reg8: 0, Reg8: 2, Reg8: 1>
==> 00000069: <Ret>: <Reg8: 0>
"""


def test_the_swap_runs_after_both_checks_and_both_exits_stay():
    out = Decompiler.render(Decompiler.build_context(_HASM, 9150), verbose=False)

    assert "goto" not in out, out
    # Both early exits return the parameter; every other path swaps. The two
    # checks are one test (`a in X && (b === undefined || b in Y)`) with the swap
    # under it and the single `return param1;` as its `else`.
    assert out.count("return param1;") == 1, out
    assert re.search(
        r"if \(param1\[r4\] in r0\[0\] && \(param1\[1\] === undefined \|\| param1\[1\] in r0\[1\]\)\) \{.*?"
        r"\} else \{\s*return param1;",
        out, re.S,
    ), out


# ----------------------------------------------------------------------------------------------------
# shared_return_labels
#
# F-124: `if (a === undefined) goto R; if (a === null) goto R; ...` where R is `return a`.
#
#     98/11208 `wrappedFn`, 96/4157 `parseFileSlash`, 96/1139 `processColor`: two constant tests
#     of the same value that share one body are not a `switch` (it needs two bodies), but the
#     second test was folded away as if it were a case link, so `a === null` fell off the end
#     of the function and returned `undefined` instead of `a`.
# ----------------------------------------------------------------------------------------------------

def test_both_labels_of_a_shared_return_keep_their_return():
    hasm = (_DATA / "two_labels_one_return_98_11208.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11208, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    # one body for both labels: one condition, not a `switch` and not an `else if`
    assert "if (r3 === undefined || r3 === null) {\n        return r3;\n    }" in out
    # the old shape: the `null` case silently returned nothing
    assert "else if (r3 !== null)" not in out


def test_a_constant_the_second_label_loads_and_the_code_after_reads_is_loaded_again_there():
    """96/1139 `processColor`: `r3 = null; if (a === r3) goto R;` and the next test reads `r3` too.
    The labels fold into one condition and the code after them gets its own copy of the load."""
    hasm = (_DATA / "shared_return_two_labels_constant_96_1139.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 1139, strict=False), verbose=False, raw=False)

    assert "if (param1 === undefined || param1 === null) {\n        return param1;\n    }" in out
    assert "else if (param1 !== null)" not in out
    assert "r6 === null || r6 === undefined" in out


# ----------------------------------------------------------------------------------------------------
# shared_return_try_exit
#
# A `try` body that ends by jumping to the function's closing `return` gets its own `return` (F-10(b), 98/14166).
#
# `r0 = undefined` is set once at the entry and the `catch` handler (which has no predecessor) falls into
# the same closing `return r0`. `_single_reaching_value` took the handler for a path that never set the
# register and refused the copy, so the `try` printed `goto label_N`. A handler now counts as running from
# inside its try range, and a copy of a constant return says the value instead of naming the register.
# ----------------------------------------------------------------------------------------------------

def _code_3() -> str:
    hasm = (_DATA / "shared_return_try_exit_98_14166.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 14166, strict=False), verbose=False, raw=False)


def test_a_try_body_that_ends_the_function_returns_instead_of_jumping():
    code = _code_3()

    assert "goto" not in code
    assert "return undefined;\n    } catch" in code


def test_the_copied_return_names_no_register_that_prints_nowhere():
    assert "return r0" not in _code_3()


# ----------------------------------------------------------------------------------------------------
# shared_return_widened
#
# F-10: an `if (c) goto sonReturn` is gone when the shared exit can be copied
# without changing what it returns.
#
#     96/10518  `r1[param1] = r0` jumps to the function's closing `return` while
#               the other arm falls into it: the closing `return` is copied for
#               the jumper instead of leaving `goto label_91`.
#     96/11046  the closing `return r0` follows `r0 = true` on one path and
#               `r0 = false` on another. A register that holds a different CONSTANT
#               per path is copied per jumper (`return false`); the closing return
#               keeps the register's name. (One that held different non-constant
#               values stays a visible `goto`: the final return then read as one.)
# ----------------------------------------------------------------------------------------------------

def _render_8(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_closing_return_is_copied_for_a_jump_into_it():
    out = _render_8("shared_return_throw_exit_96_10518.hasm", 10518)

    # Since F-163 the first attempt is `goto`-free (the transform arm's trailing jump to the code after the
    # `if` is dropped), so the copies of the closing `return` are not made: one stays, in the inner `else`.
    assert "goto" not in out
    assert out.count("return undefined;") == 1


def test_a_return_whose_register_holds_a_different_constant_per_path_is_copied_per_jumper():
    """96/11046: `r0 = false; if (!c) goto RET` in the loop, `r0 = true` on the way out. Each jumper
    gets its own `return false`; the closing `return r0` keeps the register (set to `true` before the
    loop and in it), so an equal list still returns `true`."""
    out = _render_8("shared_return_phi_96_11046.hasm", 11046)

    assert "goto" not in out
    assert out.count("return false;") == 3
    assert out.count("r0 = true;") >= 2
    assert out.count("return r0;") == 1
    # the loop's increment runs after the `if` (the `is()` test jumps onto it, the last check falls into it)
    assert out.count("r5 = r10;") == 1
    assert out.index("r5 = r10;") > out.index("r3[6].call(")


def test_a_two_block_tail_with_an_inner_test_is_copied_for_the_test_that_skips_it():
    """98/1871 `get`: `f != null ? f(p) : null` then `?? (m[p] != null ? m[p] : null)`.
    The second operand is a tail of two blocks (it holds its own test) that one
    test jumps onto and another falls into."""
    out = _render_8("shared_tail_region_98_1871.hasm", 1871)

    assert "goto" not in out
    # F-273: `f == null || (r2 = f(p)) == null` is one test (the call's result is what the function returns
    # when it is not null), so the tail is no longer copied.
    assert "if (r2 == null || (r2 = r2(param1)) == null) {" in out
    assert out.count("r3 = r3[1][param1];") == 1
    assert out.count("r2 = null;") == 1


def test_a_copy_written_in_one_arm_is_not_taken_for_the_whole_merge():
    """96/4846 `binarySubdivide`: `r14 = r0; if (c) { r15 = r0; r14 = param3 }`,
    read after the `if` as `r10 = r14`. The arm's write (a copy of `param3`
    that `Mov r13, r10` also holds) was folded into the reader, which printed
    `r10 = param3` on the path that skips the arm too."""
    out = _render_8("loop_carried_arm_copy_96_4846.hasm", 4846)

    # `Mov r13, r10` holds the parameter's register, which the loop rewrites (F-175): it is `r10`, not `param3`
    assert "r14 = r13;" in out
    assert "r10 = r14;" in out
    # only the `LoadParam` line at the top says `r10 = param3`, never the reader after the `if`
    assert out.count("r10 = param3;") == 1


def test_a_shared_tail_with_a_statement_is_copied_with_its_own_nodes():
    """96/12456 `getSchemes`: `r1 = []; return r1` is jumped to by `!param1` and
    fallen into by the last `else`. The copy must be a real copy: when it
    shared the `[]` node with the original, a fold took the assignment out of
    the copy and `!param1` returned an unassigned `r1`.

    Since the guard-exit rule (F-123) the tail is no longer copied: the last
    `else` falls on to it and `!param1` jumps onto it, which is one `r1 = [];
    return r1;` after the `if`. What must still hold is that the assignment
    exists exactly where `r1` is read."""
    out = _render_8("shared_tail_with_statements_96_12456.hasm", 12456)

    assert "goto" not in out
    assert out.count("r1 = [];") == 1
    assert out.rstrip().endswith("r1 = [];\n    return r1;\n}")


def test_a_shared_tail_of_several_statements_is_copied_for_every_jumper():
    """96/2019 `mountDeferredValueImpl`: `memoizedState = x; return x`.

    Since F-159 the tail is not copied: the last test of the first arm jumps onto it and falls into a
    lone `return`, so it follows the `if` once (`goto`-free, the same paths)."""
    out = _render_8("shared_tail_with_statements_96_2019.hasm", 2019)

    assert "goto" not in out
    assert out.count("param1.memoizedState = param2;") == 1
    assert out.rstrip().endswith("param1.memoizedState = param2;\n    return param2;\n}")


def test_a_function_with_exception_handlers_still_gets_its_shared_return_copied():
    """96/3900 `normalizeRootMargin`: a `for-of` gives the function an exception
    handler, which used to switch the copy off for the whole function. The
    shared `return "0px 0px 0px 0px"` lies outside every protected range, so
    each jumper may own a copy: no `goto label_505`.

    The crossed fold now also runs in a function with handlers (96/474), so the first two jumpers are one
    `param1 == null || param1 === ""` test and the exit is copied for it and for the `trim()` test only."""
    out = _render_8("shared_return_with_handler_96_3900.hasm", 3900)

    assert "goto" not in out
    assert out.count('return "0px 0px 0px 0px";') == 2
    assert 'if (param1 == null || param1 === "") {' in out


def test_a_phi_return_is_not_copied_in_a_function_with_exception_handlers():
    """98/2477 `getComponentNameFromType`: `return r1` follows `r1 = null` on one
    path and `r1 = displayName || name || null` on another. One copy per jumper
    left `return null` and lost the second value; the exit stays shared."""
    out = _render_8("shared_return_phi_with_handler_98_2477.hasm", 2477)

    assert "param1.displayName || param1.name || null" in out
    assert "return null;\n            case" not in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_conditions
#
# A tail block that one test jumps over and several others jump onto must keep
# every one of those tests (the silent drop of 96/652, `_interopDefault`).
#
# Hermes lowers `a && b && c ? x : y` so that the `y` block is reached by the
# failing tests' jumps and by the last test's fall-through. Dropping the last
# test's branch (`_strip_trailing_jump_to`) or leaving a residual jump to a
# sibling arm silently removed a path. The fixes covered here:
#
# - the last test joins the chain (`ShortCircuitConditionCfgPass` crossed form),
#   its join copy moving onto the edge to END;
# - a lone comparison jumping into the sibling arm is not a `case` test;
# - one call in the second test's setup is folded into the condition;
# - otherwise the tail is copied for the fall-through (`SharedTailDuplicationCfgPass`).
# ----------------------------------------------------------------------------------------------------

def _render_9(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_typeof_polyfill_keeps_every_path():
    out = _render_9("typeof_polyfill_96_652.hasm", 652)

    assert "goto" not in out
    assert 'typeof Symbol' in out
    assert "param1.constructor !== Symbol" in out
    assert out.count("typeof param1") == 2  # the plain path and the `=== Symbol.prototype` path
    assert "param1 === r2" in out or "param1 === Symbol.prototype" in out


def test_interop_default_is_one_ternary_shape():
    out = _render_9("interopDefault_96_15102.hasm", 15102)

    assert "goto" not in out
    assert "if (param1 && param1.__esModule)" in out
    assert '"default": param1' in out


def test_large_interop_default_keeps_the_esmodule_test():
    out = _render_9("interopDefault_large_98_167.hasm", 167)

    assert "goto" not in out
    assert "r3 && r3.__esModule" in out
    assert "r4 = r3;" in out


def test_second_test_with_a_read_keeps_both_values():
    out = _render_9("lazy_status_96_1003.hasm", 1003)

    assert "goto" not in out
    assert "0 === r2 || -1 === r0[0]._status" in out


def test_one_call_in_the_second_test_folds_into_the_condition():
    out = _render_9("call_in_second_test_96_7722.hasm", 7722)

    assert "goto" not in out
    assert "r0[26].call(undefined)" in out
    assert out.count("r0[26]") == 1


def test_value_ternary_that_is_only_tested_folds_into_the_condition():
    """96/12188: `!d || (k in d ? !m.__esModule : d.writable || d.configurable)`.

    The ternary's value goes through a register that only one test reads: the
    diamond becomes the test, so the default descriptor is written once."""
    out = _render_9("shared_tail_after_ternary_96_12188.hasm", 12188)

    assert "goto" not in out
    assert "if (!r4 || (\"get\" in r4 ? !param2.__esModule : r4.writable || r4.configurable)) {" in out
    assert out.count('"enumerable": true') == 1


def test_call_chain_in_the_second_test_folds_into_the_condition():
    """96/7811: `p === undefined || p === env[0].getId()`; the setup is
    `r0 = env; r1 = r0[0]; r0 = r1.getId()` - the operands of the one call."""
    out = _render_9("getParent_call_in_second_test_96_7811.hasm", 7811)

    assert "goto" not in out
    assert "param1 === getEnvironment(0)[0].getId()" in out


def test_call_chain_through_one_register_keeps_the_whole_condition():
    """96/11316: `r0 = a.props; r0 = r0.x; r0 = Object.keys(r0.value); r1 = r0.length`."""
    out = _render_9("compareProps_call_chain_96_11316.hasm", 11316)

    assert "goto" not in out
    assert "Object.keys(param1.props.jestAnimatedProps.value).length === 0" in out


def test_a_stale_inlined_callee_is_not_folded_into_a_wrong_value():
    """96/9118: the frontend inlines the callee as `r0[0]` while the setup has
    since set `r0 = undefined` (the call's `this`). Folding that read the
    constant (`undefined[0](...)`): the fold must refuse instead."""
    out = _render_9("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "undefined[0]" not in out


def test_the_guard_with_an_empty_else_is_one_if_without_a_goto():
    """96/9118 (F-04): `if (len === 1 && callee(...)) { r0 = [..] } else { r0 = [] }`. The set-up
    register is read at the join too, which once left `if (r0) goto label_44`."""
    out = _render_9("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "goto" not in out
    assert "} else {\n        r0 = [];" in out


def test_function_with_handlers_does_not_get_an_edge_block():
    """98/2917 crashed the dominator pass (`KeyError`): the edge block for a sunk
    join copy was added in a function with exception handlers, whose try ranges
    name blocks the merge had dropped. Such a function keeps the old shape."""
    out = _render_9("sunk_copy_with_handlers_98_2917.hasm", 2917)

    assert out.strip().startswith("function")


def test_value_chain_that_is_only_tested_folds_into_the_condition():
    """98/2463: `Start || Move || End || Cancel`. The last two are a value (`r5 = End || Cancel`)
    that one test reads; with it folded the chain is a single condition, and the
    comparison with `topTouchMove` is not mistaken for a later definition's value
    (`r6 = param1 === "topTouchMove"`), which an earlier condition cannot read."""
    out = _render_9("touch_chain_value_tests_98_2463.hasm", 2463)

    assert (
        'if (param1 === "topTouchStart" || param1 === "topTouchMove" || '
        '(param1 === "topTouchEnd" || param1 === "topTouchCancel")) {'
    ) in out
    assert "r6 ||" not in out


def test_negated_logical_condition_prints_with_de_morgan_only_for_exact_operands():
    """`!(a && !b)` reads `!a || b`; `!(a < b && c)` keeps its `!` (NaN)."""
    from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
    from hermes_decompiler.ir import LogicalOperator
    from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
    from hermes_decompiler.ir.expressions import BinaryExpression, Identifier, UnaryExpression

    a, b, c = Identifier("a"), Identifier("b"), Identifier("c")
    printer = ExpressionPrinter()

    free = UnaryExpression(UnaryOperator.LOGICAL_NOT, BinaryExpression(
        a, LogicalOperator.AND, UnaryExpression(UnaryOperator.LOGICAL_NOT, b)))
    ordering = UnaryExpression(UnaryOperator.LOGICAL_NOT, BinaryExpression(
        BinaryExpression(a, BinaryOperator.LESS_THAN, b), LogicalOperator.AND, c))

    assert printer.visit(free) == "!a || b"
    assert printer.visit(ordering) == "!(a < b && c)"


def test_any_of_several_parameters_is_one_condition():
    """96/4456: `if (a || b || c || d || e || f) {...}` - every test but the first sits
    behind a `LoadParam` the test already inlined; the chain used to stop after `a`
    and the rest became `else { if (b || ...) goto }`."""
    out = _render_9("any_of_params_96_4456.hasm", 4456)

    assert "goto" not in out
    assert "if (param1 || param2 || param3 || param4 || param5 || param6) {" in out


def test_second_test_with_its_own_call_keeps_each_callee():
    """98/11891: `len === 1 && (a(x) || b(x))`. The setup of the second call reads the
    environment register that the first call's setup set; once `r2` is re-assigned
    (`r2 = x`) the callee must still name the environment, not `x`."""
    out = _render_9("parseTranslateX_two_calls_98_11891.hasm", 11891)

    assert "goto" not in out
    assert (
        "r2 === 1 && (getParentEnvironment(0)[0].call(undefined, param1[0])"
        " || getParentEnvironment(0)[1].call(undefined, param1[0]))"
    ) in out


def test_constant_comparison_in_a_plain_chain_is_not_a_case_test():
    """96/150: `... || p < 0 || p === Infinity` all jump to one `throw`.

    The old output folded the three tests into `!(r1 || p < 0) && p !== Infinity` and put
    the `throw` nowhere: an invalid size returned `undefined`. The tests are one `||` and the
    `throw` is written once (it was copied per test while the fold of the call test, whose
    constant the throw's block reads, failed: 96/3450)."""
    out = _render_9("size_checks_throw_96_150.hasm", 150)

    assert "goto" not in out
    assert out.count('throw new RangeError("Size must be a finite, non-NaN, non-negative number.")') == 1
    assert '"number" !== r0 || getEnvironment(0)[20].call(undefined, param3) || param3 < 0 || param3 === Infinity' in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_each_way
#
# A small tail entered by a fall-through and by jumps, while an earlier test skips it, gets a copy per
# way in (98/2216 `getScriptURL`).
#
#     if (r5 == null) goto J;  ...  r3 = null;  if (startsWith) goto END;  ...
#     if (includes) goto J;  r5 = "file://" + r7;
#     J: r3 = r5       END: r4[5] = r3
#
# `J` has three ways in; the first attempt printed it in the `r5 == null` arm only and stored the wrong
# value on the other paths (`r4[5] = r5` even for an `assets://` URL, where it must be `null`). Level 5 of
# the retries copies `J` per way in and names the register after the join.
# ----------------------------------------------------------------------------------------------------

def test_every_way_into_the_shared_tail_writes_the_register_it_reads_after():
    hasm = (_DATA / "shared_tail_each_way_98_2216.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2216, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert out.count("r3 = r5;") == 2
    assert "r3 = null;" in out
    assert "r4[5] = r3;" in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_foreign_leaf
#
# A shared tail with another way's leaf between it and `END` is still copied (F-217, 98/6324 `isCompact`).
#
#     if (!a) goto T;  if (a === "beside") { r1 = true; goto J }  r1 = false; if (a === "below") goto J;
#     T: <test, two arms>; jmp J      X: r1 = true      J: ...
#
# The block `X` of the `beside` leaf lies in the layout between the tail and `J`, so the blocks up to `J` were not
# all the tail's own and the region was refused. The region is now the run of blocks only the tail enters, ending in
# a jump to `J`; the test that skips it gets a private copy and the `else` arm runs the tail when `a` is neither.
# ----------------------------------------------------------------------------------------------------

def test_a_leaf_between_the_tail_and_its_end_does_not_stop_the_copy():
    hasm = (_DATA / "shared_tail_foreign_leaf_98_6324.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6324, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    # The tail (the width test) runs for `!a` AND when `a` is neither `beside-icon` nor `below-icon`.
    assert out.count("r8 >= 768") == 2
    assert 'if ("below-icon" !== r9) {' in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_inside_try
#
# A shared tail inside a `try` range is copied for the test that skips it, when its ways in are inside too (F-195).
#
#     try { ...; if (A) goto T; r = f(x); if (!r) goto END; T: push(x); END: }        (a for-of body)
#
# F-193 let the copy pass work in functions with a handler when nothing it touches is protected. A for-of's whole
# body is the protected range, so every tail in it was left alone (`goto label_128` in 98/1738 `getChildNodes`, the
# filter result decided whether `push` ran and the output ran it on both paths). The copy sits right in front of the
# tail, inside the same range, so a tail and every way into it under the SAME handlers are copied; a tail something
# outside the range jumps to, or a handler's entry, is not.
#
# The copy is the block the test FALLS into, so `LoopStructurer` lays it out right behind that test (`follows`);
# by id it came last in the loop body, after the latch.
#
#     98/1738 `getChildNodes`   98/8837 `getInlineStyle`
# ----------------------------------------------------------------------------------------------------

def _render_10(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_filter_result_decides_the_push():
    out = _render_10("shared_tail_inside_try_98_1738.hasm", 1738)

    assert "goto" not in out
    # the tests now fold into one condition (F-216), so nothing needs the tail twice
    assert "if (r8 != null && (param2 == null || param2(r6))) {" in out
    assert out.count("r0.push(") == 1


def test_the_transform_check_that_fails_keeps_the_plain_assignment():
    out = _render_10("shared_tail_inside_try_98_8837.hasm", 8837)

    assert "goto" not in out
    assert out.count("r3[r11] = r10;") == 1
    # the copy of the first test's operand folds into the condition (F-225)
    assert 'if (!r10 && (r9 !== "transform" || !r0[5].call(0, r8))) {' in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_jumpers
#
# F-127: a jump into the other arm of an enclosing `if` must stay.
#
#     96/273 `q`: `if (state !== "writable" || isX(...)) n(); else schedule(n)`. Both tests
#     jump to the `n()` block and nothing falls into it. The second test's jump used to be
#     folded away (`if (!isX) { schedule }`), so `n()` never ran for it.
# ----------------------------------------------------------------------------------------------------

def _render_11(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_both_tests_that_jump_to_the_tail_reach_it():
    out = _render_11("or_condition_calls_shared_tail_96_273.hasm", 273)

    assert "goto" not in out
    # `n()` runs when the state is not writable AND when the second test holds
    assert out.count("r0 = n();") == 1
    assert 'if ("writable" === r3)' in out
    assert "if (!r2) {" in out
    assert out.index("r0 = r2(r0, n);") < out.index("r0 = n();")


# ----------------------------------------------------------------------------------------------------
# shared_tail_other_way
#
# A shared tail the test skips by jumping to the block behind it (F-186).
#
#     if (!a) goto T;                 // jumper
#     if (c) goto B;                  // the test: its fall-through is T, its jump is the block right behind T
#     T: r0 = +x; jmp END
#     B: r0 = y / 100                 // falls into END
#     END: ...
#
# `SharedTailDuplicationCfgPass` gave the test a private copy of `T` only when the test jumped straight to `END`.
# Here it jumps to `B`, which runs on into `END`: the same two-way meeting, with `T` as the test's own `else`. Left as
# it was, the structurer gave `T` to the jumper and printed `if (r4) goto label_42; r2 = -1; ... slice`, which runs
# the `slice` path for a string that does not end in `%`.
#
# Only on the rungs that already copy regions (`regions=True`): on the first ones it changed 96/2264 `pop`, which the
# plain skip had solved.
#
#     98/8059  `processPercentage`   98/11896 `parseScale`   96/2264 `pop` (must stay goto-free)
# ----------------------------------------------------------------------------------------------------

def _render_12(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_string_without_a_percent_sign_is_converted_not_sliced():
    out = _render_12("shared_tail_other_way_98_8059.hasm", 8059)

    assert "goto" not in out
    assert "if (r4) {\n            r2 = -1;" in out
    assert "} else {\n            r0 = +param1;\n        }" in out
    assert out.count("r0 = +param1;") == 2


def test_an_empty_list_is_the_else_of_the_validity_test():
    out = _render_12("shared_tail_other_way_98_11896.hasm", 11896)

    assert "goto" not in out
    # With the closure-environment read pure (F-228) the guard and the validity test are ONE condition, and the
    # empty list is the `else` of that condition (it used to be two `r7 = [];` around a nested `if`).
    assert 'if (r7 === 1 && __getClosureEnvironment__(r3[1])[0].call(undefined, r5[0])) {' in out
    assert "} else {\n                r7 = [];\n            }" in out


def test_a_loop_the_plain_skip_solved_keeps_its_shape():
    out = _render_12("shared_tail_other_way_96_2264.hasm", 2264)

    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_region_copy_values
#
# A copied tail region keeps its readers wired to their writers (98/8193 `compareIdentifiers`, 0x61 made a plain `jmp`).
#
# `SharedTailDuplicationCfgPass` copied the tail `{r3 = 1 | r2 = ...; r3 = r2}; r1 = r3` for the fall-through test.
# Two things made the copy print a silent miscompile, no `goto` and no warning:
#
# * each copied instruction was deep-copied on its own, so the copy's `r1 = r3` / `r3 = r2` lost the shared value
#   object their writer holds; the ternary fold finds a writer's readers by that identity and never reached
#   them: `r1 = r3` printed as `r1 = -1`;
# * the copy keeps the original's instruction addresses, so its `r1 = r3` counted as a read of `r3` AFTER the
#   original arm and kept the original's own reader from being repointed (`r1 = r8 >= r9 ? 1 : -1` where
#   `r11` makes it `1`).
# ----------------------------------------------------------------------------------------------------

def _render_13():
    hasm = (_DATA / "shared_tail_region_copy_98_8193.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 8193, strict=False), verbose=False, raw=False)


def test_the_copied_tail_reads_its_own_r3():
    out = _render_13()

    assert "goto label" not in out
    assert "r1 = -1;\n                if (r11) {" in out
    assert "r1 = r3;\n                }\n            }\n            r0 = r1;" in out


def test_the_original_tail_reads_r3_too():
    out = _render_13()

    assert "                r1 = r3;\n            } else {" in out
    assert "r1 = r8 >= r9 ? 1 : -1" not in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_that_only_returns_gets_a_copy_for_the_jumpers
#
# `if (X) { A; if (c) goto TAIL } T: ...; TAIL: ...` kept `if (c) goto label_N;` (98/2330, 96/7888).
#
# `T` is reached by the jump of the test of `X` and by falling out of the `c` test, and it never runs on: it returns,
# throws or continues the loop. `TerminalTailRegionCopyCfgPass` (the last rung) gives the jumpers their own copy of the
# whole region, so both arms of `X` are ordinary `if`/`else` trees.
# ----------------------------------------------------------------------------------------------------

@pytest.mark.parametrize(
    "fixture, section",
    [
        ("terminal_tail_shared_with_a_guard_in_loop_98_2330.hasm", 2330),
        ("terminal_tail_shared_with_a_guard_96_7888.hasm", 7888),
    ],
)
def test_the_guard_needs_no_goto(fixture, section):
    hasm = (_DATA / fixture).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out


# ----------------------------------------------------------------------------------------------------
# shared_tail_with_try
#
# A shared tail is copied in a function with a `try` too, when nothing it touches is protected (F-193).
#
#     if (!a) goto T; ...; if (b) goto E; T: x; jmp END; E: y; END:
#
# `SharedTailDuplicationCfgPass` gave up on every function with an exception handler (a copy sits outside every try
# range). 98/13397 `loadRoute` has a `try` as the first thing of the function and the `_result` tests far behind
# it: the second test kept `if (r2 != null) goto label_111`. A tail, and the tests in front of it, that no handler
# protects or starts at are copied as everywhere else; a function whose tail is protected is still left alone.
#
#     98/13397 `loadRoute`   96/7898 `shouldPreventRemove` (the handler guards the loop at the end, the tail is before it)
# ----------------------------------------------------------------------------------------------------

def _render_14(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_tail_behind_a_try_is_copied_for_the_test_that_skips_it():
    out = _render_14("shared_tail_with_try_98_13397.hasm", 13397)

    assert "goto" not in out
    assert "} catch (caughtException) {" in out
    assert 'if ("_result" in r0 && r0._result != null) {\n            r2 = r0;\n            r1 = r2._result;\n        } else {\n            r1 = r0;' in out


def test_the_instanceof_test_that_falls_into_the_new_set_is_one_if():
    out = _render_14("shared_tail_with_try_96_7898.hasm", 7898)

    assert "goto" not in out
    assert "r8 = r3;" in out and "r8 = param5[r1];" not in out


# ----------------------------------------------------------------------------------------------------
# shared_throw_exits_keep_the_original_for_the_earlier_jumper
#
# Shared `throw` exits reached only by jumps (98/3508 `toQueryPair`: `typeof r !== "object"` / `r == null`, twice).
#
# The first test of a pair kept a copy of the exit, the later one kept the original: the copy of the second pair sat
# behind the whole `else` arm and the test printed `if (typeof r7 !== "object") goto label_N;` with the throw after the
# arm. The EARLIER jumper now keeps the original, every later one gets a private copy.
# ----------------------------------------------------------------------------------------------------

def test_both_typeof_object_tests_throw_in_place():
    hasm = (_DATA / "shared_throw_copies_in_iterator_pair_98_3508.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3508, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert out.count('throw new TypeError("The provided value is not an object");') == 4


# ----------------------------------------------------------------------------------------------------
# shared_throw_size
#
# A shared `throw new E(message)` of thirteen instructions is still one statement (F-174, F-10b).
#
# The copy limit for a shared `throw` was twelve instructions, and `throw new TypeError("..." + p + "...")` built by
# `HermesInternal.concat` is thirteen (`LoadParam`, `GetGlobalObject`, two lookups, the concat call, `CreateThis`,
# `Construct`, `SelectObject`, ...). Both tests of a `used || locked` check jumped to it and one of them was printed as
# `goto label_62`. Each jumper gets its own `throw`.
#
#     98/4987  `checkBodyUsedError`
#     96/7669  an `invariant`-style check whose message is thrown from two tests
# ----------------------------------------------------------------------------------------------------

def _render_15(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_both_tests_throw_their_own_error():
    out = _render_15("shared_throw_98_4987.hasm", 4987)

    assert "goto" not in out
    assert out.count("throw new TypeError(r8);") == 2
    assert "if (r2 === true) {" in out


def test_a_throw_shared_by_two_tests_in_a_nested_check():
    out = _render_15("shared_throw_96_7669.hasm", 7669)

    assert "goto" not in out
    assert out.count("throw new r2(r8);") == 2


# ----------------------------------------------------------------------------------------------------
# tail_copy_register_leak
#
# A copy of a shared tail never reads a register only the OTHER path sets (F-247, 96/43 `formatValue`).
#
#     r6 = !param2.name ? "" : r15;        // r15 is written by the unrelated `[Function` path only
#
# Retry rungs copy a tail; the copy's instructions are new, so `UnfoldedMergeRepairPass` could not tell they lie
# behind a different write and handed them the register of the first path's `": " + name`.
# ----------------------------------------------------------------------------------------------------

def test_the_copy_keeps_its_own_value():
    hasm = (_DATA / "tail_copy_register_leak_96_43.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 43, strict=False), verbose=False, raw=False)

    assert '"" : r15' not in out
    assert 'r6 = "[Function" + (!param2.name ? "" : ": " + param2.name) + "]";' in out


# ----------------------------------------------------------------------------------------------------
# terminal_tail_copy_on_the_plain_layout
#
# `if (undefined === r12) goto T` into code that rung 10's layout keeps splitting (98/9589 `fe`).
#
# The `async` arm reaches the shared `iterable?` check by falling through and `T` (the sync-iterator fallback) only by the
# jump. Rung 13 (`TerminalTailRegionCopyCfgPass` on rung 10's copies) still leaves a `goto` inside the tail the copies
# split; the last rung runs the same pass on rung 1's layout.
# ----------------------------------------------------------------------------------------------------

def test_the_tail_copy_on_the_plain_layout_needs_no_goto():
    hasm = (_DATA / "terminal_tail_behind_a_returning_block_98_9589.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert 'r7 = r5[36].call(0, param1, "sync", r7);' in out


# ----------------------------------------------------------------------------------------------------
# terminal_tail_relocated_in_function_with_handlers
#
# An early-return tail laid out after the closing return becomes `if (c) { tail }` in a function with a `try` (F-277).
#
# `if (signal && signal.aborted) { return reject(new DOMException(...)) }` ahead of a `try` compiles to a branch to a
# block placed behind the function's closing `return undefined`. `relocate_terminal_tails` moves such a tail behind its
# branch, but gave up on any function that has handlers; only a branch or tail a handler guards must stay (96/3448
# `fetch` of the XHR polyfill).
# ----------------------------------------------------------------------------------------------------

def test_the_abort_tail_is_an_if_body_before_the_try():
    hasm = (_DATA / "terminal_tail_relocated_in_function_with_try_96_3448.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3448, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert 'new r4("Aborted", "AbortError")' in out
    assert out.index('"AbortError"') < out.index("try {")


# ----------------------------------------------------------------------------------------------------
# terminal_tail_relocation
#
# `if (c) goto TAIL` whose tail only ever returns is an `if (c) { tail }` (F-246, 98/12534 `pipeTo`).
#
#     if (signal.aborted) { abortAlgorithm(); return; }      // inlined by the compiler AFTER the closing `return`
#     signal.addEventListener("abort", abortAlgorithm);
#
# The branch jumped over the whole function to blocks laid out behind the last `return`; nothing structured them
# (`if (r4.aborted) goto label_633;`). On the last retry rung (`FallThroughLayoutCfgPass.relocate_terminal_tails`) the
# tail moves right behind the branch and the branch is inverted to jump over it.
# ----------------------------------------------------------------------------------------------------

def test_the_aborted_arm_is_an_else_that_returns():
    hasm = (_DATA / "terminal_tail_relocation_98_12534.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 12534, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r4.aborted) {" in out
    # the arm ends in its own `return`: without it the code after it would run for an aborted signal as well
    arm = out[out.index("r1 = q.call(0, function_14099, r1, r5);"):]
    assert arm.lstrip().split("\n")[1].strip() == "return undefined;"
