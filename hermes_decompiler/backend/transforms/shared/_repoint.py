"""Replacing every read of a folded expression with the fold's result.

IR generation resolves a register read ONCE, in bytecode order, and freezes
the defining `Expression` object straight into whatever consumes it. A fold
that later merges that definition into a larger expression (`a || b`,
`c ? x : y`) has to make every such consumer see the merged value:
`repoint_references` walks all of them and swaps the old object for the new
one. Identity is the reliable key; structural equality is only a fallback,
and only for shapes specific enough that a match is the same logical value
(see `repoint_node`).

Consumers live in more places than the instruction list:

- an instruction's `value` and `statement`;
- a block's terminator (`if` conditions, `return`/`throw` arguments,
  `switch` selectors) - `instr.terminator` is the same object as
  `block.terminator`, and both references are updated together;
- expressions already lifted into regions by the structurers that run
  before the region passes: `IfRegion.condition`, a loop's
  condition/initializer/update/iterable, `SwitchRegion.discriminant` and
  each `SwitchCase.tests`.
"""

from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.regions import RegionVisitor
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import Identifier
from ._purity import TRIVIAL_NODE_TYPES, has_side_effects

__all__ = ["repoint_node", "repoint_references", "reclaim_definition", "reclaim_unfolded_definition"]

# A merged expression is copied into terminators / region conditions only up
# to this many nodes. See `repoint_references`.
MAX_INLINED_CONDITION_NODES = 30

# Attributes of a region that hold a single expression.
_REGION_EXPRESSION_ATTRIBUTES = ("condition", "initializer", "update", "iterable", "discriminant")


def repoint_node(node, old_expr, new_expr, *, structural: bool = True):
    """Generic, type-agnostic deep replace of `old_expr` with `new_expr`.

    Every IR node (Expression and Statement, e.g. ReturnStatement) is a
    frozen, slotted dataclass whose fields are a Node (or Node | None) or a
    tuple of them. This walks `dataclasses.fields(node)` generically and
    rebuilds via `dataclasses.replace` wherever a field (or a tuple element)
    is `old_expr` by identity, or contains it - instead of hand-listing every
    wrapper shape, which is what broke silently once before
    (StoreNPToEnvironment).

    Structural equality is a fallback for Mov-introduced COPIES of
    `old_expr`, and only for non-trivial shapes: a bare Identifier or
    Literal is structurally equal to every OTHER unrelated read of the same
    name/value in the function, so matching those structurally would
    rewrite every downstream occurrence, not just the intended one. A
    trivial `old_expr` is therefore matched by identity only.

    Returns (possibly rebuilt node, changed?). Non-Node leaves (str, bool,
    enums, int, None) are returned unchanged.
    """
    if node is old_expr:
        return new_expr, True

    if (structural
            and not isinstance(old_expr, TRIVIAL_NODE_TYPES)
            and isinstance(node, type(old_expr))
            and node.structurally_equal(old_expr)):
        return new_expr, True

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return node, False

    updates = {}

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        if isinstance(value, Node):
            new_value, changed = repoint_node(value, old_expr, new_expr, structural=structural)

            if changed:
                updates[field.name] = new_value

        elif isinstance(value, tuple):
            new_items = []
            tuple_changed = False

            for item in value:
                if isinstance(item, Node):
                    new_item, changed = repoint_node(item, old_expr, new_expr, structural=structural)
                    tuple_changed = tuple_changed or changed
                    new_items.append(new_item)
                else:
                    new_items.append(item)

            if tuple_changed:
                updates[field.name] = tuple(new_items)

    if not updates:
        return node, False

    return dataclasses.replace(node, **updates), True


def _computes_the_same_value(instr, old_expr, structural: bool) -> bool:
    """A definition whose WHOLE value merely equals `old_expr` structurally
    (`r4 = r4[0]` next to an arm's `r6 = r4[0]`) computes that value itself:
    it is not a reader of the arm's, so it must not become `r4 = r6`. A `Mov`
    carrying a copy is the reader the structural fallback exists for."""
    value = instr.value

    return (
            structural
            and value is not old_expr
            and not instr.entry.opcode.startswith("Mov")
            and not isinstance(old_expr, TRIVIAL_NODE_TYPES)
            and isinstance(value, type(old_expr))
            and value.structurally_equal(old_expr)
    )


