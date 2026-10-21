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
    assert "0 === r2 || -1 === r0[0]._status" in out


def test_one_call_in_the_second_test_folds_into_the_condition():
    out = _render("call_in_second_test_96_7722.hasm", 7722)

    assert "goto" not in out
    assert "r0[26].call(undefined)" in out
    assert out.count("r0[26]") == 1


def test_value_ternary_that_is_only_tested_folds_into_the_condition():
    """96/12188: `!d || (k in d ? !m.__esModule : d.writable || d.configurable)`.

    The ternary's value goes through a register that only one test reads: the
    diamond becomes the test, so the default descriptor is written once."""
    out = _render("shared_tail_after_ternary_96_12188.hasm", 12188)

    assert "goto" not in out
    assert "if (!r4 || ((\"get\" in r4) ? !param2.__esModule : r4.writable || r4.configurable)) {" in out
    assert out.count('"enumerable": true') == 1


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
    assert "Object.keys(param1.props.jestAnimatedProps.value).length === 0" in out


def test_a_stale_inlined_callee_is_not_folded_into_a_wrong_value():
    """96/9118: the frontend inlines the callee as `r0[0]` while the setup has
    since set `r0 = undefined` (the call's `this`). Folding that read the
    constant (`undefined[0](...)`): the fold must refuse instead."""
    out = _render("parseScaleX_stale_callee_96_9118.hasm", 9118)

    assert "undefined[0]" not in out


def test_function_with_handlers_does_not_get_an_edge_block():
    """98/2917 crashed the dominator pass (`KeyError`): the edge block for a sunk
    join copy was added in a function with exception handlers, whose try ranges
    name blocks the merge had dropped. Such a function keeps the old shape."""
    out = _render("sunk_copy_with_handlers_98_2917.hasm", 2917)

    assert out.strip().startswith("function")


def test_value_chain_that_is_only_tested_folds_into_the_condition():
    """98/2463: `Start || Move || End || Cancel`. The last two are a value (`r5 = End || Cancel`)
    that one test reads; with it folded the chain is a single condition, and the
    comparison with `topTouchMove` is not mistaken for a later definition's value
    (`r6 = param1 === "topTouchMove"`), which an earlier condition cannot read."""
    out = _render("touch_chain_value_tests_98_2463.hasm", 2463)

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
    out = _render("any_of_params_96_4456.hasm", 4456)

    assert "goto" not in out
    assert "if (param1 || param2 || param3 || param4 || param5 || param6) {" in out


def test_second_test_with_its_own_call_keeps_each_callee():
    """98/11891: `len === 1 && (a(x) || b(x))`. The setup of the second call reads the
    environment register that the first call's setup set; once `r2` is re-assigned
    (`r2 = x`) the callee must still name the environment, not `x`."""
    out = _render("parseTranslateX_two_calls_98_11891.hasm", 11891)

    assert "goto" not in out
    assert (
        "r2 === 1 && (getParentEnvironment(0)[0].call(undefined, param1[0])"
        " || getParentEnvironment(0)[1].call(undefined, param1[0]))"
    ) in out


def test_constant_comparison_in_a_plain_chain_is_not_a_case_test():
    """96/150: `... || p < 0 || p === Infinity` - the last link compares with a constant
    but not the value the previous link compared, so it is part of the one condition."""
    out = _render("size_checks_throw_96_150.hasm", 150)

    assert "goto" not in out
    assert "!(r1 || param3 < 0) && param3 !== Infinity" in out
