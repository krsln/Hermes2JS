"""Exits that sit in the gaps of a merged try range are not protected (F-168).

A `for-of` body is protected by several table entries; between them lie the exits (`it.return();
r0 = []; return r0`), which Hermes keeps OUT of the range. `CFGBuilder` merges the pieces into one range
spanning the gaps, so `SharedReturnDuplicationCfgPass` treated the exits as inside a try and left the shared
ones alone: every jump to them printed as `goto label_N` and the exit bodies were printed after the loop,
where normal completion falls into them. The merged entry now keeps its `fragments`, and only a block that
overlaps one of them is protected.

    96/1324  `parseBackgroundRepeatCSSString`
    96/1330  `parseBackgroundSizeCSSString`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_shared_exits_are_copied_into_their_branches():
    out = _render("merged_try_gap_exits_96_1324.hasm", 1324)

    assert "goto" not in out
    assert out.count("return r24;") == 5 and out.count("return r1;") == 2
    assert out.rstrip().endswith("return r0;\n}")


def test_nothing_exits_after_the_loop_but_the_normal_return():
    out = _render("merged_try_gap_exits_96_1330.hasm", 1330)

    assert "goto" not in out
    assert ".return()" not in out and "GetIterator" not in out
    assert out.rstrip().split("\n")[-2].strip().startswith("return")
