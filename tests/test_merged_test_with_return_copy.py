"""A merged-away test block must not stay a predecessor of a private `return` copy (F-161).

With the shared returns copied (a retry), `ShortCircuitConditionCfgPass` folded a test block into the one before
it and left it listed as a predecessor of the copy the test jumped to; the dominator pass raised `KeyError`
and the retry was silently dropped.

    96/7449  `isValidElementType`-style chain of `||` tests (anonymous)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_retry_survives_a_folded_test_and_leaves_no_goto():
    hasm = (_DATA / "merged_test_with_return_copy_96_7449.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7449, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert "while (true)" not in out
    assert out.rstrip().endswith("return true;\n}")
