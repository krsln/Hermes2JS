"""A `for` update keeps reading the induction register when the alias copy is rewritten only on an exit path.

`r5 = r1; if (r6 === param1) { r1 = r4.completion; r5 = r1.type; ...; return r0 } ... r1 = r5 - 1`: the exit arm
rewrites both `r5` and `r1`, so `LoopInductionAliasPass` refused to fold the alias and the update printed
`r1 = r5 - 1`. The update only runs on paths that reach a latch, and neither register is written on those
(96/3146 `catch`, 8596 `cloneRecursive`; regression of F-266 which made the exit arm structure).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_update_reads_the_induction_register():
    hasm = (_DATA / "loop_update_alias_rewritten_on_exit_path_96_3146.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 3146, strict=False), verbose=False, raw=False)

    assert "r1 >= 0; r1--)" in out
    assert "r1 = r5 - 1" not in out
    assert 'r5 === "throw"' in out
