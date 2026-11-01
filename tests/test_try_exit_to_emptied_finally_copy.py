"""A try body's jump to the finally copy it ends in is dropped once the copy is gone (F-164).

    try { ...; jmp COPY } catch { ... }   COPY: <finally copy>; ret

`_FinallyAttacher` strips the copy and the emptied block is pruned, so the jump named an address no sibling had
any more and printed as `goto label_66` right before the `catch`. A target that is an emptied block running on
into the exit address is the exit.

    96/4085  `flush`
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_try_body_ends_without_a_goto():
    hasm = (_DATA / "try_exit_to_emptied_finally_copy_96_4085.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 4085, strict=False), verbose=False, raw=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in out
    assert out.count("finally {") == 1
    assert out.index("r3 = r5.enqueue(r3);") < out.index("} catch")
