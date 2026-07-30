from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    TryRegion,
    SwitchRegion,
    SwitchCase,
)
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression
from hermes_decompiler.ir.expressions.Literals import Literal
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

_EQUALITY_OPERATORS = (BinaryOperator.EQUAL, BinaryOperator.STRICT_EQUAL)

# Below this many cases, folding into a `switch` adds no value over the
# `if`/`else if` chain IfStructurer already built - not wrong, just not
# worth the structural churn for a 1-2-way branch.
_MIN_CASES = 2


class SwitchStructurer(RegionStructurer):
    """
    Folds a chain of `IfRegion`s that all compare the SAME discriminant
    expression against different constant literals - exactly what
    `if (x === 0) {...} else { if (x === 1) {...} else { ... } }`
    looks like once IfStructurer is done with a compiled `switch` - back
    into a single `SwitchRegion`.

    Hermes lowers `switch` this way (a chain of equality tests) rather
    than emitting a distinct switch/jump-table opcode for the cases
    seen so far, so this is a *region_passes*-style fold operating on
    already-built `IfRegion`s, not a fresh CFG-level structurer - it's
    kept under `structurers/` (extending `RegionStructurer`) rather
    than `region_passes/` because it does introduce a new region kind
    (`SwitchRegion`), matching this package's "builds a new region
    kind" contract.

    Known limitation: if two case tests jump to a *shared* body physically
    placed elsewhere (`case 3: case 4: sharedBody`), IfStructurer's
    dominance-based conversion can only resolve the shared body into
    the FIRST case that reaches it - the later case is left as a raw,
    unconverted conditional block (see IfStructurer's docstring on tail
    duplication). This pass doesn't try to recover that case: the chain
    simply stops there, and everything from that point on is treated as
    the `default:` body verbatim (including the leftover raw
    `if (...) goto label_N;`), which still renders correctly via
    Printer's raw-terminator fallback - just not as a clean case label.
    """

    def run(self) -> None:
        self._visit(self.graph.root)

    # -------------------------------------------------------------

    def _visit(self, region) -> None:

        if isinstance(region, SequenceRegion):
            self._fold_sequence(region)

            for child in region.children:
                self._visit(child)

            return

        if isinstance(region, LoopRegion):
            self._visit(region.body)
            return

        if isinstance(region, IfRegion):
            self._visit(region.then_body)
            if region.else_body:
                self._visit(region.else_body)
            return

        if isinstance(region, TryRegion):
            self._visit(region.try_body)
            if region.catch:
                self._visit(region.catch.body)
            if region.finally_:
                self._visit(region.finally_.body)
            return

        if isinstance(region, SwitchRegion):
            for case in region.cases:
                self._visit(case.body)
            if region.default_body:
                self._visit(region.default_body)
            return

        if hasattr(region, "body"):
            self._visit(region.body)

    # -------------------------------------------------------------

    def _fold_sequence(self, region: SequenceRegion) -> None:

        for index, item in enumerate(region.children):

            if not isinstance(item, IfRegion):
                continue

            chain = self._match_chain(item)

            if chain is None:
                continue

            discriminant, cases, default_body = chain

            if len(cases) < _MIN_CASES:
                continue

            switch_region = SwitchRegion(discriminant)

            for tests, body in cases:
                switch_region.add_case(SwitchCase(tests, body))

            if default_body is not None:
                switch_region.default_body = default_body

            self.graph.replace(item, switch_region)

            return  # region.children was just mutated - re-scan on next pass

    # -------------------------------------------------------------

    def _match_chain(self, root: IfRegion):
        """
        Walks `root`'s `else if` chain as far as it validly extends.

        Returns `(discriminant, cases, default_body)` where `cases` is
        `[(tests, body), ...]` in source order, or `None` if `root`
        itself isn't even a single `discriminant == constant` test (no
        chain at all, not even a 1-case one).
        """

        discriminant = None
        cases: list[tuple[list[Expression], SequenceRegion]] = []
        current = root

        # The SequenceRegion directly containing `current`, once we're
        # past `root` (which the caller found as a bare top-level item,
        # not wrapped in one). Needed so that if `current` itself turns
        # out not to parse as a case, we can fall back to returning
        # this container as the default body - NOT just discard
        # `current` (and everything under it - e.g. a merged
        # `case 3: case 4:` test BranchChainMerger folded into a single
        # `||` condition, which this pass can't split back into two
        # labels but must still preserve as default content).
        container: SequenceRegion | None = None

        while True:

            parsed = self._parse_case_test(current.condition, discriminant)

            if parsed is None:

                if container is not None:
                    return discriminant, cases, container

                # `root` itself didn't parse - no chain at all.
                return None

            disc_expr, test_value = parsed
            discriminant = disc_expr

            cases.append(([test_value], current.then_body))

            else_body = current.else_body

            if else_body is None:
                return discriminant, cases, None

            if (
                    len(else_body.children) == 1
                    and isinstance(else_body.children[0], IfRegion)
            ):
                current = else_body.children[0]
                container = else_body
                continue

            if (
                    len(else_body.children) == 2
                    and self._is_transparent(else_body.children[0])
                    and isinstance(else_body.children[1], IfRegion)
            ):
                # IfStructurer leaves the "spent" constant-setup block
                # (e.g. `LoadConstUInt8 r0, 1` feeding a comparison
                # that's since been folded entirely into the next
                # level's condition expression) sitting right before
                # the nested IfRegion instead of removing it. It
                # produces no visible output (see _is_transparent) and
                # doesn't break the chain.
                current = else_body.children[1]
                container = else_body
                continue

            # else_body doesn't extend the chain (not exactly one more
            # equality-test IfRegion) - whatever it is becomes default.
            return discriminant, cases, else_body

    # -------------------------------------------------------------

    @staticmethod
    def _parse_case_test(condition, expected_discriminant):
        """
        If `condition` is `<discriminant> == <constant>` (either
        operand order, `==` or `===`), and `<discriminant>` matches
        `expected_discriminant` (or `expected_discriminant` is still
        unset - the first case in the chain), returns
        `(discriminant_expr, constant_expr)`. Otherwise `None`.
        """

        if not isinstance(condition, BinaryExpression):
            return None

        if condition.operator not in _EQUALITY_OPERATORS:
            return None

        left, right = condition.left, condition.right
        left_is_const = isinstance(left, Literal)
        right_is_const = isinstance(right, Literal)

        if right_is_const and not left_is_const:
            disc_expr, test_value = left, right
        elif left_is_const and not right_is_const:
            disc_expr, test_value = right, left
        else:
            # Both constant or both non-constant - not a recognizable
            # `switch`-shaped comparison either way.
            return None

        if expected_discriminant is not None and not disc_expr.structurally_equal(expected_discriminant):
            return None

        return disc_expr, test_value

    # -------------------------------------------------------------

    @staticmethod
    def _is_transparent(item) -> bool:
        """
        True if `item` is a `BasicBlock` that produces no visible
        output when printed (see `Printer._emit_block`): every
        instruction's value has already been consumed elsewhere
        (`.used == True`) with no `.statement`/`.terminator` of its
        own.

        IfStructurer leaves exactly this kind of "spent" setup block
        (e.g. a `LoadConstUInt8 r0, 1` that only ever fed a comparison
        whose result is now folded entirely into the *next* level's
        condition expression) sitting immediately before the following
        nested IfRegion in `else_body.children`, instead of removing
        it. It must not be mistaken for real content that breaks the
        `else if` chain.
        """

        if not isinstance(item, BasicBlock):
            return False

        for instr in item.instructions:

            if instr.statement is not None:
                return False

            if instr.terminator is not None:
                return False

            if instr.value is not None and not instr.used:
                return False

        return True