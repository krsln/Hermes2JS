"""
A pure setup load folded into the second test of a short-circuit pair
(`ShortCircuitConditionCfgPass._fold_pure_setup`) is dropped with its block, so
it is only exact when nothing reads what it wrote.

- `getNavigateAction` (98/6009): the block `r7 = r4.type; r9 = "NAVIGATE"; if (r7 !==
  "stack")` writes `r9`, which the code after the `if` reads (the `type` of the
  action). Readers were inlined linearly, before control flow was known, so by
  NAME the register looks dead; the bytecode operands say otherwise. Folding it
  lost the whole `else { r9 = "NAVIGATE" }` arm and left `r9` unassigned.
- `startTimespan` (96/3349): the folded `arguments[1] !== undefined` is the same
  expression the `then` arm assigns to `r5`; a repair that repoints copies of
  the arm's value must not rewrite the `if`'s OWN condition (it runs before the
  arm), or the test reads `r5` before anything set it.
"""

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_register_read_after_the_pair_keeps_its_definition():
    out = _render("getNavigateAction_98_6009.hasm", 6009)

    # The write stays in the `else` arm, in front of the `stack` test (the shape changed with the larger tail
    # copy of F-217, which made the function goto-free: the test no longer fixes the indentation).
    assert re.search(r'\} else \{\n\s+r7 = r4\.type;\n\s+r9 = "NAVIGATE";\n\s+if \(r7 === "stack"\)', out)
    assert "goto" not in out


def test_if_condition_is_not_repointed_to_its_own_arms_register():
    out = _render("startTimespan_96_3349.hasm", 3349)

    assert "r4 > 1 && arguments[1] !== undefined" in out
    assert "r5 !== undefined" not in out
