"""`if (c) continue;` in a loop with no test and no update of its own (F-200).

    while (true) { r22 = it.next(); if (r22 === undefined) ...; if (!hasOwn(k)) goto HEADER; ... }

The loop over a `for-in`'s `GetNextPName` has no continue target (the header IS the body's first block),
so `ConditionalContinueRegionPass` skipped it and the branch back to the header stayed
`if (!r27) goto label_286` (98/2493 `recomputePluginOrdering`). The header is the next iteration.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_for_in_filter_is_a_continue():
    out = _render("conditional_continue_while_true_98_2493.hasm", 2493)

    assert "goto" not in out
    assert "if (!r27) {\n                                    continue;\n                                }" in out


def test_a_second_while_true_loop_has_no_goto():
    out = _render("conditional_continue_while_true_98_2143.hasm", 2143)

    assert "goto" not in out
