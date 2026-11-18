"""A loop whose back-edge test sits inside an `if` of its body is not a `do { } while (test)` (F-263).

`for (; 1 <= s && 0 <= c && l[s] !== a[c]; c--) {}` is lowered as a guard plus a loop whose latch test is only
reached when both bound checks passed; the paths that skip it leave the loop. Printing the latch's test as the
`while (...)` of the loop evaluated it, with stale registers, on those paths too
(98/2474 `describeNativeComponentFrame`: `} while (r9 !== r14[r8]);`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_latch_test_in_an_if_stays_a_branch_and_the_exit_is_a_break():
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)

    assert "} while (r9 !== r14[r8]);" not in out
    assert "} while (r9 !== r11[r12]);" not in out
    assert "if (r9 !== r8) {\n" in out and "continue;" in out
