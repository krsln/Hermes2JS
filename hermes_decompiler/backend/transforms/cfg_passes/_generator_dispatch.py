"""
Recognition of the hbc97+ hand-rolled generator state machine.

Up to hbc96 a generator suspended through dedicated VM opcodes
(StartGenerator/SaveGenerator/ResumeGenerator), and
`GeneratorStateMachineRegionPass` folds those back into `yield` once the
region tree exists. hbc97 removed those opcodes entirely - the repo's own
versioned opcode tables record them as `hbc58..hbc96` - and the compiler
now open-codes the state machine itself:

    entry:
        state = env[state_slot]
        if (state == EXECUTING) throw TypeError(...)   # re-entrancy guard
        if (state == COMPLETED) return {done: true}    # exhausted guard
        env[state_slot] = EXECUTING
        resumePoint = env[resume_slot]
        if (resumePoint == 0) goto R0                  # entry dispatch
        if (resumePoint == 1) goto R1
        ...
    Rk: if (action == THROW)  throw sentValue          # per-site protocol
        if (action == RETURN) return {done: true}      #   dispatch
        ...user code continues here...

    suspend site (one per `yield`):
        env[resume_slot] = k
        env[state_slot]  = SUSPENDED
        return {value: <yielded>, done: false}

Two consequences matter for structuring, and they are why this is
recognized at CFG level rather than on the region tree like its hbc96
counterpart:

  - The entry dispatch gives the *middle* of loops and try bodies extra
    predecessors, so those bodies are no longer single-entry and no
    structurer will claim them. Recognition therefore has to happen
    before any region exists.

  - A suspend site ends in `Ret`, which is a perfectly valid leaf
    terminator, so nothing downstream flags it as unstructured. The
    damage shows up somewhere else entirely - as raw gotos around the
    loop the dispatch edges punched into.

This module only *recognizes* the shape and reports it. Nothing here
mutates the CFG: the rewrite is the caller's job, so that a shape which
matches only partially can be left strictly alone rather than
half-transformed.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from hermes_decompiler.backend.analysis.cfg import BasicBlock, CFG
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)

#: `<Reg8: 1, UInt8: 3, Reg8: 4>` -> [1, 3, 4]
_OPERAND_RE = re.compile(r"(?:Reg8|UInt8|UInt16|UInt32|Addr8|Addr32|Imm32):\s*(-?\d+)")

_STORE_ENV_HANDLERS = (
    "StoreToEnvironment", "StoreToEnvironmentL",
    "StoreNPToEnvironment", "StoreNPToEnvironmentL",
)
_LOAD_ENV_HANDLERS = ("LoadFromEnvironment", "LoadFromEnvironmentL")
_LOAD_CONST_HANDLERS = ("LoadConstZero", "LoadConstUInt8", "LoadConstInt", "LoadConstDouble")
_EQ_BRANCH_HANDLERS = ("JStrictEqual", "JStrictEqualLong", "JEqual", "JEqualLong")
_NE_BRANCH_HANDLERS = (
    "JStrictNotEqual", "JStrictNotEqualLong", "JNotEqual", "JNotEqualLong",
)
_COMPARISON_HANDLERS = _EQ_BRANCH_HANDLERS + _NE_BRANCH_HANDLERS


def _operands(instruction) -> list[int]:
    entry = getattr(instruction, "entry", None)
    if entry is None:
        return []
    return [int(value) for value in _OPERAND_RE.findall(entry.args or "")]


def _const_value(instruction) -> int | None:
    """The integer a LoadConst* writes, or None if this isn't one."""
    handler = instruction.handler

    if handler == "LoadConstZero":
        return 0
    if handler not in _LOAD_CONST_HANDLERS:
        return None

    operands = _operands(instruction)
    return operands[1] if len(operands) >= 2 else None


@dataclass(frozen=True)
class SuspendSite:
    """One `yield`/`await`: where it suspends and which resume point it arms."""

    block: BasicBlock
    #: Value written to the resume-point slot - the key into the entry
    #: dispatch table, i.e. where execution continues when resumed.
    resume_point: int
    #: Index into `block.instructions` of the `env[resume_slot] = k` store.
    store_index: int
    #: The `{value, done: false}` result object's instruction index.
    result_index: int


