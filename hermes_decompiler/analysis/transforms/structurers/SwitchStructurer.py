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

# Below this many cases, folding into a `switch` adds no value over the
# `if`/`else if` chain IfStructurer already built - not wrong, just not
# worth the structural churn for a 1-2-way branch.
_MIN_CASES = 2


class SwitchStructurer(RegionStructurer):
    """
    Builds `SwitchRegion`s from whichever form Hermes compiled a
    `switch` statement into - there are two, and it's always exactly
    one or the other for a given switch, never both:

    1. **Comparison chain** (small/sparse switches): a chain of
       `IfRegion`s IfStructurer already built, all comparing the same
       discriminant against different constant literals - see
       `_match_chain`.

    2. **Jump table** (`SwitchImm`/`UIntSwitchImm`, dense switches): a
       single raw `BasicBlock` whose terminator is `TerminatorSwitch`,
       untouched by IfStructurer (which only ever consumes
       `TerminatorConditionalBranch`) - see `_fold_raw_switch`.

    Known limitation (comparison-chain path only): if two case tests
    jump to a *shared* body physically placed elsewhere (`case 3:
    case 4: sharedBody`), IfStructurer's dominance-based conversion can
    only resolve the shared body into the FIRST case that reaches it -
    the later case is left as a raw, unconverted conditional block (see
    IfStructurer's docstring on tail duplication). This pass doesn't
    try to recover that case: the chain simply stops there, and
    everything from that point on is treated as the `default:` body
    verbatim (including the leftover raw `if (...) goto label_N;`),
    which still renders correctly via Printer's raw-terminator
    fallback - just not as a clean case label.
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

            if isinstance(item, BasicBlock) and isinstance(item.terminator, TerminatorSwitch):

                if self._fold_raw_switch(region, item):
                    return  # region.children mutated - re-scan on next pass

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

            return  # region.children was just mutated - re-scan on next pass

    # -------------------------------------------------------------
    # Raw TerminatorSwitch (jump-table) folding.
    # -------------------------------------------------------------

    def _fold_raw_switch(self, region: SequenceRegion, header: BasicBlock) -> bool:
        """
        Builds a `SwitchRegion` directly from `header`'s `TerminatorSwitch`
        (a real `SwitchImm`/`UIntSwitchImm` jump table), as opposed to
        `_match_chain`'s job of folding an `if`/`else if` *comparison
        chain* - Hermes emits one or the other depending on case
        density, never both for the same switch.

        Case labels that share a target address (`case 2: case 15:
        body`) are grouped into one `SwitchCase`. A case value whose
        target equals `default_target` is dropped from the explicit
        case list - it already falls under `default:`, so listing it
        again would just be a redundant label on the same body.

        Each case/default body's extent is the contiguous run of
        `region.children` from that target's item up to whichever
        comes first: the next case/default's item (bodies are laid out
        back-to-back by address, the standard compiled-switch layout),
        `header`'s immediate post-dominator (if the switch has a real
        merge point after it), or the end of `region`. Bails (`False`)
        on anything that doesn't resolve this cleanly - the raw
        `TerminatorSwitch` block is a completely valid (if unstructured)
        fallback (see Printer's placeholder comment for it).
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
                # Already covered by `default:` - no separate label.
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
            # Two distinct case groups resolved to the exact same
            # top-level item in a way we can't split further - bail
            # rather than guess which one actually owns it.
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
                # Overlapping/out-of-order items - can't slice safely.
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
