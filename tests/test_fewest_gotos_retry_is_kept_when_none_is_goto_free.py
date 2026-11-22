"""When no retry is `goto`-free, the one with the fewest `goto`s replaces the first attempt (F-263, 98/2474).

The first attempt leaves the shared `return ""` as `if (r4[7]) goto label_899;`; the retries that copy the shared
return per jumper remove it, but three other `goto`s keep every attempt invalid, so the first attempt used to win
with all four.

Since F-301 the `goto`s that stay after every rung print as `label_N: { ... break label_N; ... }`: the retry that
copies the shared return is still the attempt that is printed (three jumps out of nested arms, no `label_899`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_retry_with_fewer_gotos_wins_when_every_attempt_has_some():
    hasm = (_DATA / "loop_latch_inside_if_98_2474.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2474, strict=False), verbose=False, raw=False)

    assert "label_899" not in out
    assert "goto" not in out
    assert sum("break label_" in line for line in out.splitlines()) == 3
