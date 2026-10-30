"""A first attempt that silently loses a path is not kept over a retry that loses none (F-171).

The first attempt of 98/10128 `interpolate` was `goto`-free, so it was never compared with the retries, but
`flow_audit` counts 4 lost paths in it: a clamped `x` never reached the range test (the `else` arm of
`x < r9` ended without running on into it). Level 5 loses nothing and still has one `goto`: a `goto` says the
structure is missing, a wrong tree says nothing. 96/6029 `_anon_0` is the same: the first attempt returned
`r1` early where the source awaits `_updateBottomIfNecessary()`.

    98/10128  `interpolate`
    96/6029   `onLayout` handler
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_clamped_input_reaches_the_range_test():
    out = _render("lossy_first_attempt_98_10128.hasm", 10128)

    assert out.index('r17 = r9;') < out.index("if (r17 > r12) {")


def test_a_changed_height_awaits_the_update():
    out = _render("lossy_first_attempt_96_6029.hasm", 6029)

    assert "return r1;" not in out
    assert out.index("await r3._updateBottomIfNecessary();") < out.index("r3.onLayout")
