"""On the last rung of the retry ladder a longer shared `return` is copied for the jumps that reach it (F-189).

    if (!a) goto T; ...; if (b) goto T; throw ...; T: Object.assign(x, { [k]: v }); return r0

`T` is seven instructions, one over the limit of the rungs before, and only jumps reach it: the second test kept
`goto label_195`. The last rung (it only runs for functions every earlier one left with a `goto`) copies a tail
up to nine instructions when nothing falls into it.

Not for a tail something falls into (98/2844 `rawToPerformanceEntry`: `r4.decodedBodySize = r5; return new r6(r4)`
after `r5 = 0` on one path and `r5 = v` on the other; the copy printed `= 0` on both).

    98/10767 `anonymous` (react-navigation)   98/2844 `rawToPerformanceEntry`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_long_tail_only_jumps_reach_is_copied_for_each_jump():
    out = _render("long_shared_return_98_10767.hasm", 10767)

    assert "goto" not in out
    assert out.count("r0 = Object.assign(param1, r0);") == 2
    assert "if (r0) {" in out


def test_a_tail_something_falls_into_keeps_its_own_values():
    out = _render("long_shared_return_98_2844.hasm", 2844)

    assert "r4.decodedBodySize = 0;" not in out
