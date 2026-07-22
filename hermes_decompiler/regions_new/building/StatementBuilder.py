from __future__ import annotations

from hermes_decompiler.regions_new.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions_new.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    CatchRegion,
    FinallyRegion,
)
from hermes_decompiler.regions_new.models.Statements import (
    InstructionStatement,
)


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

        elif isinstance(region, CatchRegion):
            self.build(region.body)

        elif isinstance(region, FinallyRegion):
            self.build(region.body)

    # ---------------------------------------------------------
    def _build_sequence(self, region: SequenceRegion):

        new_children = []

        for child in region.children:

            #
            # BasicBlock -> Statements
            #
            if isinstance(child, BasicBlock):

                for index, result in enumerate(child.instructions):
                    region.statements.append(
                        InstructionStatement(
                            parent=region,
                            block=child,
                            index=index,
                            result=result,
                        )
                    )

                # BasicBlock artık tree'de kalmıyor.
                continue

            #
            # Nested region
            #
            self.build(child)

            new_children.append(child)

        region.children = new_children
