"""`if (0 !== (x & 261930) && 0 !== (y & 42)) { ... } else { count = 0 }` kept a `goto` (F-263 sampling, 96/2153).

    r1 = f.pendingLanes; r5 = r7 & 261930; if (0 === r5) goto ZERO;
    r7 = r1; r5 = 42; r5 = r7 & r5; if (0 !== r5) goto NESTED; ZERO: count = 0 ...

The second test's setup holds a copy (`r7 = r1`) that an earlier link of the same setup already substituted into the test
(`r1 & 42`); the copy is dead on both exits, but the fold only accepted a copy the test still mentioned once, so the crossed
`&&` was refused and the nested `if` printed `if (0 !== r5) goto label_505;`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_two_tests_are_one_condition_without_a_goto():
    hasm = (_DATA / "crossed_and_after_dead_copy_setup_96_2153.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2153, strict=False), verbose=False, raw=False)

    assert "if (0 !== r5 && 0 !== (r1 & 42)) {" in out
    assert "goto label_" not in out


def test_a_copy_into_the_value_register_of_a_ternary_keeps_the_chain_apart():
    """96/13916 `listener`: `typeof e === "object" && e != null && "message" in e ? e.message : e`; the copy `r6 = e` of the
    last test is one arm's value (both arms write r6): folding it half folded the chain and left a `goto`."""
    listener = (_DATA / "ternary_value_register_copy_96_13916.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(listener, 13916, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
