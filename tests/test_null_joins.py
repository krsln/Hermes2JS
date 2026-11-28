"""A `null` written on some paths of a join, read by members, conditions and tests (F-342 to F-355).

Merged from: test_member_of_a_null_written_on_some_paths, test_null_after_a_member_read_default, test_null_default_of_a_tested_register, test_null_default_read_after_the_join, test_null_exit_after_undefined_test, test_null_merge_in_a_branch_test, test_null_met_by_two_jumps, test_null_on_one_arm_of_three_paths, test_null_written_by_a_catch_handler, test_null_written_in_an_arm_read_by_a_condition.
"""

import shutil
import subprocess
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# member_of_a_null_written_on_some_paths
#
# A member read or store whose base register holds `null` on only some paths into a join names the register (96/998 `mapIntoArray`).
#
# `switch (typeof child) { case "undefined": r14 = null; case "boolean": r14 = null }` writes `null` on two paths and
# leaves the child in the register on the third; the loop's `r11[r7]` printed as `null[r7]`, which always throws.
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "member_of_a_null_written_on_some_paths_96_998.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 998, strict=False), verbose=False, raw=False)


def test_the_base_is_the_register():
    out = _render()

    assert "r15 = r11[r7];" in out
    assert "null[" not in out
    assert "null." not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# null_after_a_member_read_default
