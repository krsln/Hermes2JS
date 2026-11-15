"""A test the try body and the catch both run into ends the catch, it is not part of it (F-188).

    try { r2 = f() } catch (e) { r2 = false }   if (!r2) { g() }   return

The test is the merge block of the handler: the try body reaches it by a `Jmp`, the catch by falling through. Once
the `IfStructurer` turned it into an `IfRegion` its emptied block was gone from the tree and `_find_catch_boundary`
(which looks for that block) ran on: the `if` and the `return` were printed inside the catch, and the try body
kept a `goto` to where the test used to be. `IfRegion.source_block` remembers the block.

Not for a test only the catch reaches (`catch (e) { if (it) it.return(); throw e }`, tests/test_arm_absorb.py).

    98/171 `polyfill`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_test_after_the_try_catch_is_not_part_of_the_catch():
    out = _render("catch_merge_if_98_171.hasm", 171)

    assert "goto" not in out
    assert "    } catch (caughtException) {\n        r2 = false;\n    }\n    if (!r2) {" in out
