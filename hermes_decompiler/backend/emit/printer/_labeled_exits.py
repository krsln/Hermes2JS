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

    def __bool__(self) -> bool:
        return bool(self.breaks)

    @classmethod
    def build(cls, root) -> "LabeledExitPlan":
        plan = cls()
        jumps: list[tuple[object, int, list[tuple[SequenceRegion, int]]]] = []
        cls._printed = set()
        cls._collect(root, [], jumps)

        # (sequence, target address) -> [first child, target child, terminators]
        wanted: dict[tuple[int, int], list] = {}
        sequences: dict[int, SequenceRegion] = {}

        for terminator, target, stack in jumps:
            for sequence, index in reversed(stack):
                found = next(
                    (j for j in range(index + 1, len(sequence.children))
                     if cls._leading_address(sequence.children[j]) == target),
                    None,
                )

                if found is None:
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

        return plan

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
