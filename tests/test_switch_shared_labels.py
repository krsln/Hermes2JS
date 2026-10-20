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
