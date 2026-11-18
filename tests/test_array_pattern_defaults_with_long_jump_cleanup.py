"""An array pattern with default values whose cleanup handlers reach the shared close by a long jump (F-278).

`const [a = "", b = "", c = ""] = text.split("/")` wraps each default in a try range whose handler is
`Catch; JmpLong CLOSE` (the shared `IteratorClose; Throw` is too far for a short `Jmp`). The cleanup vocabulary knew
`Jmp` but not `JmpLong`, so the handler was a "real catch", the pattern kept its iterator protocol and the
function a `goto` (98/7643 `resolveBlurhashString`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_defaults_pattern_is_one_statement():
    hasm = (_DATA / "array_pattern_defaults_with_long_jump_cleanup_98_7643.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7643, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert '[r11 = "", r10 = "", r7 = ""] = r6;' in out
    assert "GetIterator" not in out
