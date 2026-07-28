import re

from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion, LoopKind,
)
from hermes_decompiler.analysis.terminators import TerminatorConditionalBranch

_IF_PATTERN = re.compile(r"if\s*\((.*)\)")


class LoopConditionExtractor:

    def __init__(self, root):
        self.root = root

    def run(self):
        self._visit(self.root)

    def _visit(self, region):

        if isinstance(region, SequenceRegion):
            for child in region.children:
                self._visit(child)
            return

        if isinstance(region, LoopRegion):
            self._extract(region)
            self._visit(region.body)

    def _extract(self, loop: LoopRegion):

        header = loop.header_block
        if header is None:
            return

        last = header.last_instruction

        text = last.result

        match = _IF_PATTERN.search(text)

        if not match:
            return

        # branch = header.terminator
        #
        # if not isinstance(branch, TerminatorConditionalBranch):
        #     return

        # header.terminator = None
        # loop.condition = branch.condition

        loop.condition = match.group(1).strip()
        loop.loop_kind = LoopKind.WHILE
