from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)

_SAVE_GENERATOR_HANDLERS = ("SaveGenerator", "SaveGeneratorLong")


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
            context.js_lines.extend(
                context.analysis.generate_js(self._verbose, self._raw, creator_facts=context.creator_facts)
            )
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

        Async-ness is read off the dispatched IR: `ResumeGenerator`
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

        That IR heuristic only fires on hbc96, whose ResumeGenerator is what
        produces the placeholder it looks for in the first place - hbc97+
        emits neither, so it is OR'd with `creator_facts.is_async` (see
        CreatorTable), the batch-resolved signal that covers that version
        instead.

        `is_generator` alone still isn't enough to decide the `*`, though:
        a *plain* `async function` (no real `yield` anywhere in source) is
        lowered through this exact same suspend/resume protocol, so
        `is_generator` comes back True for it too - printing `async
        function*` in that case would show a keyword the source never had
        (and GeneratorStateMachineRegionPass would have nothing but
        Call-derived `AwaitExpression`s to fold, never a genuine
        `YieldExpression`; see its own docstring). `has_bare_yield` below
        re-derives, per suspend point, the same "was the value immediately
        before this SaveGenerator a real await?" signal
        `OpcodeDispatcher._handle_generator_await` already computed once -
        if not one single suspend point in this function turns out to be a
        genuine (non-await) yield, this is really just a plain `async
        function`, star and all dropped.
        """
        is_async = any(
            isinstance(result.value, AwaitExpression)
            and not isinstance(result.value.argument, YieldExpression)
            for result in context.analysis.results
        )

        if context.creator_facts is not None and context.creator_facts.is_async:
            is_async = True

        if context.header_kind == 'async':
            # This function's own header, independent of any batch table -
            # see SignatureStage's symmetric use of header_kind == 'generator'
            # for why an outer stub gets labeled with the keyword actually
            # written in the source even though its own body is just the
            # factory call.
            is_async = True

        results = context.analysis.results
        has_bare_yield = any(
            not (
                    idx > 0
                    and isinstance(results[idx - 1].value, AwaitExpression)
                    and not isinstance(results[idx - 1].value.argument, YieldExpression)
            )
            for idx, result in enumerate(results)
            if result.handler in _SAVE_GENERATOR_HANDLERS
        )

        if context.is_generator:
            if is_async and not has_bare_yield:
                # Every suspend point in this function was await-derived
                # and none was a genuine yield - a plain async function
                # (or an async stub with no suspend points of its own at
                # all; see SignatureStage's header_kind == 'generator'
                # note), not a real generator.
                return "async function "

            return "async function* " if is_async else "function* "

        return "async function " if is_async else "function "
