from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.PipelineStage import PipelineStage

logger = get_logger(__name__)


class SignatureStage(PipelineStage):
    """Derives the JS function name, params, and generator-ness from metadata."""

    def run(self, context: PipelineContext) -> PipelineContext:
        metadata = context.analysis.metadata

        function_name = metadata.get('function_name', f'func_{context.section_index}')

        if function_name.startswith('?anon_'):
            function_name = f'anon_{metadata.get("function_id", context.section_index)}'

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
        context.kind_facts = (
            context.kind_index.facts_for(function_id) if context.kind_index else None
        )

        if context.kind_facts is None:
            # No batch index. `is_generator` above is then the only signal
            # available, and it is a LAYOUT_V96-only one: v97+ emits no
            # suspend/resume opcodes at all, so this silently reports
            # "not a generator" for every generator in such a bundle. The
            # header Kind is the giveaway that we are on such a layout -
            # it can only be non-'normal' where Kind bits exist.
            if context.header_kind != 'normal':
                logger.warning(
                    "Function #%s (%s): header_kind=%r, but no batch index was supplied - "
                    "generator/async detection falls back to a LAYOUT_V96-only opcode check "
                    "and cannot be trusted on this bytecode version.",
                    function_id, function_name, context.header_kind,
                )
            return context

        # With an index, generator-ness is resolved rather than guessed.
        # Note this deliberately does NOT feed `context.is_generator` - see
        # PipelineContext.kind_facts for why the fact layer and the
        # render-affecting flag are kept apart until state-dispatch
        # structuring can act on it.
        facts = context.kind_facts

        if facts.is_generator_body and not context.is_generator:
            # The expected v97+ shape, not a problem: the batch proved this
            # is a body via its CreateGenerator edge, while the body itself
            # carries a hand-rolled state-dispatch machine instead of
            # suspend/resume opcodes.
            logger.debug(
                "Function #%s (%s): resolved as a %s body with no suspend/resume opcodes "
                "(hand-rolled state dispatch); stubs above it: %s.",
                function_id, function_name, facts.source_kind, facts.stub_ids or '-',
            )
        elif context.is_generator and not facts.is_generator_body:
            # The index and the bytecode disagree about this function being
            # a body at all. Unlike the case above this has no benign
            # explanation, so it is worth surfacing.
            logger.warning(
                "Function #%s (%s): bytecode contains <StartGenerator> but the batch index "
                "resolved role=%r - the creation graph may be incomplete for this batch.",
                function_id, function_name, facts.role,
            )

        return context
