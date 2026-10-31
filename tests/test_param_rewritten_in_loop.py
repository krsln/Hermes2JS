"""A register that holds a parameter on entry is not the parameter once a loop rewrites it (F-175).

`LoadParam r11, 2` makes a read of `r11` print as `param2`, and that holds for as long as nothing writes `r11`
again. 96/4846 `binarySubdivide` ends its body with `Mov r11, r15; Mov r10, r14` and reads both at the top of the
next iteration, so `r0 = param3 - param2` was only right on the first one. A register written again inside a
loop that holds the read keeps its name; the `LoadParam` line prints, and the later writes mean something.

    96/4846  `binarySubdivide`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_loop_reads_the_registers_it_rewrites():
    out = _render("loop_carried_arm_copy_96_4846.hasm", 4846)

    assert "r11 = param2;" in out
    assert "r10 = param3;" in out
    assert "r0 = r10 - r11;" in out
    assert "r11 = r15;" in out
    assert "param3 - param2" not in out
