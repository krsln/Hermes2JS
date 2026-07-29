from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from hermes_decompiler.analysis.cfg import BasicBlock
from hermes_decompiler.analysis.regions.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    CatchRegion,
    FinallyRegion, TryRegion,
)
from hermes_decompiler.opcode import OpcodeResult


@dataclass(slots=True)
class _RegionItem:
    """
    Base for an entry in `SequenceRegion.items`.

    Private to this module - `StatementBuilder` is the sole
    producer and consumer. Deliberately NOT named `Statement`/`State`
    (as it once was, in the now-removed `regions/Statements.py`):
    that collided in name and in the reader's mental model with
    `hermes_decompiler.ir.statements.Statement` (`ReturnStatement`
    etc), a completely different concept - an actual IR statement
    node, not a positional (region, index) reference into a
    BasicBlock's raw instruction list.
    """
    parent: Any = field(default=None, kw_only=True)


@dataclass(slots=True)
class _InstructionRef(_RegionItem):
    """One `BasicBlock` instruction's position within a region."""
    block: BasicBlock
    index: int
    result: OpcodeResult


class StatementBuilder:

    def build(self, region):

        if isinstance(region, SequenceRegion):
            self._build_sequence(region)

        elif isinstance(region, LoopRegion):
            self.build(region.body)

        elif isinstance(region, IfRegion):
            self.build(region.then_body)
            if region.else_body:
                self.build(region.else_body)

        elif isinstance(region, TryRegion):
            self.build(region.try_body)
            if region.catch:
                self.build(region.catch.body)
            if region.finally_:
                self.build(region.finally_.body)

        elif isinstance(region, CatchRegion):
            self.build(region.body)

        elif isinstance(region, FinallyRegion):
            self.build(region.body)

    # ---------------------------------------------------------
    def _build_sequence(self, region):

        new_children = []

        for child in region.children:

            if isinstance(child, BasicBlock):

                statements = []

                for index, result in enumerate(child.instructions):
                    statements.append(
                        _InstructionRef(
                            parent=region,
                            block=child,
                            index=index,
                            result=result,
                        )
                    )

                region.items.extend(statements)

            else:

                self.build(child)
                region.items.append(child)

            new_children.append(child)

        region.children = new_children
