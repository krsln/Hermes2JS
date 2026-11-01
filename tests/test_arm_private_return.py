"""An arm whose only way out is a private `return`, tested past its first block (F-170).

    if (a) { x = f(); if (x != null) return x.v; }  T: ...        a jumps to T

The arm's test (`x?.key != null` is three blocks) falls into the branch target; its exit is a `return` nothing else
reaches. The first attempt had no `if` for that: it printed `if (r2 != null) goto label_87; return param1.key;`,
which returned the key on the path where it is `null`. Now the target follows the `if` and `GuardExitRegionPass`
may fall on into an `if` whose test block its condition swallowed, so the `return` moves into the guard.

An arm with more exits (96/4144: three returns) keeps the old route, which copies the returns.

    96/5301  `keyExtractor`
    96/5     `metroImportDefault`
    96/4144  `parseScheme`  (must keep `return 0`)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_key_is_returned_only_when_it_is_not_null():
    out = _render("arm_private_return_96_5301.hasm", 5301)

    assert "goto" not in out
    assert "if (r2 != null) {\n            return param1.key;\n        }" in out
    assert out.count("return param1.key;") == 1
    assert out.index("return param1.key;") < out.index("r1 = param1.id;")


def test_a_cache_check_returns_inside_its_own_if():
    out = _render("arm_private_return_96_5.hasm", 5)

    assert "goto" not in out
    assert "if (r3 !== r1) {\n            r1 = r0[1];\n            r0 = r1.get(param1);\n            return r0.importedDefault;" in out


def test_an_arm_with_several_exits_keeps_its_returns():
    out = _render("arm_private_return_many_exits_96_4144.hasm", 4144)

    assert "if (r6 !== r4) {\n                return 0;\n            }" in out
