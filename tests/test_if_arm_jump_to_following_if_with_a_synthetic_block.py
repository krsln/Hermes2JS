"""A jump at the end of an `if` arm to the `if` that follows stays a `goto` when that `if` holds a synthetic block (F-263 sampling, 96/2075).

`updateSuspenseListComponent`: `if (13 === t) {...} else if (19 === t) { schedule(...); goto TAIL } else { ... continue }` followed by
`if (r13 !== param2) {...}` (TAIL is its test block). `RedundantJumpRegionPass._leading_address` finds where an `if` begins from the
lowest address among its blocks, and one of them was a `break` block made by a structurer (address -1): nothing lies below -1, so no
address came back and the arm's jump to the following `if` was never recognised as redundant.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_jump_to_the_following_if_is_dropped():
    hasm = (_DATA / "if_arm_jump_to_next_if_with_synthetic_block_96_2075.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2075, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
