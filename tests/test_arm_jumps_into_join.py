"""An arm whose last block jumps over what follows it still runs into the join (F-187).

    if (!(a instanceof B)) { if (T) { return 0 } else { X; jmp J } }  J: ...

The join `J` is reached by a `JmpTrue` (the `instanceof` test) and by the last block of the arm, which ends in a
`Jmp` to it (not a fall-through). `_arm_runs_into` only counted fall-throughs, so the join was printed inside the
`instanceof` arm and the other arm got a `goto`.

    98/8188 `compare` (semver)
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_the_arm_that_jumps_to_the_join_does_not_leave_a_goto():
    out = _render("arm_jumps_into_join_98_8188.hasm", 8188)

    assert "goto" not in out
    assert "r5 = new r4(r13, this.options);" in out
    assert out.index("r5 = new r4(r13, this.options);") < out.index("r4 = r5.version;")
