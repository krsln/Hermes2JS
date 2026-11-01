"""
A folded ternary is not copied into a test that reads after its register changed (F-140, 96/1595 `deepDiffer`).

    r1 = arguments[2] ... r5 === undefined ? -1 : arguments[2]   # the defaulted `maxDepth`
    r5 = arguments.length <= 3 ? undefined : arguments[3]        # `r5` now holds something else
    if (typeof r1 === "number") ...                              # the test reads the merge

`repoint_references` gave terminators and region conditions the ternary unconditionally, so the
tests printed `typeof (r5 === undefined ? -1 : arguments[2])` with the stale `r5`. They now take the
same per-reader decision as an instruction does (the register when the ternary's test was reassigned).
"""

from pathlib import Path

from hermes_decompiler.Decompiler import Decompiler

_DATA = Path(__file__).parent / "data"


def _code() -> str:
    hasm = (_DATA / "folded_ternary_stale_test_96_1595.hasm").read_text(encoding="utf-8")

    return Decompiler.render(Decompiler.build_context(hasm, 1595, strict=False), verbose=False, raw=False)


def test_a_test_after_the_ternary_register_changed_reads_the_register():
    code = _code()

    assert code.count('if (typeof r1 === "number") {') == 2
    assert "typeof (r5 === undefined" not in code


def test_a_copy_in_a_loop_is_not_read_by_a_branch_the_write_cannot_reach():
    # F-140: `r17 = r6` (the recursive call's argument, in the loops) made `r6 != null` in the
    # `typeof function` branch print `r17 != null`; nothing sets `r17` on that path.
    code = _code()

    assert "r17 != null" not in code
    assert "if (r6 != null) {" in code


def test_a_merge_repair_does_not_touch_an_identical_value_in_the_other_arm():
    # F-150, 96/2065 `updateClassComponent`: the update path's chain contains the mount path's
    # `A && B` as an inner part; repairing the mount path's merge turned it into `r19`, a register
    # the update path never sets.
    hasm = (_DATA / "merge_repair_other_arm_96_2065.hasm").read_text(encoding="utf-8")
    code = Decompiler.render(Decompiler.build_context(hasm, 2065, strict=False), verbose=False, raw=False)

    assert "UNSAFE_componentWillReceiveProps && r19;" not in code
    # F-151: the chain is `A && B`, not `A && (A && B)` (the other copy's fold had rewritten this
    # copy's right operand before this one folded).
    assert code.count(
        'r11 = "function" !== typeof r10.UNSAFE_componentWillReceiveProps'
        ' && "function" !== typeof r10.componentWillReceiveProps;'
    ) == 2


def test_the_merge_check_builds_one_dominator_tree_per_pass():
    # F-143, 98/2619 `beginWork`: `_register_holds_merge` built a tree on every call (170 times,
    # minutes). The CFG's edges do not change while the pass runs, so one tree serves all calls.
    from hermes_decompiler.backend.analysis.dominance.DominatorTree import DominatorTree
    from hermes_decompiler.backend.transforms.region_passes.ConditionalExpressionRegionPass import (
        ConditionalExpressionRegionPass,
    )

    trees = []
    original_check = ConditionalExpressionRegionPass._register_holds_merge

    def counting_check(self, *args, **kwargs):
        before = DominatorTree.compute
        calls = []

        def compute(tree):
            calls.append(1)
            return before(tree)

        DominatorTree.compute = compute

        try:
            return original_check(self, *args, **kwargs)
        finally:
            DominatorTree.compute = before
            trees.append(len(calls))

    ConditionalExpressionRegionPass._register_holds_merge = counting_check

    try:
        _code()
    finally:
        ConditionalExpressionRegionPass._register_holds_merge = original_check

    # (the generator may run the pass again for a retry: one tree per pass, not per call)
    assert len(trees) >= 6, "the function no longer exercises the check"
    assert sum(trees) * 3 <= len(trees)
