"""A `default:` arm that ends in its own `jmp loop-head` leaves the switch like the code behind it does (98/2204).

`parseDropShadowString`: the loop body is `if (...) {...} else { switch (...) {...} }`. Cases 0 and 1 fall into the
code behind the switch, which is an empty block `jmp loop-head` (0xd7); the `default:` arm ends in ANOTHER empty
`jmp loop-head` (0xb7). `RedundantJumpRegionPass._reaches_exit` only followed empty blocks that fall on into the exit,
so the default arm kept `goto label_183; break;`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_default_arm_ends_in_a_break():
    hasm = (_DATA / "switch_exit_trampoline_98_2204.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2204, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "r13 = r15 + 1;\n                    break;\n            }" in code
