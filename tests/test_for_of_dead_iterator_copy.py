"""The `GetIterator` setup in front of a for-of is dropped although the loop header copies the iterator (F-235).

The header's done check copies the iterator (`Mov y <- it`); the copy is inlined into its uses and prints
nothing, but its operand still names the iterator register, and the dead-setup check counted that as a read.
`r1 = GetIterator(r2);` stayed in front of every such `for (x of xs)`.

    98/4310  `anyInCell`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_an_inlined_copy_of_the_iterator_is_not_a_read():
    hasm = (_DATA / "for_of_dead_iterator_copy_98_4310.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4310, strict=False), verbose=False, raw=False)

    assert "for (let r4 of r2) {" in out
    assert "GetIterator" not in out
