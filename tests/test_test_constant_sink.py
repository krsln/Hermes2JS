"""The constant a test loads for the join moves onto the edge that jumps there (F-190/F-227, 98/2304).

    r5 = "focus";             if (p === 8)  goto L
    r5 = "windowStateChange"; if (p === 32) goto L
    r5 = "click";             if (p === 1)  goto L
    r5 = "viewHoverEnter";    if (p === 128) goto L
    <report, return>
    L: ... r5 ...

The bytecode hoists each constant in front of its test. The first output kept a `goto` AND printed only the last
constant at `L` (`sendAccessibilityEvent(r3, "viewHoverEnter")`); with the load on the taken edge the tests become
a `switch` and `L` reads the register.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "test_constant_sink_98_2304.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 2304, strict=False), verbose=False, raw=False)
    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_each_test_assigns_its_own_constant():
    code = _render()

    assert "goto" not in code
    for constant in ("focus", "windowStateChange", "click", "viewHoverEnter"):
        assert f'r5 = "{constant}";' in code


def test_the_join_reads_the_register_not_one_constant():
    code = _render()

    assert "sendAccessibilityEvent(r3, r5)" in code
    assert 'sendAccessibilityEvent(r3, "' not in code
