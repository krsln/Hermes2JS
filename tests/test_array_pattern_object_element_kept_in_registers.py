"""An object-pattern element whose leaves are also kept in registers stays one pattern (F-279).

`const [{ nextScreenId, tabPath }, x] = useNextScreenId()` where the names are captured by a closure and read
locally too: each property is read, copied into the variable's own register (`r4 = leaf`) and stored into its
environment slot, and the last read goes into the source register itself (`r5 = r5.tabPath`). The pattern stores
into the slots; the registers that are still read afterwards are restored from them (98/6599 `LinkWithPreview`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_object_element_is_a_pattern_and_the_local_copies_are_restored():
    hasm = (_DATA / "array_pattern_object_element_kept_in_registers_98_6599.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6599, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "[{ nextScreenId: __environment__[8], tabPath: __environment__[9] }, __environment__[10]] = r13;" in out
    assert "r4 = __environment__[8];" in out
    assert "r8 = __environment__[9];" in out
