"""
`||` / `?:` folds must not lose what the folded arm computed
(`shared/_absorb.py`).
"""

from __future__ import annotations

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared import substitute_register
from hermes_decompiler.ir.expressions import BinaryExpression, Identifier
from hermes_decompiler.ir.Operators import BinaryOperator

from tests.test_repoint_references import LAB_TO_XYZ


def test_substitute_register_replaces_every_use():
    one = Identifier(name="param1")
    expr = BinaryExpression(left=Identifier(name="r7"), operator=BinaryOperator.ADD, right=Identifier(name="r7"))

    out = substitute_register(expr, "r7", one)

    assert out.left is one and out.right is one
    assert substitute_register(expr, "r9", one) is expr


def test_lab_ternary_keeps_the_subtraction_the_arm_computed():
    out = Decompiler.render(Decompiler.build_context(LAB_TO_XYZ, 12962), verbose=False)

    # `r7 = r7 - 0.1379; r2 = r7 / 7.787` used to fold to `r7 / 7.787`.
    assert "(r7 - 0.13793103448275862) / 7.787" in out
    assert "(r6 - 0.13793103448275862) / 7.787" in out
    assert "(r4 - 0.13793103448275862) / 7.787" in out


def test_destructuring_guard_keeps_the_assignment_in_the_arm():
    # hermes-98 `parameterDestructureTest`: `r6 = r4` used to vanish together
    # with the folded `r3 === undefined || r3 === undefined`.
    root = Path(__file__).resolve().parent.parent / "apps/demo/fixtures/98/sections"
    path = root / "function_9488_parameterDestructureTest.hasm"
    out = Decompiler.render(Decompiler.build_context(path.read_text(encoding="utf-8"), 9488, strict=False), verbose=False)

    assert "r6 = r4" in out
    assert "r3 === undefined || r3 === undefined" not in out