@dataclass
class GeneratorDispatch:
    """A recognized hbc97+ generator state machine."""

    #: Environment slot holding the resume point (the dispatch key).
    resume_slot: int
    #: resume point -> address the entry dispatch sends it to.
    dispatch_targets: dict[int, int] = field(default_factory=dict)
    #: Blocks making up the entry dispatch chain, in bytecode order.
    dispatch_blocks: list[BasicBlock] = field(default_factory=list)
    suspend_sites: list[SuspendSite] = field(default_factory=list)

    @property
    def is_complete(self) -> bool:
        """
        True when every suspend site has a dispatch target to resume into.

        A site without one means the recognizer read the machine only
        partially; rewriting on that basis would drop a `yield` or
        redirect it to the wrong place.
        """
        if not self.suspend_sites or not self.dispatch_targets:
            return False

        return all(
            site.resume_point in self.dispatch_targets
            for site in self.suspend_sites
        )


def detect(cfg: CFG) -> GeneratorDispatch | None:
    """
    Recognize the state machine in `cfg`, or return None.

    Callers must have established independently that this function *is* a
    generator body (see FunctionKindIndex): on hbc97+ there is no opcode
    left that says so, and the shapes matched below - an environment slot
    compared against small constants, a returned two-property object - are
    individually ordinary enough to appear in hand-written code.
    """
    sites_by_slot = _suspend_sites_by_slot(cfg)

    if not sites_by_slot:
        return None

    # The resume slot is whichever candidate the entry dispatch actually
    # reads, and among candidates that parse as a complete dispatch, the
    # one whose chain starts earliest - the real dispatch always sits
    # immediately after the reentrancy/exhausted guards, at the very top
    # of the function. This tiebreak matters: a function can easily
    # contain *unrelated* code shaped just like a small dispatch (e.g. an
    # exception-cleanup block comparing some other slot against a couple
    # of small constants), which parses as "complete" too when it
    # happens to only need as many arms as that slot has suspend sites -
    # picking by lowest slot number alone was observed to prefer exactly
    # such a false match (asyncLoopTest's slot 6, matching cleanup code
    # near a rethrow) over the real one (slot 8, whose chain starts right
    # after the prologue).
    best: GeneratorDispatch | None = None
    best_start: int | None = None

    for resume_slot, sites in sites_by_slot.items():
        targets, blocks = _entry_dispatch(cfg, resume_slot)

        if not targets:
            continue

        dispatch = GeneratorDispatch(
            resume_slot=resume_slot,
            dispatch_targets=targets,
            dispatch_blocks=blocks,
            suspend_sites=sorted(sites, key=lambda s: s.block.address),
        )

        if not dispatch.is_complete:
            logger.debug(
                "Generator dispatch on env[%d] recognized only partially: "
                "resume points %s have no dispatch target; leaving the raw form in place.",
                resume_slot,
                sorted({s.resume_point for s in sites} - set(targets)),
            )
            continue

        start = blocks[0].address

        if best_start is None or start < best_start:
            best, best_start = dispatch, start

    return best


def _suspend_sites_by_slot(cfg: CFG) -> dict[int, list[SuspendSite]]:
    """
    Find every `env[slot] = k; return {value, done: false}` block.

    Keyed by slot rather than resolved immediately, because which slot is
    the resume point is only settled by the entry dispatch - a suspend
    site also writes the *state* slot, and both stores look alike here.
    """
    sites: dict[int, list[SuspendSite]] = {}
    blocks = sorted(cfg.blocks, key=lambda b: b.address)

    for block in blocks:
        result_index = _yield_result_index(block)

        if result_index is None:
            continue

        # Same prologue-constant concern as the comparison reader: the
        # value armed into the resume slot is often a register the
        # prologue loaded, not one loaded in the suspend block itself.
        constants = {
            **_constants_before(blocks, block),
            **_constant_registers(block, upto=result_index),
        }

        for index in range(result_index):
            instruction = block.instructions[index]

            if instruction.handler not in _STORE_ENV_HANDLERS:
                continue

            operands = _operands(instruction)

            if len(operands) < 3:
                continue

            _, slot, value_reg = operands[0], operands[1], operands[2]
            resume_point = constants.get(value_reg)

            if resume_point is None:
                continue

            sites.setdefault(slot, []).append(
                SuspendSite(
                    block=block,
                    resume_point=resume_point,
                    store_index=index,
                    result_index=result_index,
                )
            )

    return sites


