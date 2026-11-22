"""A forward jump no structurer could express prints as a labeled block with `break label_N;` (F-301).

98/10832: four tests in the arms of one `if` skip to the code behind it (`r6 = undefined; if (!r9[4]) ...`). Copying
that code into every arm is not an option and `if`/`else` has no form for it, but JavaScript has: `label_276: { ... }`
around the arm and `break label_276;` for the jump. It is the last resort of `generate_js`: only an attempt that still
has a `goto` after every rung is printed this way.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.backend.emit.printer._labeled_exits import LabeledExitPlan

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "forward_jumps_out_of_nested_arms_98_10832.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)


def test_the_jumps_become_labeled_breaks_and_no_goto_is_left():
    out = _render()

    assert "goto" not in out
    assert "NOT valid JavaScript" not in out
    assert "    label_276: {\n" in out
    assert "break label_276;" in out


def test_the_code_the_jumps_skip_to_follows_the_labeled_block():
    out = _render()
    block = out.split("label_276: {\n")[1]
    # the block is closed at the indentation of its label, and the skipped-to code comes right behind it
    closing = block.index("\n        }\n")

    assert block[closing + len("\n        }\n"):].lstrip().startswith("r6 = undefined;")


def test_blocks_that_only_overlap_in_part_are_nested():
    ranges = [[0, 2, "label_a", []], [1, 4, "label_b", []]]

    LabeledExitPlan._nest(ranges)

    assert ranges[1][:2] == [0, 4]
    assert ranges[0][:2] == [0, 2]


def test_a_jump_to_the_test_of_a_later_if_lands_in_front_of_that_if():
    # 98/5415 `getPatternParts`: the `default:` arm of a `switch` jumps to the test block of the `if (r27)` behind it,
    # which is not printed as a block of its own: the `if` itself is the later sibling the label closes in front of.
    hasm = (_DATA / "labeled_break_to_an_if_test_98_5415.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    assert "goto" not in out
    assert "if (r30) break label_737;" in out
    assert out.index("label_737: {") < out.index("switch (r31)")
    assert out.index("if (r27) {") > out.index("break label_737;")
