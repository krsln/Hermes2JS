"""`a || b` whose second test reads a register END reads too (F-203).

    if (c1) goto A;  r10 = env[296];  if (r10 !== 0) goto END;  A: ...chain...;  jmp JOIN;   END: r8 = r10 & -r10

The crossed fold takes the pure setup of the second test into the condition only when the register is dead
afterwards; END reads it. A constant load got its own copy on the edge into END (96/1139); an environment slot is
the same (nothing between the test and END writes it), so the test reads `r9[296]` itself and END reloads it:

    if (0 !== r0 && 0 !== r9[296]) { r10 = r9[296]; r8 = r10 & -r10 } else { ...chain... }

98/2654 `requestUpdateLane` kept `if (0 !== r10) goto label_226` before.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_test_behind_an_environment_load_that_the_end_reads_is_one_condition():
    out = _render("short_circuit_env_load_98_2654.hasm", 2654)

    assert "goto" not in out
    assert "if (0 !== r0 && 0 !== r9[296]) {\n            r10 = r9[296];\n            r8 = r10 & -r10;" in out
