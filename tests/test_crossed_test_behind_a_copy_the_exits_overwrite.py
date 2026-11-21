"""`if (typeof v === "object") { r12 = r9; if (r12 !== null) goto B } A` kept two `goto`s (98/5401 `parse`).

The second test of the crossed pair reads a copy `r12 = r9` that both exits overwrite before reading (`A` and `B` start
with `r12 = r9` again), but the fold only took a copy when an effect in the pair was read by END (`relaxed`). A copy
that global liveness shows dead on both exits is folded in every crossed pair: `typeof v === "object" && v !== null`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_copy_is_folded_into_the_second_test():
    hasm = (_DATA / "crossed_test_after_a_dead_copy_98_5401.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert 'typeof r12 === "object" && r9 !== null' in out or 'typeof r12 === "object" && (r9 !== null)' in out
