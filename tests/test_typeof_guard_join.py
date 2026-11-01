"""The code a `typeof` test jumps to is the join when the arm's own test falls into it (F-183).

    if (typeof x !== "object") goto T;
    ...; if (r != null) return r;          // taken edge: a lone `return`; the fall goes on into T
    T: <the next test>

`_DominanceIfBuilder` kept a constant comparison (`typeof x ...`) away from the rule that makes the branch target
the join (a `case` chain needs `has_else` at every link), so `T` stayed the `else` arm and the fall of the arm's
test went to `return r` instead of into `T`: `if (r3 != null) goto label_86; return param1.key;` returned the key
where the bytecode goes on to the second `typeof`. A `typeof` kind test is never a `case` label, so it now takes
the rule when the arm's test is of anything else.

Only `typeof` tests: widening it to every constant comparison turned a `return` copy into an assignment plus a
shared `return` for 98/6630 `getInitialURL` (`IfTailMergeRegionPass` hoisted the `return` of a block a guard
still jumped to) and was dropped.

    98/4239  `keyExtractor`
    98/2147  `processColor`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_second_type_test_follows_the_first_one():
    out = _render("typeof_guard_join_98_4239.hasm", 4239)

    assert "goto" not in out
    assert out.count('if (typeof param1 === "object") {') == 2
    assert out.count("return param1.key;") == 1
    assert out.index("return param1.key;") < out.index("return param1.id;")
    assert out.rstrip().endswith("return r3;\n}")


def test_a_null_result_goes_on_to_the_number_test():
    out = _render("typeof_guard_join_98_2147.hasm", 2147)

    assert "goto" not in out
    assert "if (r6 != null) {\n                    return r6;\n                }" in out
    assert out.index("return r6;") < out.index('if (typeof r7 !== "number") {')
