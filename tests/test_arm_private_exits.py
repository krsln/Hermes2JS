"""
An arm with SEVERAL private exits whose last test falls into the branch target (F-211, 96/13262
`shouldUseHorizontalLabels`).

    if (pos) { if (pos === "beside-icon") return true; if (pos === "below-icon") return false; }  <width logic>

`_returns_privately` refused an arm with a second exit, so the width logic was printed as the `then` arm and the
arm's last test as `if ("below-icon" === r4) goto L; r0 = false`. A further exit that is a `return` of its own
is fine now, and `IfTailMergeRegionPass` keeps a `return` a pending test still jumps to (96/4144 `parseScheme`,
`tests/test_arm_private_return.py`, lost its `return 0` with the first change alone).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_width_logic_follows_the_position_checks():
    hasm = (_DATA / "arm_private_exits_96_13262.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 13262, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if ("below-icon" === r4) {\n            return false;\n        }\n    }\n    r4 = r0.width;' in code
