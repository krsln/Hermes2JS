from typing import Optional

from hermes_decompiler.core.pipeline import ConversionState, Pipeline
from hermes_decompiler.models.FunctionTableRegistry import FunctionTableRegistry
from hermes_decompiler.core.stages import (
    MetadataStage,
    SignatureStage,
    BytecodeExtractionStage,
    SymbolTableStage,
    DispatchStage,
    CodeGenStage,
)


class Decompiler:
    """
    Convert .hbc assembly content to JavaScript code.

    Unlike the previous implementation, JSConverter holds NO state of its
    own (no `_functionTable` class attribute). Every call is fully
    self-contained: a fresh HermesAnalysis is created internally, and any
    cross-section knowledge (e.g., resolving function names across multiple
    section_<n>.hbc files) must be passed in explicitly via
    `function_registry`. This makes concurrent/parallel conversion safe and
    keeps tests from bleeding state into one another.
    """

    @staticmethod
    def convert(
            assembly_content: str,
            section_index: int,
            *,
            function_registry: Optional[FunctionTableRegistry] = None,
            strict: bool = False,
            verbose: bool = True,
    ) -> str:
        """
        Args:
            assembly_content: The .hbc assembly content.
            section_index: The section index for naming anonymous functions.
            function_registry: Optional shared registry for resolving
                function names across multiple sections. Pass the same
                instance across a batch of `convert()` calls (see
                FileOps) if you need that; omit it for a fully isolated,
                single-section conversion.
            strict: If True, raise immediately on the first opcode
                dispatch failure instead of emitting an inline `// Error:`
                comment and continuing.
            verbose: If True, annotate generated JS with `// CODE ->`
                source comments.

        Returns:
            The generated JavaScript code.

        Raises:
            ValueError: If the assembly content is empty or metadata is
                unparseable (preserved for backwards compatibility with
                callers catching ValueError, e.g. FileOps).
        """
        if not assembly_content.strip():
            raise ValueError("Empty assembly content")

        lines = assembly_content.strip().split('\n')
        state = ConversionState(
            section_index=section_index,
            lines=lines,
            function_registry=function_registry,
        )

        pipeline = Pipeline([
            MetadataStage(),
            SignatureStage(),
            BytecodeExtractionStage(),
            SymbolTableStage(),
            DispatchStage(strict=strict),
            CodeGenStage(verbose=verbose),
        ])

        try:
            state = pipeline.run(state)
        except Exception as e:
            # Preserve the original public contract: callers of convert()
            # historically only needed to catch ValueError for bad input.
            from hermes_decompiler.core.exceptions import MetadataParseError
            if isinstance(e, MetadataParseError):
                raise ValueError(str(e)) from e
            raise

        return '\n'.join(state.js_lines)
