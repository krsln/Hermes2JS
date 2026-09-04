from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import RegionVisitor, IfRegion, SequenceRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.ir.expressions import Identifier, YieldExpression
from .BaseRegionPass import RegionPass

logger = get_logger(__name__)

_RESUME_FLAG_NAME = "__resumeIsReturn"
_SAVE_GENERATOR_HANDLERS = ("SaveGenerator", "SaveGeneratorLong")
_RESUME_GENERATOR_HANDLER = "ResumeGenerator"


class GeneratorStateMachineRegionPass(RegionPass, RegionVisitor):
    """
    Collapse Hermes's generator suspend/resume state machine into
    plain `yield <value>;` statements.

    A generator body's *own* bytecode never contains a `yield`
    keyword's worth of structure directly - Hermes lowers every
    suspend point into four raw opcodes plus a protocol-boilerplate
    branch:

        rX = value            # LoadConst.../etc
        SaveGenerator -> R    # record the resume address, fall through
        Ret rX                 # suspend, handing `value` to the caller
    R:  ResumeGenerator rY, rZ  # rY = value passed to .next()/.throw()/
                                 #      .return(); rZ = true iff .return()
        if (rZ) {
            return rY;         # early-exit: caller called .return()
                                # before ever asking to resume normally
        } else {
            ...rest of the function's real code...
        }

    (see StartGenerator.py/ResumeGenerator.py/SaveGenerator.py/
    CompleteGenerator.py's own docstrings for the individual opcodes'
    semantics). By the time this pass runs, IfStructurer has already
    turned the `if (rZ)` branch into a clean IfRegion, so what's left
    to recognize is a fixed four-part sequence anchored on that
    IfRegion: an optional `[[value =] SaveGenerator]` block, an
    optional orphaned `[Ret rX]` block (a real artifact of Hermes's
    own bytecode layout - `Ret rX` sits at the address immediately
    after `SaveGenerator` textually, but SaveGenerator's own jump edge
    always skips straight to the resume address, so this block is
    simply never reached at runtime; whether it survives as a visible
    sibling block depends on which structurer produced this specific
    SequenceRegion, so both its presence and its absence are treated
    as normal here - see `_try_fold_at`), the `ResumeGenerator` block
    itself, and the `if (__resumeIsReturn)` IfRegion.

    Folded into:

        yield value;
        ...rest of the function's real code...

    The very first suspend point - right after `StartGenerator`, before
    any `yield` has actually run - has no preceding `SaveGenerator`/
    `Ret` pair at all (there's nothing to yield yet; it's just "wait to
    be told to start"), so it folds to no statement at all, not `yield
    undefined;`.

    Scope, deliberately narrow (bail out - leave the raw form in place -
    rather than guess) whenever the shape doesn't match exactly:

    - The resumed value (`rY` above) is bound (`rY = yield value;`)
      when something downstream reads it, and dropped (`yield value;`)
      otherwise. The one case still left unhandled: the very first
      resume, right after `StartGenerator`, has no preceding
      `SaveGenerator`/yield of its own to attach a binding to - if its
      resumed value turns out to be read (unusual: it's whatever a
      caller's very first `.next(v)` sent, before the generator body
      has run at all), this pass leaves that occurrence alone.
    - `yield*` (delegating yield) uses different opcodes entirely and
      isn't recognized here.
    - This pass only removes the *generic* suspend/resume machinery.
      It has no opinion on whether the enclosing function is really a
      sync generator (`function*`) or an `async function` compiled
      through the exact same machinery (see SignatureStage.py's own
      note on why that distinction can't be made from this function's
      bytecode alone) - either way, the fold is the same; only the
      keyword a *later* pass ultimately prints ("yield" vs "await")
      would differ, and this pass always leaves a `YieldExpression`
      for that later step to relabel if needed.
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    # ------------------------------------------------------------------
    # Traversal
    # ------------------------------------------------------------------

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            self.visit(child)

        self._fold_sequence(node)

    def _fold_sequence(self, region: SequenceRegion) -> None:
        # StartGenerator/CompleteGenerator are pure protocol markers
        # with no JS-observable effect of their own (see their own
        # handler docstrings). Stripping them first means the entry
        # suspend point (StartGenerator + the first ResumeGenerator
        # pair) and every early-return landing pad (CompleteGenerator
        # + Ret) reduce to the exact same shapes the matching below
        # already has to handle anyway.
        for child in region.children:
            if isinstance(child, BasicBlock) and child.instructions:
                child.instructions = [
                    instruction
                    for instruction in child.instructions
                    if instruction.handler not in ("StartGenerator", "CompleteGenerator")
                ]

        region.children = [
            child
            for child in region.children
            if not (isinstance(child, BasicBlock) and not child.instructions)
        ]

        index = 0

        while index < len(region.children):
            if self._try_fold_at(region, index):
                # Folding spliced the next suspend point's own blocks
                # in at this same position - re-check here rather than
                # advancing past it.
                continue

            index += 1

    # ------------------------------------------------------------------
    # Main pattern
    # ------------------------------------------------------------------

    def _try_fold_at(self, region: SequenceRegion, index: int) -> bool:
        yield_block = None
        offset = 0

        candidate = self._child_at(region, index)

        if (
                isinstance(candidate, BasicBlock)
                and candidate.instructions
                and candidate.instructions[-1].handler in _SAVE_GENERATOR_HANDLERS
        ):
            yield_block = candidate
            offset = 1

            dead_ret = self._child_at(region, index + offset)

            if (
                    isinstance(dead_ret, BasicBlock)
                    and len(dead_ret.instructions) == 1
                    and dead_ret.instructions[0].handler == "Ret"
            ):
                offset += 1
                # Same real-CFG-predecessor concern as resume_block
                # below - this block is dropped from the tree, so clear
                # its instructions rather than leaving a stale `Ret`
                # for some later pass's own CFG walk to trip over.
                dead_ret.instructions = []

        resume_block = self._child_at(region, index + offset)

        if not self._is_resume_block(resume_block):
            return False

        if_region = self._child_at(region, index + offset + 1)

        if not self._is_resume_guard(if_region):
            return False

        resumed_reg = resume_block.instructions[-2].dest_reg

        # Safety invariant this fold relies on: when `if_region` has no
        # else_body, everything that would otherwise need checking for
        # a `resumed_reg` reference must already be exhausted - i.e.
        # nothing structurally "after" this guard remains in `region`.
        # That should always hold for this specific shape (the guard's
        # then-body is a single terminal `Ret`, which - per
        # `_DominanceIfBuilder._convert` - can never itself be the
        # post-dominance merge point two branches share, so `has_else`
        # is always True and `else_body` always absorbs the rest of
        # the enclosing SequenceRegion). But that chain of reasoning
        # lives in a different file (the if-structurer) and isn't
        # asserted anywhere - if it's ever violated (a future
        # structurer change, or an hbc version with a different
        # layout), trusting "else_body is None -> nothing follows"
        # blindly would silently drop a live reference to
        # `resumed_reg`, leaving a later read of it with no defining
        # instruction anywhere in the function. Check the actual
        # remaining siblings instead of assuming; bail out to the raw,
        # unfolded form (safe, just less readable) if the invariant
        # doesn't hold rather than risk that.
        trailing_siblings = region.children[index + offset + 2:]

        if if_region.else_body is None and trailing_siblings:
            logger.warning(
                "Resume-guard at index %d has no else_body but %d "
                "trailing sibling(s) remain in the enclosing region - "
                "the 'nothing follows' invariant this pass relies on "
                "doesn't hold here. Leaving the raw suspend/resume "
                "form in place rather than risk dropping a live "
                "reference to r%d.",
                index, len(trailing_siblings), resumed_reg,
            )
            return False

        # resume_block is about to be dropped from the region tree
        # entirely (never appended to new_children below). That alone
        # isn't enough: the underlying CFG's real predecessor/successor
        # edges were built once, upfront, from the original bytecode,
        # and are NOT updated by any region-tree edit here. A later
        # pass that does reaching-definition analysis by walking those
        # real CFG predecessors (ReturnValueResolutionPass, most
        # notably) can still walk straight through this now-detached
        # block and find its stale ResumeGenerator-produced register
        # definitions, as if they were still live. Clearing its
        # instructions (nothing below needs them anymore - the
        # register we care about was already read into `resumed_reg`
        # above) makes such a walk pass straight through to whatever
        # real definition comes before it instead.
        resume_block.instructions = []

        # A None else_body means the resume-guard was the last thing in
        # its enclosing block (most commonly: a yield as the final
        # statement of a loop iteration) - there's nothing after it to
        # check (the trailing_siblings guard above confirms this
        # holds), which is fine; treat it the same as "not referenced".
        resumed_is_used = (
                if_region.else_body is not None
                and self._register_is_referenced(if_region.else_body, resumed_reg)
        )

        if resumed_is_used and yield_block is None:
            # The entry-point resume (right after StartGenerator, with
            # no preceding SaveGenerator/yield of its own) has no
            # yield_block to attach a synthetic `rY = yield ...;`
            # assignment to. Not handled - bail out rather than
            # silently drop a value that's genuinely read.
            return False

        # Same real-CFG-predecessor concern as resume_block/dead_ret
        # above - the early-return landing pad is dropped entirely
        # (never appended to new_children), so clear it too.
        for child in if_region.then_body.children:
            if isinstance(child, BasicBlock):
                child.instructions = []

        new_children = list(region.children[:index])

        if yield_block is not None and len(yield_block.instructions) >= 2:
            value_instruction = yield_block.instructions[-2]
            save_instruction = yield_block.instructions[-1]

            # The value feeding the yield becomes part of the yield
            # statement itself now - it must not also print as its
            # own separate `rX = ...;` line.
            value_instruction.definition_used = True

            yield_block.instructions = yield_block.instructions[:-2] + [
                OpcodeResult(
                    save_instruction.entry,
                    value=YieldExpression(argument=value_instruction.value),
                    # Bind the resumed value to its own register only
                    # when something downstream actually reads it -
                    # otherwise a bare `yield value;` statement, same
                    # as before.
                    dest_reg=resumed_reg if resumed_is_used else None,
                )
            ]
            yield_block.terminator = None

            new_children.append(yield_block)

        if if_region.else_body is not None:
            new_children.extend(if_region.else_body.children)

        new_children.extend(trailing_siblings)

        region.children = new_children

        return True

    @staticmethod
    def _child_at(region: SequenceRegion, index: int):
        if 0 <= index < len(region.children):
            return region.children[index]
        return None

    @staticmethod
    def _is_resume_block(block) -> bool:
        return (
                isinstance(block, BasicBlock)
                and len(block.instructions) >= 2
                and block.terminator is None
                and block.instructions[-1].handler == _RESUME_GENERATOR_HANDLER
                and block.instructions[-2].handler == _RESUME_GENERATOR_HANDLER
        )

    @staticmethod
    def _is_resume_guard(node) -> bool:
        if not isinstance(node, IfRegion):
            return False

        if not isinstance(node.condition, Identifier):
            return False

        if node.condition.name != _RESUME_FLAG_NAME:
            return False

        then_children = [
            child
            for child in node.then_body.children
            if not (isinstance(child, BasicBlock) and not child.instructions)
        ]

        if len(then_children) != 1:
            return False

        then_block = then_children[0]

        return (
                isinstance(then_block, BasicBlock)
                and [i.handler for i in then_block.instructions] == ["Ret"]
        )

    # ------------------------------------------------------------------
    # Safety: is the resumed value actually read downstream?
    # ------------------------------------------------------------------

    def _register_is_referenced(self, region: SequenceRegion, register: int | None) -> bool:
        if register is None:
            return False

        finder = _RegisterReferenceFinder(f"r{register}")
        finder.visit(region)

        return finder.found

    @staticmethod
    def _expression_references(expr, name: str) -> bool:
        if expr is None:
            return False

        if isinstance(expr, Identifier):
            return expr.name == name

        return any(
            GeneratorStateMachineRegionPass._expression_references(child, name)
            for child in getattr(expr, "children", ())
        )


class _RegisterReferenceFinder(RegionVisitor):
    """Conservative "is r{N} read anywhere in this subtree" search.

    Reuses RegionVisitor's own default traversal for region kinds this
    pass doesn't need to fold anything in (LoopRegion/TryRegion/
    SwitchRegion) so the search still reaches into them, rather than
    silently treating "not folded here" as "not referenced" - that
    would make the enclosing pass's safety check UNDER-cautious.
    """

    def __init__(self, name: str):
        self.name = name
        self.found = False

    def visit(self, node) -> None:
        if self.found:
            return
        super().visit(node)

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        for child in node.children:
            if self.found:
                return
            if isinstance(child, BasicBlock):
                self._check_block(child)
            else:
                self.visit(child)

    def visit_IfRegion(self, node: IfRegion) -> None:
        if GeneratorStateMachineRegionPass._expression_references(node.condition, self.name):
            self.found = True
            return
        super().visit_IfRegion(node)

    def _check_block(self, block: BasicBlock) -> None:
        for instruction in block.instructions or []:
            if GeneratorStateMachineRegionPass._expression_references(instruction.value, self.name):
                self.found = True
                return

        terminator = block.terminator

        if terminator is None:
            return

        condition = getattr(terminator, "condition", None)
        value = getattr(terminator, "value", None)

        if GeneratorStateMachineRegionPass._expression_references(condition, self.name):
            self.found = True
        elif GeneratorStateMachineRegionPass._expression_references(value, self.name):
            self.found = True
