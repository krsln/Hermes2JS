"""A register test the way in already decided is skipped (98/8193 `compareIdentifiers`, 96/9366).

`if (/\\d/.test(a) && ...)` style flags: `r10 = re.test(a); r11 = re.test(b)`, then a chain of
`if (!r10) goto B; r1 = -1; if (!r11) goto END; B: if (!r11) goto C; r3 = 1; if (!r10) goto E; C: ...`.
The tail copy of the shared tail (rung 6) gives the fall-through its own run of blocks, and its second test of
`r10` can only go one way. `DecidedTestThreadingCfgPass` replaces such a test with the jump it must take; before
it, both functions kept `if (!r10) goto label_119;`.

A test is left alone when dropping its dead side would leave a reader holding the dropped arm's value
(`shared_tail_region_copy_98_8193.hasm`, see `test_shared_tail_region_copy_values.py`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_98_8193_has_no_goto_and_keeps_every_path():
    out = _render("decided_test_threading_98_8193.hasm", 8193)

    assert "goto label" not in out
    # r10 true: r11 false -> -1, r11 true -> the comparison; r10 false: r11 true -> 1
    assert "r1 = !r11 ? -1 : r8 >= r9 ? 1 : -1;" in out
    assert "                } else {\n                    r3 = 1;\n                }\n                r1 = r3;" in out


def test_96_9366_has_no_goto_and_keeps_every_path():
    out = _render("decided_test_threading_96_9366.hasm", 9366)

    assert "goto label" not in out
    assert "                r3 = -1;\n                if (r4) {" in out
    assert "r3 = !r6 ? 1 : -1;" in out
