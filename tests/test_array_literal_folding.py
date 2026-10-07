"""
`NewArray` + `PutOwnByIndex` build an array literal. The element stores used
to be printed as a chained assignment that was ALSO published as a definition
of the array register - `r0 = (r0[0] = param1)[1] = "Woof"` - so the register
ended up holding the LAST ELEMENT ("Woof"), not the array. They now fold into
`r0 = [param1, "Woof"]`, or - when that is not provably equivalent - print as
a plain `r0[i] = v` statement that defines nothing.

The two inputs under tests/data are single sections cut out of a real React
Native hermes-96 bundle (function ids 10215 and 9241).
"""

from __future__ import annotations

import re
from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"
_FIXTURES = Path(__file__).resolve().parents[1] / "apps" / "demo" / "fixtures"


def _decompile(hasm: str, function_id: int) -> str:
    context = Decompiler.build_context(hasm, function_id)
    out = Decompiler.render(context, verbose=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def _fixture(version: str, function_id: int) -> str:
    path = next((_FIXTURES / version / "sections").glob(f"function_{function_id}_*.hasm"))

    return _decompile(path.read_text(encoding="utf-8"), function_id)


_CHAIN = re.compile(r"\(+\s*r\d+\[\d+\] = [^=]")  # `(rN[k] = v)`


def test_elements_fold_into_one_literal():
    # NewArray r0,2 / PutOwnByIndex r0,param1,0 / PutOwnByIndex r0,"Woof",1
    out = _fixture("96", 15202)  # Dog

    assert 'r0 = [param1, "Woof"]' in out
    assert not _CHAIN.search(out)


def test_array_register_is_never_defined_by_an_element_store():
    # `x = (arr[0] = v)` evaluates to v. The old chain made the array
    # register hold the element.
    for function_id in (15045, 15201, 15105, 15189):
        out = _fixture("96", function_id)

        assert not _CHAIN.search(out), function_id
        assert not re.search(r"\br\d+ = r\d+\[\d+\] = ", out), function_id


def test_unfoldable_store_stays_a_plain_statement():
    # The second element's value is a printed statement between the literal
    # and its second store, so folding would reorder it: `r1 = [r6]` then a
    # separate `r1[1] = r9`.
    out = _fixture("96", 15189)

    assert re.search(r"r1 = \[r6\];\n", out)
    assert re.search(r"\n\s*r1\[1\] = r9;\n", out)


def test_ternary_default_keeps_the_array_not_the_element():
    # `Array.isArray(p) ? p : [p]`: NewArray r0,1 / PutOwnByIndex r0,r1,0 /
    # Mov r3,r0. r3 must be the ARRAY - it used to be `r3 = r0[0] = param2`,
    # i.e. param2 itself, so `.reduce` ran on a non-array.
    out = _decompile((_DATA / "array_literal_resolvePath.hasm").read_text(encoding="utf-8"), 10215)

    assert "r0 = [param2]" in out
    assert "r3 = r0;\n" in out
    assert "r3 = r0[0]" not in out


def test_conditional_arm_defining_an_array_is_not_folded_into_a_ternary():
    # The if-arm builds `r7 = [-x, -y, -z]` and the merge write reads
    # `r7[r2]`. ConditionalExpressionRegionPass used to absorb such an arm
    # into `cond ? a : b`, deleting the statement that creates the array.
    out = _decompile((_DATA / "array_literal_in_conditional_arm.hasm").read_text(encoding="utf-8"), 9241)

    assert "r7 = [-r0.x, -r0.y, -r0.z]" in out
    assert "(r8 !== r7) ?" not in out
