"""
Folds a value-producing ternary / `||` / `&&` that is only TESTED into one block.

Hermes lowers `if (a || (c ? x : y || z)) T` by computing the inner value into
a register on several paths and testing that register once, in a block that
holds nothing but its branch:

    H:  if (c) goto E            // `c ? ... : ...`
    B:  r2 = x; if (r2) goto J   // `x || z`
    B2: r2 = z
    J:  goto M
    E:  r2 = !w
    M:  if (!r2) goto END        // the only reader of r2

The test cannot see through the join register, so the arms stay a diamond and
the shared target T ends up with a jump from outside the diamond (a `goto`, or
a duplicated tail). This pass replaces the whole diamond by one block

    H:  r2 = c ? !w : (x || z); if (!r2) goto END

whose pure setup the short-circuit pass already knows how to fold into the
condition of the test before it.

Only shapes that are exactly a value diamond are touched: one entry (H), one
exit (M), contiguous in the layout, every arm pure, and every register an arm
writes besides the tested one dead after M.
"""

from __future__ import annotations

import copy

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.backend.transforms.shared import has_side_effects, negate_condition
from hermes_decompiler.ir import LogicalOperator
from hermes_decompiler.ir.expressions import BinaryExpression, CallExpression, ConditionalExpression, Identifier
from hermes_decompiler.ir.expressions import MemberExpression
from hermes_decompiler.ir.expressions import UnaryExpression
from hermes_decompiler.ir.Operators import UnaryOperator
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch

from .ShortCircuitConditionCfgPass import ShortCircuitConditionCfgPass as _Liveness


