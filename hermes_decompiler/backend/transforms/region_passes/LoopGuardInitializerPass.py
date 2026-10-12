from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, LoopKind, LoopRegion, RegionVisitor, SequenceRegion
from hermes_decompiler.backend.transforms.shared import has_side_effects
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import AssignmentOperator, Node
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier
from ._base import RegionPass

logger = get_logger(__name__)


class LoopGuardInitializerPass(RegionPass, RegionVisitor):
    """Gives a `for` loop the initializer its entry guard hides.

    A counting-down loop is compiled as

        r0 = n - 1;                     // the counter's first value
        if (0 <= r0) {                  // entry guard: the loop's own test
            for (; 0 <= r0; r0 = r1 - 1) { ... }
        }

    `LoopConditionRegionPass` only looks at the block that falls into the
    loop, which is the guard's, so the initializer stays outside and the
    loop prints as `for (; 0 <= i; ...)` with `i` never assigned (or, with
    the counter left unnamed, an `if` that repeats the loop's own test).

    When the guard is exactly the loop's own first test (same condition,
    nothing else inside the `if`, no `else`) and the block in front of it
    ends with a plain write of the counter, that write moves into the loop
    header and the guard disappears: a `for` whose condition fails at once
    runs zero iterations, which is what the guard did.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in list(node.children):
            if isinstance(child, IfRegion):
                self._try_hoist(node, child)

        for child in list(node.children):
            self.visit(child)

    def _try_hoist(self, sequence: SequenceRegion, guard: IfRegion) -> None:
        if guard.else_body is not None or guard.condition is None:
            return

        items = guard.then_body.children

        if len(items) != 1 or not isinstance(items[0], LoopRegion):
            return

        loop = items[0]

        if (
                loop.loop_kind != LoopKind.FOR
                or loop.initializer is not None
                or loop.condition is None
                or not isinstance(loop.update, AssignmentExpression)
                or not isinstance(loop.update.left, Identifier)
        ):
            return

        if not (
                isinstance(guard.condition, Node)
                and guard.condition.structurally_equal(loop.condition)
        ):
            return

        index = sequence.children.index(guard)

        if index == 0 or not isinstance(sequence.children[index - 1], BasicBlock):
            return

        block = sequence.children[index - 1]
        name = loop.update.left.name

        for position in range(len(block.instructions) - 1, -1, -1):
            instruction = block.instructions[position]

            if instruction.terminator is not None:
                continue

            if instruction.dest_reg is None or f"r{instruction.dest_reg}" != name:
                if self._mentions(instruction, name):
                    # Something after the counter's write reads it: the
                    # statement has to stay where it is.
                    return
                continue

            value = instruction.value

            if value is None or has_side_effects(value) or self._mentions_node(value, name):
                return

            loop.initializer = AssignmentExpression(
                left=Identifier(name=name), operator=AssignmentOperator.ASSIGN, right=value,
            )
            block.instructions.remove(instruction)
            self.graph.replace(guard, loop)

            logger.debug("loop guard: moved the initializer of %s into the for header", name)
            return

    @staticmethod
    def _mentions_node(node, name: str) -> bool:
        return any(isinstance(n, Identifier) and n.name == name for n in node.walk())

    @classmethod
    def _mentions(cls, instruction, name: str) -> bool:
        for node in (instruction.value, getattr(instruction, "statement", None)):
            if node is not None and cls._mentions_node(node, name):
                return True

        terminator = instruction.terminator

        return terminator is not None and getattr(terminator, "condition", None) is not None \
            and cls._mentions_node(terminator.condition, name)
