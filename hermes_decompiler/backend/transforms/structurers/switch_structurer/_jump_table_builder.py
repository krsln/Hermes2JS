from __future__ import annotations

from hermes_decompiler.backend.analysis.cfg import BasicBlock
from hermes_decompiler.backend.regions import SequenceRegion, SwitchCase, SwitchRegion
from hermes_decompiler.ir.expressions import NumericLiteral
from hermes_decompiler.ir.terminators import TerminatorSwitch


class _JumpTableSwitchBuilder:
    """Builds a SwitchRegion from a raw jump-table terminator.

    Reads a BasicBlock's TerminatorSwitch (a SwitchImm / UIntSwitchImm
    jump table) directly - the dense-switch shape Hermes compiles to,
    untouched by IfStructurer (which only consumes
    TerminatorConditionalBranch).

    Sibling to `_ComparisonChainSwitchBuilder`, not a fallback for it:
    Hermes emits exactly one of the two shapes per switch, never both,
    so `SwitchStructurer` tries both builders per candidate item but
    only one can ever match.
    """

    def __init__(self, graph, cfg):
        self.graph = graph
        self.cfg = cfg

    def try_build(self, region: SequenceRegion, header: BasicBlock) -> bool:
        """Try to fold `header`'s jump table into a SwitchRegion in place.

        Case labels sharing a target address are grouped into one
        SwitchCase. A value whose target equals default_target is
        omitted from the explicit case list, since it already falls
        under `default:`.

        Each case/default body spans the contiguous run of
        region.children from that target's item up to the next
        case/default item, the header's immediate post-dominator, or
        the end of the region. Returns False on any layout that can't
        be resolved cleanly; the raw TerminatorSwitch block remains a
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

        # `is not None`, not truthiness: a default target at address 0
        # is a legitimate address, not "no default".
        if switch_term.default_target is not None:

            default_block = address_to_block.get(switch_term.default_target)

            if default_block is not None:
                default_item = self.graph.find_covering_item(region, default_block)

        all_items = [item for _, item in resolved]

        if default_item is not None:
            all_items.append(default_item)

        if not all_items:
            return False

        if len(set(id(i) for i in all_items)) != len(all_items):
            # Distinct case groups resolved to the same top-level item -
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