def _node_count(node, limit: int) -> int:
    """Number of IR nodes under `node`, counting stops once `limit` is hit."""
    count = 1

    if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
        return count

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if isinstance(child, Node):
                count += _node_count(child, limit - count)

                if count >= limit:
                    return count

    return count


def _repoint_terminator(terminator, old_expr, new_expr, structural=True):
    """Terminators are frozen dataclasses but not `Node`s; only their
    expression fields (condition / value / selector) can hold `old_expr`."""
    updates = {}

    for field in dataclasses.fields(terminator):
        value = getattr(terminator, field.name)

        if isinstance(value, Node):
            new_value, changed = repoint_node(value, old_expr, new_expr, structural=structural)

            if changed:
                updates[field.name] = new_value

    if not updates:
        return terminator

    return dataclasses.replace(terminator, **updates)


class _RegionCollector(RegionVisitor):
    def __init__(self) -> None:
        self.regions: list = []

    def visit(self, node) -> None:
        self.regions.append(node)
        super().visit(node)


def repoint_references(
        cfg, root, old_expr, new_expr, *, min_block_id: int, exclude: set, structural: bool = True,
        reader_value=None,
) -> None:
    """Make every consumer of `old_expr` read `new_expr` instead.

    `structural=False` matches by identity only (see `repoint_node`).

    `reader_value(instr)`, when given, picks what each INSTRUCTION reader
    receives instead of `new_expr` (a copy of the merged expression is only
    right while what it names still holds where the reader stands).

    `min_block_id` skips blocks that precede the fold (they cannot read a
    definition made after them); `exclude` are the instructions the fold
    itself owns (their `value` is deliberately left alone).

    Instruction values and statements always receive `new_expr`. Terminators
    and region conditions receive it only while it is small
    (`MAX_INLINED_CONDITION_NODES`): inlining a merged expression into every
    condition of a chain of folds copies it at each step and grows the
    output exponentially (one real function went from 5 KB to 105 KB). A
    condition that is left alone keeps reading the arm's own value, exactly
    as before this pass looked at conditions at all.
    """
    for_conditions = new_expr if _node_count(new_expr,
                                             MAX_INLINED_CONDITION_NODES + 1) <= MAX_INLINED_CONDITION_NODES else None

    replaced_terminators: dict[int, object] = {}
    # The instruction whose branch each terminator expression belongs to: a test is read WHERE the
    # branch stands, so a copy of the merged expression is only right while what it names still
    # holds there (96/1595 `deepDiffer`: `typeof arguments[2]` became `typeof (r5 === undefined ? ...)`
    # after `r5` was reassigned). The same `reader_value` that picks an instruction's copy decides.
    readers: list = []

    def condition_value(reader):
        if reader_value is None or reader is None:
            return for_conditions

        picked = reader_value(reader)

        return for_conditions if picked is new_expr else picked

    def swap(terminator, reader=None):
        if terminator is None:
            return None

        key = id(terminator)

        if key not in replaced_terminators:
            replacement = condition_value(reader)
            readers.append((terminator, reader))
            replaced_terminators[key] = (
                terminator if replacement is None else _repoint_terminator(terminator, old_expr, replacement,
                                                                           structural)
            )

        return replaced_terminators[key]

    for block in cfg.blocks:
        if block.id < min_block_id:
            continue

        for instr in block.instructions:
            if instr.terminator is not None:
                instr.terminator = swap(instr.terminator, instr)

            if instr in exclude:
                continue

            replacement = new_expr if reader_value is None else reader_value(instr)

            if _computes_the_same_value(instr, old_expr, structural):
                new_value, value_changed = instr.value, False
            else:
                new_value, value_changed = repoint_node(instr.value, old_expr, replacement, structural=structural)

            if value_changed:
                instr.value = new_value

            if instr.statement is not None:
                new_statement, statement_changed = repoint_node(instr.statement, old_expr, replacement,
                                                                structural=structural)

                if statement_changed:
                    instr.statement = new_statement

        if block.terminator is not None:
            block.terminator = swap(block.terminator, block.instructions[-1] if block.instructions else None)

    collector = _RegionCollector()
    collector.visit(root)

    for region in collector.regions:
        if for_conditions is None:
            continue

        # A region wholly before the fold cannot read what the fold defines (the same
        # rule the blocks above follow): its test merely LOOKS like the old value.
        covered = getattr(region, "covered_blocks", None)

        if covered and all(b.id < min_block_id for b in covered):
            continue

        # An `if`'s test runs BEFORE its arms: when the instructions the fold
        # owns sit inside the `if`, its condition cannot read what they write
        # (`if (c && arguments[1] !== undefined) { r5 = arguments[1] }` must not
        # become `r5 !== undefined`).
        if (
                region.__class__.__name__ == "IfRegion"
                and exclude
                and any(i in exclude for b in region.covered_blocks for i in b.instructions)
        ):
            continue

        for attribute in _REGION_EXPRESSION_ATTRIBUTES:
            value = getattr(region, attribute, None)

            if isinstance(value, Node):
                replacement = condition_value(_branch_reader(readers, value) or _preceding_reader(region))

                if replacement is None:
                    continue

                new_value, changed = repoint_node(value, old_expr, replacement, structural=structural)

                if changed:
                    setattr(region, attribute, new_value)

        for case in getattr(region, "cases", ()):
            tests = getattr(case, "tests", None)

            if tests:
                case.tests = [repoint_node(test, old_expr, for_conditions, structural=structural)[0] for test in tests]


