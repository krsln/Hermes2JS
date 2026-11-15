"""A shared tail the test skips by jumping to the block behind it (F-186).

    if (!a) goto T;                 // jumper
    if (c) goto B;                  // the test: its fall-through is T, its jump is the block right behind T
    T: r0 = +x; jmp END
    B: r0 = y / 100                 // falls into END
    END: ...

`SharedTailDuplicationCfgPass` gave the test a private copy of `T` only when the test jumped straight to `END`.
Here it jumps to `B`, which runs on into `END`: the same two-way meeting, with `T` as the test's own `else`. Left as
it was, the structurer gave `T` to the jumper and printed `if (r4) goto label_42; r2 = -1; ... slice`, which runs
the `slice` path for a string that does not end in `%`.

Only on the rungs that already copy regions (`regions=True`): on the first ones it changed 96/2264 `pop`, which the
plain skip had solved.

    98/8059  `processPercentage`   98/11896 `parseScale`   96/2264 `pop` (must stay goto-free)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_string_without_a_percent_sign_is_converted_not_sliced():
    out = _render("shared_tail_other_way_98_8059.hasm", 8059)

    assert "goto" not in out
    assert "if (r4) {\n            r2 = -1;" in out
    assert "} else {\n            r0 = +param1;\n        }" in out
    assert out.count("r0 = +param1;") == 2


def test_an_empty_list_is_the_else_of_the_validity_test():
    out = _render("shared_tail_other_way_98_11896.hasm", 11896)

    assert "goto" not in out
    # With the closure-environment read pure (F-228) the guard and the validity test are ONE condition, and the
    # empty list is the `else` of that condition (it used to be two `r7 = [];` around a nested `if`).
    assert 'if (r7 === 1 && __getClosureEnvironment__(r3[1])[0].call(undefined, r5[0])) {' in out
    assert "} else {\n                r7 = [];\n            }" in out


def test_a_loop_the_plain_skip_solved_keeps_its_shape():
    out = _render("shared_tail_other_way_96_2264.hasm", 2264)

    assert "goto" not in out
