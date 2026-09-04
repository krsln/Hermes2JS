from hermes_decompiler.core.Exceptions import CodeGenerationError
from hermes_decompiler.frontend.stages import (
    MetadataStage,
    SignatureStage,
    BytecodeExtractionStage,
    DispatchStage,
    CodeGenerationStage,
    ParsingStage,
)
from hermes_decompiler.pipeline.Pipeline import Pipeline
from hermes_decompiler.pipeline.PipelineContext import PipelineContext


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
                Hermes assembly (.hbc) text.

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
                If the input is empty or metadata cannot be parsed.
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
            from hermes_decompiler.core.Exceptions import MetadataParseError
            if isinstance(e, MetadataParseError):
                raise ValueError(str(e)) from e
            raise

    @staticmethod
    def render(context: PipelineContext, *, verbose: bool = True, raw: bool = True) -> str:
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
            CodeGenerationError: The code-generation stage failed for this
                section (wraps the underlying cause).
        """

        try:
            result = CodeGenerationStage(verbose=verbose, raw=raw).run(context)
        except Exception as e:
            raise CodeGenerationError(context.section_index, e) from e

        return '\n'.join(result.js_lines)

    @staticmethod
    def convert(assembly_content, section_index, *, strict=False, verbose=True, raw=True) -> str:
        """
        Convenience wrapper combining build_context() and render().

        This method preserves the historical public API while internally
        splitting analysis from rendering.
        """

        context = Decompiler.build_context(assembly_content, section_index, strict=strict)

        return Decompiler.render(context, verbose=verbose, raw=raw)
