"""`yield x` inside `for (... of ...)` folds although its return arm closes the iterators (96/3625 `generateValues`).

The compiler lays the yield out as a lone `SaveGenerator` (the value was computed in the block before) and a return
guard whose arm is `IteratorClose` + `Ret`. The guard was not recognised, so the suspend printed as `r4 = await yield;`
(not valid JavaScript) and the yielded value was nowhere in the output.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "yield_inside_a_for_of_that_closes_its_iterator_96_3625.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_or_resume_flag_is_printed():
    out = _render()

    assert "await yield" not in out
    assert "__resumeIsReturn" not in out


def test_the_value_is_yielded():
    assert "            yield r4;\n" in _render()
