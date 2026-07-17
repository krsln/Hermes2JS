from typing import List

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
        Responsible for routing OpcodeEntry objects to their corresponding
        OpcodeHandler implementations.
    """

    def __init__(self, analysis: HermesAnalysis):
        if not analysis:
            raise AnalysisContextError("Analysis context cannot be None")
        self.Analysis = analysis

    def Dispatch(self, entry: OpcodeEntry) -> OpcodeResult:
        """
            Dispatch a single opcode to its handler.

            Raises:
                NoHandlerError: No handler registered for this opcode.
                OpcodeDispatchError: Handler raised an exception.
        """
        handler_cls = OpcodeHandler.GetHandler(entry.opcode)
        if not handler_cls:
            logger.warning("TODO: NO HANDLER '%s' (line=%r)", entry.opcode, entry)
            raise NoHandlerError(entry.opcode)

        try:
            return handler_cls.Handle(self.Analysis, entry)
        except Exception as e:
            raise OpcodeDispatchError(entry.opcode, entry.bytecode, e) from e

    @staticmethod
    def DispatchAll(bytecode_lines: List[str], analysis: HermesAnalysis, *, strict: bool = False) \
            -> list[OpcodeResult]:
        """
            Process all bytecode lines with error resilience.

            Args:
                bytecode_lines: Raw bytecode listing lines.
                analysis: Analysis context.
                strict: If True, rise on the first error (useful for tests/CI).
        """
        # Local import to avoid a circular import between dispatch and parsing.
        from hermes_decompiler.parsers.line_parser import parse_line

        dispatcher = OpcodeDispatcher(analysis)
        results: List[OpcodeResult] = []

        for raw_line in bytecode_lines:
            line = raw_line.strip()

            if not line:
                continue

            parsed = parse_line(line)

            if parsed is None:
                logger.debug("Unparsed line: %s", line)
                entry = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")
                result = OpcodeResult(
                    entry,
                    JSVariable("", 0, "", f'// Unparsed: {line}')
                )
                analysis.results.append(result)
                results.append(result)
                continue

            try:
                result = dispatcher.Dispatch(parsed)

                # Special case for generator pattern
                if result.Variable.handler == "SaveGenerator":
                    OpcodeDispatcher._handle_generator_await(analysis)

                results.append(result)
            except NoHandlerError as e:
                logger.warning("No handler for opcode '%s' (line=%r)", e.opcode, raw_line)
                if strict:
                    raise
                result = OpcodeResult(
                    parsed,
                    JSVariable("-", parsed.address, "", f'// Unhandled opcode: {e.opcode}')
                )
                analysis.results.append(result)
                results.append(result)
            except OpcodeDispatchError as e:
                logger.error("Dispatch error for opcode '%s': %s", e.opcode, e.cause, exc_info=True)
                if strict:
                    raise
                result = OpcodeResult(
                    parsed,
                    JSVariable(e.opcode, parsed.address, "", f'// Error: {e.cause}')
                )
                analysis.results.append(result)
                results.append(result)

        return results

    @staticmethod
    def _handle_generator_await(analysis: HermesAnalysis) -> None:
        """Special handling for generator yield patterns."""
        if len(analysis.results) < 2:
            return

        prev = analysis.results[len(analysis.results) - 2]
        if prev.Variable.handler.startswith("Call"):
            prev.Variable.value = f"await {prev.Variable.value}"
            prev.result = f"{prev.Variable.name} = {prev.Variable.value}"
