"""An `if` arm's trailing jump to the code that follows the whole `if` is dropped (F-163).

    if (a) { ... } else if (b) { ...; goto J } else { ...; return }  J: <join>

The inner `if` has no merge of its own (its `else` returns), so its first arm kept the jump to the outer join.
Falling off the end of the arm reaches the same place.

    96/3847  `setStyleAttributePreprocessor`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_arm_falls_through_to_the_join_without_a_goto():
    hasm = (_DATA / "if_arm_jump_to_join_96_3847.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3847, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.count('r1["process"] = param2;') == 1
    assert out.rstrip().endswith("r0 = r0[0];\n    r0[param1] = r1;\n}")
