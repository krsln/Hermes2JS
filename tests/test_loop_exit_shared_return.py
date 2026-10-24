"""
Exits of a loop body that jump to a shared `return` behind the loop (96/4123 `parseHost`,
the IPv4 part loop):

    for (i = 0; i < n - 1; i++) { ...; if (part < 0 || part > 255) return null; ... }
    <code after the loop>

Two things went wrong while the `return` was one block with many predecessors:

- `if (part < 0) goto RET; rest` became `if (part >= 0) { rest }`: the body just ended and the
  loop went on (`return null` was gone);
- a zero-trip guard `if (0 < n) { loop }` whose loop ends into the code the guard jumps to
  (the part after the loop) put that code in the other arm only: after the loop it never ran.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_loop_exits_to_a_shared_return_stay_exits():
    out = _render("loop_exit_shared_return_96_4123.hasm", 4123)

    loop = out[out.index("for (i = 0; i < r7 - 1; i++) {"):]
    body = loop[:loop.index("r2 = r7 - 1;")]

    assert "goto" not in out
    assert body.count("return null;") == 2


def test_the_code_after_a_zero_trip_loop_runs_after_the_loop_too():
    out = _render("loop_exit_shared_return_96_4123.hasm", 4123)

    loop_at = out.index("for (i = 0; i < r7 - 1; i++) {")

    assert out.count("r0 = r3 + r2;") == 1
    assert out.index("r0 = r3 + r2;") > loop_at
