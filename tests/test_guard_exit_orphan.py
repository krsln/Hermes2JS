"""A guard whose exit block no sequence holds still becomes `if (c) { return }` (F-197).

    if (r3) goto L;  ...  L: return undefined      (L has one way in; an earlier pass took it out of the tree)

`GuardExitRegionPass` only moved an exit block that a sequence held. A bare `return undefined` no sequence held
was left as `if (r3) goto label_213` (98/8283 `_handleAnimatedStylesUpdate`). Such a block is the guard's exit
all the same: it is added to the then-body, nothing else prints it.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_a_guard_with_an_orphan_return_exit_has_no_goto():
    out = _render("guard_exit_orphan_98_8283.hasm", 8283)

    assert "goto" not in out
    # The guard's test and the call behind it are one condition (a function with a `for-of` handler no longer
    # keeps the fold off): the call still runs only after `r3` held.
    assert "if (r3 && isStyleAttached.call(0, param1[0])) {\n            return undefined;\n        } else {" in out
