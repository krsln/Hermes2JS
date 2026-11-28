"""`switch` recovery: cases, fall-through, defaults, joins, shared labels.

Merged from: test_case_exemption_subject, test_dropped_case_jump, test_string_switch, test_switch_case_fallthrough, test_switch_default_is_the_code_behind_it, test_switch_exit_trampoline, test_switch_join_after_a_throwing_default, test_switch_shared_labels.
"""

import shutil
import subprocess
from hermes_disassembler.format.BytecodeFileHeader import BytecodeFileHeader
from hermes_disassembler.format.FunctionHeader import parse_function_headers
from hermes_disassembler.format.FunctionHeaderOverflow import resolve_overflowed_headers
from hermes_disassembler.format.Opcode import decode_function
from hermes_disassembler.format.StringTable import StringTable
from hermes_disassembler.format.SwitchTable import resolve_string_switch_entries
from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler


# ----------------------------------------------------------------------------------------------------
# case_exemption_subject
#
# Two constant comparisons are a `case` chain only when they test the same value (96/956 `replacer`).
#
#     if (typeof v !== "object") return v;   if (v === null) return v;   ...rest
#
# Both jump to one `return`. The `null` test sits beside a constant comparison, which made
# `_absorb_residual_conditional` leave the shared target to `SwitchStructurer`, but the two tests
# look at different values (`typeof v` and `v`): no `switch` comes out of them and the `null`
# path lost its `return` (it fell off the end as `undefined`).
# ----------------------------------------------------------------------------------------------------

_DATA = Path(__file__).parent / "data"


