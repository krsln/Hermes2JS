"""Two tests that load the same register again are not a `case` chain (F-244, 98/2621 `appendAllChildrenToContainer`).

    r20 = r21.tag;           if (22 !== r20) goto CHILD
    r20 = r21.memoizedState; if (null !== r20) goto HIDDEN       // else falls into CHILD
    CHILD: ...

The first test's target is the second one's fall-through: `22 !== tag || null === state` goes to CHILD (the crossed
`||` fold). `_is_case_test` compared the subjects as expressions - both `r20` - and kept the tests apart as a
`switch` chain although the second block writes `r20` again; the `||` stayed two raw branches and the function printed
`goto label_146` (and ran the wrong arm).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_register_loaded_again_is_not_the_same_subject():
    hasm = (_DATA / "short_circuit_reloaded_register_98_2621.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2621, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (22 === r20 && null !== r21.memoizedState) {" in out
