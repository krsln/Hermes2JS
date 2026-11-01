"""A try body that ends in its own `return` keeps it when the catch ends in a jump (F-156).

    try { ...; return r1; } catch { ...; goto T } finally { r3[9] = false; }

`_FinallyAttacher` relocates the tail after the finally copy out of the try and keeps ONE of
the two (catch first). The try's `return r1` was dropped, so the call result was never returned.

    96/840  `preprocessException`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_try_body_still_returns_its_value():
    hasm = (_DATA / "try_return_beside_catch_jump_96_840.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 840, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    try_part = out[out.index("try {"):out.index("} catch")]

    assert "return r1;" in try_part
