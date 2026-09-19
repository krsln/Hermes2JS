from hermes_decompiler.frontend.parsing.BatchContext import BatchContext
from hermes_decompiler.frontend.parsing.BatchStage import BatchStage
from hermes_decompiler.frontend.parsing.ClassEnvironmentTable import ClassEnvironmentTable
from hermes_decompiler.frontend.parsing.EnvironmentOriginTable import EnvironmentOriginTable


class ClassEnvironmentTableStage(BatchStage):
    """Builds ClassEnvironmentTable - see that class's own docstring. Same
    EnvironmentOriginTableStage dependency (and same fallback) as
    PrivateNameTableStage.
    """

    def run(self, context: BatchContext) -> BatchContext:
        environment_origins = context.environment_origin_table or EnvironmentOriginTable.empty()

        context.class_environment_table = ClassEnvironmentTable.from_sections(context.sections, environment_origins)

        return context
