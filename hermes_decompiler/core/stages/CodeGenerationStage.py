from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.core.PipelineContext import PipelineContext
from hermes_decompiler.core.PipelineStage import PipelineStage

logger = get_logger(__name__)


class CodeGenerationStage(PipelineStage):
    """Assembles the final JS function source from analysis.results."""

    def __init__(self, verbose: bool = True):
        self._verbose = verbose

    def run(self, context: PipelineContext) -> PipelineContext:
        header = f'{"async function* " if context.is_async else "function "}{context.function_name}({", ".join(context.params)}) {{'
        context.js_lines = [header]

        if context.bytecode_lines:
            context.js_lines.extend(context.analysis.generate_js(self._verbose))
        else:
            context.js_lines.append('    // No bytecode provided')

        context.js_lines.append('}')
        return context
