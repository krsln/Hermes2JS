"""`if (c) goto TAIL` whose tail only ever returns is an `if (c) { tail }` (F-246, 98/12534 `pipeTo`).

    if (signal.aborted) { abortAlgorithm(); return; }      // inlined by the compiler AFTER the closing `return`
    signal.addEventListener("abort", abortAlgorithm);

The branch jumped over the whole function to blocks laid out behind the last `return`; nothing structured them
(`if (r4.aborted) goto label_633;`). On the last retry rung (`FallThroughLayoutCfgPass.relocate_terminal_tails`) the
tail moves right behind the branch and the branch is inverted to jump over it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_aborted_arm_is_an_else_that_returns():
    hasm = (_DATA / "terminal_tail_relocation_98_12534.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 12534, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r4.aborted) {" in out
    # the arm ends in its own `return`: without it the code after it would run for an aborted signal as well
    arm = out[out.index("r1 = q.call(0, function_14099, r1, r5);"):]
    assert arm.lstrip().split("\n")[1].strip() == "return undefined;"