def _yield_result_index(block: BasicBlock) -> int | None:
    """
    Index of the `{value, done: false}` object this block returns, if any.

    `done: false` is the whole test: a generator's *completion* paths
    build the same shape with `done: true`, and folding one of those into
    a `yield` would turn a return into an infinite generator.
    """
    from hermes_decompiler.ir.terminators import TerminatorReturn

    if not isinstance(block.terminator, TerminatorReturn) or not block.instructions:
        return None

    for index in range(len(block.instructions) - 1, -1, -1):
        literal = getattr(block.instructions[index].entry, "object_literal", None)

        if not isinstance(literal, dict) or "done" not in literal:
            continue

        return index if literal.get("done") is False else None

    return None


def _constant_registers(block: BasicBlock, upto: int) -> dict[int, int]:
    """register -> integer constant most recently loaded into it."""
    constants: dict[int, int] = {}

    for instruction in block.instructions[:upto]:
        value = _const_value(instruction)

        if value is None:
            continue

        operands = _operands(instruction)

        if operands:
            constants[operands[0]] = value

    return constants


def _constants_before(blocks: list[BasicBlock], target: BasicBlock) -> dict[int, int]:
    """
    Constant registers visible at `target`, accumulated in address order.

    Block-local tracking is not enough here: the state machine loads its
    comparison constants once in the straight-line prologue and then
    compares against them from blocks further down. Scanning in address
    order is an approximation of reaching-definitions, and a deliberately
    safe one - a register that was really overwritten on some other path
    yields a comparison that simply fails to match, and an unmatched
    comparison ends recognition rather than rewriting anything.
    """
    constants: dict[int, int] = {}

    for block in blocks:
        if block.address >= target.address:
            break
        constants.update(_constant_registers(block, upto=len(block.instructions)))

    return constants


def _entry_dispatch(cfg: CFG, resume_slot: int) -> tuple[dict[int, int], list[BasicBlock]]:
    """
    Walk the entry dispatch chain that switches on `env[resume_slot]`.

    Returns `(resume point -> address the user code resumes at, blocks in
    the chain)`.

    Two details make this more than a comparison-chain walk, and both were
    found by reading real hbc98 output rather than assumed:

      - The last resume point has no test of its own. The chain compares
        `resumePoint == 0 .. N-2` and simply falls through for `N-1`, so
        the highest arm is implicit and must be recovered from the chain's
        fall-through rather than from any branch.

      - A dispatch arm does not land on user code. It lands on a
        per-site protocol preamble that re-dispatches on the *action*
        argument (`.next()` / `.throw()` / `.return()`), routing the
        latter two to a throw and an early completion. Only the
        `.next()` path - the fall-through past those tests - is the
        resume point in source terms, so the arm has to be followed
        through them.

    Following the chain along fall-through edges only is what keeps the
    re-entrancy and exhausted guards ahead of it, which compare the
    *state* slot, from being mistaken for dispatch arms.
    """
    from hermes_decompiler.ir.terminators import TerminatorConditionalBranch

    blocks = sorted(cfg.blocks, key=lambda b: b.address)
    by_address = {block.address: block for block in blocks}

    start = _dispatch_start(blocks, resume_slot)

    if start is None:
        return {}, []

    action_register = _action_register(blocks)

    raw_targets: dict[int, int] = {}
    chain: list[BasicBlock] = []

    index, register = start

    while index < len(blocks):
        block = blocks[index]
        comparison = _equality_comparison(block, blocks)

        if (
                not isinstance(block.terminator, TerminatorConditionalBranch)
                or comparison is None
                or comparison[0] != register
                or comparison[2]  # a dispatch arm is always `== k`
        ):
            break

        chain.append(block)
        raw_targets[comparison[1]] = block.terminator.target
        index += 1

    if not chain:
        return {}, []

    # The implicit final arm: whatever the chain falls through to belongs
    # to the next resume point after the last one tested.
    if index < len(blocks):
        raw_targets[max(raw_targets) + 1] = blocks[index].address

    targets = {
        resume_point: _skip_action_dispatch(by_address, address, action_register)
        for resume_point, address in raw_targets.items()
    }

    return targets, chain


