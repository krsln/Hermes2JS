"""`if (undefined === r12) goto T` into code that rung 10's layout keeps splitting (98/9589 `fe`).

The `async` arm reaches the shared `iterable?` check by falling through and `T` (the sync-iterator fallback) only by the
jump. Rung 13 (`TerminalTailRegionCopyCfgPass` on rung 10's copies) still leaves a `goto` inside the tail the copies
split; the last rung runs the same pass on rung 1's layout.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_tail_copy_on_the_plain_layout_needs_no_goto():
    hasm = (_DATA / "terminal_tail_behind_a_returning_block_98_9589.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto label_" not in out
    assert 'r7 = r5[36].call(0, param1, "sync", r7);' in out
