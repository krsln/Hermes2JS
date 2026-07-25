from __future__ import annotations

from hermes_decompiler.regions.cfg.BasicBlock import BasicBlock
from hermes_decompiler.regions.models.Regions import (
    SequenceRegion,
    LoopRegion,
    IfRegion,
    CatchRegion,
    FinallyRegion,
)
from hermes_decompiler.regions.models.Statements import (
    InstructionState,
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
    def _build_sequence(self, region):

        new_children = []

        for child in region.children:

            if isinstance(child, BasicBlock):

                statements = []

                for index, result in enumerate(child.instructions):
                    print(type(result.variable.value).__name__)
                    # TODO: burada ir/expressions|statements setlenebilir
                    statements.append(
                        InstructionState(
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
