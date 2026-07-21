from hermes_decompiler.Logger import get_logger
from hermes_decompiler.core.pipeline import ConversionState, Stage
from hermes_decompiler.core.exceptions import MetadataParseError
from hermes_decompiler.dispatch.Dispatcher import OpcodeDispatcher
from hermes_decompiler.parsers.metadata_parser import parse_hbc_metadata, parse_exception_handlers

logger = get_logger(__name__)


class MetadataStage(Stage):
    """Parses the .hbc header line (line 0) into analysis.metadata."""

    def run(self, state: ConversionState) -> ConversionState:
        if not state.lines:
            raise MetadataParseError("No lines to parse metadata from")

        try:
            metadata = parse_hbc_metadata(state.lines[0])

            metadata["exception_handlers"] = []

            if len(state.lines) > 1 and state.lines[1].strip().startswith("[Exception handlers:"):
                metadata["exception_handlers"] = parse_exception_handlers(state.lines[1])

            state.analysis.metadata = metadata
            state.analysis.metadataList.append(metadata)
        except Exception as e:
            raise MetadataParseError(f"Failed to parse metadata: {e}") from e

        return state


class SignatureStage(Stage):
    """Derives the JS function name, params, and async-ness from metadata."""

    def run(self, state: ConversionState) -> ConversionState:
        metadata = state.analysis.metadata

        function_name = metadata.get('function_name', f'func_{state.section_index}')
        if function_name.startswith('?anon_'):
            function_name = f'anon_{metadata.get("function_id", state.section_index)}'
        state.function_name = function_name

        param_count = metadata.get('param_count', 0)
        state.params = [f'param{i}' for i in range(param_count)]

        joined = '\n'.join(state.lines)
        state.is_async = '<StartGenerator>' in joined

        return state


class BytecodeExtractionStage(Stage):
    """Slices out the lines following the 'Bytecode listing' marker, if any."""

    def run(self, state: ConversionState) -> ConversionState:
        start = next((i for i, line in enumerate(state.lines) if "Bytecode listing" in line), -1)
        state.bytecode_lines = state.lines[start + 1:] if start >= 0 else []
        return state


class DispatchStage(Stage):
    """Runs every bytecode line through its opcode handler."""

    def __init__(self, strict: bool = False):
        self._strict = strict

    def run(self, state: ConversionState) -> ConversionState:
        if not state.bytecode_lines:
            return state

        results = OpcodeDispatcher.dispatch_all(state.bytecode_lines, state.analysis, strict=self._strict)
        if len(results) != len(state.analysis.results):
            logger.warning(
                "Section section_%s: Dispatcher returned %s results but analysis.results has %s",
                state.section_index, len(results), len(state.analysis.results),
            )

        return state


class CodeGenStage(Stage):
    """Assembles the final JS function source from analysis.results."""

    def __init__(self, verbose: bool = True):
        self._verbose = verbose

    def run(self, state: ConversionState) -> ConversionState:
        header = f'{"async function* " if state.is_async else "function "}{state.function_name}({", ".join(state.params)}) {{'
        state.js_lines = [header]

        if state.bytecode_lines:
            state.js_lines.extend(state.analysis.generate_js(self._verbose))
        else:
            state.js_lines.append('    // No bytecode provided')

        state.js_lines.append('}')
        return state
