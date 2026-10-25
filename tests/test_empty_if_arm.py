"""
`if` arms that print nothing are removed (`EmptyIfArmRegionPass`).

Structuring leaves an arm behind when a branch only skips code the earlier passes folded or dropped:

- `if (c) { } else { X }` becomes `if (!c) { X }`    (98/1957 `setEventInitTimeStamp`)
- `if (c) { X } else { }` becomes `if (c) { X }`     (96/8802 `timeoutCallback`)
- `if (c) { }` is dropped when `c` cannot run anything (96/4724 `shouldUseTurboAnimatedModule`: both
  branches `Ret r0`)

An arm counts as empty the way `RegionPrinter._emit_block` decides it: a definition no reader folded
away is a line of output, so an arm that holds one is kept.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_an_empty_then_arm_turns_the_test_around():
    code = _code("empty_arm_inverted_98_1957.hasm", 1957)

    assert 'if (typeof param2 === "number") {' in code
    assert "else" not in code
    assert 'typeof param2 !== "number"' not in code


def test_an_empty_else_arm_is_dropped():
    code = _code("empty_else_96_8802.hasm", 8802)

    assert "if (r0) {" in code
    assert "else" not in code


def test_a_test_without_effect_and_without_arms_is_dropped():
    code = _code("empty_lone_if_96_4724.hasm", 4724)

    assert "if (" not in code
    assert "return false;" in code
