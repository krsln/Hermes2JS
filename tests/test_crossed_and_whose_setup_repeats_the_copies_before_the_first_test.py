"""`if (r9 && !(r26 === "after" && r7 && r6)) { arm }` kept `if (r6) goto label_N;` (98/4238 `computeWindowedRenderLimits`).

    r0 = r3; r28 = r18; if (!r9) goto JOIN;
    if (r26 !== "after") goto ARM; if (!r7) goto ARM;
    r0 = r3; r28 = r18; if (r6) goto JOIN; ARM: ...

The second test repeats the copies the path already made, with nothing written in between; they were treated as copies for
the edge into JOIN (a loop latch, where no edge block may go), so the crossed `&&` was refused. A copy the path already made
is simply dropped.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_three_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_and_after_repeated_copies_98_4238.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4238, strict=False), verbose=False, raw=False)

    assert 'if (r9 && (r26 !== "after" || !r7 || !r6)) {' in out
    assert "goto label_" not in out
