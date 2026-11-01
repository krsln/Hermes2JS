"""
F-10 (non-return targets): three or more case labels sharing one body.

    96/7527  `encoderForArrayFormat`: "comma", "separator" and "bracket-separator"
             all jump to the same block. The last test used to stay behind as
             `if ("bracket-separator" === r3) goto label_70;` inside `default`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_every_label_of_a_shared_body_joins_one_case_group():
    out = _render("switch_three_shared_labels_96_7527.hasm", 7527)

    assert "goto" not in out
    assert 'case "comma":\n        case "separator":\n        case "bracket-separator":' in out
    assert "default:\n            return function_7536;" in out


def test_labels_after_an_inverted_one_continue_the_same_switch():
    """96/4122 `defaultPort`: `"https"`/`"wss"` share `return 443`.

    The `"ws"` test is inverted, which pushed the rest of the chain into `default`;
    on its own that tail has one body and stayed `if`s, and the `"wss"` jump to
    `return 443` was dropped. It now continues the outer `switch`.
    """
    out = _render("switch_nested_chain_default_96_4122.hasm", 4122)

    assert "goto" not in out
    assert 'case "https":\n        case "wss":\n            return 443;' in out
    assert "default:\n            return null;" in out


def test_a_chain_with_a_return_behind_it_keeps_the_label_of_its_shared_body():
    """96/777 `_unsupportedIterableToArray`: `"Map"` and `"Set"` share `Array.from`.

    With the return copied into each path the `"Set"` test is inverted and the rest of
    the chain (`"Arguments"`, then the default) is followed by the return. That tail
    kept the chain from becoming a `switch`, and the `"Set"` jump was dropped (a
    `Set` came out as `undefined`). The return now follows the `switch`.
    """
    out = _render("switch_labels_then_tail_96_777.hasm", 777)

    assert "goto" not in out
    assert 'case "Map":\n                case "Set":\n                    r0 = Array.from(param1);\n                    return r0;' in out
    assert '"Set" !==' not in out
