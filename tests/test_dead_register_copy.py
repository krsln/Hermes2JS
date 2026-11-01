"""
A register copy that nothing reads is removed (F-31), on every path and not only when the
register is overwritten later in the same sequence (`DeadMovEliminationPass`).

- 96/1982 `checkIfSnapshotChanged`: `Mov r0, r2 (param1)` in front of a `try`, overwritten
  before anything reads it (the sequential check cannot see past the `try`).
- 96/12298 `populateParams`: `r1 = param2` in front of `if (!param2)` is dead; without it the
  nested `else { if }` becomes an `else if` chain.

What must stay:
- a copy a tail-merged instruction reads (96/4939: `Mov r16, r18` was copied after the flow
  snapshot, the original is gone) and a write to a parameter's register, whose reads print as
  `paramN` (96/4846, `tests/test_shared_return_widened.py`).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code(name: str, function_id: int) -> str:
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, function_id, strict=False), verbose=False, raw=False)


def test_a_copy_that_nothing_reads_is_removed():
    code = _code("dead_copy_unread_96_1982.hasm", 1982)

    assert "r0 = param1;" not in code
    assert "r0 = param1.value;" in code


def test_a_dead_copy_in_front_of_a_test_no_longer_nests_the_else():
    code = _code("dead_copy_chain_96_12298.hasm", 12298)

    assert "} else if (!param2) {" in code
    assert "r1 = param2;\n        r1 = Object.keys(r1);" in code


def test_a_copy_read_by_a_tail_merged_instruction_stays():
    code = _code("dead_copy_goto_96_4939.hasm", 4939)

    assert "r18 = r23;" in code
    assert "r16 = r18;" in code
