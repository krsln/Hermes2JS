from __future__ import annotations

import copy
import dataclasses
import re

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.core.Exceptions import StructurerInvariantError
from hermes_decompiler.ir import LogicalOperator, Node
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Identifier, Literal, UndefinedLiteral
from hermes_decompiler.ir.terminators import TerminatorConditionalBranch, TerminatorJump
from hermes_decompiler.backend.transforms.shared import (
    negate_condition, TRIVIAL_NODE_TYPES, has_side_effects, keep_call_this_unbound, substitute_register,
)


class ShortCircuitConditionCfgPass:
    """Collapses pure control-flow short-circuit condition chains.

    This pass runs before RegionGraph and IfStructurer and recognizes
    control-flow-only `&&` / `||` expressions lowered into multiple
    conditional test blocks that share a branch target::
        if (a) goto T; if (!a) goto ELSE;
        if (b) goto T; if (!b) goto ELSE;
        ... ...
    The exact source operator is already reflected in the polarity of
    the individual conditions. For example, JmpTrue and JmpFalse may
    negate operands as required by the original short-circuit expression.
    At the CFG level, this pass therefore only needs to recognize a chain
    of single-purpose test blocks whose conditional branches share the
    same target, then combine their conditions into one logical expression.

    This allows source constructs such as `a || b` to be represented as
    one structured condition rather than multiple independent branches.
    Without this normalization, the shared target may have multiple
    predecessors, causing IfStructurer's single-entry validation to reject
    what was originally a single source-level condition. After the chain
    is merged, the shared target has one predecessor and can be structured
    normally.

    This pass handles only control-flow conditions. Value-producing
    short-circuit expressions, such as ``const x = a || b;``
    are handled later by `region_passes.BooleanChainRegionPass`. The two
    passes operate on intentionally disjoint inputs: this pass only merges
    pure test blocks, while BooleanChainRegionPass handles blocks that
    participate in value-producing assignments. Re-check this separation
    before loosening `_is_pure_test_block`.

    The pass must run after `cfg.compute_loops()` so loop blocks can be
    excluded from merging. Loop rotation may duplicate the same source
    condition into separate guard and continue-test blocks that resemble
    a short-circuit chain but must remain structurally distinct.

    It must also run before ``RegionGraph`` is constructed.
    """

    def __init__(self, cfg: CFG):
        self.cfg = cfg
        self._loop_blocks = self._collect_loop_blocks(cfg)

    @staticmethod
    def _collect_loop_blocks(cfg: CFG) -> frozenset[BasicBlock]:
        """Return every block that belongs to a discovered loop."""

        loop_analysis = cfg.loop_analysis

        if loop_analysis is None:
            raise StructurerInvariantError(
                "Loop analysis must be computed before "
                "ShortCircuitConditionCfgPass."
            )

        blocks: set[BasicBlock] = set()

        for loop in loop_analysis.loops.values():
            blocks.add(loop.header)
            blocks.update(loop.members)

        return frozenset(blocks)

    def _both_tests_leave_the_loop(self, block, successor, branch) -> bool:
        """`if (a) break-to-X; if (b) break-to-X;` inside a loop body.

        Two tests that jump out of every loop they sit in, to the one block
        outside (`if (tag === 24 || tag === 3) { found }`), are an ordinary `||`;
        the loop's own latch/continue tests are never like that.
        """
        if successor is None or not isinstance(successor.terminator, TerminatorConditionalBranch):
            return False

        if successor.terminator.target != branch.target or branch.target <= successor.address:
            return False

        target = next((b for b in self.cfg.blocks if b.address == branch.target), None)

        if target is None:
            return False

        for loop in self.cfg.loop_analysis.loops.values():
            inside = loop.header is block or block in loop.members or loop.header is successor or successor in loop.members

            if inside and (target is loop.header or target in loop.members):
                return False

        return True

    def run(self) -> None:
        self._created = False

        while self._merge_one_pass():
            pass

        if self._created:
            # An edge block the analyses have not seen: dominance is asked about it.
            self.cfg.compute_dominators()
            self.cfg.compute_post_dominators()

    def _merge_one_pass(self) -> bool:
        """Find and merge the first eligible (block, fallthrough) pair.

        Returns True if a merge happened (caller should re-scan, since
        merging can expose further chains: a||b||c merges pairwise).
        """

        for block in self.cfg.blocks:

            merged = self._try_merge(block)

            if merged:
                return True

        return False

    def _try_merge(self, block: BasicBlock) -> bool:

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return False

        successor = self._fallthrough(block)

        if block in self._loop_blocks and not self._both_tests_leave_the_loop(block, successor, branch):
            # Loop header/latch/member - never fold its condition into
            # or out of another block. See _collect_loop_blocks.
            return False

        if successor is None:
            return False

        if successor in self._loop_blocks and not self._both_tests_leave_the_loop(block, successor, branch):
            return False

        if branch.target <= block.address:
            # Backward branch = loop latch/continue test, never a
            # short-circuit && / || chain (those only ever jump
            # forward toward a merge point). Must not touch these -
            # loop structuring / LoopConditionExtractor needs the
            # original per-iteration test blocks intact.
            return False

        pure = self._is_pure_test_block(successor)

        if not pure and not self._is_inlined_setup_block(successor) and not self._is_pure_setup_block(successor):
            # Has real work in it (side effects) - not just a test,
            # can't be folded into block's condition.
            return False

        if list(successor.predecessors) != [block]:
            # Reached from somewhere other than block's fallthrough -
            # not part of the same short-circuit chain.
            return False

        next_branch = successor.terminator

        if not isinstance(next_branch, TerminatorConditionalBranch):
            return False

        if next_branch.target <= successor.address:
            # Same reasoning as the guard on `branch` above - a
            # backward second test means this is loop machinery, not
            # a short-circuit chain, even if the target happens to
            # coincide with branch.target.
            return False

        if (
                next_branch.target == branch.target
                and not pure
                # A constant comparison behind inlined setup is a link of a `case` chain:
                # SwitchStructurer wants those as separate tests. A plain value
                # (`a || b || c` over parameters) is one condition.
                and not (
                self._is_inlined_setup_block(successor)
                and self._is_case_test(next_branch.condition, branch.condition)
                and self._case_chain_has_another_body(block, successor, branch.target))
        ):
            # `a || (r2 = f; b)` with a pure `f`: the test takes the value.
            exits = [s for s in (self._arm_of(block, branch), self._fallthrough(successor)) if s is not None]

            # A constant the second test loads and the code after both tests reads
            # (`r3 = null; if (a === r3) goto R;` ... `b === r3`): the test takes the
            # value, the fall-through gets its own copy of the load (96/1139).
            constants = (
                self._constants_for_the_end_edge(successor, exits[0], exits[1], [])
                if len(exits) == 2 else []
            )
            folded = (
                self._fold_pure_setup(successor, next_branch.condition, exits, rematerialized=constants)
                if len(exits) == 2 else None
            )

            if folded is None:
                return False

            self._merge(block, successor, next_branch, folded, rematerialize=constants)
            return True

        if next_branch.target != branch.target or not pure:
            # Different targets: not a same-target chain. It can still be the
            # crossed form (see `_try_merge_crossed`).
            return self._try_merge_crossed(block, successor, next_branch)

        self._merge(block, successor, next_branch)
        return True

    def _try_merge_crossed(self, block, successor, next_branch) -> bool:
        """`if (!a || b) { A } END` compiles to

            X: if (!a) goto A          (first jump lands on the second
            Y: if (b') goto END         test's fall-through)
            A: ...

        `END` is reached exactly when X's test fails and Y's holds, so the
        two blocks are one test `!c1 && c2` jumping to `END`, falling through
        to `A`. The tests may have been given their constants as setup
        (`r3 = "px"; if (r4 !== r3)`) that the condition already inlined.
        """
        branch = block.terminator
        fall_through = self._fallthrough(successor)

        if fall_through is None or fall_through.address != branch.target:
            return False

        second = next_branch.condition
        arm = self._arm_of(block, branch)
        end_block = next((x for x in successor.successors if x.address == next_branch.target), None)
        sunk: list = []

        if not self._is_inlined_setup_block(successor):
            if end_block is None or end_block in self._loop_blocks or arm in self._loop_blocks:
                return False

            # Join copies (`Mov r4, r3`) the arm overwrites anyway only matter
            # on the way to END: they move onto that edge (see `_sink_copies`).
            sunk = self._copies_for_the_end_edge(successor, arm, end_block)

            # A constant the test reads AND END reads (`r1 = 0; ... a[r1]` in the
            # test, `a[r1]` again in END): the test takes the value, END gets its
            # own copy of the load on the edge into it (96/9112 `parseTranslateX`).
            constants = self._constants_for_the_end_edge(successor, arm, end_block, sunk)

            # A pure value the second test reads through its register
            # (`r0 = arguments[1]; if (r0 !== undefined)`): the test takes the
            # value itself when nothing reads the register afterwards.
            second = self._fold_pure_setup(
                successor, second, [arm, end_block], skip=sunk, rematerialized=constants,
            )

            if second is None:
                return False

            sunk = sorted([*sunk, *constants], key=lambda i: i.address)

        if self._setup_feeds_a_join(successor, arm, ignore={i.dest_reg for i in sunk}):
            return False

        edge = None

        if sunk:
            edge = self._sink_copies(sunk, end_block, successor)

            if edge is None:
                return False

        combined = BinaryExpression(
            left=negate_condition(branch.condition),
            operator=LogicalOperator.AND,
            right=second,
        )

        merged = TerminatorConditionalBranch(
            condition=combined, target=edge.address if edge is not None else next_branch.target,
        )

        # `block` now jumps to Y's old target and falls through to `A`.
        self._rewire_crossed(block, successor, branch, merged, end_block, edge)
        return True

    def _copies_for_the_end_edge(self, successor: BasicBlock, arm: BasicBlock, end_block: BasicBlock) -> list:
        """The `Mov`s of the second test block that only END reads: dead on entry
        to the arm (which writes the register first) and to every handler, and
        not read by anything else of the block."""
        setup = [i for i in successor.instructions if i.terminator is None]
        copies = []

        for instruction in setup:
            if (
                    instruction.dest_reg is None
                    or instruction.value is None
                    or instruction.statement is not None
                    or not self._dead_on_entry(arm, instruction.dest_reg, set())
                    or not all(self._dead_on_entry(b, instruction.dest_reg, set()) for b in self._handlers())
            ):
                continue

            if instruction.entry.opcode in ("Mov", "MovLong"):
                if not any(
                        other is not instruction and (
                                self._reads_operand(other, instruction.dest_reg)
                                or (other.value is not None
                                    and self._mentions(other.value, f"r{instruction.dest_reg}"))
                        )
                        for other in successor.instructions
                ):
                    copies.append(instruction)

        return copies

    def _constants_for_the_end_edge(self, successor: BasicBlock, arm: BasicBlock, end_block: BasicBlock, taken) -> list:
        """Constant loads of the second test block that END also reads: the arm
        overwrites the register first, and only this block leads to END, so a
        copy of the load on the edge into END gives it the same value."""
        if list(end_block.predecessors) != [successor] or self.cfg.exception_handlers:
            return []

        found = []

        for instruction in successor.instructions:
            if (
                    instruction.terminator is not None
                    or any(instruction is t for t in taken)
                    or instruction.dest_reg is None
                    or instruction.statement is not None
                    or not instruction.entry.opcode.startswith("LoadConst")
                    or not isinstance(instruction.value, (Literal, UndefinedLiteral))
                    or sum(1 for i in successor.instructions if i.dest_reg == instruction.dest_reg) != 1
                    or not self._dead_on_entry(arm, instruction.dest_reg, set())
                    or self._dead_on_entry(end_block, instruction.dest_reg, set())
            ):
                continue

            found.append(instruction)

        return found

    def _sink_copies(self, copies: list, end_block: BasicBlock, successor: BasicBlock):
        """A block on the edge into `end_block` that runs the copies. It sits right
        before END; the block that used to fall into END jumps over it."""
        blocks = self.cfg.blocks
        index = blocks.index(end_block)

        if self.cfg.exception_handlers:
            # An edge block would sit outside every try range.
            return None

        if index == 0 or blocks[index - 1] is successor:
            return None

        last = blocks[index - 1]

        if last.terminator is not None and not isinstance(last.terminator, TerminatorJump):
            if end_block in last.successors:
                return None
        elif last.terminator is None:
            if end_block not in last.successors or last.address >= end_block.address - 1:
                return None

        edge = BasicBlock(max(b.id for b in blocks) + 1, end_block.address - 1)

        for instruction in copies:
            duplicate = copy.copy(instruction)
            duplicate.value = copy.deepcopy(instruction.value)
            edge.instructions.append(duplicate)

        if last.terminator is None:
            last.terminator = TerminatorJump(target=end_block.address)

        edge.successors.append(end_block)
        end_block.predecessors.append(edge)
        blocks.insert(index, edge)
        self._created = True

        return edge

    @staticmethod
    def _is_pure_setup_block(block: BasicBlock) -> bool:
        """Only value writes plus its own branch (the crossed form folds them
        into the test, see `_fold_pure_setup`). At most one of them may have an
        effect (a call): it runs once, on the same path, inside the test."""
        setup = [i for i in block.instructions if i.terminator is None]

        return (
                all(i.dest_reg is not None and i.value is not None and i.statement is None for i in setup)
                and sum(1 for i in setup if has_side_effects(i.value)) <= 1
        )

    def _fold_pure_setup(self, successor: BasicBlock, condition, exits: list, skip=(), rematerialized=()):
        """The second test's condition with its pure setup instructions
        substituted in, or None when that is not exact.

        Every setup instruction must be a side-effect-free value whose register
        is dead on entry to both exits of the pair (written before any read,
        on every path), so dropping the write loses nothing."""
        setup = [i for i in successor.instructions if i.terminator is None and not any(i is k for k in skip)]
        effect_seen = False
        probe = condition  # what the later instructions have made of it (only to count uses)

        for position in range(len(setup) - 1, -1, -1):
            instruction = setup[position]

            if instruction.value is not None and has_side_effects(instruction.value):
                # One effect, evaluated once and in order, inside a test that has
                # no effect of its own; what ran before it is its own operands.
                name = f"r{instruction.dest_reg}"
                if (
                        effect_seen
                        or (has_side_effects(probe) and not self._read_before_any_effect(probe, name))
                        or sum(1 for n in probe.walk() if isinstance(n, Identifier) and n.name == name) != 1
                        or not self._feeds_only(instruction, setup[:position])
                ):
                    return None
                effect_seen = True

            if (
                    instruction.dest_reg is None
                    or instruction.value is None
                    or instruction.statement is not None
                    # A copy (`Mov r5, r4`) is an input of a join the exits read
                    # through another register's inlined value; a fold cannot see
                    # that, so only values the test itself computes are folded.
                    or instruction.entry.opcode in ("Mov", "MovLong")
                    or not (
                    # The global object is the same on every path and every reader
                    # already inlined it: nothing is left to read the register.
                    instruction.entry.opcode == "GetGlobalObject"
                    # A load END gets its own copy of is only dead on the first exit.
                    or all(self._dead_on_entry(b, instruction.dest_reg, set())
                           for b in (exits[:1] if any(instruction is r for r in rematerialized) else exits))
            )
                    # A handler is entered by an edge the CFG does not have: it
                    # may read the register the try body had set.
                    or not (
                    instruction.entry.opcode == "GetGlobalObject"
                    or all(self._dead_on_entry(b, instruction.dest_reg, set()) for b in self._handlers())
            )
            ):
                return None
            probe = substitute_register(probe, f"r{instruction.dest_reg}", instruction.value)

        # Forward, one register file: a name inside a value means the register as it
        # was at that instruction, and a register the setup writes twice
        # (`r0 = env; r1 = r0[0]; r0 = undefined`) is not one name.
        current: dict = {}
        resolved: dict = {}
        writes = [i.dest_reg for i in setup]

        for instruction in setup:
            # A name that reads a register the setup has since overwritten with a
            # constant is the frontend's stale inline of the older value
            # (`r4 = r0[0]` ... `r0 = undefined` ... `r4(r0)`): which one is meant is
            # not known here.
            read_here = self._source_registers(instruction)

            for node in instruction.value.walk():
                if (
                        isinstance(node, Identifier)
                        and isinstance(current.get(node.name), (Literal, UndefinedLiteral))
                        and writes.count(int(node.name[1:])) > 1
                        # Named by the instruction's own operands, it is that constant.
                        and int(node.name[1:]) not in read_here
                ):
                    return None

            # A copy: the setup's own node stays the identity a later repair looks for.
            value = copy.deepcopy(self._substitute_all(instruction.value, current, resolved))
            resolved[id(instruction.value)] = value
            current[f"r{instruction.dest_reg}"] = value

        return self._substitute_all(condition, current, resolved)

    @classmethod
    def _read_before_any_effect(cls, node, name: str) -> bool:
        """Is `name` evaluated before anything in `node` that can have an effect?
        Then an effect substituted for it still runs first, as it did as setup."""
        return cls._eval_order(node, name) == "read"

    @classmethod
    def _eval_order(cls, node, name: str):
        """'read' if `name` is reached first, 'effect' if an effect is, else None
        (operands left to right, an operation after its operands)."""
        if isinstance(node, Identifier):
            return "read" if node.name == name else None

        if not isinstance(node, Node):
            return None

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            for child in (value if isinstance(value, tuple) else (value,)):
                if isinstance(child, Node):
                    found = cls._eval_order(child, name)

                    if found is not None:
                        return found

        children = [
            c for f in dataclasses.fields(node)
            for c in (getattr(node, f.name) if isinstance(getattr(node, f.name), tuple) else (getattr(node, f.name),))
            if isinstance(c, Node)
        ]

        # The operation itself is the effect once its operands have run.
        return "effect" if has_side_effects(node) and not any(has_side_effects(c) for c in children) else None

    @classmethod
    def _substitute_all(cls, node, mapping: dict, resolved: dict | None = None):
        """`node` with every `Identifier` named in `mapping` replaced, at once.

        A subtree that IS (by identity) an earlier instruction's value was inlined
        from there: its names mean the registers as that instruction saw them, so
        it takes that instruction's own resolution instead of being read again
        with the registers as they are now (`r4 = r2[1]` ... `r2 = a[0]` ... `r4(r2)`)."""
        if resolved and id(node) in resolved:
            return resolved[id(node)]

        if isinstance(node, Identifier):
            return mapping.get(node.name, node)

        if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
            return node

        updates = {}

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            if isinstance(value, Node):
                new_value = cls._substitute_all(value, mapping, resolved)

                if new_value is not value:
                    updates[field.name] = new_value
            elif isinstance(value, tuple):
                items = tuple(cls._substitute_all(i, mapping, resolved) if isinstance(i, Node) else i for i in value)

                if any(new is not old for new, old in zip(items, value)):
                    updates[field.name] = items

        return dataclasses.replace(node, **keep_call_this_unbound(node, updates)) if updates else node

    @classmethod
    def _source_registers(cls, instruction) -> set:
        """The registers the BYTECODE instruction reads (its operands after the destination)."""
        entry = getattr(instruction, "entry", None)
        operands = [int(m) for m in cls._OPERAND_RE.findall(getattr(entry, "args", "") or "")]

        if instruction.dest_reg is not None and operands and operands[0] == instruction.dest_reg:
            operands = operands[1:]

        return set(operands)

    def _feeds_only(self, effect, earlier: list) -> bool:
        """Is everything set up before `effect` either a constant, already inlined
        into its reader, or part of the chain that computes `effect`'s operands
        (`r0 = env; r1 = r0[0]; r0 = r1.getId()`)? Those are evaluated before the
        effect inside the one expression, as they were."""
        needed = {n.name for n in effect.value.walk() if isinstance(n, Identifier)}

        for instruction in reversed(earlier):
            name = f"r{instruction.dest_reg}"

            if name in needed:
                needed |= {n.name for n in instruction.value.walk() if isinstance(n, Identifier)}
            elif not (
                    isinstance(instruction.value, TRIVIAL_NODE_TYPES)
                    or instruction.definition_used
                    # A pure value nothing in the chain reads (`r0 = getEnvironment(0)` whose
                    # member was resolved to a name): dropping it loses nothing, and the fold
                    # has already checked its register is dead on both exits.
                    or (instruction.value is not None and not has_side_effects(instruction.value))
            ):
                return False

        return True

    def _handlers(self) -> list[BasicBlock]:
        return [b for b in self.cfg.blocks if not b.predecessors and b is not self.cfg.entry]

    @classmethod
    def _dead_on_entry(cls, block: BasicBlock, register: int, visited: set) -> bool:
        """True if no path from the start of `block` reads `rN` before writing it."""
        if block in visited:
            return True

        visited.add(block)
        name = f"r{register}"

        for instruction in block.instructions:
            # The bytecode operands are the reads at THIS point. A name inside an
            # inlined value is only where the value was defined (a join read
            # prints the arm's copy: `r2[0] = r3` for a read of r1), so names count
            # only where no operands describe the instruction: a condition merged
            # from several tests, or an instruction a pass made.
            described = bool(
                getattr(getattr(instruction, "entry", None), "args", "")) and instruction.terminator is None
            nodes = [] if described else [
                instruction.value, instruction.statement, getattr(instruction.terminator, "condition", None),
                getattr(instruction.terminator, "value", None),
            ]

            if any(n is not None and cls._mentions(n, name) for n in nodes) or cls._reads_operand(instruction,
                                                                                                  register):
                return False

            if instruction.dest_reg == register and instruction.terminator is None:
                return True

        return all(cls._dead_on_entry(succ, register, visited) for succ in block.successors)

    _OPERAND_RE = re.compile(r"Reg(?:8|32):\s*(\d+)")

    @classmethod
    def _reads_operand(cls, instruction, register: int) -> bool:
        """Does the BYTECODE instruction read `rN`? Readers were linearly inlined
        before any control flow was known, so a read of a join register may no
        longer name it in the printed tree; the operands still do. The first
        operand of a writing instruction is its destination."""
        entry = getattr(instruction, "entry", None)
        operands = [int(m) for m in cls._OPERAND_RE.findall(getattr(entry, "args", "") or "")]

        if instruction.dest_reg is not None and operands and operands[0] == instruction.dest_reg:
            operands = operands[1:]

        return register in operands

    @classmethod
    def _mentions(cls, node, name: str) -> bool:
        if isinstance(node, Identifier):
            return node.name == name

        return isinstance(node, Node) and any(isinstance(n, Identifier) and n.name == name for n in node.walk())

    @staticmethod
    def _is_inlined_setup_block(block: BasicBlock) -> bool:
        """Only constants the test already inlined, plus its own branch."""
        for instr in block.instructions:
            if instr.terminator is not None:
                continue

            if not (instr.definition_used and isinstance(instr.value, TRIVIAL_NODE_TYPES)):
                return False

        return True

    def _arm_of(self, block, branch):
        return next(s for s in block.successors if s.address == branch.target)

    @classmethod
    def _setup_feeds_a_join(cls, successor: BasicBlock, arm: BasicBlock, ignore=frozenset()) -> bool:
        """True if `arm` (the other way out of the pair) writes a register the
        removed setup writes and then flows straight into the exit. The two
        writes are the arms of one join (`r14 = r20` / `r14 = null`, then
        `r14` is read): deleting one with the block leaves the readers on
        the wrong value."""
        written = {i.dest_reg for i in successor.instructions if i.dest_reg is not None} - set(ignore)

        if not written or len(arm.successors) != 1:
            return False

        end_block = next((s for s in successor.successors if s is not arm), None)

        if end_block is not None:
            # Only a register the exit goes on to read is a join.
            written = {r for r in written if not cls._dead_on_entry(end_block, r, set())}

        return (
                end_block is not None
                and arm.successors[0] is end_block
                and any(i.dest_reg in written for i in arm.instructions)
        )

    def _rewire_crossed(self, block, successor, branch, merged, end_block=None, edge=None) -> None:
        if end_block is None:
            end_block = next(s for s in successor.successors if s.address == merged.target)

        a_block = next(s for s in block.successors if s.address == branch.target)

        block.terminator = merged

        for instr in block.instructions:
            if instr.terminator is branch:
                instr.terminator = merged
                break

        successor.instructions.clear()

        for target in (end_block, a_block):
            if successor in target.predecessors:
                target.predecessors.remove(successor)

        block.successors = []
        self._connect(block, edge if edge is not None else end_block)
        self._connect(block, a_block)

        if successor in self.cfg.blocks:
            self.cfg.blocks.remove(successor)

    @staticmethod
    def _fallthrough(block: BasicBlock) -> BasicBlock | None:
        """Return the successor reached when `block`'s condition is false.

        I.e., the one that isn't the branch target.
        """

        branch = block.terminator

        if not isinstance(branch, TerminatorConditionalBranch):
            return None

        candidates = [s for s in block.successors if s.address != branch.target]

        if len(candidates) != 1:
            return None

        return candidates[0]

    @staticmethod
    def _compared_constant(condition):
        """`x` of `x === <literal>` / `x !== <literal>` (either side), else None."""
        if not (
                isinstance(condition, BinaryExpression)
                and condition.operator in (BinaryOperator.STRICT_EQUAL, BinaryOperator.STRICT_NOT_EQUAL)
        ):
            return None

        if isinstance(condition.right, Literal | UndefinedLiteral):
            return condition.left

        if isinstance(condition.left, Literal | UndefinedLiteral):
            return condition.right

        return None

    def _case_chain_has_another_body(self, block, successor, target: int) -> bool:
        """Does the `case` chain these two tests belong to jump anywhere else?

        `if (a === undefined) goto R; if (a === null) goto R;` is one body with two labels:
        no `switch` comes out of it, so it is one condition (`a === undefined || a === null`).
        With a third test going elsewhere it is a `switch` and the tests stay apart.
        """
        subject = self._compared_constant(block.terminator.condition)

        def same_subject(candidate) -> bool:
            branch = candidate.terminator

            if not isinstance(branch, TerminatorConditionalBranch):
                return False

            other = self._compared_constant(branch.condition)

            return other is not None and subject is not None and other.structurally_equal(subject)

        current = successor
        seen = {block, successor}

        while True:
            following = self._fallthrough(current)

            if following is None or following in seen:
                break

            seen.add(following)

            if not same_subject(following):
                break

            if following.terminator.target != target:
                return True

            current = following

        current = block

        while len(current.predecessors) == 1:
            previous = next(iter(current.predecessors))

            if previous in seen or not same_subject(previous) or self._fallthrough(previous) is not current:
                break

            seen.add(previous)

            if previous.terminator.target != target:
                return True

            current = previous

        return False

    @classmethod
    def _is_case_test(cls, condition, previous) -> bool:
        """A link of a `case` chain: the same value compared with a constant again."""
        subject = cls._compared_constant(condition)

        return subject is not None and cls._compared_constant(previous) is not None \
            and subject.structurally_equal(cls._compared_constant(previous))

    @staticmethod
    def _is_pure_test_block(block: BasicBlock) -> bool:
        """Return True if `block` contains nothing but its own terminator.

        I.e., it exists solely to evaluate one more condition and
        branch, with no other observable side effects that would be
        lost if folded into the preceding block's condition.

        This is also what keeps this pass disjoint from
        BooleanChainRegionPass: any block that assigns a value (the
        pattern that pass folds) has more than one instruction here
        and is correctly rejected. See the class docstring's "Not
        responsible for value-producing &&/||" section before
        loosening this check.
        """

        return len(block.instructions) <= 1

    def _merge(
            self,
            block: BasicBlock,
            successor: BasicBlock,
            next_branch: TerminatorConditionalBranch,
            second=None,
            rematerialize=(),
    ) -> None:

        branch = block.terminator
        if not isinstance(branch, TerminatorConditionalBranch):
            raise StructurerInvariantError(
                f"ShortCircuitConditionCfgPass expected block {block.id!r} to "
                f"end in a TerminatorConditionalBranch, got {type(branch).__name__}"
            )

        combined_condition = BinaryExpression(
            left=branch.condition,
            operator=LogicalOperator.OR,
            right=second if second is not None else next_branch.condition,
        )

        merged_terminator = TerminatorConditionalBranch(
            condition=combined_condition,
            target=branch.target,
        )

        block.terminator = merged_terminator

        # Printer walks block.instructions (a list of OpcodeResult),
        # rendering each entry's own .terminator - not
        # block.terminator. CFGBuilder points both at the same object
        # when the block is first built, but they're independent
        # references from here on: updating only block.terminator
        # (above) fixes CFG/IfStructurer analysis but leaves the
        # printed text showing the stale, unmerged condition. Find
        # that instruction and update it too.
        for instr in block.instructions:
            if instr.terminator is branch:
                instr.terminator = merged_terminator
                break

        # successor had exactly one instruction (its own terminator
        # entry, per _is_pure_test_block) - drop it, it's now folded
        # into block.terminator.
        copies = []

        for instruction in rematerialize:
            duplicate = copy.copy(instruction)
            duplicate.value = copy.deepcopy(instruction.value)
            copies.append(duplicate)

        successor.instructions.clear()

        new_fallthrough = self._fallthrough(successor)

        if copies and new_fallthrough is not None:
            new_fallthrough.instructions[0:0] = copies

        # -------------------------------------------------------------
        # Rewire edges: block -> {target_block, new_fallthrough},
        # bypassing successor entirely.
        # -------------------------------------------------------------

        target_block = None
        for s in block.successors:
            if s.address == branch.target:
                target_block = s
                break

        block.successors = []

        if target_block is not None:
            self._connect(block, target_block)
            if successor in target_block.predecessors:
                target_block.predecessors.remove(successor)

        if new_fallthrough is not None:
            self._connect(block, new_fallthrough)
            if successor in new_fallthrough.predecessors:
                new_fallthrough.predecessors.remove(successor)

        if successor in self.cfg.blocks:
            self.cfg.blocks.remove(successor)

    @staticmethod
    def _connect(source: BasicBlock, target: BasicBlock) -> None:

        if target not in source.successors:
            source.successors.append(target)

        if source not in target.predecessors:
            target.predecessors.append(source)
