"""A value diamond with ONE call in an arm, tested as the next link of an `&&` chain (98/12704 `_initBody`).

`else if (support.arrayBuffer && support.blob && isDataView(body))` compiles to
`X: if (!arrayBuffer || !blob) goto T; r7 = body && DataView.prototype.isPrototypeOf(body) [a diamond]; M: if (r7) goto DVARM; T: ...`.
`ValueConditionFoldCfgPass` only folded diamonds whose arms were all pure, so the diamond stayed three blocks and
`T` was entered from X and from M's fall-through: the printed `if (r7) goto label_442;` jumped to the very code below
it and the not-DataView path (`T`) was lost. A call evaluated inside the value runs on the same path as in the arm,
so ONE of them is allowed when the diamond is that link of a chain (`_crossed_into`); the receiver the call keeps by
name (`r9 = DataView.prototype; r9.isPrototypeOf(p)`) goes into the value.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render(name, index):
    hasm = (_DATA / name).read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, index, strict=False), verbose=False, raw=False)


def test_the_dataview_test_joins_the_and_chain():
    out = _render("value_diamond_with_call_98_12704.hasm", 12704)

    assert "goto" not in out
    assert "r5.arrayBuffer && r5.blob && (param1 && DataView.prototype.isPrototypeOf(param1))" in out


def test_a_guarded_call_in_the_condition_reads_the_right_register():
    out = _render("value_diamond_with_call_98_9957.hasm", 9957)

    assert "param1 === r3 && (r1[0] && r1[0].onDismiss)" in out
    assert "r4 = r1[0];\n            r3 = r4.onDismiss();" in out