def _action_register(blocks: list[BasicBlock]) -> int | None:
    """
    The register holding the resume action (`.next`/`.throw`/`.return`).

    It arrives as the generator body's second parameter, so it is
    whichever register `LoadParam ..., 1` writes.
    """
    for block in blocks:
        for instruction in block.instructions:
            if instruction.handler != "LoadParam":
                continue

            operands = _operands(instruction)

            if len(operands) >= 2 and operands[1] == 1:
                return operands[0]

    return None


def _skip_action_dispatch(
        by_address: dict[int, BasicBlock],
        address: int,
        action_register: int | None,
) -> int:
    """
    Advance past a dispatch arm's `.throw()`/`.return()` tests.

    Returns the address where the `.next()` path - the only one with a
    source-level meaning - actually continues. Unrecognized shapes are
    returned unchanged rather than guessed past.
    """
    from hermes_decompiler.ir.terminators import TerminatorConditionalBranch

    if action_register is None:
        return address

    blocks = sorted(by_address.values(), key=lambda b: b.address)
    ordered = [block.address for block in blocks]
    seen: set[int] = set()

    while address in by_address and address not in seen:
        seen.add(address)
        block = by_address[address]
        comparison = _equality_comparison(block, blocks)

        if (
                not isinstance(block.terminator, TerminatorConditionalBranch)
                or comparison is None
                or comparison[0] != action_register
        ):
            return address

        negated = comparison[2]

        if negated:
            # `if (action != RETURN) goto body` - the branch itself is
            # the ordinary path.
            address = block.terminator.target
            continue

        # `if (action == THROW) goto throw` - the test branches *away*
        # to the protocol path, so the ordinary resume falls through.
        position = ordered.index(address)

        if position + 1 >= len(ordered):
            return address

        address = ordered[position + 1]

    return address


def _dispatch_start(blocks: list[BasicBlock], resume_slot: int) -> tuple[int, int] | None:
    """
    Locate `rX = env[resume_slot]` and return `(block index, rX)`.

    The *last* load before the first comparison wins: Hermes reloads the
    slot into a fresh register right before dispatching on it.
    """
    for index, block in enumerate(blocks):
        for instruction in block.instructions:
            if instruction.handler not in _LOAD_ENV_HANDLERS:
                continue

            operands = _operands(instruction)

            if len(operands) >= 3 and operands[2] == resume_slot:
                return index, operands[0]

    return None


def _equality_comparison(
        block: BasicBlock,
        blocks: list[BasicBlock] | None = None,
) -> tuple[int, int, bool] | None:
    """
    `(register, constant, negated)` this block's branch compares, else None.

    `negated` is True for the `JStrictNotEqual` family, where the branch
    is taken when the values *differ*. That flips which edge is the
    ordinary continuation, and the state machine uses both polarities -
    the `.return()` test in particular is emitted as "if action is NOT
    return, go on with the body".

    Reads raw operands rather than the lifted condition expression: the
    comparison is against a freshly loaded constant register, so matching
    on registers keeps this independent of how far expression propagation
    happened to fold things.
    """
    if not block.instructions:
        return None

    branch = block.instructions[-1]

    if branch.handler not in _COMPARISON_HANDLERS:
        return None

    operands = _operands(branch)

    if len(operands) < 3:
        return None

    _, left, right = operands[0], operands[1], operands[2]

    constants = _constant_registers(block, upto=len(block.instructions) - 1)

    if blocks is not None:
        # Block-local definitions win over anything carried in from the
        # prologue, so seed with the wider map and let the local one
        # overwrite it.
        constants = {**_constants_before(blocks, block), **constants}

    negated = branch.handler in _NE_BRANCH_HANDLERS

    # Either side may hold the constant.
    if right in constants:
        return left, constants[right], negated
    if left in constants:
        return right, constants[left], negated

    return None
