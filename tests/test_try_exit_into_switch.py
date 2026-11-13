"""`try { ...; } catch {}` at the end of an `if`, with a `switch` behind it: the try's own jump is no `goto` (98/2636).

`commitDeletionEffectsOnFiber`: `if (hook && typeof hook.onCommitFiberUnmount === "function") { try { ... } catch {} }`
and then `switch (param3.tag)`. The try body ends in a jump over the handler to the switch's header block. The next
statement being a `switch` (a compound region whose header block the tree no longer holds), `RedundantJumpRegionPass`
could not say where control resumes and left `goto label_47`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_jump_over_the_handler_into_the_switch_is_dropped():
    hasm = (_DATA / "try_exit_into_switch_98_2636.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2636, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert "} catch (caughtException) {\n        }\n    }\n    switch (param3.tag) {" in code
