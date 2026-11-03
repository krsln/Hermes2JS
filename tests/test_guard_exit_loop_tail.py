"""The tail a `for-of` body jumps to when it finds its item becomes the body of the `if` (F-202).

    for (x of xs) { if (a) continue; else { ...; if (found) goto TAIL } }   TAIL: ...; return r;   return undefined

`GuardExitRegionPass._try_region_exit` moves such a tail into the guard, but only when the guard's other edge is
"the next thing that runs". Here that edge enters a bare `continue` block of the other arm (the guard ends an `else`
arm that ends the loop body), and the function's own last `return` (the loop's natural exit) is entered by another
path than the guard's. Both now qualify; the natural exit stays where it is.

    98/5429 `findInitialRoute`; 98/11278 (no loop: only the function's own last `return` stays out of the tail)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_found_tail_of_a_for_of_is_the_body_of_its_if():
    out = _render("guard_exit_loop_tail_98_5429.hasm", 5429)

    assert "goto" not in out
    assert "if (r10) {\n                r1 = r3;" in out
    assert out.rstrip().endswith("}\n        }\n    }\n}")


def test_a_second_function_of_the_shape_has_no_goto():
    out = _render("guard_exit_loop_tail_98_11278.hasm", 11278)

    assert "goto" not in out
