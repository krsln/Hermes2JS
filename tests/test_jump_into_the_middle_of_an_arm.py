"""
A jump that lands in the MIDDLE of the other arm of an `if`, or in the middle of an arm of a later `if` that has no
`else`, prints as labeled blocks (F-322, 98/3523 `parseURL`: a URL-state machine whose `goto`s were left after every
rung). The tests build the region trees by hand, the real function takes over a minute to render.
"""

from types import SimpleNamespace

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.emit.printer._labeled_exits import LabeledExitPlan
from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.ir.terminators import TerminatorJump


def _block(block_id: int, address: int, jumps_to: int | None = None) -> BasicBlock:
    block = BasicBlock(block_id, address)
    terminator = TerminatorJump(jumps_to) if jumps_to is not None else None
    block.instructions = [SimpleNamespace(statement=None, terminator=terminator)] if terminator else []

    return block


def _sequence(*children) -> SequenceRegion:
    sequence = SequenceRegion()

    for child in children:
        sequence.append(child)

    return sequence


def test_a_jump_into_the_middle_of_the_other_arm_is_a_labeled_break():
    # if (c) { A; B; C } else { goto C }   -- the `else` arm lands on C, the third block of the `then` arm
    jump = _block(3, 30, jumps_to=12)
    region = IfRegion()
    region.then_body = _sequence(_block(0, 10), _block(1, 11), _block(2, 12))
    region.else_body = _sequence(jump)

    root = _sequence(region)
    plan = LabeledExitPlan.build(root)

    assert plan.breaks[id(jump.instructions[0].terminator)] == "label_12"
    assert plan.crossed[id(region)][1:3] == ("label_12", "label_12_end")
    assert plan.crossed_at[id(region)] == 2
    # the two blocks in front of the landing are inside the labeled block, which the arm's sequence closes
    assert plan.closes[(id(region.then_body), 1)] == 1


def test_a_jump_into_the_middle_of_a_later_if_without_else_is_a_labeled_break():
    # goto C; ...; if (c) { A; B; C }   -- the code in front of the `if` jumps over its test onto C
    jump = _block(0, 5, jumps_to=22)
    region = IfRegion()
    region.then_body = _sequence(_block(1, 20), _block(2, 21), _block(3, 22))
    region.else_body = None

    root = _sequence(jump, region)
    plan = LabeledExitPlan.build(root)

    assert plan.breaks[id(jump.instructions[0].terminator)] == "label_22"
    assert plan.crossed[id(region)] == (False, "label_22", "label_22_end", True)
    assert plan.crossed_at[id(region)] == 2
    assert plan.opens[(id(root), 0)] == ["label_22_end", "label_22"]
