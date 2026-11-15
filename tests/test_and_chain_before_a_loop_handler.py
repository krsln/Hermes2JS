"""An `&&` chain with a `?:` value, in a function whose only handler guards a later `for-of` (96/12624).

`const p = "params" in o && typeof o.params === "object" && o.params ? o.params : {}` before a `for (const k of keys)`:
the three tests jump to the `{}` arm. Folding the second test's setup into the first test drops its writes, and
`_fold_pure_setup` refused that in any function with an exception handler (the handler may read what the try body
had set). The `for-of` handler guards the loop only and reads the iterator, which `IteratorBegin` sets after the
tests, so it does not see those registers. The printed tail was a miscompile: the not-an-object path ran the
`o.params` arm.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_value_tests_become_one_condition_with_an_else():
    out = _render("and_chain_value_ternary_96_12624.hasm", 12624)

    assert "goto label" not in out
    assert 'if ("params" in r2 && typeof r2.params === "object" && r4.params) {\n        r2 = r4;\n        r1 = r2.params;\n    } else {\n        r1 = {  };\n    }' in out
