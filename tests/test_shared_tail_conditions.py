"""
A tail block that one test jumps over and several others jump onto must keep
every one of those tests (the silent drop of 96/652, `_interopDefault`).

Hermes lowers `a && b && c ? x : y` so that the `y` block is reached by the
failing tests' jumps and by the last test's fall-through. Dropping the last
test's branch (`_strip_trailing_jump_to`) or leaving a residual jump to a
sibling arm silently removed a path. The fixes covered here:

- the last test joins the chain (`ShortCircuitConditionCfgPass` crossed form),
  its join copy moving onto the edge to END;
- a lone comparison jumping into the sibling arm is not a `case` test;
- one call in the second test's setup is folded into the condition;
- otherwise the tail is copied for the fall-through (`SharedTailDuplicationCfgPass`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_typeof_polyfill_keeps_every_path():
    out = _render("typeof_polyfill_96_652.hasm", 652)

    assert "goto" not in out
    assert 'typeof Symbol' in out
    assert "param1.constructor !== Symbol" in out
    assert out.count("typeof param1") == 2  # the plain path and the `=== Symbol.prototype` path
    assert "param1 === r2" in out or "param1 === Symbol.prototype" in out


def test_interop_default_is_one_ternary_shape():
    out = _render("interopDefault_96_15102.hasm", 15102)

    assert "goto" not in out
    assert "if (param1 && param1.__esModule)" in out
    assert '"default": param1' in out


def test_large_interop_default_keeps_the_esmodule_test():
    out = _render("interopDefault_large_98_167.hasm", 167)

    assert "goto" not in out
    assert "r3 && r3.__esModule" in out
    assert "r4 = r3;" in out


def test_second_test_with_a_read_keeps_both_values():
    out = _render("lazy_status_96_1003.hasm", 1003)

    assert "goto" not in out
    assert "-1 !== r0[0]._status" in out


def test_one_call_in_the_second_test_folds_into_the_condition():
    out = _render("call_in_second_test_96_7722.hasm", 7722)

    assert "goto" not in out
    assert "r0[26].call(undefined)" in out
    assert out.count("r0[26]") == 1


def test_tail_after_a_value_ternary_keeps_the_ternary_test():
    """96/12188: `!d || (k in d ? !m.__esModule : d.writable || d.configurable)`.

    The tail (the 6-instruction default descriptor) is jumped to by `!d` and
    fallen into by the test of the ternary's value; both keep their exit."""
    out = _render("shared_tail_after_ternary_96_12188.hasm", 12188)

    assert "goto" not in out
    assert "if (r2) {" in out
    assert out.count('"enumerable": true') == 2


def test_call_chain_in_the_second_test_folds_into_the_condition():
    """96/7811: `p === undefined || p === env[0].getId()`; the setup is
    `r0 = env; r1 = r0[0]; r0 = r1.getId()` - the operands of the one call."""
    out = _render("getParent_call_in_second_test_96_7811.hasm", 7811)

    assert "goto" not in out
    assert "param1 === getEnvironment(0)[0].getId()" in out


def test_call_chain_through_one_register_keeps_the_whole_condition():
    """96/11316: `r0 = a.props; r0 = r0.x; r0 = Object.keys(r0.value); r1 = r0.length`."""
    out = _render("compareProps_call_chain_96_11316.hasm", 11316)

    assert "goto" not in out
    assert "Object.keys(param1.props.jestAnimatedProps.value.value).length === 0" in out


def test_a_stale_inlined_callee_is_not_folded_into_a_wrong_value():
    """96/9118: the frontend inlines the callee as `r0[0]` while the setup has
    since set `r0 = undefined` (the call's `this`). Folding that read the
    constant (`undefined[0](...)`): the fold must refuse instead."""
    out = _render("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "undefined[0]" not in out
