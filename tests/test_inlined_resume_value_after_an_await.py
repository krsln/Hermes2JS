"""A resumed value read by a consumer that inlined it keeps its binding (96/6672, `Asset.downloadAsync`).

`this.localUri = await downloadAsync(...)`: the compiler stores the resumed register straight into the property, so
the consumer's value was the resume placeholder (`await yield`, not valid JavaScript) and nothing named the
register, which made the fold believe the resumed value was never read and print `await call();` + `await yield`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "inlined_resume_value_read_after_an_await_96_6672.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_no_placeholder_is_printed():
    assert "await yield" not in _render()


def test_the_awaited_value_is_bound_and_stored():
    out = _render()

    assert "r3 = await r8(this.uri, this.hash, this.type);\n            this.localUri = r3;" in out
