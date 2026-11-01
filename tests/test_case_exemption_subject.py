"""
Two constant comparisons are a `case` chain only when they test the same value (96/956 `replacer`).

    if (typeof v !== "object") return v;   if (v === null) return v;   ...rest

Both jump to one `return`. The `null` test sits beside a constant comparison, which made
`_absorb_residual_conditional` leave the shared target to `SwitchStructurer`, but the two tests
look at different values (`typeof v` and `v`): no `switch` comes out of them and the `null`
path lost its `return` (it fell off the end as `undefined`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_null_test_beside_a_typeof_test_keeps_its_exit():
    hasm = (_DATA / "two_constant_tests_one_return_96_956.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 956, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r4 === null) {" in out
