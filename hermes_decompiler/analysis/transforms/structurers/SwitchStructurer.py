from __future__ import annotations

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.terminators import TerminatorSwitch
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    TryRegion,
    SwitchRegion,
    SwitchCase,
)
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression, Expression, NumericLiteral
from hermes_decompiler.ir.expressions.Literals import Literal
from hermes_decompiler.analysis.transforms.structurers._base import RegionStructurer

_EQUALITY_OPERATORS = (BinaryOperator.EQUAL, BinaryOperator.STRICT_EQUAL)
_INEQUALITY_OPERATORS = (BinaryOperator.NOT_EQUAL, BinaryOperator.STRICT_NOT_EQUAL)

# Below this many cases, folding into a `switch` adds no value over the
# `if`/`else if` chain IfStructurer already built — not wrong, just not
# worth the structural churn for a 1–2-way branch.
_MIN_CASES = 2


class SwitchStructurer(RegionStructurer):
    """
    Builds `SwitchRegion`s from whichever form Hermes compiled a
    `switch` statement into. For any given switch Hermes emits exactly
    one of the two shapes, never both:

    1. **Comparison chain** (small / sparse switches)
       A chain of `IfRegion`s already produced by IfStructurer, each
       testing the same discriminant against a different constant
       literal. Recovered by `_match_chain`.

    2. **Jump table** (`SwitchImm` / `UIntSwitchImm`, dense switches)
       A single raw `BasicBlock` whose terminator is `TerminatorSwitch`.
       Untouched by IfStructurer (which only consumes
       `TerminatorConditionalBranch`). Recovered by `_fold_raw_switch`.

    Shared-body recovery (comparison-chain path)
    --------------------------------------------
    When two or more case labels share a single body
    (`case 3: case 4: sharedBody`), IfStructurer’s dominance-based
    conversion typically attaches the body to the first label only.
    Later labels remain as residual conditionals that later folding
    often turns into inverted tests inside what looks like the
    `default` arm, e.g.:

        case 3:
            sharedBody
        default:
            if (4 !== disc) { realDefault }

    This pass recovers those residual tests:

    * Consecutive equality tests that resolve to the same body are
      merged into a single multi-value `SwitchCase`.
    * An inverted residual of the form `if (C !== disc) { realDefault }`
      (or the symmetric operand order) contributes `C` to the preceding
      case’s test list and promotes the residual’s then-body to the
      true `default`.

    Anything that cannot be recovered cleanly is left as the default
    body; the printer’s raw-terminator fallback still renders a correct
    (if less tidy) result.
    """

    def run(self) -> None:
        self._visit(self.graph.root)

    # -------------------------------------------------------------
    # Region walk
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
    # Sequence folding entry point
    # -------------------------------------------------------------

    def _fold_sequence(self, region: SequenceRegion) -> None:

        for index, item in enumerate(region.children):

            if isinstance(item, BasicBlock) and isinstance(
                    item.terminator, TerminatorSwitch
            ):
                if self._fold_raw_switch(region, item):
                    # children mutated — re-scan on the next pass
                    return
                continue

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
            # children mutated — re-scan on the next pass
            return

    # -------------------------------------------------------------
    # Raw TerminatorSwitch (jump-table) folding
    # -------------------------------------------------------------

    def _fold_raw_switch(self, region: SequenceRegion, header: BasicBlock) -> bool:
        """
        Build a `SwitchRegion` directly from `header`’s
        `TerminatorSwitch` (a real `SwitchImm` / `UIntSwitchImm` jump
        table).

        Case labels that share a target address are grouped into one
        `SwitchCase`. A case value whose target equals `default_target`
        is omitted from the explicit case list — it already falls under
        `default:`.

        Each case / default body’s extent is the contiguous run of
        `region.children` from that target’s item up to the next
        case/default item, the header’s immediate post-dominator, or
        the end of the region. Returns `False` on any layout that cannot
        be resolved cleanly; the raw `TerminatorSwitch` block remains a
        valid unstructured fallback.
        """

        switch_term = header.terminator
        assert isinstance(switch_term, TerminatorSwitch)

        try:
            header_index = region.children.index(header)
        except ValueError:
            return False

        address_to_block = {b.address: b for b in self.cfg.blocks}

        groups: dict[int, list[int]] = {}

        for value, target in switch_term.case_map.items():

            if target == switch_term.default_target:
                continue

            groups.setdefault(target, []).append(value)

        resolved: list[tuple[list[int], object]] = []

        for target, values in groups.items():

            target_block = address_to_block.get(target)

            if target_block is None:
                return False

            item = self.graph.find_covering_item(region, target_block)

            if item is None or item is header:
                return False

            resolved.append((sorted(values), item))

        default_item = None

        if switch_term.default_target:

            default_block = address_to_block.get(switch_term.default_target)

            if default_block is not None:
                default_item = self.graph.find_covering_item(region, default_block)

        all_items = [item for _, item in resolved]

        if default_item is not None:
            all_items.append(default_item)

        if not all_items:
            return False

        if len(set(id(i) for i in all_items)) != len(all_items):
            # Distinct case groups resolved to the same top-level item —
            # cannot split further without guessing ownership.
            return False

        try:
            item_index = {id(i): region.children.index(i) for i in all_items}
        except ValueError:
            return False

        ordered_items = sorted(all_items, key=lambda i: item_index[id(i)])

        end_boundary = len(region.children)

        if self.cfg.post_dominator_tree is not None:

            merge_block = self.cfg.post_dominator_tree.immediate_post_dominator(header)

            if merge_block is not None:

                merge_item = self.graph.find_covering_item(region, merge_block)

                if merge_item is not None:
                    end_boundary = region.children.index(merge_item)

        boundaries = [item_index[id(i)] for i in ordered_items] + [end_boundary]

        bodies: dict[int, SequenceRegion] = {}

        for position, item in enumerate(ordered_items):
            start = boundaries[position]
            stop = boundaries[position + 1]

            if stop <= start:
                return False

            body_items = region.children[start:stop]
            body = SequenceRegion()
            self.graph.transfer(body_items, body)
            bodies[id(item)] = body

        switch_region = SwitchRegion(switch_term.selector)

        for values, item in sorted(resolved, key=lambda r: item_index[id(r[1])]):
            tests = [NumericLiteral(value=v) for v in values]
            switch_region.add_case(SwitchCase(tests, bodies[id(item)]))

        if default_item is not None:
            switch_region.default_body = bodies[id(default_item)]

        del region.children[header_index:end_boundary]
        region.children.insert(header_index, switch_region)
        switch_region.parent = region

        return True

    # -------------------------------------------------------------
    # Comparison-chain matching
    # -------------------------------------------------------------

    def _match_chain(self, root: IfRegion):
        """
        Walk `root`’s `else if` chain as far as it validly extends.

        Returns `(discriminant, cases, default_body)` where `cases` is
        `[(tests, body), …]` in source order, or `None` when `root`
        itself is not even a single `discriminant == constant` test.

        Shared-body and inverted-residual recovery are performed
        inline so that labels such as `case 3: case 4:` are restored
        instead of leaving a residual conditional inside `default`.
        """

        discriminant = None
        cases: list[tuple[list[Expression], SequenceRegion]] = []
        current = root

        # SequenceRegion that directly contains `current` once we have
        # moved past `root`. Used as a safe fallback default body when
        # a later link fails to parse as a case test.
        container: SequenceRegion | None = None

        while True:
            parsed = self._parse_case_test(current.condition, discriminant)

            if parsed is None:
                # Attempt inverted / shared recovery before giving up.
                recovered = self._try_recover_shared_or_inverted(
                    current, discriminant, cases, container
                )

                if recovered is not None:
                    return recovered

                if container is not None:
                    return discriminant, cases, container

                return None

            disc_expr, test_value = parsed
            discriminant = disc_expr

            body = current.then_body

            if cases and self._same_body(cases[-1][1], body):
                # Same physical body as the previous case — multi-value
                # label (case N: case M: sharedBody).
                cases[-1][0].append(test_value)
            else:
                cases.append(([test_value], body))

            else_body = current.else_body
            if else_body is None:
                return discriminant, cases, None

            # Continue the chain when the else arm is exactly one more
            # equality-test IfRegion (optionally preceded by a
            # transparent spent const-setup block left by IfStructurer).
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
                current = else_body.children[1]
                container = else_body
                continue

            # else_body does not extend the chain. Try to recover an
            # inverted residual that still belongs to the last case.
            recovered_default = self._try_recover_inverted_default(
                else_body, discriminant, cases
            )

            if recovered_default is not None:
                return discriminant, cases, recovered_default

            return discriminant, cases, else_body

    # -------------------------------------------------------------
    # Shared-body / inverted residual recovery
    # -------------------------------------------------------------

    def _try_recover_shared_or_inverted(
            self,
            current: IfRegion,
            discriminant,
            cases: list,
            container: SequenceRegion | None,
    ):
        """
        Called when `current.condition` is not a plain equality test.
        Handles the common residual shape produced after IfStructurer
        and compound-condition folding:

            if (C !== disc) { realDefault }          # else empty
            if (disc != C)  { realDefault }

        The constant `C` is appended to the most recent case’s test
        list and the residual’s then-body becomes the true default.
        """
        if discriminant is None or not cases:
            return None

        inv = self._parse_inverted_case_test(current.condition, discriminant)
        if inv is None:
            return None

        _, extra_value = inv

        # Prefer the shape where the then-arm is the real default and
        # the else-arm is empty / transparent.
        if self._is_empty_or_transparent_body(current.else_body):
            cases[-1][0].append(extra_value)
            return discriminant, cases, current.then_body

        # Symmetric shape: then empty, else is the real default.
        if self._is_empty_or_transparent_body(current.then_body):
            cases[-1][0].append(extra_value)
            return discriminant, cases, current.else_body

        return None

    def _try_recover_inverted_default(
            self,
            else_body: SequenceRegion,
            discriminant,
            cases: list,
    ):
        """
        Inspect a non-chain else arm for a single inverted residual:

            SequenceRegion
              └── IfRegion  condition = (C !== disc)   else = None
                    └── then = realDefault

        On success appends `C` to the last case and returns the residual
        then-body as the switch’s default.
        """
        if discriminant is None or not cases:
            return None
        if not isinstance(else_body, SequenceRegion):
            return None

        # Tolerate a leading transparent block (spent const load).
        meaningful = [
            c for c in else_body.children if not self._is_transparent(c)
        ]
        if len(meaningful) != 1 or not isinstance(meaningful[0], IfRegion):
            return None

        residual = meaningful[0]
        if residual.else_body is not None and not self._is_empty_or_transparent_body(
                residual.else_body
        ):
            return None

        inv = self._parse_inverted_case_test(residual.condition, discriminant)
        if inv is None:
            return None

        _, extra_value = inv
        cases[-1][0].append(extra_value)
        return residual.then_body

    # -------------------------------------------------------------
    # Condition parsers
    # -------------------------------------------------------------

    @staticmethod
    def _parse_case_test(condition, expected_discriminant):
        """
        Recognise `<discriminant> == <constant>` (either operand order,
        `==` or `===`). When `expected_discriminant` is already set it
        must structurally match. Returns `(discriminant_expr, constant)`
        or `None`.
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
            return None

        if (
                expected_discriminant is not None
                and not disc_expr.structurally_equal(expected_discriminant)
        ):
            return None

        return disc_expr, test_value

    @staticmethod
    def _parse_inverted_case_test(condition, expected_discriminant):
        """
        Recognise `<discriminant> != <constant>` (either operand order,
        `!=` or `!==`). Same contract as `_parse_case_test`.
        """

        if not isinstance(condition, BinaryExpression):
            return None

        if condition.operator not in _INEQUALITY_OPERATORS:
            return None

        left, right = condition.left, condition.right
        left_is_const = isinstance(left, Literal)
        right_is_const = isinstance(right, Literal)

        if right_is_const and not left_is_const:
            disc_expr, test_value = left, right
        elif left_is_const and not right_is_const:
            disc_expr, test_value = right, left
        else:
            return None

        if (
                expected_discriminant is not None
                and not disc_expr.structurally_equal(expected_discriminant)
        ):
            return None

        return disc_expr, test_value

    # -------------------------------------------------------------
    # Body / transparency helpers
    # -------------------------------------------------------------

    @staticmethod
    def _same_body(a, b) -> bool:
        """
        True when two case bodies are the same physical region (shared
        fall-through) or share the same entry block address.
        """
        if a is b:
            return True
        if a is None or b is None:
            return False

        def _entry_address(body):
            if isinstance(body, BasicBlock):
                return body.address
            if isinstance(body, SequenceRegion) and body.children:
                first = body.children[0]
                if isinstance(first, BasicBlock):
                    return first.address
                if hasattr(first, "covered_blocks") and first.covered_blocks:
                    return min(first.covered_blocks, key=lambda blk: blk.id).address
            if hasattr(body, "covered_blocks") and body.covered_blocks:
                return min(body.covered_blocks, key=lambda blk: blk.id).address
            return None

        addr_a = _entry_address(a)
        addr_b = _entry_address(b)
        return addr_a is not None and addr_a == addr_b

    @staticmethod
    def _is_empty_or_transparent_body(body) -> bool:
        if body is None:
            return True
        if isinstance(body, SequenceRegion):
            if len(body.children) == 0:
                return True
            return all(SwitchStructurer._is_transparent(c) for c in body.children)
        return SwitchStructurer._is_transparent(body)

    @staticmethod
    def _is_transparent(item) -> bool:
        """
        True when `item` is a `BasicBlock` that produces no visible
        output when printed: every instruction’s value has already been
        consumed elsewhere and the block holds no statement or
        terminator of its own.

        IfStructurer occasionally leaves exactly this kind of spent
        setup block (e.g. a `LoadConstUInt8` that only fed a comparison
        now folded into the next level’s condition) immediately before
        a nested IfRegion. It must not be treated as real content that
        breaks the `else if` chain.
        """

        if not isinstance(item, BasicBlock):
            return False

        for instr in item.instructions:

            if instr.statement is not None:
                return False

            if instr.terminator is not None:
                return False

            if instr.value is not None and not instr.definition_used:
                return False

        return True
