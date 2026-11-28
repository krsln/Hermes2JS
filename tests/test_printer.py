"""The printer and small frontend cases: names, literals, builtins, windows, placeholders, retries.

Merged from: test_call_builtin_window_frame_size, test_closure_env_pure, test_console_log_read_passed_on, test_fewest_gotos_retry_is_kept_when_none_is_goto_free, test_lossy_first_attempt, test_lost_path_retry, test_new_object_identity, test_printer_negation_grouping, test_printer_property_names_that_are_not_identifiers, test_reserved_words_are_not_function_names, test_split_output_file, test_super_call_window, test_this_placeholder_copied_before_a_throw.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.emit.printer.ExpressionPrinter import ExpressionPrinter
from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.core.Naming import to_js_identifier
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.Operators import BinaryOperator, UnaryOperator
from hermes_decompiler.ir.expressions import (
    BinaryExpression,
    CallExpression,
    Identifier,
    MemberExpression,
    UnaryExpression,
)


# ----------------------------------------------------------------------------------------------------
# call_builtin_window_frame_size
#
# The call-argument window of `CallBuiltin` sits a fixed distance below the
# frame size (7 on hbc96, 8 on hbc98 - read off the opcodes the function uses),
# so a recent unrelated write one slot above the real window cannot move it:
#
#   96/2877   copyDataProperties(r10, r9)    (was (r11, r10): the `this` slot)
#   98/11966  throwTypeError("...")          (was r30, an older `this` slot)
# ----------------------------------------------------------------------------------------------------

_HASM_96 = r"""
=> [Function #2877 "toJSON" of 75 bytes]: 1 params, frame size=18, strict=1, exc handler=0, debug info=0  @ offset 0x0014c22d

Bytecode listing:

==> 00000000: <LoadParam>: <Reg8: 1, UInt8: 0>
==> 00000003: <NewObject>: <Reg8: 0>
==> 00000005: <GetEnvironment>: <Reg8: 2, UInt8: 1>
==> 00000008: <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 0>
==> 0000000c: <GetByIdShort>: <Reg8: 6, Reg8: 2, UInt8: 1, string_id: 107>  # String: 'default' (Identifier)
==> 00000011: <GetEnvironment>: <Reg8: 2, UInt8: 0>
==> 00000014: <LoadFromEnvironment>: <Reg8: 10, Reg8: 2, UInt8: 0>
==> 00000018: <LoadConstUndefined>: <Reg8: 4>
==> 0000001a: <LoadConstString>: <Reg8: 9, string_id: 9976>  # String: 'toJSON' (Identifier)
==> 0000001e: <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
==> 00000021: <LoadConstUndefined>: <Reg8: 11>
==> 00000023: <Mov>: <Reg8: 8, Reg8: 1>
==> 00000026: <Call>: <Reg8: 3, Reg8: 6, UInt8: 5>
==> 0000002a: <NewArray>: <Reg8: 2, UInt16: 0>
==> 0000002e: <Call2>: <Reg8: 9, Reg8: 3, Reg8: 4, Reg8: 2>
==> 00000033: <Mov>: <Reg8: 10, Reg8: 0>
==> 00000036: <CallBuiltin>: <Reg8: 2, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
==> 0000003a: <GetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 8013>  # String: 'attribution' (Identifier)
==> 00000040: <LoadConstString>: <Reg8: 1, string_id: 8013>  # String: 'attribution' (Identifier)
==> 00000044: <PutOwnByVal>: <Reg8: 0, Reg8: 2, Reg8: 1, UInt8: 1>
==> 00000049: <Ret>: <Reg8: 0>
"""

_HASM_98 = r"""
=> [Function #1 "f" of 40 bytes]: 2 params, frame size=38, strict=1, exc handler=0, debug info=0  @ offset 0x00000000

Bytecode listing:

==> 00000000: <GetParentEnvironment>: <Reg8: 6, UInt8: 0>
==> 00000003: <LoadParam>: <Reg8: 13, UInt8: 1>
==> 00000006: <LoadConstUndefined>: <Reg8: 30>
==> 00000008: <LoadFromEnvironment>: <Reg8: 8, Reg8: 6, UInt8: 18>
==> 0000000c: <JmpTypeOfIs>: <Addr32: 16, Reg8: 8, UInt16: 128>  # Address: 0000001c
==> 00000014: <LoadConstString>: <Reg8: 29, string_id: 4299>  # String: 'Trying to call a non-function' (String)
==> 00000018: <CallBuiltin>: <Reg8: 5, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
==> 0000001c: <Ret>: <Reg8: 13>

"""


def _js(hasm: str, function_id: int) -> str:
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_hbc96_window_top_follows_frame_size():
    js = _js(_HASM_96, 2877)

    assert "copyDataProperties(r10, r9)" in js


def test_hbc98_window_top_ignores_unrelated_recent_write_above_it():
    js = _js(_HASM_98, 1)

    assert 'throwTypeError("Trying to call a non-function")' in js


# ----------------------------------------------------------------------------------------------------
# closure_env_pure
#
# `__getClosureEnvironment__(r)` is environment plumbing, not a call that runs user code (F-228, 98/11900).
#
#     if (len !== 1) goto T;  r5 = <closure env>; r6 = f(x); if (r6 || x === 0) goto B;  T: r6 = [];  B: ...
#
# The crossed fold `len === 1 && (f(x) || x === 0)` counts the side effects of the second test's set-up: the closure
# environment read counted as one (so did the call), two in all, and the fold was refused. With the read in
# `PURE_CALLEES` the pair is one condition and the `goto` is gone.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_the_closure_environment_read_is_pure():
    read = CallExpression(callee=Identifier(name="__getClosureEnvironment__"), arguments=(Identifier(name="r4"),))

    assert not has_side_effects(read)


def test_the_guard_and_the_pair_become_one_condition():
    hasm = (_DATA / "closure_env_pure_98_11900.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11900, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "=== 1 && (" in code


# ----------------------------------------------------------------------------------------------------
# console_log_read_passed_on
#
# A `console.log` read that is passed on keeps its register (98/6517 `log`).
#
# `r3 = console.log` is read later by `apply(r3, ...)` (a spread call through `arraySpread`/`apply`). The printer left the
# `rN =` off every unused statement that starts with `console.log`, a rule meant for a discarded call, so the line
# printed as a bare `console.log;` and `r3` was read without ever being set.
# ----------------------------------------------------------------------------------------------------

def _render() -> str:
    hasm = (_DATA / "console_log_read_passed_on_98_6517.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 6517, strict=False), verbose=False, raw=False)


def test_the_read_keeps_its_register():
    out = _render()

    assert "r3 = console.log;" in out
    assert "r9 = r3;" in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# fewest_gotos_retry_is_kept_when_none_is_goto_free
#
# When no retry is `goto`-free, the one with the fewest `goto`s replaces the first attempt (F-263, 98/2474).
#
# The first attempt leaves the shared `return ""` as `if (r4[7]) goto label_899;`; the retries that copy the shared
# return per jumper remove it, but three other `goto`s keep every attempt invalid, so the first attempt used to win
# with all four.
#
# Since F-301 the `goto`s that stay after every rung print as `label_N: { ... break label_N; ... }`: the retry that
# copies the shared return is still the attempt that is printed (three jumps out of nested arms, no `label_899`).
# ----------------------------------------------------------------------------------------------------

def test_the_retry_with_fewer_gotos_wins_when_every_attempt_has_some():
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)

    assert "label_899" not in out
    assert "goto" not in out
    assert sum("break label_" in line for line in out.splitlines()) == 3


# ----------------------------------------------------------------------------------------------------
# lossy_first_attempt
#
# A first attempt that silently loses a path is not kept over a retry that loses none (F-171).
#
# The first attempt of 98/10128 `interpolate` was `goto`-free, so it was never compared with the retries, but
# `flow_audit` counts 4 lost paths in it: a clamped `x` never reached the range test (the `else` arm of
# `x < r9` ended without running on into it). Level 5 loses nothing and still has one `goto`: a `goto` says the
# structure is missing, a wrong tree says nothing. 96/6029 `_anon_0` is the same: the first attempt returned
# `r1` early where the source awaits `_updateBottomIfNecessary()`.
#
#     98/10128  `interpolate`
#     96/6029   `onLayout` handler
# ----------------------------------------------------------------------------------------------------

def _render_2(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_clamped_input_reaches_the_range_test():
    out = _render_2("lossy_first_attempt_98_10128.hasm", 10128)

    assert out.index('r17 = r9;') < out.index("if (r17 > r12) {")


def test_a_changed_height_awaits_the_update():
    out = _render_2("lossy_first_attempt_96_6029.hasm", 6029)

    assert "return r1;" not in out
    assert out.index("await r3._updateBottomIfNecessary();") < out.index("r3.onLayout")


# ----------------------------------------------------------------------------------------------------
# lost_path_retry
#
# A tree without a `goto` that lost a path gets the shared-return/-tail retries too.
#
# 98/12551: `if ("readable" !== state) goto TAIL; ...; r1 = r3[98].call(...); TAIL: r3[105].call(...); throw p`.
# The first attempt printed the `else` arm without the `TAIL` it falls into (the function returned
# `undefined` where it had to call and throw). `flow_audit.count_lost_edges` sees the lost path, so the
# retries run, and one that has no `goto` and loses fewer paths is the output. 96/2602 is the same
# mechanism (the `6 === tag` test's edge to the shared body, F-148).
# ----------------------------------------------------------------------------------------------------

def _render_3(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_the_fall_through_arm_still_runs_the_shared_throw_tail():
    out = _render_3("lost_throw_tail_98_12551.hasm", 12551)

    assert "goto" not in out
    assert out.count("throw param1;") == 2
    assert out.count("r3[105]") == 2


def test_the_edge_of_a_case_test_to_the_shared_body_is_kept():
    out = _render_3("lost_case_edge_96_2602.hasm", 2602)

    assert "goto" not in out
    assert "case 6:" in out or "6 === r4" in out


# ----------------------------------------------------------------------------------------------------
# new_object_identity
#
# An object made by `new` is ONE object, so it is built once and read through its register (F-146, 96/1163
# `PlatformColor`).
#
#     r1 = new Array(n)          // CreateThis / Construct / SelectObject
#     loop: r1[i] = arguments[i]
#     return { resource_paths: r1 }
#
# The value of `SelectObject` is the `NewExpression` itself, and `get_register_expression` inlined it into
# every reader: the loop printed `new Array(r5)[r0] = arguments[r0]`, a fresh array on every iteration
# that nothing keeps, and the result held a second one. A `new` is now kept in its register like a call
# or a literal object, when a read sits in a loop its definition is outside of or when another read
# of it does (the scratch pass of `OpcodeDispatcher` says which definitions print).
#
# 96/15130 `tag` stores the array in the environment first and fills it in the loop afterwards:
# `r0[0] = new Array(n)` stored one array and the loop filled a second one.
# ----------------------------------------------------------------------------------------------------

def _render_4(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def _code() -> str:
    return _render_4("new_object_identity_96_1163.hasm", 1163)


def test_a_new_object_read_twice_is_built_once():
    code = _code()

    assert code.count("new Array(") == 1


def test_the_loop_fills_the_register_that_is_returned():
    code = _code()

    assert "r1 = new Array(r5);" in code
    assert "r1[r0] = arguments[r0];" in code
    assert '"resource_paths": r1' in code


def test_a_new_object_stored_before_a_loop_fills_the_stored_object():
    code = _render_4("new_object_stored_then_filled_96_15130.hasm", 15130)

    assert code.count("new Array(") == 1
    assert "r0[0] = r4;" in code
    assert "r4[r9] = arguments[r2];" in code


def test_a_new_object_read_three_times_is_one_object():
    """96/4138 `createSearchParams` (F-147): the object is indexed twice and returned. The constructor is
    read from the global object here, so that `SelectObject` sees a `NewExpression` as in a whole bundle."""
    code = _render_4("new_object_read_three_times_96_4138.hasm", 4138)

    assert code.count("new ") == 1
    assert "r0 = new URLSearchParams();" in code
    assert "r0[r2].url = param1;" in code
    assert "return r0;" in code


# ----------------------------------------------------------------------------------------------------
# printer_negation_grouping
#
# A `!` over `&&`/`||` is printed as its De Morgan form when the operands negate
# cleanly (`!(a !== b && c === d)` -> `a === b || c !== d`). The parent of such a
# node has to group it by the form that is actually printed, not by the `!` it was
# built as. Before, a flipped `||` under `&&` lost its parentheses, which changed
# the value (98/9594, F-02):
#
#     !!((A && B) || C)  printed  !(P || Q) && R       (not the same value)
#     !(A && B) && C     printed  P || Q && C          (`&&` binds tighter)
# ----------------------------------------------------------------------------------------------------

_x, _y, _z = Identifier("x"), Identifier("y"), Identifier("z")


def _not(expression):
    return UnaryExpression(UnaryOperator.LOGICAL_NOT, expression)


def _eq(left, right):
    return BinaryExpression(left, BinaryOperator.STRICT_EQUAL, right)


def _ne(left, right):
    return BinaryExpression(left, BinaryOperator.STRICT_NOT_EQUAL, right)


def _and(left, right):
    return BinaryExpression(left, LogicalOperator.AND, right)


def _or(left, right):
    return BinaryExpression(left, LogicalOperator.OR, right)


_A, _B, _C = _eq(_x, _y), _ne(_x, _z), _eq(_y, _z)


def _print(expression) -> str:
    return ExpressionPrinter().visit(expression)


def test_the_flipped_form_alone_has_no_parentheses():
    assert _print(_not(_and(_A, _B))) == "x !== y || x === z"


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        # `||` (flipped from `!(&&)`) as the left operand of `&&`
        (_and(_not(_and(_A, _B)), _C), "(x !== y || x === z) && y === z"),
        # ... and as the right one
        (_and(_C, _not(_and(_A, _B))), "y === z && (x !== y || x === z)"),
        # `&&` (flipped from `!(||)`) under `||` needs none: `&&` binds tighter
        (_or(_not(_or(_A, _B)), _C), "x !== y && x === z || y === z"),
        # `||` as the left operand of `||` needs none; as the right one it keeps the
        # printer's usual grouping of an equal-precedence right operand
        (_or(_not(_and(_A, _B)), _C), "x !== y || x === z || y === z"),
        (_or(_C, _not(_and(_A, _B))), "y === z || (x !== y || x === z)"),
    ],
)
def test_a_flipped_negation_is_grouped_by_its_printed_form(expression, expected):
    assert _print(expression) == expected


def test_double_negation_keeps_the_value():
    """`!!((A && B) || C)`: the inner `!` flips to `(P || Q) && R`; the outer one
    must negate all of it."""
    expression = _not(_not(_or(_and(_A, _B), _C)))

    assert _print(expression) == "!((x !== y || x === z) && y !== z)"


def test_a_negation_that_does_not_flip_keeps_its_parentheses():
    a, b = Identifier("a"), Identifier("b")

    assert _print(_not(_and(a, b))) == "!(a && b)"
    assert _print(_and(_not(_and(a, b)), Identifier("c"))) == "!(a && b) && c"


# ----------------------------------------------------------------------------------------------------
# printer_property_names_that_are_not_identifiers
#
# A static property whose name is not an identifier prints in brackets (`param1["@@iterator"]`, 96/775).
#
# Hermes (and the Babel helpers compiled with it) read `@@iterator` and `@@nativeEmitterSubscription@@`; printed as
# `param1.@@iterator` the output did not parse (11 files in 96 and 98). A private name (`#x`) keeps its dot form.
# ----------------------------------------------------------------------------------------------------

def _print_2(name, optional=False):
    return ExpressionPrinter().visit(MemberExpression(Identifier("param1"), Identifier(name), optional=optional))


@pytest.mark.parametrize("name", ["@@iterator", "@@nativeEmitterSubscription@@", "a-b"])
def test_a_name_that_is_not_an_identifier_is_bracketed(name):
    assert _print_2(name) == f'param1["{name}"]'


def test_an_optional_access_keeps_its_question_mark():
    assert _print_2("@@iterator", optional=True) == 'param1?.["@@iterator"]'


@pytest.mark.parametrize("name", ["props", "_x", "$el", "#__private_2__", "größe"])
def test_an_identifier_keeps_the_dot(name):
    assert _print_2(name) == f"param1.{name}"


# ----------------------------------------------------------------------------------------------------
# reserved_words_are_not_function_names
#
# A function named like a reserved word gets a trailing underscore (`return_`, `in_`; 30 files in 96 and 98).
#
# Class methods called `return`, `delete`, `catch`, `in`, `with` compile to functions of that name; printed as is,
# `function delete(...)` and `{ "return": return }` do not parse. 96/142 builds an iterator object from two such
# closures.
# ----------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("name", ["return", "delete", "catch", "in", "with", "typeof", "static", "yield"])
def test_a_reserved_word_gets_an_underscore(name):
    assert to_js_identifier(name) == f"{name}_"


@pytest.mark.parametrize("name", ["next", "Return", "returns", "of", "get", "async", "$delete"])
def test_other_names_are_untouched(name):
    assert to_js_identifier(name) == name


def test_a_closure_named_return_is_read_through_its_safe_name():
    hasm = (_DATA / "closure_named_after_a_reserved_word_96_142.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert '"return": return_ }' in out
    assert ": return }" not in out


# ----------------------------------------------------------------------------------------------------
# split_output_file
#
# Tests `scripts/split_output_file.py`'s `FUNCTION_HEADER_RE`.
#
# Regression test for a pre-existing bug: the regex required a function
# header line to start with `[Function`, but real hermes-dec output (and
# `hermes_disassembler.emit.HasmWriter`'s output, built to match it)
# actually prefixes that line with `=> ` - confirmed against
# `apps/demo/fixtures/96/sections/section_15042.hasm`, a real hermes-dec
# fixture already committed in this repo. Before the fix, every function
# in a hermes-dec dump fell back to anonymous `section_N` naming instead
# of the descriptive `function_N_name` the code is clearly meant to
# produce (`Section.base_filename()`) - visible in that same fixture
# file's own name, `section_15042.hasm` rather than
# `function_15042_runAllTests.hasm`.
# ----------------------------------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE = REPO_ROOT / "apps" / "demo" / "fixtures" / "96" / "sections" / "function_15042_runAllTests.hasm"


@pytest.fixture(scope="module")
def split_output_file():
    # scripts_dir = str(REPO_ROOT / "scripts")
    # if scripts_dir not in sys.path:
    #     sys.path.insert(0, scripts_dir)
    # import split_output_file as split_output_file  # noqa: PLC0415
    import scripts.split_output_file as split_output_file

    return split_output_file


def test_matches_real_hermes_dec_prefixed_line(split_output_file):
    if not FIXTURE.is_file():
        pytest.skip(f"fixture not found: {FIXTURE}")
    first_line = FIXTURE.read_text().splitlines()[1]  # line 0 is a leading blank line, see fixture
    assert first_line.startswith("=> [Function")

    match = split_output_file.FUNCTION_HEADER_RE.match(first_line)
    assert match is not None
    assert match.group("number") == "15042"
    assert match.group("name") == "runAllTests"


def test_still_matches_bare_form_without_prefix(split_output_file):
    """Backward compatibility: a line with no '=> ' prefix must still match."""
    match = split_output_file.FUNCTION_HEADER_RE.match('[Function #7 "foo" of 10 bytes]')
    assert match is not None
    assert match.group("number") == "7"
    assert match.group("name") == "foo"


def test_section_is_recognized_as_a_function(split_output_file, tmp_path):
    """
    End-to-end: a hermes-dec-style dump containing an '=> [Function...'
    line, split via the real iter_sections(), is recognized as a
    function section (not an anonymous one) and named accordingly.
    """
    text = (
        '=> [Function #3 "clear" of 5 bytes]: 1 params, frame size=1, '
        "strict=0, exc handler=0, debug info=0  @ offset 0x00000000\n"
        "\n"
        "Bytecode listing:\n"
        "\n"
        "==> 00000000: <Ret>: <Reg8: 0>\n"
    )
    hasm_path = tmp_path / "output.hasm"
    hasm_path.write_text(text)

    sections = list(split_output_file.iter_sections(hasm_path, split_output_file.DEFAULT_SEPARATOR))
    assert len(sections) == 1
    assert sections[0].is_function
    assert sections[0].base_filename() == "function_3_clear"


# ----------------------------------------------------------------------------------------------------
# super_call_window
#
# hermes-98 `super(...)` / `new` plumbing: `CallWithNewTarget`, the `SelectObject`
# that follows it, and the dead `CreateThisForNew` that precedes a `Construct`.
#
# Small hand-written sections, same shape as `test_slot_and_define_folding.py`.
# The layouts mirror real functions of the hermes-98 test bundle
# (`CustomEvent`, `createInstance`), where the old output was, respectively,
# `Reflect.construct(r2, [r-1, r0, r1], new.target)` followed by
# `CreateThisForSuper(r2)[r1]`, and a dead `r2 = CreateThisForNew(r1)` before
# `return new r1[3]()`.
# ----------------------------------------------------------------------------------------------------

def _section(*instructions: str) -> str:
    body = "\n".join(f"==> {i * 4:08x}: {text}" for i, text in enumerate(instructions))

    return (
            '\n=> [Function #1 "f" of 99 bytes]: 3 params, frame size=20, strict=1, exc handler=0, '
            "debug info=0  @ offset 0x00000000\n\nBytecode listing:\n\n" + body + "\n\n"
    )


def _out(*instructions: str) -> str:
    out = Decompiler.render(Decompiler.build_context(_section(*instructions), 1), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


# `super(param1, param2)`: the window is [this, arg1, arg2] = r8, r7, r6, with
# `this` copied from CreateThisForSuper's register (r3) by a Mov.
_SUPER_PRELUDE = (
    "<GetParentEnvironment>: <Reg8: 2, UInt8: 0>",
    "<GetNewTarget>: <Reg8: 5>",
    "<CreateThisForSuper>: <Reg8: 3, Reg8: 2, Reg8: 5, UInt8: 0>",
    "<LoadParam>: <Reg8: 7, UInt8: 1>",
    "<Mov>: <Reg8: 8, Reg8: 3>",
    "<LoadParam>: <Reg8: 6, UInt8: 2>",
    "<CallWithNewTarget>: <Reg8: 1, Reg8: 2, Reg8: 5, UInt8: 3>",
)


def test_super_call_window_is_read_from_the_top_of_the_frame():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    # Not relative to the callee register (r2): that gave `[r-1, r0, r1]`.
    assert "Reflect.construct(r2, [param1, param2], new.target)" in out.replace("getParentEnvironment(0)", "r2")
    assert "r-1" not in out


def test_the_this_placeholder_never_reaches_the_output():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    assert "CreateThisForSuper" not in out


def test_select_object_after_super_is_an_alias_not_a_computed_member():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 1>")

    assert "return r1;" in out
    # `SelectObject r1, r3, r1` is a no-op on the register: no `r1 = r1`.
    assert "r1 = r1" not in out


def test_select_object_into_another_register_is_a_plain_alias():
    out = _out(*_SUPER_PRELUDE, "<SelectObject>: <Reg8: 4, Reg8: 3, Reg8: 1>", "<Ret>: <Reg8: 4>")

    # r4 is just the super call's result, so the return reads it directly -
    # not `CreateThisForSuper(r2)[r1]`.
    assert "return r1;" in out
    assert "CreateThisForSuper" not in out


def test_super_call_is_not_moved_past_statements_between_it_and_select_object():
    out = _out(
        *_SUPER_PRELUDE,
        "<LoadConstString>: <Reg8: 9, string_id: 6>  # String: 'after-super' (String)",
        "<PutByIdStrict>: <Reg8: 9, Reg8: 9, UInt8: 0, string_id: 7>  # String: 'p' (Identifier)",
        "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    # Folding the call into the SelectObject would print it after these.
    assert out.index("Reflect.construct") < out.index("after-super")


def test_super_call_without_arguments_has_an_empty_argument_list():
    out = _out(
        "<GetParentEnvironment>: <Reg8: 2, UInt8: 0>",
        "<GetNewTarget>: <Reg8: 5>",
        "<CreateThisForSuper>: <Reg8: 3, Reg8: 2, Reg8: 5, UInt8: 0>",
        "<Mov>: <Reg8: 8, Reg8: 3>",
        "<CallWithNewTarget>: <Reg8: 1, Reg8: 2, Reg8: 5, UInt8: 1>",
        "<SelectObject>: <Reg8: 1, Reg8: 3, Reg8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    assert "[]" in out
    assert "CreateThisForSuper" not in out


def test_new_expression_drops_the_dead_create_this_for_new():
    # hermes-98 allocates `this` in r2 but hands Construct an unrelated,
    # never-written `this` slot (r3), so r2 used to print as a dead line.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 2, Reg8: 1, UInt8: 0>",
        "<LoadConstUndefined>: <Reg8: 3>",
        "<Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>",
        "<Ret>: <Reg8: 1>",
    )

    assert "return new r1[3]();" in out
    assert "CreateThisForNew" not in out


def test_a_create_this_for_new_from_another_constructor_is_left_alone():
    # Only the placeholder made from THIS `new`'s constructor register (r1)
    # is consumed; an unrelated one (r5, made from r4) must not be swallowed.
    # The never-written `this` slot is r6, the highest register of the window.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 4, Reg8: 1, UInt8: 4>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 5, Reg8: 4, UInt8: 0>",
        "<CreateThisForNew>: <Reg8: 2, Reg8: 1, UInt8: 0>",
        "<LoadConstUndefined>: <Reg8: 6>",
        "<Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>",
        "<PutByIdStrict>: <Reg8: 1, Reg8: 5, UInt8: 0, string_id: 7>  # String: 'p' (Identifier)",
        "<Ret>: <Reg8: 1>",
    )

    # r5 is read afterwards, so it is not a dead placeholder: it keeps its
    # definition (naming the constructor it came from, r4 = r1[4]) and the
    # reader names the register.
    assert "r5 = CreateThisForNew(r1[4])" in out
    assert "r1.p = r5" in out
    assert out.count("CreateThisForNew") == 1


def test_a_placeholder_nothing_reads_is_dropped():
    # `r3 = CreateThisForNew(r1)` in front of a `typeof` guard, never read.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 3, Reg8: 1, UInt8: 0>",
        "<Ret>: <Reg8: 1>",
    )

    assert "CreateThisForNew" not in out


def test_a_placeholder_with_several_readers_is_one_object_not_one_per_use():
    # An inlined `_classCallCheck`-style constructor body: the fresh object is
    # written to twice. Inlining the placeholder at each use printed
    # `CreateThisForNew(r1[3])._a = 0; CreateThisForNew(r1[3])._b = 0`.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 1, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 1, Reg8: 1, UInt8: 3>",
        "<CreateThisForNew>: <Reg8: 7, Reg8: 1, UInt8: 0>",
        "<LoadConstZero>: <Reg8: 0>",
        "<PutByIdStrict>: <Reg8: 7, Reg8: 0, UInt8: 0, string_id: 6>  # String: '_a' (Identifier)",
        "<PutByIdStrict>: <Reg8: 7, Reg8: 0, UInt8: 1, string_id: 7>  # String: '_b' (Identifier)",
        "<Ret>: <Reg8: 7>",
    )

    assert out.count("CreateThisForNew") == 1
    assert "r7._a = 0" in out and "r7._b = 0" in out


def test_default_derived_constructor_forwards_arguments():
    # hermes-98 implicit `constructor(...args) { super(...args) }`.
    out = _out(
        "<GetParentEnvironment>: <Reg8: 0, UInt8: 0>",
        "<LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 2>",
        "<LoadParentNoTraps>: <Reg8: 2, Reg8: 0>",
        "<GetNewTarget>: <Reg8: 1>",
        "<CreateThisForSuper>: <Reg8: 4, Reg8: 2, Reg8: 1, UInt8: 0>",
        "<Mov>: <Reg8: 5, Reg8: 2>",
        "<Mov>: <Reg8: 3, Reg8: 1>",
        "<CallBuiltin>: <Reg8: 0, UInt8: 50, UInt8: 4>  # Built-in function: [#50 applyArguments]",
        "<Ret>: <Reg8: 0>",
    )

    assert "Reflect.construct(r2, arguments, new.target)" in out
    assert "CreateThisForSuper" not in out
    assert "applyArguments" not in out


# ----------------------------------------------------------------------------------------------------
# this_placeholder_copied_before_a_throw
#
# A `CreateThisForNew` placeholder and its copy in a block that throws print nothing (98/3382 `normalizeRootMargin`).
#
# `new SyntaxError(r13)` folds the construction, but the compiler had allocated the `this` object in `r8` and copied it
# to `r14` right before the throw. `DeadThisPlaceholderPass` only dropped a placeholder whose register is mentioned
# nowhere else in the function, and `r8` is reused, so the line printed as `r8 = CreateThisForNew(r9)` reading `r9`,
# which the folded `new` had already consumed.
# ----------------------------------------------------------------------------------------------------

def _render_5() -> str:
    hasm = (_DATA / "this_placeholder_copied_before_a_throw_98_3382.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 3382, strict=False), verbose=False, raw=False)


def test_the_placeholder_and_its_copy_are_gone():
    out = _render_5()

    assert "throw new SyntaxError(r13);" in out
    assert "CreateThisForNew(r9)" not in out
    assert "r14 = r8;" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_5(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
