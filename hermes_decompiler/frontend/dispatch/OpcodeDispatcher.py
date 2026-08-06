from typing import List

from hermes_decompiler.core.Exceptions import AnalysisContextError, NoHandlerError, OpcodeDispatchError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import HandlerLoader, OpcodeHandler, OpcodeContext
from hermes_decompiler.ir.expressions import AwaitExpression, Expression, RawExpression
from hermes_decompiler.runtime import HermesAnalysis

logger = get_logger(__name__)

# HandlerLoader.load() populates OpcodeHandler.registry via __init_subclass__
# side effects. It's idempotent (re-importing already-imported modules is a
# no-op), so doing it once at module load time - rather than once per
# JSOpcodeDispatcher() instance - is both correct and avoids repeated
# import-machinery overhead when many sections are converted in one process.
HandlerLoader.load()


class OpcodeDispatcher:
    """
        Responsible for routing OpcodeEntry objects to their corresponding
        OpcodeHandler implementations.
    """

    def __init__(self, analysis: HermesAnalysis):
        if not analysis:
            raise AnalysisContextError("Analysis context cannot be None")
        self.analysis = analysis

    def dispatch(self, entry: OpcodeEntry, entries: List[OpcodeEntry], index: int) -> OpcodeResult:
        """
            Dispatch a single opcode to its handler.

            Raises:
                NoHandlerError: No handler registered for this opcode.
                OpcodeDispatchError: Handler raised an exception.
        """

        handler_cls = OpcodeHandler.get_handler(entry.opcode)

        if not handler_cls:
            logger.warning("TODO: NO HANDLER '%s' (line=%r)", entry.opcode, entry)
            raise NoHandlerError(entry.opcode)

        try:
            context = OpcodeContext(self.analysis, entry, entries, index)
            return handler_cls.handle(context)
        except Exception as e:
            raise OpcodeDispatchError(entry.opcode, entry.bytecode, e) from e

    @staticmethod
    def dispatch_all(entries: List[OpcodeEntry], analysis: HermesAnalysis, *, strict: bool = False) -> list[
        OpcodeResult]:
        dispatcher = OpcodeDispatcher(analysis)
        results: List[OpcodeResult] = []

        for i, entry in enumerate(entries):

            if not entry.opcode:
                result = OpcodeResult(ctx.entry, value=RawExpression(source=f"// Unparsed: {entry.bytecode}"))
                analysis.add_result(result)
                results.append(result)
                continue

            try:
                result = dispatcher.dispatch(entry, entries, i)

                # Special case for generator pattern
                if result.handler == "SaveGenerator":
                    OpcodeDispatcher._handle_generator_await(analysis)

                results.append(result)
            except NoHandlerError as e:
                logger.warning("No handler for opcode '%s' (line=%r)", e.opcode, raw_line)
                if strict:
                    raise
                result = OpcodeResult(ctx.entry, value=RawExpression(source=f"// Unhandled opcode: {e.opcode}"))
                analysis.add_result(result)
                results.append(result)
            except OpcodeDispatchError as e:
                logger.error("Dispatch error for opcode '%s': %s", e.opcode, e.cause, exc_info=True)
                if strict:
                    raise
                result = OpcodeResult(ctx.entry, value=RawExpression(source=f"// Error: {e.cause}"))
                analysis.add_result(result)
                results.append(result)

        return results

    @staticmethod
    def _handle_generator_await(analysis: HermesAnalysis) -> None:
        """
        Rewrites

            rX = Call(...)
            SaveGenerator

        into

            rX = await Call(...)

        before any later opcode consumes that register.
        """

        if len(analysis.results) < 2:
            return

        prev = analysis.results[-2]

        if prev.handler.startswith("Call") and isinstance(prev.value, Expression):
            prev.value = AwaitExpression(argument=prev.value)
