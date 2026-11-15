"""A jump to a loop block's address finds the block, not the bare `break` split off it (F-229, 98/14187).

    do {
        if (typeof cb !== "function") goto INC;  ...  if (cb == null) goto INC;  cb.call(...);
        INC: r0 = r0 + 1; r4 = ...; if (!(r0 < r4)) break; ...
    } while (...)

`LoopBreakStructurer` (shape D) turns the block's own test into `if (c) { break; }` and gives the new block that
block's address, so the address lookup of `_DominanceIfBuilder` found the `break` for the target `INC` of both
guards: the join it saw was a block with no way in, and neither guard became an `if`. The lookup now prefers the
real block.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_two_guards_of_the_loop_body_nest():
    hasm = (_DATA / "bare_break_shadow_98_14187.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 14187, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (typeof r11 === "function") {' in code
    assert "if (r11 != null) {" in code
