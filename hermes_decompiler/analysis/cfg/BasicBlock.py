from __future__ import annotations

from typing import List

from hermes_decompiler.analysis.terminators import Terminator
from hermes_decompiler.frontend.opcode import OpcodeResult


class BasicBlock:
    """
    `__eq__`/`__hash__` are overridden to be based on `self.id` (a
    monotonically increasing counter assigned once, in a single
    deterministic pass over bytecode addresses, by `CFGBuilder` - see
    that file) rather than falling back to Python's default identity
    (`id()`-address-based) hashing.

    This matters beyond just "two BasicBlock objects with the same id
    should compare equal": several passes put BasicBlocks into a `set`
    (`NaturalLoop.members`/`.exits`, `Region.covered_blocks`, ...), and at
    least one (`IfStructurer._representative_block`) pulls an element
    back out via `next(iter(some_set))`, relying on the assumption that
    "any member is an equally valid representative". That assumption is
    fine in principle, but with the default identity hash, a Python
    `set`'s iteration order depends on each object's memory address -
    which differs between process runs (ASLR, allocation history) even
    for byte-identical input `.hbc` data. The result was exactly the
    symptom reported: the same bytecode structuring differently (a
    proper `while (...) { ... }` vs. a raw `if (...) goto label_N`
    fallback block) across separate runs of the same program.

    Hashing by `self.id` instead makes iteration order of any
    `set[BasicBlock]` - and therefore every decision downstream that
    reads "first"/"any" element from one - fully reproducible for the
    same input, run after run.
    """

    def __init__(self, block_id: int, address: int):
        self.id = block_id
        self.address = address

        self.instructions: List[OpcodeResult] = []
        self.terminator: Terminator | None = None

        self.predecessors: List["BasicBlock"] = []
        self.successors: List["BasicBlock"] = []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BasicBlock):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"BasicBlock(id={self.id}, address={self.address})"

    @property
    def first_instruction(self) -> OpcodeResult | None:
        return self.instructions[0] if self.instructions else None

    @property
    def last_instruction(self) -> OpcodeResult | None:
        return self.instructions[-1] if self.instructions else None

    def add_instruction(self, result: OpcodeResult):
        self.instructions.append(result)
