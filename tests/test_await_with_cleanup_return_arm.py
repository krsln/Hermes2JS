"""An `await` whose resume guard's return arm holds cleanup code folds anyway (96/14482, 14867, 8059 `_anon_0`).

    try { await loadSingleFontAsync(a, b); markLoaded(a); } finally { delete loadPromises[a]; }

The `finally` is copied onto the `.return()` path, so the guard `if (resumeIsReturn)` after the suspend does not
end in a lone `Ret`. An `await` never resumes with the return flag set, so that arm is dead and the guard folds;
before, the save stayed a `goto label_46` and a second `await yield` was printed.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_await_folds_and_the_dead_return_arm_is_dropped():
    hasm = (_DATA / "await_with_cleanup_return_arm_96_14482.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 14482, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert "await yield" not in out
    assert "__resumeIsReturn" not in out
    assert "await r6(r5, r1);\n        r5 = r3[5];" in out
