"""A copied tail region keeps its readers wired to their writers (98/8193 `compareIdentifiers`, 0x61 made a plain `jmp`).

`SharedTailDuplicationCfgPass` copied the tail `{r3 = 1 | r2 = ...; r3 = r2}; r1 = r3` for the fall-through test.
Two things made the copy print a silent miscompile, no `goto` and no warning:

* each copied instruction was deep-copied on its own, so the copy's `r1 = r3` / `r3 = r2` lost the shared value
  object their writer holds; the ternary fold finds a writer's readers by that identity and never reached
  them: `r1 = r3` printed as `r1 = -1`;
* the copy keeps the original's instruction addresses, so its `r1 = r3` counted as a read of `r3` AFTER the
  original arm and kept the original's own reader from being repointed (`r1 = r8 >= r9 ? 1 : -1` where
  `r11` makes it `1`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render():
    hasm = (_DATA / "shared_tail_region_copy_98_8193.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 8193, strict=False), verbose=False, raw=False)


def test_the_copied_tail_reads_its_own_r3():
    out = _render()

    assert "goto label" not in out
    assert "r1 = -1;\n                if (r11) {" in out
    assert "r1 = r3;\n                }\n            }\n            r0 = r1;" in out


def test_the_original_tail_reads_r3_too():
    out = _render()

    assert "                r1 = r3;\n            } else {" in out
    assert "r1 = r8 >= r9 ? 1 : -1" not in out