def _branch_reader(readers, condition):
    """The instruction whose branch the region test `condition` was built from (a terminator
    holding the same expression), or None when no branch can be matched."""
    for terminator, reader in readers:
        if reader is None or not dataclasses.is_dataclass(terminator):
            continue

        for field in dataclasses.fields(terminator):
            held = getattr(terminator, field.name)

            if held is condition or (isinstance(held, Node) and held.structurally_equal(condition)):
                return reader

    return None


def _preceding_reader(region):
    """The last instruction before `region` in its sequence: where its test is read."""
    children = getattr(getattr(region, "parent", None), "children", None)

    if not children:
        return None

    position = next((n for n, child in enumerate(children) if child is region), None)

    for child in reversed(children[:position] if position is not None else ()):
        instructions = getattr(child, "instructions", None)

        if instructions:
            return instructions[-1]

    return None


def _contains(node, target) -> bool:
    """True if `target` occurs inside `node`, by identity."""
    if node is target:
        return True

    if not dataclasses.is_dataclass(node):
        return False

    for field in dataclasses.fields(node):
        value = getattr(node, field.name)

        for child in (value if isinstance(value, tuple) else (value,)):
            if child is not None and not isinstance(child, (str, int, float, bool)) and _contains(child, target):
                return True

    return False


def _is_referenced(cfg, root, target, *, ignore_blocks, ignore_instructions, ignore_regions) -> bool:
    for block in cfg.blocks:
        if block in ignore_blocks:
            continue

        for instr in block.instructions:
            if instr in ignore_instructions:
                continue

            for held in (instr.value, instr.statement, instr.terminator):
                if held is not None and _contains(held, target):
                    return True

        if block.terminator is not None and _contains(block.terminator, target):
            return True

    collector = _RegionCollector()
    collector.visit(root)

    for region in collector.regions:
        if region in ignore_regions:
            continue

        for attribute in _REGION_EXPRESSION_ATTRIBUTES:
            value = getattr(region, attribute, None)

            if isinstance(value, Node) and _contains(value, target):
                return True

        for case in getattr(region, "cases", ()):
            if any(_contains(test, target) for test in (getattr(case, "tests", None) or ())):
                return True

    return False


