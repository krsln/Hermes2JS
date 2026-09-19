from hermes_decompiler.frontend.parsing.BatchContext import BatchContext
from hermes_decompiler.frontend.parsing.BatchStage import BatchStage
from hermes_decompiler.frontend.parsing.EnvironmentOriginTable import EnvironmentOriginTable


class EnvironmentOriginTableStage(BatchStage):
    """Builds EnvironmentOriginTable - see that class's own docstring. No
    dependency on any other batch stage, but PrivateNameTableStage and
    ClassEnvironmentTableStage both depend on ITS output, so this needs
    to run before either of them - see BatchPipeline's docstring.
    """

    def run(self, context: BatchContext) -> BatchContext:
        context.environment_origin_table = EnvironmentOriginTable.from_sections(context.sections)

        return context