#
# A `null` that defaults a member read is read as the register after the join (98/5017 `Asset`, 96/13091).
#
# `r6 = x.y; if (r6 == null) r6 = null; ...; if (r6)`: the test after the `if` printed the arm's `null` (`if (null)`),
# although the register holds the member value on the other path.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "null_after_a_member_read_default_98_5017.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_test_reads_the_register():
    out = _render_2()

    assert "if (r6) {" in out
    assert "if (null) {" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_2(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_2(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_default_of_a_tested_register
#
# A `null` default of the register the jump just tested is read as the register (96/553, 98/12637 `TransformStream`).
#
# `if (r9 === undefined) r9 = null; ...; r14 = r9; if (r14 != null)`: the reads after the `if` printed the arm's
# `null` (`if (null != null)`), so every `transformer.cancel` / `.flush` / `.start` read was dead code.
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    hasm = (_DATA / "null_default_of_a_tested_register_96_553.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_reads_name_the_register():
    out = _render_3()

    assert "null != r9" in out
    assert "null != null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_3(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_3(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_default_read_after_the_join
#
# A parameter's `null` default is read as the register after the join (96/998 `mapIntoArray`, 98/3523 `parseURL`).
#
# `LoadParam r11; if (r11 === undefined) r11 = null; ...; read r11`: the read after the `if` was the inlined `null`
# (`!null || r11.key !== r3.key`), although the register holds the parameter on the other path.
# ----------------------------------------------------------------------------------------------------

def _render_4() -> str:
    hasm = (_DATA / "null_default_read_after_the_join_96_998.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_read_names_the_register():
    out = _render_4()

    assert "(!r11 || r11.key !== r3.key)" in out
    assert "!null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_4(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_4(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_exit_after_undefined_test
#
# `if (a === undefined) goto T; r0 = null; if (a === null) goto T;` where T is `return r0`
# (98/7358 `collectSpans`).
#
# The `null` test is followed by an unrelated comparison (`length === 0`) that jumps to the same
# kind of exit. That one used to count as a second `case` body, so the shared target was left to
# `SwitchStructurer` and the jump was dropped: `null` fell off the end and returned `undefined`
# instead of `null`. Only tests on the SAME value make a `case` chain.
# ----------------------------------------------------------------------------------------------------

def _render_5(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_null_argument_still_returns_null():
    out = _render_5("null_test_after_undefined_test_98_7358.hasm", 7358)

    assert "goto" not in out
    assert out.count("return null;") >= 2
    assert "case null:\n            return null;" in out or "param1 === null" in out


# ----------------------------------------------------------------------------------------------------
# null_merge_in_a_branch_test
#
# A branch test reads the register that merges `null` with other values (98/2151 `normalizeColor`, 98/2671).
#
# `switch (name) { case ...: r7 = 0xff0000ff; ... default: r7 = null }` and then `if (r7 != null)`: the test inlined the
# `null` of the last write (`null != null`), so the whole `if` was constant.
# ----------------------------------------------------------------------------------------------------

def _render_6() -> str:
    hasm = (_DATA / "null_merge_in_a_branch_test_98_2151.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_test_reads_the_register_2():
    out = _render_6()

    assert "if (r7 != null) {" in out
    assert "null != null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_5(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_6(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_met_by_two_jumps
#
# A `null` that two jumps land on is read as the register, and the copy on the other path prints (98/2044 `mapIntoArray`).
#
# `Mov r14, p; <boolean test> -> L; r14 = null; L:` entered from `undefined` too. The read after the span saw only the
# `null` (`if (null !== null)`), and the copy `r14 = param1` was printed nowhere, so the default path left `r14` unset.
# ----------------------------------------------------------------------------------------------------

def _render_7() -> str:
    hasm = (_DATA / "null_met_by_two_jumps_98_2044.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_read_names_the_register_2():
    out = _render_7()

    assert "null !== r14" in out
    assert "if (null !== null)" not in out


def test_the_copy_on_the_other_path_prints():
    assert "r14 = param1;" in _render_7()


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_6(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_7(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_on_one_arm_of_three_paths
#
# A `null` written on one arm of a three-path join is read as the register (96/12871 `Color`).
#
# `r3 = p; if (p) { r3 = p; if (p in table) r3 = null }; <read r3>`: the read sees `p`, `null` or the falsy `p`. The
# nested-join guard named the register only for identifiers and binary expressions, so the constant was inlined:
# `!r3 || null in table`, `if (!null) model = "rgb"`.
# ----------------------------------------------------------------------------------------------------

def _render_8() -> str:
    hasm = (_DATA / "null_on_one_arm_of_three_paths_96_12871.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_reads_name_the_register_2():
    out = _render_8()

    assert "!r3 || r3 in r4[2]" in out
    assert "if (!r3) {" in out
    assert "null in " not in out
    assert "!null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_7(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_8(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_written_by_a_catch_handler
#
# A `null` written by a `catch` handler does not replace the try body's value after the `try` (96/6880, 96/6826).
#
# `try { r1 = requireNativeModule("ExpoGo") } catch { r1 = null }; env[0] = r1`: the store behind the `try` printed
# `env[0] = null`, so the module was thrown away on the path that did not throw.
# ----------------------------------------------------------------------------------------------------

def _render_9() -> str:
    hasm = (_DATA / "null_written_by_a_catch_handler_96_6880.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_store_reads_the_register():
    out = _render_9()

    assert "r2[0] = r1;" in out
    assert "r2[0] = null;" not in out


def test_the_handler_still_assigns_null():
    assert "} catch (caughtException) {\n        r1 = null;\n    }" in _render_9()


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_8(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_9(), encoding="utf-8")

    assert subprocess.run(["node", "--check", str(path)], capture_output=True, text=True).returncode == 0


# ----------------------------------------------------------------------------------------------------
# null_written_in_an_arm_read_by_a_condition
#
# A `null` written in an `if` arm and read by the condition right after it names the register (98/3490 `TextDecoder`).
#
# `r6 = lookup[...]; if (r6 == null) { r6 = null }` and then `r6 === null || r6.name === "replacement"`: the condition
# held the arm's own `null` node and printed `null === null`. The repair looked for the reader of a test at the last
# instruction BEFORE the `if` whose arm wrote the register, which cannot be reached from that write, so it left the
# condition alone. The reader of a test is the last instruction of the region before it.
# ----------------------------------------------------------------------------------------------------

def _render_10() -> str:
    hasm = (_DATA / "null_written_in_an_arm_read_by_a_condition_98_3490.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 3490, strict=False), verbose=False, raw=False)


def test_the_condition_reads_the_register():
    out = _render_10()

    assert 'if (r6 === null || r6.name === "replacement") {' in out
    assert "null === null" not in out


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses_9(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_10(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr
