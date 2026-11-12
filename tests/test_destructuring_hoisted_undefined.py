"""`const [uri, scale = "1x"] = x.split(" ")`: the `undefined` the checks compare with is loaded ahead of the chain (F-215, 98/10271).

A default on a LATER element makes the compiler load `undefined` once, before element 1's own `LoadConstUndefined`
and its fetch: the head block read `LoadConstUndefined; LoadConstUndefined; Mov; IteratorNext; Mov; StrictEq; JmpTrue`,
a shape the pass did not know, so the iterator protocol stayed open-coded with a `goto`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_default_on_the_second_element_is_one_pattern():
    hasm = (_DATA / "destructuring_hoisted_undefined_98_10271.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10271, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert '[r5, r6 = "1x"] = r4;' in code
    assert "goto" not in code
    assert "GetIterator" not in code
