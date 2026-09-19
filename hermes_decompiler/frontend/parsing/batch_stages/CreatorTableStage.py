from hermes_decompiler.frontend.parsing.BatchContext import BatchContext
from hermes_decompiler.frontend.parsing.BatchStage import BatchStage
from hermes_decompiler.frontend.parsing.CreatorTable import CreatorTable


class CreatorTableStage(BatchStage):
    """Builds CreatorTable - see that class's own docstring. No dependency
    on any other batch stage; can run in any position in the stage list.
    """

    def run(self, context: BatchContext) -> BatchContext:
        context.creator_table = CreatorTable.from_sections(context.sections)

        return context
