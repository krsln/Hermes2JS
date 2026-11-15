"""A shared tail with another way's leaf between it and `END` is still copied (F-217, 98/6324 `isCompact`).

    if (!a) goto T;  if (a === "beside") { r1 = true; goto J }  r1 = false; if (a === "below") goto J;
    T: <test, two arms>; jmp J      X: r1 = true      J: ...

The block `X` of the `beside` leaf lies in the layout between the tail and `J`, so the blocks up to `J` were not
all the tail's own and the region was refused. The region is now the run of blocks only the tail enters, ending in
a jump to `J`; the test that skips it gets a private copy and the `else` arm runs the tail when `a` is neither.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_leaf_between_the_tail_and_its_end_does_not_stop_the_copy():
    hasm = (_DATA / "shared_tail_foreign_leaf_98_6324.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6324, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    # The tail (the width test) runs for `!a` AND when `a` is neither `beside-icon` nor `below-icon`.
    assert out.count("r8 >= 768") == 2
    assert 'if ("below-icon" !== r9) {' in out
