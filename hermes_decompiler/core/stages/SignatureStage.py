from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.core.PipelineContext import PipelineContext
from hermes_decompiler.core.PipelineStage import PipelineStage

logger = get_logger(__name__)


class SignatureStage(PipelineStage):
    """Derives the JS function name, params, and async-ness from metadata."""

    def run(self, context: PipelineContext) -> PipelineContext:
        metadata = context.analysis.metadata

        function_name = metadata.get('function_name', f'func_{context.section_index}')
        if function_name.startswith('?anon_'):
            function_name = f'anon_{metadata.get("function_id", context.section_index)}'
        context.function_name = function_name

        param_count = metadata.get('param_count', 0)
        context.params = [f'param{i}' for i in range(param_count)]

        joined = '\n'.join(context.lines)
        context.is_async = '<StartGenerator>' in joined

        return context