def reclaim_definition(cfg, root, last, old_value, arm_result, *, ignore_blocks, ignore_regions) -> bool:
    """Make sure a fold's result `last` is actually PRINTED.

    A definition read while it was current is inlined into its reader and
    flagged `definition_used`, which suppresses its own statement. For
    `r = a; if (!r) r = b` that reader is the `if`'s condition - the very
    region the fold deletes - so after `r = a || b` no statement remains:
    later readers see `rN` assigned nowhere (the missing `r5 = param1`).

    If the only reader of `old_value` was that deleted condition, the flag is
    stale and is cleared. Left alone when:

    - the arm's result (`arm_result`) was itself consumed inline: those
      readers now hold the whole merged expression, so `last` is already
      spelled out where it is used and printing it too would only repeat it;
    - `old_value` is still referenced elsewhere;
    - `old_value` has side effects (printing it as well as inlining it would
      run it twice).

    Returns True if `last` is (now) printed as its own statement.
    """
    if not last.definition_used:
        return True

    if arm_result.definition_used or has_side_effects(old_value):
        return False

    if _is_referenced(
            cfg, root, old_value,
            ignore_blocks=ignore_blocks,
            ignore_instructions={last},
            ignore_regions=ignore_regions,
    ):
        return False

    last.definition_used = False

    return True


def _reads_register_by_name(cfg, register: int, after_address: int, ignore_node=None, root=None) -> bool:
    """True if, going forward in bytecode order from `after_address`, some
    consumer refers to register `rN` BY NAME before `rN` is written again.

    That is the bytecode reading the register after the merge, so an
    assignment to it must exist in the output. The redefinition stop matters:
    Hermes reuses low registers as temporaries all over a function, so the
    name `r0` appearing SOMEWHERE later says nothing about THIS value.
    """
    name = f"r{register}"

    def holds_name(node) -> bool:
        # An inlined copy of the arm's own value reads the register too, but
        # the fold repoints those copies to the folded expression.
        if ignore_node is not None and node is ignore_node:
            return False

        if isinstance(node, Identifier):
            return node.name == name

        if not dataclasses.is_dataclass(node):
            return False

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            for child in (value if isinstance(value, tuple) else (value,)):
                if child is not None and not isinstance(child, (str, int, float, bool)) and holds_name(child):
                    return True

        return False

    # An `if` the structurers already built keeps its test in the region, not
    # in a terminator, so a bare `if (r5)` is only visible through `root`. It
    # is read just before the region's first block.
    events = [
        (instr.address, 1, [instr.value, instr.statement, instr.terminator], instr.dest_reg)
        for block in cfg.blocks for instr in block.instructions if instr.address > after_address
    ]

    if root is not None:
        collector = _RegionCollector()
        collector.visit(root)

        for region in collector.regions:
            condition = getattr(region, "condition", None)
            covered = region.covered_blocks if condition is not None else None

            if covered:
                start = min(block.address for block in covered)

                if start > after_address:
                    events.append((start - 0.5, 0, [condition], None))

    for _, _, held_nodes, dest_reg in sorted(events, key=lambda event: event[:2]):
        for held in held_nodes:
            if held is not None and holds_name(held):
                return True

        if dest_reg == register:
            return False

    return False


def reclaim_unfolded_definition(cfg, root, last, arm_result, *, ignore_blocks, ignore_regions) -> None:
    """The same stale flag as in `reclaim_definition`, for a merge the fold
    passes LEFT as an `if`: `rN = a; if (!a) { ...; rN = b }`.

    The `if`'s condition inlines `a` and flags `rN = a` as used, so it is not
    printed - yet later code reads `rN` by name, and on the path that skips
    the `if` nothing assigned it. Only acted on when such a by-name read
    exists (otherwise the assignment really is dead) and the arm's result was
    not itself consumed inline. "Such a read" means one that follows the arm in
    bytecode order with no write to the register in between.
    """
    if not last.definition_used or arm_result.definition_used:
        return

    if not _reads_register_by_name(cfg, last.dest_reg, arm_result.address):
        return

    reclaim_definition(
        cfg, root, last, last.value, arm_result,
        ignore_blocks=ignore_blocks, ignore_regions=ignore_regions,
    )
