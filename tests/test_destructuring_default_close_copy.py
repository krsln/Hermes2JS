"""
`for (const [key, value = ""] of entries)`: the default's guard closes a copy of the iterator (F-214, 98/5707).

The handler around the default value is `Catch ex; JmpTrue done; Mov r20 <- it; IteratorClose r20, 1; Throw ex`. It
closes a register that was copied from the iterator, which the cleanup check did not accept: the handler stayed, it
cut through the pattern, and the whole destructuring printed as the open-coded iterator protocol with a `goto`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_default_value_pattern_is_one_destructuring():
    hasm = (_DATA / "destructuring_default_close_copy_98_5707.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 5707, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert '[r14, r13 = ""] = r19;' in code
    assert "GetIterator" not in code