class ValueConditionFoldCfgPass:
    _MAX_BLOCKS = 12

    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self._loop_blocks = _Liveness._collect_loop_blocks(cfg)

    def run(self) -> int:
        if self.cfg.exception_handlers:
            return 0

        folded = 0

        while any(self._try(block) for block in list(self.cfg.blocks)):
            folded += 1

        if folded:
            # M was the merge point of the diamond; the analyses still name it.
            self.cfg.compute_dominators()
            self.cfg.compute_post_dominators()

        return folded

    # ------------------------------------------------------------------ #

    def _try(self, m: BasicBlock) -> bool:
        branch = m.terminator

        if not isinstance(branch, TerminatorConditionalBranch) or m in self._loop_blocks:
            return False
        if len(m.predecessors) < 2 or any(i.terminator is None for i in m.instructions):
            return False

        register = self._tested_register(branch.condition)

        if register is None:
            return False

        blocks = self.cfg.blocks
        end = blocks.index(m)

        for distance in range(2, self._MAX_BLOCKS + 1):
            if end - distance < 0:
                break

            head = blocks[end - distance]

            if head in self._loop_blocks:
                break

            if self._fold(head, m, register):
                return True

        return False

    @staticmethod
    def _tested_register(condition) -> int | None:
        if isinstance(condition, UnaryExpression) and condition.operator == UnaryOperator.LOGICAL_NOT:
            condition = condition.operand

        if isinstance(condition, Identifier) and condition.name.startswith("r") and condition.name[1:].isdigit():
            return int(condition.name[1:])

        return None

    def _fold(self, head: BasicBlock, m: BasicBlock, register: int) -> bool:
        if not isinstance(head.terminator, TerminatorConditionalBranch):
            return False

        visited: list[BasicBlock] = []
        value = self._value(head, m, register, visited)

        if value is None:
            return False

        blocks = self.cfg.blocks
        region = blocks[blocks.index(head):blocks.index(m)]

        # Exactly the blocks between H and M, entered only through H, left only into M.
        if len(visited) != len(region) or set(visited) != set(region):
            return False
        if any(p not in region for p in m.predecessors):
            return False
        if any(p not in region for block in region[1:] for p in block.predecessors):
            return False

        successors = list(m.successors)

        # At most ONE effect in the whole diamond: it stays evaluated once, on the path its arm was on
        # (`r7 = p && DataView.prototype.isPrototypeOf(p)`, 98/12704). Two would need their order proven.
        effects = sum(
            1 for block in region for i in block.instructions
            if i.terminator is None and i.value is not None and has_side_effects(i.value)
        )

        if effects > 1 or (effects and not self._crossed_into(head, m)):
            return False

        # Whatever an arm wrote besides the tested register must be unread after M.
        dropped = {
            i.dest_reg for block in region[1:] for i in block.instructions
            if i.terminator is None and i.dest_reg is not None and i.dest_reg != register
        }

        # A receiver the call keeps by name (`r9 = DataView.prototype; ... r9.isPrototypeOf(p)`) is a pure value
        # written once in the diamond: it goes into the value, in the place the name stood.
        for reg in sorted(dropped, reverse=True):
            name = f"r{reg}"
            writes = [
                i for block in region[1:] for i in block.instructions
                if i.terminator is None and i.dest_reg == reg
            ]

            if (
                    len(writes) == 1 and writes[0].value is not None and writes[0].statement is None
                    and not has_side_effects(writes[0].value)
                    and sum(1 for n in value.walk() if isinstance(n, Identifier) and n.name == name) == 1
                    and any(
                isinstance(n, CallExpression) and isinstance(n.callee, MemberExpression)
                and isinstance(n.callee.obj, Identifier) and n.callee.obj.name == name
                for n in value.walk()
            )
                    and not any(isinstance(n, Identifier) and n.name == name for n in writes[0].value.walk())
            ):
                value = _Liveness._substitute_all(value, {name: copy.deepcopy(writes[0].value)})

        # A temporary the arms computed stays a NAME inside the value (`r0 = r2 instanceof ...`,
        # its own statement printed above): dropping it would leave that name unset.
        named = {n.name for n in value.walk() if isinstance(n, Identifier)}

        if f"r{register}" in named or any(f"r{reg}" in named for reg in dropped):
            return False

        for reg in dropped:
            if not all(_Liveness._dead_on_entry(s, reg, set()) for s in successors):
                return False

        self._rewrite(head, m, register, value, region)

        return True

    @staticmethod
    def _crossed_into(head: BasicBlock, m: BasicBlock) -> bool:
        """`X: if (c) goto T; H: <value diamond>; M: if (r) goto E; T: ...`: X jumps to M's fall-through, so the
        diamond is the next link of an `A && B && value` chain (a call in it runs only after A and B held, as
        inside the chain). Anywhere else a call in an arm is left alone."""
        if len(head.predecessors) != 1:
            return False

        before = head.predecessors[0]

        if not isinstance(before.terminator, TerminatorConditionalBranch) or before.terminator.target <= before.address:
            return False

        blocks = [b for b in m.successors if b.address != m.terminator.target]

        return len(blocks) == 1 and blocks[0].address == before.terminator.target

    def _rewrite(self, head, m, register, value, region) -> None:
        template = next(
            (i for i in reversed(head.instructions) if i.terminator is None and i.dest_reg == register), None
        )

        if template is None:
            template = next(
                i for block in region[1:] for i in block.instructions
                if i.terminator is None and i.dest_reg == register
            )
            template = copy.copy(template)

        template.value = value
        if not hasattr(self.cfg, "folded_values"):
            self.cfg.folded_values = []
        self.cfg.folded_values.append(template)
        template.statement = None
        template.definition_used = False

        m_terminator_instruction = next(i for i in m.instructions if i.terminator is m.terminator)
        kept = [
            i for i in head.instructions
            if i.terminator is None and not (i.dest_reg == register)
        ]

        head.instructions = kept + [template, m_terminator_instruction]
        head.terminator = m.terminator

        for block in region[1:]:
            self.cfg.blocks.remove(block)

        for block in region[1:] + [m]:
            for successor in block.successors:
                if block in successor.predecessors:
                    successor.predecessors.remove(block)

        for successor in m.successors:
            if head not in successor.predecessors:
                successor.predecessors.append(head)

        head.successors = list(m.successors)
        self.cfg.blocks.remove(m)

    # ------------------------------------------------------------------ #

    def _pure(self, block: BasicBlock) -> bool:
        for i in block.instructions:
            if i.terminator is not None:
                continue
            # One call is fine (see `_fold`): inside the value it runs where the arm ran it.
            if i.dest_reg is None or i.value is None or i.statement is not None:
                return False

        return True

    def _chain_to(self, block: BasicBlock, m: BasicBlock, visited: list) -> bool:
        """`block` only jumps on to M (through empty blocks)."""
        while block is not m:
            if any(i.terminator is None for i in block.instructions):
                return False
            if len(block.successors) != 1 or block.successors[0].address <= block.address:
                return False
            if block not in visited:
                # A join the arms share is an empty jump: seen twice, still one block.
                visited.append(block)
            block = block.successors[0]

        return True

    def _value(self, block: BasicBlock, m: BasicBlock, register: int, visited: list):
        if block is m or block in visited:
            return None

        visited.append(block)

        if not self._pure(block):
            return None

        name = f"r{register}"
        defs = [i for i in block.instructions if i.terminator is None and i.dest_reg == register]
        terminator = block.terminator

        if not isinstance(terminator, TerminatorConditionalBranch):
            if not defs or len(block.successors) != 1 or block.successors[0].address <= block.address:
                return None
            if block.instructions[-1].terminator is None and block.instructions[-1] is not defs[-1]:
                return None
            if any(i.terminator is None and i is not defs[-1] and i.dest_reg == register for i in block.instructions):
                return None
            if not self._chain_to(block.successors[0], m, visited):
                return None

            return defs[-1].value

        target = next((s for s in block.successors if s.address == terminator.target), None)
        fall = next((s for s in block.successors if s.address != terminator.target), None)

        if target is None or fall is None or terminator.target <= block.address:
            return None

        condition = terminator.condition

        if defs:
            last = defs[-1]

            if block.instructions[-2:][0] is not last and block.instructions[-1] is not last:
                return None

            # `v = a; if (v) goto M` keeps a when it is truthy: a || (what follows).
            for operator, keeps in ((LogicalOperator.OR, condition),
                                    (LogicalOperator.AND, negate_condition(condition))):
                if repr(keeps) == repr(last.value) and self._chain_to(target, m, visited):
                    rest = self._value(fall, m, register, visited)

                    if rest is None:
                        return None

                    return BinaryExpression(left=last.value, operator=operator, right=rest)

            if any(isinstance(n, Identifier) and n.name == name for n in condition.walk()):
                return None

        if any(isinstance(n, Identifier) and n.name == name for n in condition.walk()):
            return None

        # `r = undefined; if (a == null) goto M; r = a.b; M:` (`a?.b`): the jump to M itself keeps the value
        # the block just wrote (98/7639). The fold drops every write of the register, so only a block that writes
        # it once qualifies (98/5937 read an earlier value of it), and the value must not be read after M
        # (98/6004 returned it).
        if target is m and (
                len(defs) != 1
                or not all(_Liveness._dead_on_entry(s, register, set()) for s in m.successors)
        ):
            return None

        then = defs[-1].value if target is m else self._value(target, m, register, visited)
        other = self._value(fall, m, register, visited)

        if then is None or other is None:
            return None

        return ConditionalExpression(test=condition, consequent=then, alternate=other)
