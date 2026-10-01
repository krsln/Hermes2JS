from __future__ import annotations

import dataclasses

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import (
    IfRegion,
    LoopKind,
    LoopRegion,
    RegionVisitor,
    SwitchRegion,
)
from hermes_decompiler.ir import Node
from hermes_decompiler.ir.expressions import AssignmentExpression, Identifier
from ._base import RegionPass


class InductionVariableNamingPass(RegionPass, RegionVisitor):
    """Renames a `for` loop's own induction register to a short,
    conventional name (`i`, `j`, `k`, ...) instead of leaving Hermes'
    raw `rN` visible.

    Scoped to exactly the ONE case this can name with confidence: the
    register `LoopConditionRegionPass._extract_update` already
    recorded as `loop.update`'s own left-hand side (`loop.update.left`)
    for a loop it classified `FOR`. That's a real, singular claim about
    the register's role for the ENTIRE loop, made by a pass that
    already had to prove the register behaves like a counter to get
    there - not a guess this pass makes on its own.

    Renaming ANY other register in the function is deliberately left
    alone. Most of the plain `rN = ...` noise elsewhere is Hermes'
    allocator routing a value through a register for a line or two on
    its way somewhere else (`r2 = console; r2 = r2.log; ...`) - not a
    "variable" a person would ever have named, and picking out which
    of those are worth a name and which aren't is a fuzzier, harder
    problem than this pass takes on.

    Rename scope: `loop.condition`/`loop.update`/`loop.initializer`
    (wherever the register appears in the loop's own extracted
    metadata) plus every reference inside `loop.body` itself -
    matching how far the induction register's OWN lifetime is actually
    known to extend. A `for`-loop's induction register can, in
    principle, still be read after the loop ends too (`for (...) {...}
    console.log(i)`), but confirming that final value safely would
    need tracking the register past the loop's own exit, including
    whichever branch(es) actually exit it (`break`, a natural
    completion, ...) - not attempted here; a register genuinely read
    after the loop stays as `rN` there.

    Nested loops each get their own name (`i`, `j`, `k`, ... in
    nesting order) - `self._depth` only increments across a
    SUCCESSFULLY renamed loop, so an inner loop whose OWN induction
    register couldn't be identified doesn't throw off an even-more-
    deeply-nested loop's naming.

    Expression nodes (`Identifier` included) are FROZEN dataclasses -
    `_rename_expr` REBUILDS a new tree bottom-up (`dataclasses.replace`)
    rather than mutating in place, and every call site reassigns the
    result back into whichever mutable field held the old tree
    (`instruction.value`, `loop.condition`, `case.test`, ...).

    Must run LAST, after every other pass that inspects a register
    NUMBER (`_condition_boundary_registers_safe`,
    `_LoopConditionRegisterCollector`, `IfTailMergeRegionPass`'s
    instruction comparison, ...) - a register this pass has renamed no
    longer matches `name.startswith("r") and name[1:].isdigit()`
    anywhere it was renamed, so any LATER pass keying off that pattern,
    or off the raw register number, would silently stop recognizing
    it.
    """

    _NAMES = ("i", "j", "k", "l", "m", "n")

    def run(self) -> None:
        self._depth = 0
        self.visit(self.graph.root)

    # ------------------------------------------------------------------

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        renamed = self._maybe_rename(node)

        if renamed:
            self._depth += 1

        self.visit(node.body)

        if renamed:
            self._depth -= 1

    def _maybe_rename(self, node: LoopRegion) -> bool:
        if node.loop_kind != LoopKind.FOR:
            return False

        update = node.update

        if not isinstance(update, AssignmentExpression) or not isinstance(update.left, Identifier):
            return False

        old_name = update.left.name

        if not (old_name.startswith("r") and old_name[1:].isdigit()):
            return False

        if self._depth >= len(self._NAMES):
            return False

        new_name = self._NAMES[self._depth]

        if node.condition is not None:
            node.condition = self._rename_expr(node.condition, old_name, new_name)

        node.update = self._rename_expr(node.update, old_name, new_name)

        if node.initializer is not None:
            node.initializer = self._rename_expr(node.initializer, old_name, new_name)

        _RegisterRenamer(old_name, new_name).visit(node.body)

        return True

    # ------------------------------------------------------------------

    @staticmethod
    def _rename_expr(node, old_name: str, new_name: str):
        """Returns a tree with every `Identifier(name=old_name)` under
        `node` replaced by a fresh `Identifier(name=new_name)`. `node`
        itself, and every `Expression` node in the codebase, is a
        FROZEN dataclass, so this rebuilds bottom-up via
        `dataclasses.replace` rather than mutating - a node with
        nothing to change under it is returned completely UNCHANGED
        (same object, not a copy), so a caller can cheaply tell via
        `is` whether anything actually needs reassigning.
        """
        if isinstance(node, Identifier):
            if node.name == old_name:
                return Identifier(name=new_name)
            return node

        if not dataclasses.is_dataclass(node) or not isinstance(node, Node):
            return node

        changes = {}

        for field in dataclasses.fields(node):
            value = getattr(node, field.name)

            if isinstance(value, Node):
                new_value = InductionVariableNamingPass._rename_expr(value, old_name, new_name)

                if new_value is not value:
                    changes[field.name] = new_value

            elif isinstance(value, tuple):
                new_items = tuple(
                    InductionVariableNamingPass._rename_expr(item, old_name, new_name)
                    if isinstance(item, Node)
                    else item
                    for item in value
                )

                if new_items != value:
                    changes[field.name] = new_items

        if not changes:
            return node

        return dataclasses.replace(node, **changes)


