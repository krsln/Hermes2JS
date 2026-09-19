from hermes_decompiler.frontend.batch_pipeline.BatchContext import BatchContext
from hermes_decompiler.frontend.batch_pipeline.BatchStage import BatchStage
from hermes_decompiler.frontend.batch_pipeline.tables import EnvironmentOriginTable, ClassEnvironmentTable


class ClassEnvironmentTableStage(BatchStage):
    """Builds ClassEnvironmentTable - see that class's own docstring. Same
    EnvironmentOriginTableStage dependency (and same fallback) as
    PrivateNameTableStage.
    """

    def run(self, context: BatchContext) -> BatchContext:
        environment_origins = context.environment_origin_table or EnvironmentOriginTable.empty()

        context.class_environment_table = ClassEnvironmentTable.from_sections(context.sections, environment_origins)

        return context
