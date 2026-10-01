from hermes_decompiler.frontend.batch_pipeline.BatchContext import BatchContext
from hermes_decompiler.frontend.batch_pipeline.BatchStage import BatchStage
from hermes_decompiler.frontend.batch_pipeline.tables import EnvironmentOriginTable, PrivateNameTable


class PrivateNameTableStage(BatchStage):
    """Builds PrivateNameTable - see that class's own docstring. Depends on
    EnvironmentOriginTableStage having already run; falls back to an
    empty EnvironmentOriginTable (every lookup then simply resolves to
    nothing) if it hasn't, rather than raising - the same
    degrade-gracefully policy the tables themselves use throughout.
    """

    def run(self, context: BatchContext) -> BatchContext:
        environment_origins = context.environment_origin_table or EnvironmentOriginTable.empty()

        context.private_name_table = PrivateNameTable.from_sections(context.sections, environment_origins)

        return context
