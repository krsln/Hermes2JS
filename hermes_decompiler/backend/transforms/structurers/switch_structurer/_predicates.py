"""Predicates specific to `_ComparisonChainSwitchBuilder`.

Not shared with `_JumpTableSwitchBuilder`: the jump-table path works
directly off a `TerminatorSwitch`'s case_map, so it never needs to ask
whether a block is a spent-setup leftover or whether two arms share a
physical body - those questions only arise when reconstructing a
switch out of the IfRegion chain `IfStructurer` already built.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import SequenceRegion


def same_body(a, b) -> bool:
    """Return True if a and b are the same physical case body.

    True for a shared fall-through region (identity) or when both
    resolve to the same entry-block address.
    """
    if a is b:
        return True
    if a is None or b is None:
        return False

    def _entry_address(body):
        if isinstance(body, BasicBlock):
            return body.address
        if isinstance(body, SequenceRegion) and body.children:
            first = body.children[0]
            if isinstance(first, BasicBlock):
                return first.address
            if hasattr(first, "covered_blocks") and first.covered_blocks:
                return min(first.covered_blocks, key=lambda blk: blk.id).address
        if hasattr(body, "covered_blocks") and body.covered_blocks:
            return min(body.covered_blocks, key=lambda blk: blk.id).address
        return None

    addr_a = _entry_address(a)
    addr_b = _entry_address(b)
    return addr_a is not None and addr_a == addr_b


def is_transparent(item) -> bool:
    """Return True if `item` is a BasicBlock with no visible output.

    Every instruction's value is already consumed elsewhere, and the
    block holds no statement or terminator of its own. IfStructurer
    occasionally leaves this kind of spent setup block (e.g., a
    LoadConstUInt8 that only fed a comparison now folded into the next
    level's condition) immediately before a nested IfRegion; it must
    not be treated as real content that breaks the `else if` chain.
    """
    if not isinstance(item, BasicBlock):
        return False

    for instr in item.instructions:

        if instr.statement is not None:
            return False

        if instr.terminator is not None:
            return False

        if instr.value is not None and not instr.definition_used:
            return False

    return True


def is_empty_or_transparent_body(body) -> bool:
    """Return True if `body` is empty, None, or holds only transparent blocks."""
    if body is None:
        return True
    if isinstance(body, SequenceRegion):
        if len(body.children) == 0:
            return True
        return all(is_transparent(c) for c in body.children)
    return is_transparent(body)
