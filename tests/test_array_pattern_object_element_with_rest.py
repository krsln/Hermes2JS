"""An object pattern with a `...rest` as an element of an array pattern collapses into one destructuring.

`const [a, { if: b, ...rest }] = param` stores each property straight into an environment slot and builds the
rest with `copyDataProperties`; the iterator cleanup `try` around it kept the function full of `goto`
(98/10811). `ArrayDestructuringCfgPass` now reads `{ if: slot, ...slot }` as the element, and the register that
kept the rest value is restored from its slot.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_object_element_with_rest_is_one_pattern():
    hasm = (_DATA / "array_pattern_object_element_with_rest_98_10811.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 10811, strict=False), verbose=False, raw=False)

    assert "[__environment__[0], { if: __environment__[1], ...__environment__[2] }] = param1;" in out
    assert "r4 = __environment__[2];" in out
    assert "goto" not in out
    assert "GetIterator" not in out
