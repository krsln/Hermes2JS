"""`this.mode = a.mode || this.mode || null;` keeps its store target (96/3440 and 98/9908 `Request`).

Folding `a.mode || this.mode` repoints every structural copy of the arm's value `this.mode`, and the member the
statement WRITES prints the same, so the store became `a.mode || this.mode = ...` (not valid JavaScript).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "folded_chain_must_not_rewrite_a_store_target_96_3440.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_store_keeps_its_target():
    assert "this.mode = r1.mode || this.mode || null;" in _render()


def test_no_assignment_has_a_logical_expression_as_its_target():
    for line in _render().split("\n"):
        if " = " not in line or line.strip().startswith(("if ", "} else if ", "while ", "for ")):
            continue

        left = line.split(" = ")[0].strip()

        assert " || " not in left and " && " not in left, line
