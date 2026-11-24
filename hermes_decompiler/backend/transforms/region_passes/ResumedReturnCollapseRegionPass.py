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

        if not self._same(guard.then_body, guard.else_body):
            return False

        previous = sequence.children[before]
        body = previous.try_body if isinstance(previous, TryRegion) else None

        if body is None or not body.children or not isinstance(body.children[-1], BasicBlock):
            return False

        resume = body.children[-1]
        pair = resume.instructions

        if len(pair) != 2 or not self._is_the_placeholder(pair[0], returned) or not self._is_the_flag(pair[1]):
            return False

        # The block stays, empty: the code in front of it may end in a jump onto its address (96/14945).
        resume.instructions = []

        kept = guard.then_body.children

        for child in guard.else_body.children:
            if isinstance(child, BasicBlock):
                child.instructions = []

        sequence.children[before + 1:before + 2] = list(kept)

        return True

    @classmethod
    def _returned_register(cls, arm) -> str | None:
        """`rN` when every `return` in the arm returns the same register (and there is one)."""
        names: set[str | None] = set()

        if not cls._collect_returns(arm, names) or len(names) != 1:
            return None

        return next(iter(names))

    @classmethod
    def _collect_returns(cls, node, names: set) -> bool:
        """Adds the register of each `return rN;` below `node`; False for a region this pass does not read."""
        if isinstance(node, BasicBlock):
            for instruction in node.instructions:
                if isinstance(instruction.statement, ReturnStatement):
                    value = instruction.value
                    names.add(value.name if isinstance(value, Identifier) else None)

            return True

        if isinstance(node, SequenceRegion):
            return all(cls._collect_returns(child, names) for child in node.children)

        if isinstance(node, IfRegion):
            return (
                cls._collect_returns(node.then_body, names)
                and (node.else_body is None or cls._collect_returns(node.else_body, names))
            )

        return False

    @staticmethod
    def _same_node(a, b) -> bool:
        if a is None or b is None:
            return a is b

        return a.structurally_equal(b)

    @classmethod
    def _same(cls, a, b) -> bool:
        """Do two arms run the same instructions (the copies of a `finally` body)?"""
        if isinstance(a, BasicBlock) and isinstance(b, BasicBlock):
            return len(a.instructions) == len(b.instructions) and all(
                x.dest_reg == y.dest_reg and cls._same_node(x.value, y.value)
                and cls._same_node(x.statement, y.statement)
                for x, y in zip(a.instructions, b.instructions)
            )

        if isinstance(a, SequenceRegion) and isinstance(b, SequenceRegion):
            return len(a.children) == len(b.children) and all(cls._same(x, y) for x, y in zip(a.children, b.children))

        if isinstance(a, IfRegion) and isinstance(b, IfRegion):
            if not cls._same_node(a.condition, b.condition) or (a.else_body is None) != (b.else_body is None):
                return False

            return cls._same(a.then_body, b.then_body) and (a.else_body is None or cls._same(a.else_body, b.else_body))

        return False

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
