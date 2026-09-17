from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class SignatureStage(PipelineStage):
    """Derives the JS function name, params, and generator-ness from metadata."""

    def run(self, context: PipelineContext) -> PipelineContext:
        metadata = context.analysis.metadata

        function_name = metadata.get('function_name', f'func_{context.section_index}')

        # commented: func ref must be same
        # if function_name == '?anon_0_':
        #     function_name = f'anon_{metadata.get("function_id", context.section_index)}'

        context.function_name = function_name

        param_count = metadata.get('param_count', 0)
        context.params = [
            f"param{i}"
            for i in range(1, param_count)
        ]

        # This only detects "is *some* flavor of generator", not "is async".
        #
        # Hermes lowers a plain `function*` generator and an `async function`
        # (or async generator) through the *identical* StartGenerator/
        # SaveGenerator/ResumeGenerator/CompleteGenerator suspend-resume
        # opcodes - there is no bytecode marker on this function's own
        # disassembly that tells the two apart. The real distinguishing
        # fact - whether the *caller* drives this closure directly (plain
        # generator) or hands it to Hermes's async-spawn machinery (async) -
        # lives in a different function's bytecode (whoever creates this
        # closure), which isn't available from a single section in
        # isolation.
        #
        # So we deliberately do NOT set an `is_async` flag here. Instead,
        # CodeGenerationStage derives async-ness after dispatch, from
        # whether any *real* AwaitExpression (a Call whose result feeds a
        # suspend point, as opposed to the unconditional placeholder every
        # resume point produces - see ResumeGenerator.py) survived in the
        # dispatched IR. That's still the same "Call directly before a
        # suspend" heuristic already used to decide "yield" vs "await" at
        # each individual suspend point (see GeneratorStateMachineRegionPass
        # and OpcodeDispatcher._handle_generator_await) - just applied once,
        # here, to the header keyword too, so the two stay consistent with
        # each other instead of the header unconditionally claiming "async".
        joined = '\n'.join(context.lines)
        context.is_generator = '<StartGenerator>' in joined

        context.header_kind = metadata.get('header_kind', 'normal')

        function_id = metadata.get('function_id', context.section_index)
        context.creator_facts = (
            context.creator_table.facts_for(function_id) if context.creator_table else None
        )

        if context.creator_facts is not None and context.creator_facts.is_generator:
            # The one signal that survives on hbc97+: nothing in this
            # function's own bytecode says so (see the docstring above and
            # CreatorTable's), but some other function's CreateGenerator
            # names this one as its target, which is true on every
            # version and is exactly what "is a generator body" means.
            context.is_generator = True

        if context.header_kind == 'generator':
            # This function's *own* header, independent of any batch
            # table: on hbc97+, an outer stub that only calls
            # CreateGenerator and returns still carries this - see
            # PipelineContext.header_kind. That stub's own bytecode has
            # no suspend/resume machinery either, exactly like the
            # CreateGenerator-target case above, so it gets the same
            # treatment for the same reason: printing it as `function*`
            # matches the keyword actually written in the source, even
            # though the body shown here is just the factory call - the
            # real `yield`s live in the separate CreateGenerator target.
            # This is also what covers a standalone section processed
            # without a creator_table at all, where this function's own
            # header is the only signal available.
            context.is_generator = True

        return context
