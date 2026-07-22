import re

from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
)


class LoopConditionExtractor:

    _IF_PATTERN = re.compile(r"if\s*\((.*)\)")

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

    def _extract(self, loop):

        if loop.header is None:
            return

        block = loop.header.block

        if not block.instructions:
            return

        last = block.instructions[-1]

        text = last.result

        match = self._IF_PATTERN.search(text)

        if not match:
            return

        loop.condition = match.group(1).strip()

        loop.loop_kind = "while"