from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    RegionVisitor,
    IfRegion,
    SequenceRegion,
)
from hermes_decompiler.core.logging import get_logger
from ._base import RegionPass

logger = get_logger(__name__)


class IfTailMergeRegionPass(RegionPass, RegionVisitor):
    """Hoists an `IfRegion`'s two branches' common TRAILING instructions
    out into a single shared block right after the `IfRegion`, when
    Hermes has physically duplicated them into both branches instead of
    letting them jointly fall through to one shared instance.

    Source:

        if (i === 2) {
            console.log("continue-case");
            i++;
            continue;
        }
        i++;

    Hermes compiles the `i++` shared by both paths - the one right
    before `continue` and the one that's the loop's ordinary
    completion - as two separate, textually identical copies, one
    inlined into each branch, rather than one shared instruction both
    paths jump to (that would need an actual block boundary and a real
    jump, which straight-line duplication avoids). With nothing but a
    `continue`-shaped jump to look for (see `LoopContinueRegionPass`'s
    own docstring for that OTHER, jump-based case this one does NOT
    handle), the duplicate slips through as plain, unremarkable body
    content in both branches:

        if (r7 === 2) {
            console.log("continue-case");
            r6 = r7 + 1;
        } else {
            r6 = r7 + 1;
        }

    The duplicated instruction is typically NOT the whole of either
    branch's own last block - Hermes still emits the `then` branch's
    OWN content (the `console.log` call above) in the SAME physical
    block as its copy of the shared tail, so this compares TRAILING
    INSTRUCTIONS one at a time (from the end of each branch's own last
    block backward), not whole blocks: as many as keep matching are
    split off, however few or many that turns out to be, leaving each
    branch's own distinct prefix behind untouched.

    This pass finds that matching run and reinserts ONE copy as an
    ordinary sibling right after the `IfRegion`:

        if (r7 === 2) {
            console.log("continue-case");
        }
        r6 = r7 + 1;

    Confirmed bug (`whileTest`): the duplicate `r6 = r7 + 1` printed
    unchanged in BOTH branches, `LoopContinueRegionPass` finding nothing
    to convert in either - not just noisier output, but a case that
    read as though `i++` happened twice some iterations (once per
    branch, textually) even though at runtime it's exactly once either
    way.

    Only ever compares/splits `BasicBlock` items - a branch whose
    trailing item is itself a nested `Region` (another `IfRegion`, a
    `TryRegion`, ...) is left alone entirely; those don't arise from
    this specific straight-line-duplication idiom, and reasoning about
    a shared tail inside two structurally-equal-but-distinct nested
    regions is a fair amount riskier than splitting two blocks' plain
    instruction lists, for something that isn't a confirmed shape yet.

    Deliberately narrow beyond that too: an instruction only counts as
    matching its counterpart when its destination register, computed
    value (by `repr`, matching the same-file convention
    `_handler_builder.py`/`LoopConditionRegionPass.py` already use for
    comparing `Expression` trees, since these nodes don't define
    `__eq__`), emitted statement (if any), and terminator (if any - the
    SAME kind, aimed at the SAME address) all agree. Anything that
    merely LOOKS similar but differs in any of this stops the match
    right there, keeping whatever already matched before it.

    Must run after `IfStructurer` (needs real `IfRegion`s to inspect)
    and before `LoopConditionRegionPass` (so a merged tail that turns
    out to BE the loop's own per-iteration update - `whileTest`'s own
    `r6 = r7 + 1` - is already sitting as ordinary, singular body
    content by the time that pass goes looking for one, rather than
    still being duplicated across both branches where it can't
    recognize either copy as it).

    Skips a function ENTIRELY the moment it contains any
    `StartGenerator`/`SaveGenerator`/`SaveGeneratorLong`/
    `ResumeGenerator` instruction, however far from the actual merge
    site - confirmed regression: allocating a brand new `BasicBlock`
    (a fresh id, appended to `self.cfg.blocks`) and relocating content
    out of an existing one is exactly the kind of raw-CFG-shape change
    `GeneratorStateMachineRegionPass`'s suspend/resume dispatch
    recognition (much later in `StructuralAnalyzer`'s own pass order)
    turned out to be sensitive to - a previously-correctly-resolved
    `async function` started rendering raw, invalid `goto label_N;`
    once this pass had touched its blocks, EVEN on an if/else pair
    nowhere near the actual `SaveGenerator`/`ResumeGenerator` site
    itself. Generator/async dispatch recognition is independently
    fragile enough already (see that pass's own docstring) that
    running this cosmetic cleanup anywhere in the same function isn't
    worth the risk until that interaction is understood on its own
    terms.
    """

    _GENERATOR_HANDLERS = frozenset((
        "StartGenerator",
        "SaveGenerator",
        "SaveGeneratorLong",
        "ResumeGenerator",
    ))

    def run(self) -> None:
        if self._is_generator_or_async(self.cfg):
            return

        self.visit(self.graph.root)

    @classmethod
    def _is_generator_or_async(cls, cfg) -> bool:
        return any(
            instruction.handler in cls._GENERATOR_HANDLERS
            for block in cfg.blocks
            for instruction in block.instructions
        )

    # ------------------------------------------------------------------

    def visit_SequenceRegion(self, node: SequenceRegion) -> None:
        insertions: list[tuple[int, BasicBlock]] = []

        for index, child in enumerate(node.children):
            self.visit(child)

            if isinstance(child, IfRegion):
                merged = self._try_merge_tail(child)

                if merged is not None:
                    insertions.append((index, merged))

        # Applied back-to-front so each insertion's own index is still
        # valid relative to `node.children` at the moment it's applied -
        # inserting earlier in the list would otherwise shift every
        # later insertion's recorded index out from under it.
        for index, merged_block in reversed(insertions):
            self.graph.insert_at(node, index + 1, merged_block)

    # ------------------------------------------------------------------

    def _try_merge_tail(self, if_region: IfRegion) -> BasicBlock | None:
        """If `if_region`'s two branches' own last blocks share a
        matching run of TRAILING instructions, split it off both and
        return one shared copy (a brand new `BasicBlock`) - or `None`
        if there's nothing to merge (no `else_body`, either branch's
        last item isn't a plain `BasicBlock`, or their very last
        instructions don't even match).

        An `else_body` left completely empty by this (the common case:
        Hermes' compiled `else` here often holds nothing BUT the
        duplicated tail) has its `IfRegion.else_body` cleared to `None`
        entirely, rather than printing a pointless empty `else {}`. A
        `then_body` left completely empty is left AS an empty body -
        an `if (cond) {}` with all its meaning in the condition itself
        is at least accurate, if unusual; nothing currently exercises
        that shape.
        """
        if if_region.else_body is None:
            return None

        then_body = if_region.then_body
        else_body = if_region.else_body

        if not then_body.children or not else_body.children:
            return None

        then_block = then_body.children[-1]
        else_block = else_body.children[-1]

        if not isinstance(then_block, BasicBlock) or not isinstance(else_block, BasicBlock):
            return None

        match_count = 0

        while (
                match_count < len(then_block.instructions)
                and match_count < len(else_block.instructions)
                and self._instructions_equal(
            then_block.instructions[-1 - match_count],
            else_block.instructions[-1 - match_count],
        )
        ):
            match_count += 1

        if match_count == 0:
            return None

        matched_instructions = then_block.instructions[len(then_block.instructions) - match_count:]

        self._trim_trailing(then_body, then_block, match_count)
        self._trim_trailing(else_body, else_block, match_count)

        new_id = max((block.id for block in self.cfg.blocks), default=0) + 1
        merged_block = BasicBlock(new_id, address=matched_instructions[0].address)
        merged_block.instructions = matched_instructions

        terminator_instruction = next(
            (instruction for instruction in matched_instructions if instruction.terminator is not None),
            None,
        )

        if terminator_instruction is not None:
            merged_block.terminator = terminator_instruction.terminator

        self.cfg.blocks.append(merged_block)

        if not else_body.children:
            if_region.else_body = None

        return merged_block

    # ------------------------------------------------------------------

    def _trim_trailing(self, body: SequenceRegion, block: BasicBlock, match_count: int) -> None:
        """Remove `block`'s own last `match_count` instructions - the
        ones just confirmed to match the other branch's - dropping
        `block` from `body` entirely if that consumes all of it,
        otherwise leaving `block`'s own distinct prefix behind with no
        terminator (the matched, now-removed suffix owned whichever
        terminator there was, if any - see `_try_merge_tail`, which
        reattaches it to the new shared block instead).
        """
        remaining = len(block.instructions) - match_count

        if remaining == 0:
            self.graph.splice_out(body, len(body.children) - 1, len(body.children))
            return

        block.instructions = block.instructions[:remaining]
        block.terminator = None
        body.invalidate_coverage()

    # ------------------------------------------------------------------

    @staticmethod
    def _instructions_equal(instruction_a, instruction_b) -> bool:
        """True when two instructions compute the same thing: same
        destination register, equal (by `repr`) value and statement,
        and terminators of the same kind aimed at the same address (or
        both none).

        Never compares `.address` or any other purely positional
        detail - Hermes' two physical copies of the same logical
        statement legitimately live at different addresses; only their
        CONTENT needs to agree.
        """
        if instruction_a.dest_reg != instruction_b.dest_reg:
            return False

        if repr(instruction_a.value) != repr(instruction_b.value):
            return False

        if repr(instruction_a.statement) != repr(instruction_b.statement):
            return False

        terminator_a = instruction_a.terminator
        terminator_b = instruction_b.terminator

        if (terminator_a is None) != (terminator_b is None):
            return False

        if terminator_a is not None:
            if type(terminator_a) is not type(terminator_b):
                return False

            if terminator_a.targets != terminator_b.targets:
                return False

        return True
