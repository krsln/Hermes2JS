"""Forward jumps that no structurer could express, printed as `label_N: { ... break label_N; ... }`.

A jump out of nested `if` arms to the code right behind them (98/10832: four tests inside the arms of one `if`
all skip to the code that follows it) has no `if`/`else` form without copying that code. JavaScript has a form for
it: a labeled block and a labeled `break`.

    S: [ ..., child i (holds the jump), ..., child j (starts at the target T), ... ]

wraps the children from the first one that holds a jump to T up to child j - 1 in `label_T: { ... }`, and the jump
becomes `break label_T;` (`if (c) break label_T;` for a conditional one). Control that leaves the block by running
off its end reaches child j exactly as before, so nothing else changes: this is only the printed form.

It is the LAST resort of `HermesAnalysis.generate_js`, used on the attempt that still has a `goto` after every
rung: any tree that printed without one keeps the shape it has.
"""

from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopRegion, SequenceRegion, SwitchRegion, TryRegion
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump


class LabeledExitPlan:
    """Which sequences open or close a labeled block, and which jumps print as `break`."""

    _printed: set = set()

    def __init__(self) -> None:
        # (id(sequence), child index) -> labels opened in front of that child, outermost first
        self.opens: dict[tuple[int, int], list[str]] = {}
        # (id(sequence), child index) -> number of blocks closed behind that child
        self.closes: dict[tuple[int, int], int] = {}
        # id(terminator) -> label
        self.breaks: dict[int, str] = {}
        self.sequences: set[int] = set()
        # id(IfRegion) -> (the arm that jumps is the `then` arm, label of the jump target, label of the join)
        self.crossed: dict[int, tuple[bool, str, str, bool]] = {}
        # id(IfRegion) -> index of the first child of the other arm that the jumps land on (0: its start)
        self.crossed_at: dict[int, int] = {}

    def __bool__(self) -> bool:
        return bool(self.breaks)

    def labels(self) -> set[str]:
        return {label for opened in self.opens.values() for label in opened} | {
            label for _, label, _, _ in self.crossed.values()} | {
            join for _, _, join, _ in self.crossed.values()}

    @classmethod
    def build(cls, root) -> "LabeledExitPlan":
        plan = cls()
        jumps: list[tuple[object, int, list[tuple[SequenceRegion, int]]]] = []
        cls._printed = set()
        cls._collect(root, [], jumps)

        # (sequence, target address) -> [first child, target child, terminators]
        wanted: dict[tuple[int, int], list] = {}
        sequences: dict[int, SequenceRegion] = {}
        # (sequence, index of a later `if`, address of the first block of one of its arms) -> [first child, ...]
        split_wanted: dict[tuple[int, int, int], list] = {}

        for terminator, target, stack in jumps:
            for sequence, index in reversed(stack):
                found = next(
                    (j for j in range(index + 1, len(sequence.children))
                     if cls._leading_address(sequence.children[j]) == target),
                    None,
                )

                if found is None:
                    split = next(
                        (j for j in range(index + 1, len(sequence.children))
                         if cls._arm_leading(sequence.children[j], target) is not None),
                        None,
                    )

                    if split is not None:
                        entry = split_wanted.setdefault((id(sequence), split, target), [index, sequence, []])
                        entry[0] = min(entry[0], index)
                        entry[2].append(terminator)
                        break

                    continue

                entry = wanted.setdefault((id(sequence), target), [index, found, []])
                entry[0] = min(entry[0], index)
                entry[2].append(terminator)
                sequences[id(sequence)] = sequence
                break

        by_sequence: dict[int, list[list]] = {}

        for (sequence_id, target), (start, target_child, terminators) in wanted.items():
            by_sequence.setdefault(sequence_id, []).append([start, target_child - 1, f"label_{target}", terminators])

        for sequence_id, ranges in by_sequence.items():
            cls._nest(ranges)
            plan.sequences.add(sequence_id)

            for start, end, label, terminators in sorted(ranges, key=lambda r: (r[0], -r[1])):
                plan.opens.setdefault((sequence_id, start), []).append(label)
                plan.closes[(sequence_id, end)] = plan.closes.get((sequence_id, end), 0) + 1

                for terminator in terminators:
                    plan.breaks[id(terminator)] = label

        cls._split_if(plan, split_wanted, by_sequence)
        cls._cross_arm(root, plan)

        return plan

    @staticmethod
    def _landing(arm, target: int) -> int | None:
        """The index of the child of the arm whose first block is `target`."""
        for position, child in enumerate(arm.children):
            if LabeledExitPlan._leading_address(child) == target:
                return position

        return None

    @staticmethod
    def _arm_leading(node, target: int):
        """(is the `then` arm, index of the child) when a child of one arm of an `if` starts at `target`, else
        None. The `else` arm needs an `else`; a `then` arm without one is entered as well (a jump over its test)."""
        if not isinstance(node, IfRegion):
            return None

        position = LabeledExitPlan._landing(node.then_body, target)

        if position is not None:
            return True, position

        if node.else_body is not None:
            position = LabeledExitPlan._landing(node.else_body, target)

            if position is not None:
                return False, position

        return None

    @classmethod
    def _split_if(cls, plan: "LabeledExitPlan", split_wanted: dict, by_sequence: dict) -> None:
        """A jump that lands on the first block of one ARM of a later sibling `if` (96/2141: `goto 413`, the `then`
        arm of the `if (r16)` behind the code that jumps). The jumping code and the test of the `if` go into the
        labeled block, the other arm leaves the whole by `break join`:

            join: { target: { <code>; if (<the other arm runs>) { other arm; break join; } } this arm }"""
        for (sequence_id, index, target), (start, sequence, terminators) in split_wanted.items():
            ranges = by_sequence.get(sequence_id, [])
            label = f"label_{target}"
            join = f"{label}_end"

            if label in plan.labels() or join in plan.labels():
                continue

            if any(r[0] < start <= r[1] < index or start < r[0] <= index < r[1] for r in ranges):
                continue

            region = sequence.children[index]
            target_is_then, position = cls._arm_leading(region, target)

            if position:
                arm = region.then_body if target_is_then else region.else_body
                plan.crossed_at[id(region)] = position
                plan.sequences.add(id(arm))
                plan.closes[(id(arm), position - 1)] = plan.closes.get((id(arm), position - 1), 0) + 1

            plan.sequences.add(sequence_id)
            plan.opens.setdefault((sequence_id, start), []).extend([join, label])
            plan.closes[(sequence_id, index)] = plan.closes.get((sequence_id, index), 0) + 1
            plan.crossed[id(region)] = (not target_is_then, label, join, True)

            for terminator in terminators:
                plan.breaks[id(terminator)] = label

    @classmethod
    def _cross_arm(cls, node, plan: "LabeledExitPlan") -> None:
        """Jumps from one arm of an `if` onto the first block of the OTHER arm (98/2775: a loop in the `else`
        arm leaves into the code of the `then` arm). No sibling follows the jump, so:

            join: { target: { if (<the jumping arm runs>) { arm; break join; } } other arm }

        a jump onto the other arm becomes `break target;`, the end of the jumping arm `break join;`."""
        if isinstance(node, BasicBlock):
            return

        if isinstance(node, SequenceRegion):
            for child in node.children:
                cls._cross_arm(child, plan)

            return

        if isinstance(node, IfRegion) and node.else_body is not None:
            for jumping_is_then, jumper, other in (
                    (True, node.then_body, node.else_body), (False, node.else_body, node.then_body)):
                landings = {}

                for position, child in enumerate(other.children):
                    address = cls._leading_address(child)

                    if address is not None:
                        landings.setdefault(address, position)

                jumps: list = []
                cls._collect(jumper, [], jumps)

                for address, position in landings.items():
                    mine = [t for t, target, _ in jumps if target == address and id(t) not in plan.breaks]

                    if not mine or f"label_{address}" in plan.labels():
                        continue

                    label = f"label_{address}"

                    for terminator in mine:
                        plan.breaks[id(terminator)] = label

                    plan.crossed[id(node)] = (jumping_is_then, label, f"{label}_end", False)

                    if position:
                        plan.crossed_at[id(node)] = position
                        plan.sequences.add(id(other))
                        plan.closes[(id(other), position - 1)] = plan.closes.get((id(other), position - 1), 0) + 1

                    break

                if id(node) in plan.crossed:
                    break

        for child in cls._children(node):
            cls._cross_arm(child, plan)

    @staticmethod
    def _nest(ranges: list[list]) -> None:
        """Widens a block that only partly overlaps an earlier-ending one so that the two nest."""
        changed = True

        while changed:
            changed = False

            for inner in ranges:
                for outer in ranges:
                    if inner is outer or not inner[0] < outer[0] <= inner[1] < outer[1]:
                        continue

                    outer[0] = inner[0]
                    changed = True

    @classmethod
    def _collect(cls, node, stack, jumps) -> None:
        if isinstance(node, SequenceRegion):
            for index, child in enumerate(node.children):
                here = [*stack, (node, index)]

                if isinstance(child, BasicBlock):
                    cls._printed.add(child)
                    cls._collect_block(child, here, jumps)
                else:
                    cls._collect(child, here, jumps)

            return

        if isinstance(node, BasicBlock):
            return

        for child in cls._children(node):
            cls._collect(child, stack, jumps)

    @staticmethod
    def _collect_block(block: BasicBlock, stack, jumps) -> None:
        for instruction in block.instructions:
            terminator = instruction.terminator

            if instruction.statement is not None or terminator is None:
                continue

            if isinstance(terminator, (TerminatorJump, TerminatorConditionalBranch)):
                jumps.append((terminator, terminator.target, stack))

    @staticmethod
    def _children(region) -> list:
        if isinstance(region, LoopRegion):
            return [region.body]

        if isinstance(region, IfRegion):
            return [region.then_body] + ([region.else_body] if region.else_body is not None else [])

        if isinstance(region, TryRegion):
            return [
                body
                for body in (
                    region.try_body,
                    region.catch.body if region.catch is not None else None,
                    region.finally_.body if region.finally_ is not None else None,
                )
                if body is not None
            ]

        if isinstance(region, SwitchRegion):
            return [case.body for case in region.cases] + ([region.default_body] if region.default_body else [])

        return []

    @classmethod
    def _leading_address(cls, node) -> int | None:
        """The address of the first block `node` prints."""
        while True:
            if isinstance(node, BasicBlock):
                return node.address if node.address >= 0 else None

            if isinstance(node, SequenceRegion):
                if not node.children:
                    return None

                node = node.children[0]
                continue

            if isinstance(node, LoopRegion):
                header = getattr(node, "header_block", None)

                return header.address if header is not None and header.address >= 0 else None

            # An `if` whose test block is not printed anywhere else (its branch became the `if`) starts at that
            # block: 98/5415 lands in front of `if (r27) { ... }`. A test block that is also a sibling in front of
            # it is not a place to land: the sibling is.
            if isinstance(node, IfRegion):
                source = getattr(node, "source_block", None)

                if source is not None and source.address >= 0 and source not in cls._printed:
                    return source.address

            return None
