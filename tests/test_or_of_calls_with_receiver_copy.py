"""`a.includes("x") || a.includes("y")` behind receiver copies folds into one test (98/12172).

    r12 = r10; r11 = r12.includes("translate"); if (r11) goto T;
    r12 = r10; r11 = r12.includes("perspective"); if (!r11) goto PLAIN;
    T: typeof r9 === "number" ...

The second block's `r12 = r10` only feeds the receiver of its one call, so `_fold_pure_setup` takes `r10` for
it; before, the copy kept the crossed `||` from folding and the function printed three `goto`s.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_or_of_two_calls_is_one_condition():
    hasm = (_DATA / "or_of_calls_with_receiver_copy_98_12172.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 12172, strict=False), verbose=False, raw=False)

    assert "goto label" not in out
    # Since F-297 the receiver copy is folded away on every crossed pair, so both tests and the `typeof` check make
    # one `if`.
    assert 'if ((r11 || r10.includes("perspective")) && typeof r9 === "number") {' in out