def test_a_null_test_beside_a_typeof_test_keeps_its_exit():
    hasm = (_DATA / "two_constant_tests_one_return_96_956.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 956, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r4 === null) {" in out


# ----------------------------------------------------------------------------------------------------
# dropped_case_jump
#
# A `case` test left to the `switch` pass keeps its jump when no `switch` comes out of it (F-179).
#
# `tag === 27` and `tag === 5` jump to one body. `_absorb_residual_conditional` dropped the second jump into the
# sibling arm on the promise that `SwitchStructurer` builds a `switch`; with two bodies behind a residual that is
# not a pure chain it does not, and the path was lost: `if (27 === t) { X } else if (5 !== t) { ... }` ran nothing
# for `5`. The dropped jump is recorded and `restore_dropped_case_jumps` makes it `if (27 === t || 5 === t) { X }`
# when no `switch` took the chain.
#
#     98/2633  `commitLayoutEffectOnFiber`
#     98/2628  `safelyAttachRef`: 26 and 27 share the body
# ----------------------------------------------------------------------------------------------------

def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_both_tests_reach_the_shared_body():
    out = _render("dropped_case_jump_98_2633.hasm", 2633)

    # the dispatch on the fiber tag now comes out as a `switch` (its default jumps to the code behind it, which
    # used to leave the jump table raw): the labels `5`, `26` and `27` share one body, none is an `else if`
    assert "        case 5:\n        case 26:\n        case 27:\n" in out
    assert "5 !== r9" not in out


def test_the_second_label_is_not_an_else_if():
    out = _render("dropped_case_jump_98_2628.hasm", 2628)

    # the third label (`5`) joins the same condition: it was a `goto label_73` behind the first two (F-180)
    assert "if (26 === r6 || 27 === r6 || 5 === r6) {" in out
    assert "goto" not in out
    assert "27 !== r6" not in out


# ----------------------------------------------------------------------------------------------------
# string_switch
#
# `StringSwitchImm` comes out as a `switch` (F-219).
#
# Its case strings and targets sit in a table of the bytecode file that real hermes-dec never prints, so the decompiler
# used to get a switch with no cases and printed every case body in a row. The disassembler now writes
# `# String switch table: [["to top", "00000072"], ...]` and the decompiler reads it.
#
#     98/2184  `getDirectionForKeyword`: twelve strings on eight bodies (two spellings per corner)
#     98/2140  `getNativeComponentAttributes`: the cases jump to the `if` behind the switch, which the structurer had
#              built before, so the test block of that `if` is the merge
# ----------------------------------------------------------------------------------------------------

_BUNDLE = Path(__file__).resolve().parent.parent / "apps" / "testy" / "98" / "index.android.bundle"




def test_the_table_is_read_from_the_bundle():
    if not _BUNDLE.is_file():
        pytest.skip(f"fixture not found: {_BUNDLE}")

    data = _BUNDLE.read_bytes()
    header = BytecodeFileHeader.parse(data)
    table = StringTable.parse(data, header)
    resolved = resolve_overflowed_headers(data, header, parse_function_headers(data, header))

    for entry in resolved:
        for instruction in decode_function(data, entry.offset, entry.bytecode_size_in_bytes, header.version):
            if instruction.name == "StringSwitchImm" and instruction.operands == (1, 3, 86, 82, 12):
                cases = [(table.resolve(s), target - entry.offset) for s, target in
                         resolve_string_switch_entries(data, instruction)]

                assert len(cases) == 12
                assert cases[0] == ("to top", 0x72)
                assert dict(cases)["to top right"] == dict(cases)["to right top"] == 0x52
                return

    raise AssertionError("the StringSwitchImm of 98/2184 was not found")


def test_the_cases_are_strings_and_spellings_share_a_body():
    out = _render("string_switch_98_2184.hasm", 2184)

    assert "switch (r1) {" in out
    assert '            case "to bottom left":\n            case "to left bottom":\n' in out
    assert '            case "to top":\n' in out
    assert "Raw TerminatorSwitch" not in out
    assert "goto" not in out


def test_a_switch_whose_merge_is_the_test_of_an_if():
    out = _render("string_switch_merge_98_2140.hasm", 2140)

    assert 'case "CGColor":' in out
    assert "goto" not in out


# ----------------------------------------------------------------------------------------------------
# switch_case_fallthrough
#
# A `case` whose code runs on into the next one prints no `break` (F-177).
#
# Hermes lays `case 5: case 26: case 27: if (!a) f();` out right in front of `case 6: g(); return`, and the
# first body falls into the second. The printer ended every case body with an `break;` it added itself, so
# `g()` was skipped on those three values: 96/2103 `commitDeletionEffectsOnFiber` dropped the
# `recursivelyTraverseDeletionEffects` call. A jump-table body that flows into the next case's entry is
# marked `falls_through` (only when that case is printed right after it) and the safety `break` is left out.
#
#     96/2103   cases 5, 26, 27 -> case 6
#     96/2607   the same function in the other bundle layout: cases 5, 26 -> case 6
# ----------------------------------------------------------------------------------------------------

def test_the_shared_labels_run_on_into_case_6():
    out = _render("switch_case_fallthrough_96_2103.hasm", 2103)

    assert "goto" not in out
    start = out.index("        case 5:")
    end = out.index("        case 6:")
    assert "break;" not in out[start:end]
    assert "r1[429].call(undefined, param3, param2);" in out[start:end]


def test_the_same_shape_in_another_function():
    out = _render("switch_case_fallthrough_96_2607.hasm", 2607)

    start = out.index("        case 5:")
    end = out.index("        case 6:")
    assert "break;" not in out[start:end]


# ----------------------------------------------------------------------------------------------------
# switch_default_is_the_code_behind_it
#
# A jump table whose default target is the code BEHIND the switch builds a `switch` followed by that code (F-321,
# 98/2672 `unwindUnitOfWork`).
#
#     do { switch (fiber.tag) { case 24: ...; break; ... case 19: ... } <test of the completed work> ... } while (r6)
#
# Every arm jumps to that code and so does the default. Its test (`if (completedWork !== null)`) had become an `if`
# without a `source_block` (`LoopBreakStructurer` consumes its branch), so the switch did not find it as its default
# item, took it for the last case's body and the other arms' jumps into it stayed `goto label_1119`.
# ----------------------------------------------------------------------------------------------------

def _render_2() -> str:
    hasm = (_DATA / "switch_default_is_the_code_behind_it_98_2672.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 2672, strict=False), verbose=False, raw=False)


def test_the_code_behind_the_switch_follows_it():
    out = _render_2()

    assert "goto label_" not in out
    assert "\n        }\n        if (null !== r10) {\n" in out
    assert "case 19:" not in out.split("if (null !== r10) {")[1]


@pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")
def test_the_output_parses(tmp_path: Path):
    path = tmp_path / "out.js"
    path.write_text(_render_2(), encoding="utf-8")

    done = subprocess.run(["node", "--check", str(path)], capture_output=True, text=True)

    assert done.returncode == 0, done.stderr


# ----------------------------------------------------------------------------------------------------
# switch_exit_trampoline
#
# A `default:` arm that ends in its own `jmp loop-head` leaves the switch like the code behind it does (98/2204).
#
# `parseDropShadowString`: the loop body is `if (...) {...} else { switch (...) {...} }`. Cases 0 and 1 fall into the
# code behind the switch, which is an empty block `jmp loop-head` (0xd7); the `default:` arm ends in ANOTHER empty
# `jmp loop-head` (0xb7). `RedundantJumpRegionPass._reaches_exit` only followed empty blocks that fall on into the exit,
# so the default arm kept `goto label_183; break;`.
# ----------------------------------------------------------------------------------------------------

def test_the_default_arm_ends_in_a_break():
    hasm = (_DATA / "switch_exit_trampoline_98_2204.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2204, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r13 = r15 + 1;\n                    break;\n            }" in code


# ----------------------------------------------------------------------------------------------------
# switch_join_after_a_throwing_default
#
# The code behind a jump-table `switch` whose `default:` can `throw` was printed as the body of the empty cases
# (98/2632 `commitBeforeMutationEffects`).
#
# A `throw` in the default arm leaves the switch header without an immediate post-dominator, so the join (`r10 =
# r12.sibling ...`) looked like one more case body: `case 3: case 4: ...` held it, `case 0`/`case 1` ended in a
# `break` that skipped it, and the `try` in `case 1` kept a `goto` into it. The join is the last jump table target
# that the other arms jump into: it follows the switch.
# ----------------------------------------------------------------------------------------------------

def _render_3() -> str:
    hasm = (_DATA / "switch_join_after_a_throwing_default_98_2632.hasm").read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_goto_is_left():
    assert "goto label_" not in _render_3()


def test_the_join_runs_after_the_switch_not_inside_the_empty_cases():
    out = _render_3()
    empty_cases = out.split("case 3:")[1].split("default:")[0]

    assert "sibling" not in empty_cases
    assert out.index("r12.sibling") > out.index("default:")


# ----------------------------------------------------------------------------------------------------
# switch_shared_labels
#
# F-10 (non-return targets): three or more case labels sharing one body.
#
#     96/7527  `encoderForArrayFormat`: "comma", "separator" and "bracket-separator"
#              all jump to the same block. The last test used to stay behind as
#              `if ("bracket-separator" === r3) goto label_70;` inside `default`.
# ----------------------------------------------------------------------------------------------------

def _render_4(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_every_label_of_a_shared_body_joins_one_case_group():
    out = _render_4("switch_three_shared_labels_96_7527.hasm", 7527)

    assert "goto" not in out
    assert 'case "comma":\n        case "separator":\n        case "bracket-separator":' in out
    assert "default:\n            return function_7536;" in out


def test_labels_after_an_inverted_one_continue_the_same_switch():
    """96/4122 `defaultPort`: `"https"`/`"wss"` share `return 443`.

    The `"ws"` test is inverted, which pushed the rest of the chain into `default`;
    on its own that tail has one body and stayed `if`s, and the `"wss"` jump to
    `return 443` was dropped. It now continues the outer `switch`.
    """
    out = _render_4("switch_nested_chain_default_96_4122.hasm", 4122)

    assert "goto" not in out
    assert 'case "https":\n        case "wss":\n            return 443;' in out
    assert "default:\n            return null;" in out


def test_a_chain_with_a_return_behind_it_keeps_the_label_of_its_shared_body():
    """96/777 `_unsupportedIterableToArray`: `"Map"` and `"Set"` share `Array.from`.

    With the return copied into each path the `"Set"` test is inverted and the rest of
    the chain (`"Arguments"`, then the default) is followed by the return. That tail
    kept the chain from becoming a `switch`, and the `"Set"` jump was dropped (a
    `Set` came out as `undefined`). The return now follows the `switch`.
    """
    out = _render_4("switch_labels_then_tail_96_777.hasm", 777)

    assert "goto" not in out
    assert 'case "Map":\n                case "Set":\n                    r0 = Array.from(param1);\n                    return r0;' in out
    assert '"Set" !==' not in out
