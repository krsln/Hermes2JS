"""`if (X) { A; if (c) goto TAIL } T: ...; TAIL: ...` kept `if (c) goto label_N;` (98/2330, 96/7888).

`T` is reached by the jump of the test of `X` and by falling out of the `c` test, and it never runs on: it returns,
throws or continues the loop. `TerminalTailRegionCopyCfgPass` (the last rung) gives the jumpers their own copy of the
whole region, so both arms of `X` are ordinary `if`/`else` trees.
"""

from pathlib import Path

import pytest

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


@pytest.mark.parametrize(
    "fixture, section",
    [
        ("terminal_tail_shared_with_a_guard_in_loop_98_2330.hasm", 2330),
        ("terminal_tail_shared_with_a_guard_96_7888.hasm", 7888),
    ],
)
def test_the_guard_needs_no_goto(fixture, section):
    hasm = (_DATA / fixture).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
