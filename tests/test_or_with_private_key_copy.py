"""A copy only the second test reads no longer keeps `||` from folding (96/9613 `getNormalizedCSSTransitionConfigUpdates`).

    for (key of keys) {
        if (!(a.settings[key] && deepEqual(a.settings[key], b.settings[key]))) { r0.settings = b.settings; break; }
    }

compiles to `if (!r8) goto BREAK; ...; r11 = r7; ... r8[r11] ... r8[r11]; r8 = call; if (r8) goto CONTINUE; BREAK:`.
The key copy `r11 = r7` is read twice by the test and by nothing else, so `_fold_pure_setup` folds it; before, the
`||` stayed two blocks and the loop printed `if (r8) goto label_326; continue;`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_break_condition_is_one_test():
    hasm = (_DATA / "or_with_private_key_copy_96_9613.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 9613, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    assert "if (!(r8 && r2[4].deepEqual.call(undefined, param1.settings[r7], param2.settings[r7]))) {" in out
    assert "r9.settings = r8;\n                break;" in out
