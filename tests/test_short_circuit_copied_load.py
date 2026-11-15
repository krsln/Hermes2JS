"""A later test of an `||`/`&&` chain whose setup copies a register and loads from the copy (F-216, 98/11306).

    for (const item of items) { if (!item || item.type !== "menu" || !item.menu) continue; ... }

Each test after the first sets its operand up with `r9 = r8; r9 = r9.type`. The fold of a test's pure setup into the
condition refused every `Mov`, so the later tests stayed behind the first one as `goto`s to the loop's `continue`.
A copy whose register the same block writes again is not seen by anything outside the block: `r9 = r8; r9 = r9.type`
reads `r8.type`, and the fold takes it when the register is dead on both exits, as for any other pure load.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_the_tests_of_the_chain_are_one_condition():
    hasm = (_DATA / "short_circuit_copied_load_98_11306.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 11306, strict=False), verbose=False, raw=False)
    code = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "goto" not in code
    assert 'if (!r9 || r8.type !== "menu" || !r8.menu) {\n            continue;' in code
