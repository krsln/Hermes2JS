"""An inner `for` keeps the register name the enclosing loop still tests (98/2632 `commitBeforeMutationEffects`).

`do { ... for (r1 = r9[267]; null !== r1; r1 = r12.return) { ... r1 = r10; break } } while (null !== r1)`: the
induction register was renamed `i`, so the outer test read an `r1` that no path of the inner loop wrote any more.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_inner_for_keeps_the_register_the_outer_loop_tests():
    hasm = (_DATA / "switch_join_after_a_throwing_default_98_2632.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "} while (null !== r1);" in out
    assert "for (r1 = r9[267]; null !== r1; r1 = r12.return)" in out
