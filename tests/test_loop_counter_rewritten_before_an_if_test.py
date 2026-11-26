"""
A loop's counter register is not renamed when the body rewrites it and an `if` test reads it afterwards (96/1931
`reconcileChildFibersImpl`: `r7 = r3.type; if (r7 === r8) {...}` in a loop that counts with r7).

The test of an `if` belongs to the `IfRegion`, no instruction reads it any more, so `_body_writes` saw the write but
no later read and the pass renamed every `r7` it could reach to `i`, the test included: `i === r8` read the counter
where the code meant the type. The tests of the `if`s now count as reads, placed right after the block they replaced.
"""

from types import SimpleNamespace

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, SequenceRegion
from hermes_decompiler.backend.transforms.region_passes.InductionVariableNamingPass import InductionVariableNamingPass
from hermes_decompiler.ir.expressions import Identifier


def _instruction(dest_reg: int, value):
    return SimpleNamespace(name=f"r{dest_reg}", value=value, statement=None, terminator=None)


def _loop(test_reads: str):
    head = BasicBlock(0, 10)
    head.instructions.append(_instruction(7, Identifier("param2")))  # `r7 = <type>`, a write that is no update

    arm = BasicBlock(1, 20)
    arm.instructions.append(_instruction(3, Identifier("r8")))

    test = IfRegion()
    test.condition = Identifier(test_reads)
    test.source_block = head
    test.then_body.append(arm)

    body = SequenceRegion()
    body.append(head)
    body.append(test)

    return SimpleNamespace(body=body, update=None, initializer=None)


def test_a_test_that_reads_the_rewritten_counter_keeps_the_register_name():
    assert InductionVariableNamingPass._body_writes(_loop("r7"), "r7") is True


def test_a_test_that_reads_something_else_changes_nothing():
    assert InductionVariableNamingPass._body_writes(_loop("r9"), "r7") is False
