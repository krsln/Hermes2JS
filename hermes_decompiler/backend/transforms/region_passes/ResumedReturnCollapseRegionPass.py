from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import IfRegion, RegionVisitor, SequenceRegion, TryRegion
from hermes_decompiler.ir.expressions import AwaitExpression, Identifier, YieldExpression
from hermes_decompiler.ir.statements import ReturnStatement
from ._base import RegionPass

_RESUME_FLAG_NAME = "__resumeIsReturn"


class ResumedReturnCollapseRegionPass(RegionPass, RegionVisitor):
    """`return await x;` inside a `try`: the second suspend of the pair leaves nothing but a `return`.

    An async function that returns inside a `try` awaits the value once more before it leaves (96/12653):

        try { r3 = await r4.json(); <save>; <resume: r3 = resumed, flag = resumed-is-return> }
        if (flag) { return r3; } else { return r3; }

    Both arms return the register the resume wrote, so the guard decides nothing and the resumed value is the value
    the first await already produced. The resume placeholder (`r3 = await yield`, not valid JavaScript), the flag and
    the guard go, and `return r3;` stays behind the `try`, where the guard stood.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in list(node.children):
            if not isinstance(child, BasicBlock):
                self.visit(child)

        index = 1

        while index < len(node.children):
            guard = node.children[index]

            if isinstance(guard, IfRegion) and self._collapse(node, index - 1, guard):
                node.invalidate_coverage()
                continue

            index += 1

    def _collapse(self, sequence: SequenceRegion, before: int, guard: IfRegion) -> bool:
        if not (isinstance(guard.condition, Identifier) and guard.condition.name == _RESUME_FLAG_NAME):
            return False

        if guard.else_body is None:
            return False

        returned = self._returned_register(guard.then_body)

        if returned is None or returned != self._returned_register(guard.else_body):
            return False

        previous = sequence.children[before]
        body = previous.try_body if isinstance(previous, TryRegion) else None

        if body is None or not body.children or not isinstance(body.children[-1], BasicBlock):
            return False

        resume = body.children[-1]
        pair = resume.instructions

        if len(pair) != 2 or not self._is_the_placeholder(pair[0], returned) or not self._is_the_flag(pair[1]):
            return False

        resume.instructions = []
        body.children = body.children[:-1]
        body.invalidate_coverage()

        kept = guard.then_body.children

        for child in guard.else_body.children:
            if isinstance(child, BasicBlock):
                child.instructions = []

        sequence.children[before + 1:before + 2] = list(kept)

        return True

    @staticmethod
    def _returned_register(arm) -> str | None:
        """`rN` when the arm is one block that only runs `return rN;`."""
        if not isinstance(arm, SequenceRegion) or len(arm.children) != 1:
            return None

        block = arm.children[0]

        if not isinstance(block, BasicBlock) or len(block.instructions) != 1:
            return None

        instruction = block.instructions[0]

        if not isinstance(instruction.statement, ReturnStatement):
            return None

        value = instruction.value

        return value.name if isinstance(value, Identifier) else None

    @staticmethod
    def _is_the_placeholder(instruction, register: str) -> bool:
        value = instruction.value

        return (
            instruction.dest_reg is not None
            and f"r{instruction.dest_reg}" == register
            and isinstance(value, AwaitExpression)
            and isinstance(value.argument, YieldExpression)
            and value.argument.argument is None
        )

    @staticmethod
    def _is_the_flag(instruction) -> bool:
        value = instruction.value

        return isinstance(value, Identifier) and value.name == _RESUME_FLAG_NAME
