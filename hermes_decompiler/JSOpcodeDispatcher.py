from typing import Optional

from hermes_decompiler.handlers import import_handlers
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.core.exceptions import AnalysisContextError, NoHandlerError, OpcodeDispatchError
from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)

# import_handlers() populates OpcodeHandler.registry via __init_subclass__
# side effects. It's idempotent (re-importing already-imported modules is a
# no-op), so doing it once at module load time - rather than once per
# JSOpcodeDispatcher() instance - is both correct and avoids repeated
# import-machinery overhead when many sections are converted in one process.
import_handlers()


class OpcodeDispatcher:
    """
    Routes a single OpcodeEntry to its registered OpcodeHandler.

    Raises structured exceptions (AnalysisContextError, NoHandlerError,
    OpcodeDispatchError) instead of returning them embedded as comment
    strings in a JSVariable - it's the caller's job (dispatch_all, below)
    to decide whether to convert those into inline `// Error`: comments
    for the generated JS or to propagate them.
    """

    def __init__(self, analysis: HermesAnalysis):
        self.Analysis = analysis

    def Dispatch(self, line: OpcodeEntry) -> OpcodeResult:
        if not self.Analysis:
            raise AnalysisContextError("Analysis context is not set on JSOpcodeDispatcher")

        handler = OpcodeHandler.GetHandler(line.opcode)
        if not handler:
            logger.warning("TODO: NO HANDLER '%s' (line=%r)", line.opcode, line)
            raise NoHandlerError(line.opcode)

        try:
            return handler.Handle(self.Analysis, line)
        except Exception as e:
            raise OpcodeDispatchError(line.opcode, line.bytecode, e) from e

    @staticmethod
    def DispatchAll(bytecode_lines: list[str], analysis: HermesAnalysis, *, strict: bool = False) \
            -> list[OpcodeResult]:
        """
        Dispatch every bytecode line to its opcode handler.

        Args:
            bytecode_lines: Raw lines from the "Bytecode listing" section.
            analysis: The per-conversion analysis context.
            strict: If True, re-raise on the first parse/dispatch failure
                (useful for CI/tests, to catch regressions immediately).
                If False (default), log and emit an inline `// Error:` /
                `// Unhandled opcode:` comment and keep going, matching the
                original tool's "best effort" behavior for large binaries
                where a handful of unrecognized opcodes shouldn't abort the
                whole file.

        Returns:
            List of OpcodeResult, one per input line (parsed or not).
        """
        # Local import to avoid a circular import between dispatch and parsing.
        from hermes_decompiler.parsers.line_parser import parse_line

        dispatcher = OpcodeDispatcher(analysis)

        results: list[OpcodeResult] = []
        cleaned_lines = [line.strip() for line in bytecode_lines if line.strip()]

        for line in cleaned_lines:
            parsed_line = parse_line(line)

            if parsed_line is None:
                logger.debug("Unparsed line: %s", line)
                entry = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")
                result = OpcodeResult(entry, JSVariable("", 0, "", f'// Unparsed: {line}'))
                analysis.results.append(result)
                results.append(result)
                continue

            try:
                dispatched = dispatcher.Dispatch(parsed_line)

                # await control
                if dispatched.Variable.handler == "SaveGenerator":
                    prev = analysis.results[len(analysis.results) - 2]
                    if prev.Variable.handler.startswith("Call"):
                        prev.Variable.value = f"await {prev.Variable.value}"
                        prev.result = f"{prev.Variable.name} = {prev.Variable.value}"

                results.append(dispatched)
            except NoHandlerError as e:
                logger.warning("No handler for opcode '%s' (line=%r)", e.opcode, line)
                if strict:
                    raise
                result = OpcodeResult(parsed_line,
                                      JSVariable("-", parsed_line.address, "", f'// Unhandled opcode: {e.opcode}'))
                analysis.results.append(result)
                results.append(result)
            except OpcodeDispatchError as e:
                logger.error("Dispatch error for opcode '%s': %s", e.opcode, e.cause, exc_info=True)
                if strict:
                    raise
                result = OpcodeResult(parsed_line,
                                      JSVariable(e.opcode, parsed_line.address, "", f'// Error: {e.cause}'))
                analysis.results.append(result)
                results.append(result)

        return results
