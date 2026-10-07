from __future__ import annotations

import dataclasses
import re

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import Region
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import (
    ArrayExpression, ArrayHole, AssignmentExpression, Identifier, RawExpression, SpreadElement, UndefinedLiteral,
)
from hermes_decompiler.ir.Operators import AssignmentOperator
from ._base import RegionPass

_REGISTER = re.compile(r"\br(\d+)\b")


class FlowSnapshot:
    """The CFG's flow as it was before any structurer ran.

    The structurers rewrite block/successor edges (a try body is split off,
    blocks are duplicated or detached), so afterwards the CFG is no longer a
    sound flow graph. Liveness needs the original one; instruction CONTENT
    is read from the live objects (passes rewrite those in place).
    """

    def __init__(self, cfg):
        self.blocks = [
            (block.id, [s.id for s in block.successors], list(block.instructions))
            for block in cfg.blocks
        ]
        self.handlers: dict[int, list[int]] = {}

        for handler in cfg.exception_handlers:
            for block in handler["try_blocks"]:
                self.handlers.setdefault(block.id, []).append(handler["handler_block"].id)


class DeadUndefinedStorePass(RegionPass):
    """Removes an `rN = undefined;` whose value nothing can read.

    Hermes initialises every local to `undefined` at function entry
    (`LoadConstUndefined`) - the declarations of `const`/`let` bindings -
    and then assigns the real value later (a destructuring pattern, a
    for-of element, an ordinary initializer). The entry store stays in the
    output as a line of noise at the top of the function (`r8 = undefined;
    r7 = undefined; ...`).

    Whether one is dead is a question about EVERY path after it, so this
    is a real backward liveness analysis over the CFG (the structured
    region tree has no single "what runs next"), not the sequential walk
    `DeadMovEliminationPass` does for register copies:

      - A register read by name anywhere in an instruction's value,
        statement or terminator is a read.
      - Reads that no longer sit in an instruction - a loop's
        `condition`/`update`/`initializer`, an `if` condition, a `switch`
        discriminant, the for-of iterable - live on the region objects
        instead. Those registers are treated as live EVERYWHERE: never
        removed, and no precise answer is attempted for them.
      - Inside a `try` any instruction may throw into the handler, so what
        the handler reads stays live across the whole try block (a store of
        `undefined` right before a call that throws is observable there).
      - A "silent definition" (`rN = rN`, which the printer omits - the
        destructuring pass leaves these) is a WRITE of `rN`, not a read.

    Only a plain, printed `rN = undefined` is ever a candidate (no
    statement, no inlined use, not pinned): anything else may be doing
    work this analysis does not model.
    """

    def __init__(self, graph, cfg, snapshot: FlowSnapshot | None = None):
        super().__init__(graph, cfg)
        self.snapshot = snapshot

    def run(self) -> None:
        if self.snapshot is None:
            return

        candidates = self._candidates()

        if not candidates:
            return

        present = {
            id(i) for block in list(self.cfg.blocks) + list(self.graph.blocks())
            for i in block.instructions
        }
        known = {id(i) for _, _, instrs in self.snapshot.blocks for i in instrs}
        always_live = self._region_reads()

        # Instructions created after the snapshot have no known position.
        for block in list(self.cfg.blocks) + list(self.graph.blocks()):
            for i in block.instructions:
                if id(i) not in known:
                    always_live |= self._effects(i)[1]

        blocks = [
            (bid, succ, [i for i in instrs if id(i) in present])
            for bid, succ, instrs in self.snapshot.blocks
        ]
        live_in: dict[int, set[int]] = {bid: set() for bid, _, _ in blocks}

        def block_out(bid, succ):
            out = set()

            for s in succ:
                out |= live_in.get(s, set())

            for h in self.snapshot.handlers.get(bid, ()):
                out |= live_in.get(h, set())

            return out

        changed = True

        while changed:
            changed = False

            for bid, succ, instrs in reversed(blocks):
                handler = set()

                for h in self.snapshot.handlers.get(bid, ()):
                    handler |= live_in.get(h, set())

                state = self._scan(instrs, block_out(bid, succ), handler)[0]

                if state != live_in[bid]:
                    live_in[bid] = state
                    changed = True

        current = {id(i): b for b in self.graph.blocks() for i in b.instructions}
        dead = []

        for bid, succ, instrs in blocks:
            handler = set()

            for h in self.snapshot.handlers.get(bid, ()):
                handler |= live_in.get(h, set())

            _, live_after = self._scan(instrs, block_out(bid, succ), handler)

            for instruction in instrs:
                if id(instruction) in candidates and id(instruction) in current:
                    reg = instruction.dest_reg

                    if reg not in live_after[id(instruction)] and reg not in always_live:
                        dead.append((current[id(instruction)], instruction))

        for block, instruction in dead:
            block.instructions.remove(instruction)

    # -----------------------------------------------------------------

    def _candidates(self) -> dict[int, tuple[BasicBlock, object]]:
        found = {}

        for block in self.graph.blocks():
            for instruction in block.instructions:
                if (
                        instruction.dest_reg is not None
                        and isinstance(instruction.value, UndefinedLiteral)
                        and instruction.statement is None
                        and instruction.terminator is None
                        and not instruction.definition_used
                        and not instruction.definition_pinned
                ):
                    found[id(instruction)] = (block, instruction)

        return found

    def _scan(self, instructions, live_out: set[int], always: set[int]):
        """Backward scan of one block: (live-in, {id(instruction): live after it})."""
        live = set(live_out)
        after: dict[int, set[int]] = {}

        for instruction in reversed(instructions):
            after[id(instruction)] = set(live)

            written, reads = self._effects(instruction)

            live -= written

            live |= reads
            live |= always

        return live, after

    def _effects(self, instruction):
        """(registers written, registers read) of one instruction."""
        dest = instruction.dest_reg
        written: set[int] = set() if dest is None else {dest}
        reads: set[int] = set()

        statement = instruction.statement
        pattern = self._pattern_assignment(statement) or self._pattern_assignment(instruction.value)

        for held in (instruction.value, statement, instruction.terminator):
            if held is None or held is pattern:
                continue

            reads |= self._registers_read(held)

        if pattern is not None:
            # `[a, [b, c = d], ...rest] = src`: the leaves are WRITTEN
            # (every one, even if undefined); only `src` and the defaults read.
            reads |= self._registers_read(pattern.right)
            self._pattern_effects(pattern.left, written, reads)

        # `rN = rN`: the silent definition the destructuring pass leaves.
        if (
                dest is not None
                and isinstance(instruction.value, Identifier)
                and instruction.value.name == f"r{dest}"
        ):
            reads.discard(dest)

        return written, reads

    @staticmethod
    def _pattern_assignment(statement):
        if (
                isinstance(statement, AssignmentExpression)
                and statement.operator == AssignmentOperator.ASSIGN
                and isinstance(statement.left, ArrayExpression)
        ):
            return statement

        return None

    def _pattern_effects(self, node, written: set[int], reads: set[int]) -> None:
        if isinstance(node, ArrayExpression):
            for element in node.elements:
                self._pattern_effects(element, written, reads)
        elif isinstance(node, SpreadElement):
            self._pattern_effects(node.argument, written, reads)
        elif isinstance(node, AssignmentExpression):
            self._pattern_effects(node.left, written, reads)
            reads |= self._registers_read(node.right)
        elif isinstance(node, Identifier):
            if node.name.startswith("r") and node.name[1:].isdigit():
                written.add(int(node.name[1:]))
        elif node is not None and not isinstance(node, ArrayHole):
            reads |= self._registers_read(node)

    # -----------------------------------------------------------------

    def _region_reads(self) -> set[int]:
        """Registers read by an expression that lives on a region object."""
        reads: set[int] = set()
        seen: set[int] = set()

        def visit(value) -> None:
            if value is None or isinstance(value, (str, int, float, bool, BasicBlock)):
                return

            if id(value) in seen:
                return

            seen.add(id(value))

            if isinstance(value, Node):
                reads.update(self._registers_read(value))
                return

            if isinstance(value, (list, tuple, set, frozenset)):
                for item in value:
                    visit(item)
                return

            if isinstance(value, dict):
                for item in value.values():
                    visit(item)
                return

            if isinstance(value, Region) or dataclasses.is_dataclass(value):
                for name, item in vars(value).items() if hasattr(value, "__dict__") else ():
                    if name != "parent":
                        visit(item)

        visit(self.graph.root)

        return reads

    @staticmethod
    def _registers_read(node) -> set[int]:
        registers: set[int] = set()

        def visit(n) -> None:
            if isinstance(n, Identifier):
                if n.name.startswith("r") and n.name[1:].isdigit():
                    registers.add(int(n.name[1:]))
                return

            if isinstance(n, RawExpression):
                registers.update(int(m) for m in _REGISTER.findall(n.source))
                return

            if not dataclasses.is_dataclass(n):
                return

            for field in dataclasses.fields(n):
                value = getattr(n, field.name)

                for item in (value if isinstance(value, tuple) else (value,)):
                    if isinstance(item, Node) or (dataclasses.is_dataclass(item) and not isinstance(item, type)):
                        visit(item)

        visit(node)
        return registers
