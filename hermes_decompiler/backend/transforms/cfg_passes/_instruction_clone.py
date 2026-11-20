"""One way to copy an instruction for a block a pass duplicates.

Passes tell writers apart by the identity of the value they hold: a copy that shares the node with the original is
folded together with it (96/12456: `r1 = []` vanished from the copy). So the value and the statement are deep
copies, never shared.
"""

from __future__ import annotations

import copy

_COPY = object()


def clone_instruction(instruction, *, terminator=_COPY, memo=None, statement: bool = True):
    """A copy of `instruction` that shares no value node with it.

    `terminator`: left out, the terminator is copied (a copy of it, not the object); `None`, the clone has none;
    any other terminator replaces the instruction's own when it has one (the clone of a block's last instruction).
    `memo` is the `copy.deepcopy` memo, shared by the instructions of one block copied together.
    `statement=False` leaves the statement as it is (a copy of a plain `Mov` has none).
    """
    duplicate = copy.copy(instruction)
    duplicate.value = copy.deepcopy(instruction.value, memo)

    if statement:
        duplicate.statement = copy.deepcopy(instruction.statement, memo)

    original = instruction.terminator

    if terminator is _COPY:
        duplicate.terminator = copy.copy(original) if original is not None else None
    elif original is None:
        duplicate.terminator = None
    else:
        duplicate.terminator = terminator

    return duplicate
