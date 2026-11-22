"""`if (c) continue;` whose branch targets a second copy of the back edge (98/4271 `VirtualizedList.render`).

The compiler ends the loop body with two blocks that are nothing but `Jmp header`: the normal latch and a second
one only the spacer test (`if (disableVirtualization) <next item>`) jumps to. `ConditionalContinueRegionPass` only
knew a copy that had already been emptied, so the branch stayed `if (r20) goto label_991;`.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _render() -> str:
    hasm = (_DATA / "continue_to_a_second_back_edge_stub_98_4271.hasm").read_text(encoding="utf-8")
    out = Decompiler.render(Decompiler.build_context(hasm, 0, strict=False), verbose=False, raw=False)

    return "\n".join(line for line in out.split("\n") if not line.strip().startswith("//"))


def test_no_goto_is_left():
    assert "goto" not in _render()


def test_the_virtualization_test_continues_with_the_next_item():
    out = _render()

    assert "r20 = r20.disableVirtualization;\n                if (r20) {\n                    continue;\n                }" in out