class _RegisterRenamer(RegionVisitor):
    """Applies one register's rename across a region subtree, every
    `Identifier` reference (via `InductionVariableNamingPass._rename_expr`,
    reassigned back into whichever field held it).

    Only RENAMES REFERENCES to the register (`Identifier(name=old_name)`
    wherever one is READ - a value, a condition, a statement argument);
    deliberately never touches a `dest_reg`-based WRITE elsewhere in the
    body, even one that reuses the exact same register number.
    Confirmed regression (`labeledBreakTest`/`labeledContinueTest`): a
    plain `console.log(...)` call with a DISCARDED result - the
    Printer suppresses the `rN = ` prefix for exactly that reason, so
    it normally prints as a bare statement - happened to land its
    (unused) result in the very same register number the loop's own
    induction variable used earlier in the SAME body, well after `i`'s
    own last meaningful use. Converting that write into an explicit
    assignment turned `console.log(...)` into `i = console.log(...)`:
    syntactically fine, semantically a fabricated, wrong claim that
    the call's result becomes the loop counter. Telling that shape
    apart from a genuine re-write of the SAME logical counter mid-body
    would need real liveness/reaching-definition analysis this pass
    doesn't do; leaving every `dest_reg` write exactly as `rN = ...`
    is the safe default until that's built.
    """

    def __init__(self, old_name: str, new_name: str) -> None:
        self.old_name = old_name
        self.new_name = new_name

    def generic_visit(self, node) -> None:
        if not isinstance(node, BasicBlock):
            return

        for instruction in node.instructions:
            if instruction.value is not None:
                instruction.value = InductionVariableNamingPass._rename_expr(
                    instruction.value, self.old_name, self.new_name,
                )

            if instruction.statement is not None:
                instruction.statement = InductionVariableNamingPass._rename_expr(
                    instruction.statement, self.old_name, self.new_name,
                )

    def visit_IfRegion(self, node: IfRegion) -> None:
        node.condition = InductionVariableNamingPass._rename_expr(node.condition, self.old_name, self.new_name)
        super().visit_IfRegion(node)

    def visit_SwitchRegion(self, node: SwitchRegion) -> None:
        for case in node.cases:
            case.tests = [
                InductionVariableNamingPass._rename_expr(test, self.old_name, self.new_name)
                for test in case.tests
            ]
        super().visit_SwitchRegion(node)

    def visit_LoopRegion(self, node: LoopRegion) -> None:
        if node.condition is not None:
            node.condition = InductionVariableNamingPass._rename_expr(node.condition, self.old_name, self.new_name)

        if node.update is not None:
            node.update = InductionVariableNamingPass._rename_expr(node.update, self.old_name, self.new_name)

        if node.initializer is not None:
            node.initializer = InductionVariableNamingPass._rename_expr(
                node.initializer, self.old_name, self.new_name,
            )

        super().visit_LoopRegion(node)
