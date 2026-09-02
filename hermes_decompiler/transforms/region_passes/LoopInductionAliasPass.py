from __future__ import annotations

import dataclasses

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.models import RegionVisitor, TerminatorConditionalBranch
from hermes_decompiler.analysis.models.regions import IfRegion, LoopRegion, SwitchRegion
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import BinaryExpression, Identifier

from hermes_decompiler.transforms.region_passes.BaseRegionPass import RegionPass

logger = get_logger(__name__)


class LoopInductionAliasPass(RegionPass, RegionVisitor):
    """Eliminates the per-iteration let-scoping alias for a for loop's induction variable.

    Rewrites the body to read the SAME register the
    `for (init; cond; update)` header itself uses - letting the
    Printer render a single `i` instead of two distinct registers that
    happen to alias each other every iteration.

    The shape this targets (see forTest in section_15051_raw.js)::
        r5 = 0                          # initializer (already
                                         # extracted into
                                         # loop.initializer by
                                         # LoopConditionRegionPass)
        header:
            r6 = r5                     # <-- the alias Mov this pass
                                         #     removes
            ... body reads/writes r6 only, never r5 ...
        update:
            r5 = r6 + 1                 # already extracted into
                                         # loop.update by
                                         # LoopConditionRegionPass,
                                         # but its right-hand side
                                         # still references r6 (the
                                         # alias), not r5
    Without this pass the alias Mov either prints as a redundant
    `let i_alias = i;` first statement, or - worse - silently
    vanishes (inlined by `OpcodeHandler.get_register_expression` into
    whichever instruction first reads it) while every OTHER read of
    the alias register in the body still renders as its own register
    name, never as `i`. Neither outcome matches what the surrounding
    `for (let i = ...)` header implies.

    Pipeline placement
    ------------------
    Must run strictly after LoopConditionRegionPass, in
    StructuralAnalyzer.build()'s stage-3 block, immediately after
    `LoopConditionRegionPass(graph, self.cfg).run()`:

      - It needs loop.update already populated (that's where the
        induction register's identity is read from - see
        `_induction_register`; this pass never re-derives it via its
        own reaching-def heuristic, to avoid a second, possibly
        divergent copy of that logic).
      - Because LoopConditionRegionPass runs after IfStructurer /
        TryStructurer / SwitchStructurer, any `if (r6 === 3)` test
        inside the loop body has already been folded into an
        IfRegion.condition (or a SwitchRegion case test) by the time
        this pass sees it - no longer a raw BasicBlock.terminator. The
        repoint walk below is therefore a full RegionVisitor traversal
        of loop.body, not a flat scan over
        loop.body.covered_blocks the way e.g., LoopBreakStructurer
        (which runs before structuring) can get away with.
      - Should run before ForEachRegionPass: that pass's own register
        resolution (`_resolve_identifier`) walks every block in the
        whole graph looking for a register's defining instruction and
        takes whichever one it finds first - fewer, cleaner
        (unaliased) registers in the loop body reduce the risk of it
        resolving against the wrong candidate.
      - Ordering relative to LoopContinueRegionPass doesn't matter:
        that pass only touches TerminatorJump/ContinueStatement
        shapes, never register identities.

    Deliberately narrow / conservative
    -----------------------------------
    Every one of the following must hold, or the pass leaves that
    loop's registers untouched rather than guessing:

      1. The loop was classified LoopKind.FOR and
         LoopConditionRegionPass already recovered both
         loop.initializer and loop.update (loop.update.left is where
         the induction register's name comes from - see
         `_induction_register`; loop.initializer.right is what the
         header Mov's resolved value gets checked against - see point
         2 below and `_is_induction_alias_copy`'s own docstring).
      2. loop.update.right contains a register operand other than the
         induction register itself (`_body_register`) - that register
         is body_reg, the per-iteration alias. Read directly off
         metadata LoopConditionRegionPass already recovered, not
         assumed from position: at three levels of loop nesting,
         Hermes may place another per-iteration alias Mov - for some
         unrelated outer-scoped `let` variable captured across the
         loop, not the induction variable at all - textually before
         this loop's own induction alias in the same header block (see
         `tripleNestedLabeledTest`: the middle loop's header carries
         `Mov r13, r10`, an unrelated accumulator carry-forward, ahead
         of `Mov r11, r9`, the actual induction alias this pass needs).
         Requiring "first instruction" would silently skip the real
         alias in that case; deriving body_reg from loop.update.right
         instead sidesteps position altogether.
      3. The header contains some instruction (anywhere in it, not
         necessarily first) with dest_reg == body_reg whose resolved
         value structurally matches loop.initializer.right
         (`_is_induction_alias_copy` - see its own docstring for why
         value, not name, is the reliable signature) -
         `_find_alias_instruction`.
      4. `body_reg` is not itself the induction register (nothing to do)
         and is never the destination of any other instruction
         anywhere in the loop body (`_body_reg_only_defined_here`). -
         If it were, this alias Mov would only be establishing the
         first of several distinct values that register takes on
         during one iteration, and blindly substituting induction_reg
         for every read would silently discard whatever that later
         write meant.

    Residual false-positive risk (accepted, documented): body_reg
    itself is no longer a guess (point 2 derives it directly from
    loop.update.right), but which instruction in the header counts as
    that register's alias copy (point 3) still matches by value rather
    than a positively-identified Mov opcode (this pass only has access
    to already-resolved OpcodeResults, not the original bytecode
    entry/opcode name). If the header contains more than one
    instruction writing body_reg and an earlier, unrelated one happens
    to resolve to the same value as the initializer (e.g., coincidentally
    also literal `0`), `_find_alias_instruction` would pick that one
    instead of the real alias. This is bounded and non-corrupting even
    if it happens: the substitution only ever touches reads of that one
    specific body_reg number, so at worst it mislabels one register as
    `i` cosmetically - it can never rewrite an unrelated computation's
    actual value, since `_body_reg_only_defined_here` still requires
    body_reg to have exactly one definition (the matched instruction)
    in the whole loop body before anything is touched.

    A loop that fails any of these keeps its two distinct registers and
    may still print an extra alias line / a mismatched body register -
    a readability regression, never a correctness one (nothing about
    the loop's actual control flow or values changes; only which
    register name backs a given read is ever rewritten).
    """

    def run(self) -> None:
        self.visit(self.graph.root)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        self._try_unify(node)
        self.visit(node.body)

    # ------------------------------------------------------------------
    # Candidate recognition
    # ------------------------------------------------------------------

    def _try_unify(self, loop: LoopRegion) -> None:

        header = loop.header_block

        if header is None or loop.update is None or loop.initializer is None:
            # loop.update / loop.initializer are only ever populated
            # for LoopKind.FOR by
            # LoopConditionRegionPass._extract_for_components - this
            # pass only ever targets that shape, and needs BOTH (see
            # point 2/3 in the class docstring for why the initializer
            # in particular is required now).
            return

        induction_reg = self._induction_register(loop)

        if induction_reg is None:
            return

        body_reg = self._body_register(loop, induction_reg)

        if body_reg is None:
            return

        alias_instr = self._find_alias_instruction(header, body_reg, loop.initializer)

        if alias_instr is None:
            return

        covered = loop.body.covered_blocks

        # Position of the alias Mov within the header. Only writes to
        # body_reg from this point forward can invalidate treating
        # alias_instr as body_reg's source of truth for the rest of
        # the iteration - an earlier write in the same header (e.g. a
        # throwaway temporary that reused this register number before
        # it was ever repurposed as the induction alias) is already
        # dead by the time alias_instr executes and is irrelevant.
        alias_index = next(
            i for i, instr in enumerate(header.instructions)
            if instr is alias_instr
        )

        if not self._body_reg_only_defined_here(
                covered, header, alias_index, alias_instr, body_reg
        ):
            return

        # ---- convert: drop the alias Mov, repoint every read ----

        header.instructions.remove(alias_instr)

        old_ref = Identifier(name=f"r{body_reg}")
        new_ref = Identifier(name=f"r{induction_reg}")

        # Mirror the same before/after split when repointing: reads of
        # body_reg in the header that occur BEFORE alias_instr refer
        # to whatever that earlier, unrelated definition held (e.g. a
        # temporary object reference), never to the induction value -
        # rewriting them would silently corrupt that earlier value's
        # use, not just rename it.
        self._repoint_blocks(covered, old_ref, new_ref, header=header, from_index=alias_index)
        self._repoint_region(loop.body, old_ref, new_ref)

        if loop.update is not None:
            new_right, changed = self._repoint_node(loop.update.right, old_ref, new_ref)
            if changed:
                loop.update = dataclasses.replace(loop.update, right=new_right)

        logger.debug(
            "LoopInductionAliasPass: loop header %d - merged alias r%d into "
            "induction register r%d",
            header.id, body_reg, induction_reg,
        )

    @staticmethod
    def _induction_register(loop: LoopRegion) -> int | None:
        """Read the induction register's identity straight out of loop.update.left.

        `loop.update.left` is `Identifier(f"r{dest_reg}")`, set
        verbatim by `LoopConditionRegionPass._extract_update` - reused
        directly here rather than re-derived, since a second,
        separately-maintained copy of that heuristic could silently
        drift from the one LoopConditionRegionPass actually used to
        pick loop.update in the first place.
        """

        left = loop.update.left

        if not isinstance(left, Identifier) or not left.name.startswith("r"):
            return None

        suffix = left.name[1:]

        if not suffix.isdigit():
            return None

        return int(suffix)

    @staticmethod
    def _body_register(loop: LoopRegion, induction_reg: int) -> int | None:
        """Recover the per-iteration alias register from loop.update.right.

        For `r1 = r8 + 1`, that's `r8` - read directly off
        loop.update.right rather than assuming the header's first
        instruction is the alias Mov (see class docstring point 2 for
        why position can't be trusted at three levels of nesting).

        loop.update.right is either a bare Identifier (a Mov-style
        update) or, far more commonly, a BinaryExpression whose two
        operands are the alias register and a step literal (an
        Inc/Dec-style update, e.g. `r8 + 1`) - both shapes are
        handled. Returns None if neither shape yields a register
        operand distinct from induction_reg (a non-canonical update
        this pass shouldn't guess about).
        """

        right = loop.update.right

        if isinstance(right, Identifier):
            operands = [right]
        elif isinstance(right, BinaryExpression):
            operands = [right.left, right.right]
        else:
            return None

        for operand in operands:
            if not isinstance(operand, Identifier) or not operand.name.startswith("r"):
                continue

            suffix = operand.name[1:]

            if not suffix.isdigit():
                continue

            reg = int(suffix)

            if reg != induction_reg:
                return reg

        return None

    def _find_alias_instruction(self, header: BasicBlock, body_reg: int, initializer):
        """Search the whole header block for the induction alias Mov.

        Not just the first instruction (see class docstring point 2):
        looks for an unconditional instruction writing body_reg whose
        resolved value matches loop.initializer.right
        (`_is_induction_alias_copy`).

        Scans in order and returns the first match. If body_reg is
        written more than once in the header, further occurrences are
        body_reg's problem to have (`_body_reg_only_defined_here`,
        called afterward by `_try_unify`, rejects that case entirely)
        - this method only needs to identify a candidate, not validate
        uniqueness itself.
        """

        for instr in header.instructions:

            if instr.terminator is not None:
                continue

            if instr.dest_reg != body_reg:
                continue

            if self._is_induction_alias_copy(instr.value, initializer):
                return instr

        return None

    @staticmethod
    def _is_induction_alias_copy(mov_value, initializer) -> bool:
        """Recognize the header's alias Mov by its resolved value, not its name.

        The identifier-name check doesn't work: IR generation
        (OpcodeHandler.get_register_expression) resolves every
        register read against whatever that register's textually most
        recent defining expression is, walking the raw bytecode in
        address order exactly once, with no notion of the CFG's
        back-edges. For the header's alias Mov, the textually
        preceding write to the induction register is always the
        loop's own initializer, so the Mov's resolved value comes out
        as a copy of whatever the initializer itself resolved to (e.g.,
        the bare literal `0`), never as a live register reference.
        section_15051_raw.js's own disassembly confirms this for the
        motivating example::

            <Mov>: <Reg8: 6, Reg8: 5>
            USED -> r6 = 0;

        The Mov's "USED" value is the literal `0`, not `r5`. So the
        reliable signature is: does this instruction's resolved value
        match loop.initializer.right (already recovered by
        LoopConditionRegionPass), not "is it named r{induction_reg}".

        Uses structurally_equal (not `is`/`==`) since nothing here
        guarantees the two sides are the literal same object -
        get_register_expression clones on any read past the first,
        and either side could independently have been through that.
        """

        if mov_value is None or initializer.right is None:
            return False

        if isinstance(mov_value, Node) and isinstance(initializer.right, Node):
            return mov_value.structurally_equal(initializer.right)

        return mov_value == initializer.right

    @staticmethod
    def _body_reg_only_defined_here(
            covered, header, alias_index: int, alias_instr, body_reg: int
    ) -> bool:
        """Return True if alias_instr is body_reg's only definition from
        that point in the iteration onward.

        body_reg must be a pure, single-definition alias for the
        induction register for the rest of the loop iteration (see
        class docstring point 3) - any instruction writing body_reg
        AFTER the alias Mov means the alias isn't the register's only
        source of truth from there on, and folding it away would
        misrepresent that later write's meaning.

        A write to body_reg BEFORE the alias Mov, in the header
        itself, is a different story: it's already dead by the time
        alias_instr executes (nothing between it and alias_instr reads
        it - if something did, alias_instr wouldn't be a definitionally
        clean copy in the first place, but that's a separate liveness
        concern this pass doesn't need to re-derive; register
        allocators reusing a just-freed slot for the next temporary,
        e.g., a throwaway property lookup right before the induction
        alias copy, is routine). Rejecting the whole loop over that
        reuse - as an earlier version of this check did - meant the
        alias Mov's value was left to fall back to whatever
        OpcodeHandler.get_register_expression resolved it to
        (see `_is_induction_alias_copy`'s docstring): the initializer's
        literal, baked in as if it never changed - silently wrong for
        every iteration past the first, not just a missed cosmetic
        rename.
        """

        for block in covered:

            if block is header:
                instructions = header.instructions[alias_index + 1:]
            else:
                instructions = block.instructions

            for instr in instructions:

                if instr is alias_instr:
                    continue

                if instr.dest_reg == body_reg:
                    return False

        return True

    # ------------------------------------------------------------------
    # Repointing - BasicBlock level
    # ------------------------------------------------------------------

    def _repoint_blocks(
            self, covered, old_ref: Identifier, new_ref: Identifier,
            header=None, from_index: int = 0,
    ) -> None:
        """Rewrite every remaining instruction's .value/.statement in covered blocks.

        `header`/`from_index` restrict which of the header's own
        instructions get repointed: anything before the alias Mov's
        former position reads body_reg's EARLIER, unrelated definition
        (see `_body_reg_only_defined_here`), not the induction value -
        repointing those too would rename an unrelated read out from
        under its real meaning. Every other covered block runs after
        the header completes for that iteration, so no such split is
        needed there.

        Also - defensively - repoints any block that (unusually) still
        carries a raw TerminatorConditionalBranch at this point in the
        pipeline. Normally none should, since IfStructurer/
        SwitchStructurer already ran, but per
        StructuralAnalyzer._audit_unstructured_blocks a shape can
        legitimately be left unstructured - if so, its condition still
        needs the same repoint or it would keep referencing the
        now-deleted alias register.
        """

        for block in covered:

            instructions = (
                block.instructions[from_index:]
                if block is header
                else block.instructions
            )

            for instr in instructions:

                new_value, changed = self._repoint_node(instr.value, old_ref, new_ref)
                if changed:
                    instr.value = new_value

                if instr.statement is not None:
                    new_stmt, changed = self._repoint_node(instr.statement, old_ref, new_ref)
                    if changed:
                        instr.statement = new_stmt

            terminator = block.terminator

            if isinstance(terminator, TerminatorConditionalBranch):
                new_condition, changed = self._repoint_node(terminator.condition, old_ref, new_ref)

                if changed:
                    new_terminator = dataclasses.replace(terminator, condition=new_condition)
                    block.terminator = new_terminator

                    for instr in block.instructions:
                        if instr.terminator is terminator:
                            instr.terminator = new_terminator
                            break

    # ------------------------------------------------------------------
    # Repointing - region level (IfRegion.condition / Switch case tests)
    # ------------------------------------------------------------------

    def _repoint_region(self, region, old_ref: Identifier, new_ref: Identifier) -> None:
        """Repoint condition-bearing attributes that live on region objects.

        By the time this pass runs, IfStructurer/SwitchStructurer have
        already promoted the loop body's inner `if (r6 === 3)` tests
        out of raw block terminators and into exactly these slots (see
        class docstring "Pipeline placement"). `_repoint_blocks` above
        does not see these; walking the region tree is the only way to
        reach them.

        Field access on IfRegion/SwitchRegion uses getattr with a
        default rather than a hard attribute reference: this pass was
        written against the shapes visible in the supplied sources
        (IfRegion.condition, SwitchRegion.cases/.tests/.body) without
        the exact regions module available to confirm field names
        against. If a name here doesn't match the real model, this
        degrades to a silent no-op for that one region rather than
        raising - consistent with this pass's "leave it as-is rather
        than guess wrong" posture, but worth double-checking against
        hermes_decompiler/analysis/models/regions.py directly rather
        than trusting this guess long-term.
        """

        if isinstance(region, IfRegion):

            condition = getattr(region, "condition", None)

            if condition is not None:
                new_condition, changed = self._repoint_node(condition, old_ref, new_ref)
                if changed:
                    region.condition = new_condition

            for attr in ("then_body", "else_body"):
                child = getattr(region, attr, None)
                if child is not None:
                    self._repoint_region(child, old_ref, new_ref)

            return

        if isinstance(region, SwitchRegion):

            for case in getattr(region, "cases", ()):

                tests = getattr(case, "tests", None)

                if tests:
                    new_tests = []
                    any_changed = False

                    for test in tests:
                        new_test, changed = self._repoint_node(test, old_ref, new_ref)
                        new_tests.append(new_test)
                        any_changed = any_changed or changed

                    if any_changed:
                        try:
                            case.tests = type(tests)(new_tests)
                        except TypeError:
                            case.tests = new_tests

                body = getattr(case, "body", None)
                if body is not None:
                    self._repoint_region(body, old_ref, new_ref)

            default_body = getattr(region, "default_body", None)
            if default_body is not None:
                self._repoint_region(default_body, old_ref, new_ref)

            return

        # SequenceRegion / LoopRegion (nested) / TryRegion / BasicBlock:
        # no condition-bearing attribute of their own to repoint here -
        # just recurse into whatever sub-regions they hold. A nested
        # LoopRegion's own `.condition` / `.update` / `.initializer`
        # are deliberately NOT touched: this pass never expects the
        # OUTER loop's alias register to leak into an inner loop's own
        # already-independently-computed loop metadata, and touching
        # it on a guess is exactly the kind of over-reach the rest of
        # this pass avoids.
        for attr in ("children", "body", "try_body"):
            child = getattr(region, attr, None)

            if child is None:
                continue

            if attr == "children":
                for item in child:
                    if not isinstance(item, BasicBlock):
                        self._repoint_region(item, old_ref, new_ref)
                continue

            self._repoint_region(child, old_ref, new_ref)

        catch = getattr(region, "catch", None)
        if catch is not None:
            self._repoint_region(catch.body, old_ref, new_ref)

        finally_ = getattr(region, "finally_", None)
        if finally_ is not None:
            self._repoint_region(finally_.body, old_ref, new_ref)

    # ------------------------------------------------------------------
    # Generic identity-based deep replace
    # ------------------------------------------------------------------

    def _repoint_node(self, node, old_ref: Identifier, new_ref: Identifier):
        """Same generic dataclass-tree walker as
        BooleanChainRegionPass._repoint_node /
        ConditionalExpressionRegionPass._repoint_node, duplicated here
        rather than factored out (matching those files' own precedent
        of not guessing at a shared-extraction target), with one
        deliberate difference: no structural-equality fallback.

        Those two passes add a structural-equality branch to catch a
        specific Mov-copy whose object identity changed mid-fold. Here
        there is no such salvaged object to chase by identity in the
        first place - old_ref/new_ref are freshly built Identifiers
        keyed purely on register name, so matching is done directly by
        name (`node.name == old_ref.name`) instead. Adding the other
        passes' structural-equality fallback here would be actively
        wrong: `Identifier(name="r6")` is trivially structurally equal
        to every other unrelated read of r6 anywhere in the entire
        function, and this walk is only ever called with sub-trees
        already scoped to this one loop (loop.body / loop.update), not
        the whole CFG - so a name match within that scope is exactly
        what's wanted, nothing more needs to be excluded.
        """

        if isinstance(node, Identifier) and node.name == old_ref.name:
            return new_ref, True

        if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
            return node, False

        updates = {}
        any_changed = False

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            if isinstance(value, Node):
                new_value, changed = self._repoint_node(value, old_ref, new_ref)
                if changed:
                    updates[field.name] = new_value
                    any_changed = True

            elif isinstance(value, tuple):
                new_items = []
                tuple_changed = False

                for item in value:
                    if isinstance(item, Node):
                        new_item, changed = self._repoint_node(item, old_ref, new_ref)
                        if changed:
                            tuple_changed = True
                        new_items.append(new_item)
                    else:
                        new_items.append(item)

                if tuple_changed:
                    updates[field.name] = tuple(new_items)
                    any_changed = True

            # else: plain value (str/bool/enum/int/None) - nothing to do

        if not any_changed:
            return node, False

        return dataclasses.replace(node, **updates), True
