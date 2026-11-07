"""Two tests that jump to one short tail ending in `return`/`throw`: the later one gets its own copy (F-196).

    for (x of xs) { if (A) goto B; if (C) goto B; }   return;   B: position = "absolute"; return

F-194 copied a tail that runs on into a join. The break path of a for-of that sets something and leaves ends in
its own `return`: the loop's natural exit is a different, bare `return` block, the break path sits right behind
the loop and the structurers took IT for the loop's exit, so the natural exit printed the `position` line too
(98/8693 `maybeModifyStyleForKeyframe`: a list without `originX`/`originY` got `position = "absolute"`), and a
`goto` stayed. The tail (up to six instructions, exactly two forward conditional ways in, nothing falls into it)
now gets a copy ending in the same `return`/`throw` for the later test, on the last rung only.

    98/8693 `maybeModifyStyleForKeyframe`   98/11911 `transformOrigin` (`r6 < 1 || r7.length > 3` -> `throw`)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_natural_exit_of_the_loop_does_not_set_the_position():
    out = _render("second_jumper_exit_98_8693.hasm", 8693)

    assert "goto" not in out
    # only the break paths set it, each leaves the function right away; nothing behind the loop does
    # (F-216: both tests are one `||` now, so the one break path is written once)
    assert out.count('if (r7 || "originY" in r6) {\n                param1.style.position = "absolute";\n                return undefined;\n            }') == 1
    assert out.count('param1.style.position = "absolute";') == 1


def test_a_throw_tail_two_tests_jump_to_is_copied():
    out = _render("second_jumper_exit_98_11911.hasm", 11911)

    assert "goto" not in out
    assert out.count("throw new Error(r19);") >= 3
