"""
`NewObject` + `PutNewOwnById` build an object literal one property at a
time. They fold into `r0 = { "k": v, ... }` when that is exactly equivalent
(see `frontend/handlers/construct/_literal_fold.py`) and otherwise print as
plain `rN.k = v` statements, which define nothing.

Inputs are real hermes-96 fixture sections, a few of them edited (the
property name lives in the opcode's `# String: '...'` comment) to reach
cases the fixtures don't contain.
"""

from __future__ import annotations

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from test_register_semantics import dangling_registers, decompile

_FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures" / "96" / "sections"
_DATA = Path(__file__).parent / "data"


def _section(function_id: int) -> str:
    return next(_FIXTURES.glob(f"function_{function_id}_*.hasm")).read_text(encoding="utf-8")


def _decompile_text(hasm: str, function_id: int) -> str:
    out = Decompiler.render(Decompiler.build_context(hasm, function_id), verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_properties_fold_into_one_literal():
    # NewObject r0 / PutNewOwnByIdShort x3 -> one literal, then `return r0`.
    out = decompile("96", 15146)  # makeCounter

    assert 'r0 = { "increment": increment, "decrement": decrement, "value": value }' in out
    assert not re.search(r"\br0\.(increment|decrement|value) = ", out)
    assert dangling_registers(out) == []


def test_single_property_literal_in_a_branch():
    out = decompile("96", 15102)  # _interopDefault: param1 ? param1 : { default: param1 }

    assert 'r1 = { "default": param1 }' in out


def test_a_property_whose_value_is_a_printed_definition_stays_a_statement():
    # `{ a: 1, d: <another literal built before the store> }`: the inner
    # literal is a printed statement between the outer one and its store,
    # so the store is not folded (it would reorder the inner literal).
    out = decompile("96", 15095)  # objectLiteralTest

    assert re.search(r"r3 = \{[^\n]*\}\n(?:.*\n)*?\s*r2\.d = r3\n", out)
    assert dangling_registers(out) == []


def test_proto_key_is_never_folded():
    # In a literal `{ "__proto__": v }` SETS THE PROTOTYPE; the opcode
    # defines an own data property of that name. Keep it a statement.
    hasm = _section(15102).replace("'default'", "'__proto__'")
    out = _decompile_text(hasm, 15102)

    assert "r1.__proto__ = param1" in out
    assert '"__proto__"' not in out


def test_repeated_key_keeps_the_later_store_as_a_statement():
    # increment, increment(again), value: the duplicate is not folded, and
    # once a store had to stay a statement the register has been read, so the
    # rest stay statements too - order is preserved either way.
    hasm = _section(15146).replace("'decrement'", "'increment'")
    out = _decompile_text(hasm, 15146)

    assert re.search(r'r0 = \{ "increment": \w+ \}', out)
    assert re.search(r"\n\s*r0\.increment = \w+\n", out)
    assert re.search(r"\n\s*r0\.value = \w+\n", out)


def test_literal_definition_in_a_boolean_chain_arm_is_not_dropped():
    # `cond && { color }`: the arm builds `r7 = { "color": ... }` and a later
    # store reads `r7` by name. BooleanChainRegionPass used to absorb the
    # arm ("only pure instructions") and delete the statement building r7,
    # leaving `r5[1] = cond && r7` with no `r7` anywhere.
    hasm = (_DATA / "object_literal_in_boolean_chain_arm.hasm").read_text(encoding="utf-8")
    out = _decompile_text(hasm, 13197)

    assert 'r7 = { "color": param1.tintColor }' in out
    assert "&& r7" not in out
