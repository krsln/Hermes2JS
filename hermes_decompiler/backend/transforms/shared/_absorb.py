"""Folding an arm into one expression without losing what the arm computed.

`a || b`, `c ? x : y` and `a ?? b` folds keep only the arm's FINAL value and
delete the rest of the arm. That is only right for an instruction nothing
refers to by name. Hermes writes intermediate results into registers, and the
final value names them (`r7 = r7 - 0.1379; r2 = r7 / 7.787`): the fold used to
keep `r7 / 7.787`, silently dropping the subtraction, and `assert` came out as
`r0 = param1 || r0[10](r1)` with the `r1 = "Assertion failed: " + param2` that
`r1` refers to gone.

`absorb_arm_definitions` decides, for every PRINTED definition the arm would
lose, between three outcomes:

- nothing reads its register (a dead write): dropped, as before;
- only the arm's final value reads it: its value is substituted into that
  value (`(r7 - 0.1379) / 7.787`), which is exactly what the register held;
- anything else (the register is read after the merge, the value has side
  effects, a register it reads is overwritten before the final write): the
  fold is refused - the arm stays an `if`.
"""

from __future__ import annotations

import dataclasses

from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier
from ._purity import has_side_effects, prints_definition
from ._repoint import _reads_register_by_name

__all__ = ["absorb_arm_definitions", "substitute_register"]

#: A substituted value that would be copied more than once must stay small.
_MAX_DUPLICATED_NODES = 12


def _count_register(node, name: str) -> int:
    if isinstance(node, Identifier):
        return 1 if node.name == name else 0

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return 0

    total = 0

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if isinstance(child, Node):
                total += _count_register(child, name)

    return total


def _node_count(node) -> int:
    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return 1

    total = 1

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if isinstance(child, Node):
                total += _node_count(child)

    return total


def _registers_named(node) -> set[str]:
    if isinstance(node, Identifier):
        return {node.name}

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return set()

    names: set[str] = set()

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if isinstance(child, Node):
                names |= _registers_named(child)

    return names


def substitute_register(node, name: str, replacement):
    """`node` with every `Identifier(name)` replaced by `replacement`."""
    if isinstance(node, Identifier):
        return replacement if node.name == name else node

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return node

    updates = {}

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        if isinstance(value, Node):
            new_value = substitute_register(value, name, replacement)

            if new_value is not value:
                updates[field.name] = new_value

        elif isinstance(value, tuple):
            new_items = tuple(
                substitute_register(item, name, replacement) if isinstance(item, Node) else item
                for item in value
            )

            if any(new is not old for new, old in zip(new_items, value)):
                updates[field.name] = new_items

    return dataclasses.replace(node, **updates) if updates else node


def absorb_arm_definitions(cfg, arm_instructions, result):
    """The arm's final value with its printed definitions folded in.

    `arm_instructions` are the arm's instructions in order, `result` is the
    one whose value the fold keeps (it may or may not be listed - it is
    skipped). Returns the value to fold, or None if the arm cannot be folded
    without losing a definition. The returned value is `result.value` itself
    when there was nothing to absorb.
    """
    value = result.value
    earlier_list = [instr for instr in arm_instructions if instr is not result]

    for position in range(len(earlier_list) - 1, -1, -1):
        earlier = earlier_list[position]

        if not prints_definition(earlier):
            continue

        register = earlier.dest_reg

        # An expression statement printed without a register is its own
        # observable line; never absorbed here.
        if register is None or has_side_effects(earlier.value):
            return None

        name = f"r{register}"

        # The merge's own write replaces the register; otherwise a read after
        # the merge needs this very definition.
        if register != result.dest_reg and _reads_register_by_name(cfg, register, result.address,
                                                                   ignore_node=result.value):
            return None

        uses = _count_register(value, name)

        if uses == 0:
            continue  # a dead write

        if uses > 1 and _node_count(earlier.value) > _MAX_DUPLICATED_NODES:
            return None

        # What `earlier.value` reads must still hold the same thing when the
        # final value is evaluated: refuse if a later arm instruction
        # overwrites one of those registers.
        read_names = _registers_named(earlier.value)

        for between in earlier_list[position + 1:]:
            if between.dest_reg is not None and f"r{between.dest_reg}" in read_names:
                return None

        value = substitute_register(value, name, earlier.value)

    return value
