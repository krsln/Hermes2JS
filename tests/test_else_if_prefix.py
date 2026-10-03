"""
`else { <prefix>; if (c) {...} }` prints as a flat `else if (c)` only when the
prefix is clutter. A prefix that DEFINES a register the nested condition reads
(`r1 = param1.length`) must stay: dropping it leaves `else if (r1 === 1)` with
no `r1`. Only constant loads (`r1 = 5`, the value is already embedded in the
nested condition) may be looked past.

Measured over the full hermes-96/98 bundles, this removes 79 of 261 (96) and
64 of 362 (98) dangling registers, with none introduced.
"""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.transforms.shared import prints_non_constant_statement
from hermes_decompiler.ir.expressions import Identifier, Literal, MemberExpression, NumericLiteral
from test_register_semantics import decompile

_DATA = Path(__file__).parent / "data"


def _instruction(value, definition_used=False):
    return SimpleNamespace(value=value, definition_used=definition_used)


def test_non_constant_definition_is_a_printing_statement():
    member = MemberExpression(obj=Identifier(name="param1"), prop=Identifier(name="length"), computed=False)

    assert prints_non_constant_statement(_instruction(member))
    assert prints_non_constant_statement(_instruction(Identifier(name="r4")))


def test_constant_load_is_not():
    assert not prints_non_constant_statement(_instruction(NumericLiteral(value=5)))
    assert isinstance(NumericLiteral(value=5), Literal)


def test_folded_definition_prints_nothing():
    member = MemberExpression(obj=Identifier(name="param1"), prop=Identifier(name="length"), computed=False)

    assert not prints_non_constant_statement(_instruction(member, definition_used=True))
    assert not prints_non_constant_statement(_instruction(None))


def test_definition_read_by_the_nested_condition_is_kept():
    # `if (a) return; else if (param1.length === 1) return undefined;` -
    # the else branch is `r1 = param1.length; if (r1 === 1) ...`.
    hasm = (_DATA / "else_if_prefix_definition.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 7547), verbose=False)
    out = "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))

    assert "r1 = param1.length" in out
    assert "else if (r1 === 1)" not in out
    assert out.index("r1 = param1.length") < out.index("if (r1 === 1)")


def test_generator_state_is_loaded_before_the_state_check():
    # `else if (r12 === 3)` used to read r12 with `r12 = r1[0]` gone.
    out = decompile("98", 12484)

    assert "r12 = r1[0]" in out
    assert "else if (r12 === 3)" not in out
    assert out.index("r12 = r1[0]") < out.index("if (r12 === 3)")
