"""The `Ret` behind a `SaveGenerator` is not a handler for the register guard of a test chain (96/6029 `_anon_0`).

    if (prev && prev.height === this._frame.height) skip;   // the second test's setup reads/writes r1
    await this._updateBottomIfNecessary();                   // SaveGenerator; Ret r1  (no CFG predecessor)

`_handlers()` took every block without a predecessor for a handler that may read any register, and the
suspend's `Ret r1` read `r1`, which the test also writes, so the fold of the second test gave up and left a `goto`.
That `Ret` runs right after the save and reads what the call before it computed.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_height_test_is_one_condition_before_the_await():
    hasm = (_DATA / "test_before_await_suspend_96_6029.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 6029, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (!r1 || r1.height !== r2[0]._frame.height) {" in out
    assert out.index("await r3._updateBottomIfNecessary();") > out.index("if (!r1 || r1.height")
