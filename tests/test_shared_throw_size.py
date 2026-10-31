"""A shared `throw new E(message)` of thirteen instructions is still one statement (F-174, F-10b).

The copy limit for a shared `throw` was twelve instructions, and `throw new TypeError("..." + p + "...")` built by
`HermesInternal.concat` is thirteen (`LoadParam`, `GetGlobalObject`, two lookups, the concat call, `CreateThis`,
`Construct`, `SelectObject`, ...). Both tests of a `used || locked` check jumped to it and one of them was printed as
`goto label_62`. Each jumper gets its own `throw`.

    98/4987  `checkBodyUsedError`
    96/7669  an `invariant`-style check whose message is thrown from two tests
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_both_tests_throw_their_own_error():
    out = _render("shared_throw_98_4987.hasm", 4987)

    assert "goto" not in out
    assert out.count("throw new TypeError(r8);") == 2
    assert "if (r2 === true) {" in out


def test_a_throw_shared_by_two_tests_in_a_nested_check():
    out = _render("shared_throw_96_7669.hasm", 7669)

    assert "goto" not in out
    assert out.count("throw new r2(r8);") == 2
