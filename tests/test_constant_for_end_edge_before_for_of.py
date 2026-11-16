"""A later `for-of`'s handler does not stop a constant from moving onto the edge into END (96/11000).

    typeof a === "object" && a !== null && a.value === undefined  ->  END: Object.keys(a) ... for (const k of keys)

The last test reads `r5 = undefined`, and END (the `for-of`'s `r7 === r5` exit test) reads it too, so the test takes the
value and END gets its own copy. The `for-of` has an iterator-close handler that reads `r2`, which the test block
also writes; but `IteratorBegin` in END writes `r2` before the protected range starts, so the handler never sees the
test's value. The guard looked at every handler and gave up, leaving two `goto`s.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_three_tests_are_one_condition_before_the_for_of():
    hasm = (_DATA / "constant_for_end_edge_before_for_of_96_11000.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11000, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r3 !== null && param1.value === undefined) {" in out
