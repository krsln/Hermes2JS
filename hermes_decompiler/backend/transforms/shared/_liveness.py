"""Register liveness questions the CFG passes ask about hand-built blocks.

The instruction trees were inlined before any control flow was known, so a read of a join register may no longer
name it in the printed tree; the bytecode operands still do. These helpers answer from both.
"""

from __future__ import annotations

import re

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier

OPERAND_REGISTER_RE = re.compile(r"Reg(?:8|32):\s*(\d+)")


def mentions_register(node, name: str) -> bool:
    """Does the tree `node` name the identifier `name` (`r3`)?"""
    if isinstance(node, Identifier):
        return node.name == name

    return isinstance(node, Node) and any(isinstance(n, Identifier) and n.name == name for n in node.walk())


def reads_operand(instruction, register: int) -> bool:
    """Does the BYTECODE instruction read `rN`? The first operand of a writing instruction is its destination."""
    entry = getattr(instruction, "entry", None)
    operands = [int(m) for m in OPERAND_REGISTER_RE.findall(getattr(entry, "args", "") or "")]

    if instruction.dest_reg is not None and operands and operands[0] == instruction.dest_reg:
        operands = operands[1:]

    return register in operands


def is_dead_on_entry(block: BasicBlock, register: int, visited: set) -> bool:
    """True if no path from the start of `block` reads `rN` before writing it."""
    if block in visited:
        return True

    visited.add(block)
    name = f"r{register}"

    for instruction in block.instructions:
        # The bytecode operands are the reads at THIS point. A name inside an inlined value is only where the value
        # was defined (a join read prints the arm's copy: `r2[0] = r3` for a read of r1), so names count only where
        # no operands describe the instruction: a condition merged from several tests, or an instruction a pass made.
        described = bool(
            getattr(getattr(instruction, "entry", None), "args", "")) and instruction.terminator is None
        nodes = [] if described else [
            instruction.value, instruction.statement, getattr(instruction.terminator, "condition", None),
            getattr(instruction.terminator, "value", None),
        ]

        if any(n is not None and mentions_register(n, name) for n in nodes) or reads_operand(instruction, register):
            return False

        if instruction.dest_reg == register and instruction.terminator is None:
            return True

    return all(is_dead_on_entry(succ, register, visited) for succ in block.successors)
