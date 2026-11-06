"""
`if (!c) goto T; BODY; T: tail` where BODY exits on every path and only this branch enters T (F-208,
98/12276 `validateType`).

After the shared `throw` and the `Object.assign(...); return` were copied per jumper, the guard
`if (!param1.extrapolateRight) goto T` still jumped to a tail in its own sequence, behind an if/else whose
arms both exit. `GuardExitRegionPass` skipped every exit held by the guard's own sequence (the
`IfStructurer`'s job) but that one never got built; with code between the two, the exit now moves into the `if`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "guard_exit_same_sequence_98_12276.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 12276, strict=False), verbose=False, raw=False)


def test_the_guard_takes_its_exit_into_the_if():
    code = _code()

    assert "goto" not in code
    assert "if (!param1.extrapolateRight) {\n                r5 = Object.assign(r2, param1);\n                return r2;\n            }" in code
