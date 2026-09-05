from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class CodeGenerationStage(PipelineStage):
    """Assembles the final JS function source from analysis.results."""

    def __init__(self, verbose: bool = True, raw: bool = False):
        self._verbose = verbose
        self._raw = raw

    def run(self, context: PipelineContext) -> PipelineContext:
        prefix = self._function_prefix(context)
        header = f'{prefix}{context.function_name}({", ".join(context.params)}) {{'
        context.js_lines = [header]

        if context.bytecode_lines:
            context.js_lines.extend(context.analysis.generate_js(self._verbose, self._raw))
        else:
            context.js_lines.append('    // No bytecode provided')

        context.js_lines.append('}')
        return context

    @staticmethod
    def _function_prefix(context: PipelineContext) -> str:
        """
        Choose the `function`/`function*`/`async function`/`async function* `
        keyword sequence.

        `context.is_generator` (see SignatureStage) only says the bytecode
        uses the generator suspend/resume protocol - Hermes lowers plain
        `function*` generators and async functions/generators through the
        identical opcodes, so it can't say which one this is on its own.

        Async-ness is instead read off the dispatched IR: `ResumeGenerator`
        unconditionally produces an `AwaitExpression(YieldExpression())`
        placeholder at every suspend point (real or not - see its own
        docstring), so a bare `isinstance(..., AwaitExpression)` check would
        say "async" for every generator, sync or not. The one place a *real*
        await appears is `OpcodeDispatcher._handle_generator_await`, which
        wraps an immediately-preceding Call's own value - i.e. an
        `AwaitExpression` whose argument is anything other than a bare
        `YieldExpression`. That's the same signal already used to decide
        "yield" vs "await" at each individual suspend point; this just reuses
        it once more here so the header agrees with the body it introduces.
        """
        is_async = any(
            isinstance(result.value, AwaitExpression)
            and not isinstance(result.value.argument, YieldExpression)
            for result in context.analysis.results
        )

        if context.is_generator:
            return "async function* " if is_async else "function* "

        return "async function " if is_async else "function "
