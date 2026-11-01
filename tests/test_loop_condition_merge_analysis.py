"""
Two loop tests that both leave the loop are merged into one `||` (F-129). The test
block that merged away used to stay a member of the loop (and a node of the dominator
trees) the earlier analyses had found, and the structurer failed on it with an
`IndexError` (96/2075, 2264, 2581, 2590, 13786; 98/2617).

The analyses are recomputed once the merge pass has changed the graph.
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def test_a_loop_test_merged_away_does_not_stay_in_the_loop_analysis():
    """96/2264 `pop` (a heap sift-down): rendering used to raise."""
    hasm = (_DATA / "loop_tests_merged_stale_analysis_96_2264.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2264, strict=False), verbose=False, raw=False)

    assert out.startswith("function pop(param1)")


def test_a_merged_away_test_block_leaves_the_try_blocks_of_its_handler():
    """96/2146 `throwAndUnwindWorkLoop`: the handler still listed the merged block, so the
    dominator tree computed again afterwards looked it up and raised a `KeyError`."""
    hasm = (_DATA / "loop_tests_merged_in_try_96_2146.hasm").read_text(encoding="utf-8")

    out = Decompiler.render(Decompiler.build_context(hasm, 2146, strict=False), verbose=False, raw=False)

    assert out.startswith("function throwAndUnwindWorkLoop(")
