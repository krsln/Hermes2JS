"""A `break` out of a loop that closes an `else` arm: the loop's way out only jumps on (F-198).

    else { ...; do { ...; if (c) goto MERGE; ... } while (d); }     MERGE: code after the whole `if`

The latch falls into a lone `jmp MERGE` and the break jumps to MERGE itself, which the arms of the other
`if` reach as well. `LoopBreakStructurer` took MERGE for a join the loop does not own and left
`if (!(r26 > r18)) goto label_616` (98/10142 `BezierEasing`). A `break` lands right behind the loop, on that
jump, so it is the same way out. The `break` block is synthetic (address -1) so the `if` that jumps over the
block it splits still finds that block.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_break_to_the_join_behind_a_forwarding_exit_is_a_break():
    out = _render("loop_break_forwarded_exit_98_10142.hasm", 10142)

    assert "goto" not in out
    assert "if (!(r26 > r18)) {\n                            break;\n                        }" in out
    # the `if` in front of it keeps its own join
    assert "if (0 < r12) {\n                            r5 = r0;\n                            r6 = r10;\n                        }" in out
