"""
F-10 (non-return targets): `if (!a || b) { A } END` where the second test's setup
loads a constant that END reads too.

    96/9112  `parseTranslateX`: `len !== 1` jumps to `r0 = []`, `isLength(x) ||
             isPercent(x)` jumps to the object build, which indexes with the very
             register (`r1 = 0`) the tests loaded. The tests take the constant and
             END gets its own load on the edge into it, so the whole thing is one
             `if (len === 1 && (a || b)) { ... } else { r0 = [] }`.
    96/4063  `handler`: `if (c === -1 && this.n !== 0)` then `if (c === -1)`; the
             crossed form read an unassigned register for `this.n !== 0`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_constant_both_tests_and_the_end_block_read_is_loaded_again_for_the_end_block():
    out = _render("crossed_condition_with_constant_96_9112.hasm", 9112)

    assert "goto" not in out
    assert (
        "if (r1 === 1 && (getEnvironment(0)[0].call(undefined, param1[0]) || "
        "getEnvironment(0)[1].call(undefined, param1[0]))) {"
    ) in out
    # END indexes with the register the load wrote, so the load is there.
    assert out.index("r1 = 0;") < out.index("param1[r1]")
    assert "} else {\n        r0 = [];" in out


def test_the_second_exit_of_a_crossed_pair_reads_the_property_not_a_dead_register():
    out = _render("crossed_condition_two_exits_96_4063.hasm", 4063)

    assert "if (param2 === -1 && this.utf8BytesNeeded !== 0) {" in out
    assert "} else if (param2 === -1) {" in out
    assert "r5 !== 0" not in out
