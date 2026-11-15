"""
`DeadMovEliminationPass` counts the condition of a branch that stayed raw as a read (F-224, 98/11466).

    r12 = r18; r18 = r13; if (r18) goto BODY;  r18 = r12; if (r18) goto BODY;  <else arm: r18 = r16 ...>

A `goto` the structurers could not remove prints its own condition, but the pass only looked at statements and
values: the copy `r18 = r12` right before the test looked unread (`r18` is written again further on), was dropped,
and `if (r18) goto` tested the value of the first test instead of `r12`.
"""

from pathlib import Path

import pytest

from hermes_decompiler.backend.transforms.cfg_passes.ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass
from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_raw_branch_keeps_the_copy_it_reads(monkeypatch: pytest.MonkeyPatch):
    # The fold of F-225 turns this shape into one condition; without it the branch stays raw.
    monkeypatch.setattr(ShortCircuitConditionCfgPass, "_copy_feeds_the_test", lambda *a, **k: False)
    hasm = (_DATA / "dead_mov_raw_branch_98_11466.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11466, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "r18 = r12;\n            if (r18) goto" in code
