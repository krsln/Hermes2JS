from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import SequenceRegion

"""
Predicates specific to `_ComparisonChainSwitchBuilder`. Not shared with
`_JumpTableSwitchBuilder`: the jump-table path works directly off a
`TerminatorSwitch`'s case_map, so it never needs to ask whether a block
is a "spent setup" leftover or whether two arms share a physical body -
those questions only arise when reconstructing a switch out of the
`IfRegion` chain `IfStructurer` already built.
"""


def same_body(a, b) -> bool:
    """
    True when two case bodies are the same physical region (shared
    fall-through) or share the same entry block address.
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
    """
    True when `item` is a `BasicBlock` that produces no visible output
    when printed: every instruction's value has already been consumed
    elsewhere and the block holds no statement or terminator of its
    own.

    IfStructurer occasionally leaves exactly this kind of spent setup
    block (e.g. a `LoadConstUInt8` that only fed a comparison now
    folded into the next level's condition) immediately before a
    nested IfRegion. It must not be treated as real content that
    breaks the `else if` chain.
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
    if body is None:
        return True
    if isinstance(body, SequenceRegion):
        if len(body.children) == 0:
            return True
        return all(is_transparent(c) for c in body.children)
    return is_transparent(body)
