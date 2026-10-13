"""
`is_inert_block` lets IfStructurer look past clutter when deciding whether an
`if` is the sole meaningful content of an arm (`a && b`, `a || b` folds). A
definition that still PRINTS (`r2 = 1`, `r6 = r4`) is a statement later code
may read by name, so a block holding one is not clutter: folding past it
deletes its only definition (reverting this adds 19 path-flagged functions
over the 96/98 bundles).
"""

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.ir.expressions import NumericLiteral
from hermes_decompiler.backend.transforms.structurers.if_structurer._predicates import is_inert_block


def _block_with(definition_used: bool) -> BasicBlock:
    entry = OpcodeEntry("LoadConstUInt8", "0x0", opcode="LoadConstUInt8", args="Reg8: 2, UInt8: 1")
    result = OpcodeResult(entry, value=NumericLiteral(value=1), dest_reg=2)
    result.definition_used = definition_used

    block = BasicBlock(1, 0)
    block.instructions.append(result)

    return block


def test_block_without_instructions_is_inert():
    assert is_inert_block(BasicBlock(1, 0))


def test_block_with_a_printed_definition_is_not_inert():
    assert not is_inert_block(_block_with(definition_used=False))
