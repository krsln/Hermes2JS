from hermes_decompiler.core.Exceptions import CodeGenerationError, MetadataParseError, StructurerInvariantError
from hermes_decompiler.pipeline.Pipeline import Pipeline
from hermes_decompiler.pipeline.PipelineContext import PipelineContext
from hermes_decompiler.pipeline.stages import (
    MetadataStage,
    SignatureStage,
    BytecodeExtractionStage,
    DispatchStage,
    CodeGenerationStage,
    ParsingStage,
)


class Decompiler:
    """
    High-level entry point for Hermes bytecode decompilation.

    The decompilation process is intentionally split into two phases:

        1. build_context()
           Executes the analysis pipeline and produces a fully populated
           PipelineContext.

        2. render()
           Generates JavaScript from an existing PipelineContext.

    Separating analysis from rendering allows the same context to be rendered
    multiple times (for example, normal and raw output) without repeating
    parsing, opcode dispatch, or control-flow analysis.

    The class is stateless and therefore safe for concurrent use.
    """

    @staticmethod
    def build_context(assembly_content: str, section_index: int, *, strict: bool = False) -> PipelineContext:
        """
        Execute the decompilation pipeline and return the resulting
        PipelineContext.

        The returned context contains all intermediate analysis results required
        for code generation and may be rendered multiple times using different
        rendering options.

        Args:
            assembly_content:
                Hermes assembly (.hasm) text.

            section_index:
                Section identifier used for naming generated artifacts and
                anonymous functions.

            strict:
                If True, abort immediately on the first opcode dispatch error.
                Otherwise, recover where possible and continue generating output.

        Returns:
            A fully populated PipelineContext.

        Raises:
            ValueError:
                If the input is empty, or the .hasm metadata header line
                could not be parsed.
            NoHandlerError, OpcodeDispatchError:
                Only when `strict=True`: no opcode handler is registered
                for an opcode encountered during dispatch, or a
                registered handler raised while processing one. Both are
                `HasmDecompilerError` subclasses (see `core.Exceptions`).
                When `strict=False` (the default), these are instead
                logged and recovered from inline and never reach the
                caller - see `OpcodeDispatcher._run_pass`.
        """

        if not assembly_content.strip():
            raise ValueError("Empty assembly content")

        lines = assembly_content.strip().split('\n')
        state = PipelineContext(section_index=section_index, lines=lines)

        pipeline = Pipeline([
            MetadataStage(),
            SignatureStage(),
            BytecodeExtractionStage(),
            ParsingStage(),

            DispatchStage(strict=strict),
        ])

        try:
            return pipeline.run(state)
        except Exception as e:
            # Preserve the original public contract: callers of convert()
            # historically only needed to catch ValueError for bad input.
            if isinstance(e, MetadataParseError):
                raise ValueError(str(e)) from e
            raise

    @staticmethod
    def render(context: PipelineContext, *, verbose: bool = True, raw: bool = False) -> str:
        """
        Render JavaScript from an existing PipelineContext.

        Unlike build_context(), this method performs no parsing or analysis.
        It only executes the code generation stage, allowing the same analysis
        result to be rendered with different formatting options.

        Args:
            context:
                Previously built PipelineContext.

            verbose:
                Include source bytecode annotations.

            raw:
                Produce the raw renderer output.

        Returns:
            Generated JavaScript source code.

        Raises:
            StructurerInvariantError: A structurer pass hit a state its own
                logic assumes can never happen - i.e. a bug in the decompiler
                itself, not a failure caused by this section's input. Left
                unwrapped and unrecovered (regardless of any `strict` setting
                upstream) so it can never be mistaken for, or silently
                absorbed as, an ordinary per-section CodeGenerationError -
                see that exception's own docstring in `core.Exceptions`.
            CodeGenerationError: The code-generation stage failed for this
                section for any other reason (wraps the underlying cause).
        """

        try:
            result = CodeGenerationStage(verbose=verbose, raw=raw).run(context)
        except StructurerInvariantError:
            # A decompiler bug, not an expected input-driven failure - never
            # wrap this into CodeGenerationError, or callers like
            # FileOperations.process_section would log-and-continue past it
            # exactly like any other recoverable per-section error.
            raise
        except Exception as e:
            raise CodeGenerationError(context.section_index, e) from e

        return '\n'.join(result.js_lines)

    @staticmethod
    def convert(assembly_content, section_index, *, strict=False, verbose=True, raw=False) -> str:
        """
        Convenience wrapper combining build_context() and render().

        This method preserves the historical public API while internally
        splitting analysis from rendering.
        """

        context = Decompiler.build_context(assembly_content, section_index, strict=strict)

        return Decompiler.render(context, verbose=verbose, raw=raw)
