from typing import List, Tuple

from hermes_decompiler.backend.runtime import HermesAnalysis
from hermes_decompiler.core.Exceptions import AnalysisContextError, NoHandlerError, OpcodeDispatchError
from hermes_decompiler.core.logging import get_logger
from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import HandlerLoader, OpcodeHandler, OpcodeContext
from hermes_decompiler.ir.expressions import AwaitExpression, Expression, RawExpression

logger = get_logger(__name__)

# HandlerLoader.load() populates ``OpcodeHandler.registry`` via __init_subclass__
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
    def dispatch_all(entries: List[OpcodeEntry], analysis: HermesAnalysis, *, strict: bool = False):
        # Static, one-time backward-jump scan - see `compute_loop_ranges`.
        # Shared by both passes below.
        loop_ranges = OpcodeDispatcher.compute_loop_ranges(entries)

        # --- Pass 1 (scratch, discarded) ---------------------------------
        # Runs the exact same dispatch as the real pass, on a throwaway
        # HermesAnalysis, purely to harvest which register gets WRITTEN
        # at which address. `dest_reg`/`entry.address` are recorded on
        # every OpcodeResult unconditionally (regardless of any inlining
        # decision), so this pass doesn't need loop-range awareness
        # itself to produce correct data - it only needs to finish a
        # normal walk. Errors are always swallowed here (never `strict`):
        # a bad opcode shouldn't stop harvesting, and any real error is
        # still reported/raised by pass 2 below.
        scratch = HermesAnalysis(metadata=analysis.metadata)
        scratch.loop_ranges = loop_ranges
        OpcodeDispatcher._run_pass(entries, scratch, strict=False)

        loop_carried_writes: dict[str, list[int]] = {}
        for result in scratch.results:
            if result.dest_reg is None:
                continue
            address = result.address
            if any(start <= address <= end for start, end in loop_ranges):
                loop_carried_writes.setdefault(result.name, []).append(address)

        # --- Pass 2 (real) ------------------------------------------------
        # Same walk again, on the caller's actual `analysis`, now armed
        # with both the loop ranges and the loop-carried write addresses
        # harvested above - see `HermesAnalysis.defined_and_used_in_same_loop`.
        analysis.loop_ranges = loop_ranges
        analysis.loop_carried_writes = loop_carried_writes
        OpcodeDispatcher._run_pass(entries, analysis, strict=strict)

    @staticmethod
    def _run_pass(entries: List[OpcodeEntry], analysis: HermesAnalysis, *, strict: bool) -> None:
        dispatcher = OpcodeDispatcher(analysis)

        for i, entry in enumerate(entries):

            if not entry.opcode:
                result = OpcodeResult(entry, value=RawExpression(source=f"// Unparsed: {entry.bytecode}"))
                analysis.add_result(result)
                continue

            analysis.current_address = entry.address

            try:
                result = dispatcher.dispatch(entry, entries, i)

                # Special case for generator pattern
                if result.handler == "SaveGenerator":
                    OpcodeDispatcher._handle_generator_await(analysis)

            except NoHandlerError as e:
                logger.warning("No handler for opcode '%s' (line=%r)", e.opcode, entry.bytecode)
                if strict:
                    raise
                result = OpcodeResult(entry, value=RawExpression(source=f"// Unhandled opcode: {e.opcode}"))
                analysis.add_result(result)
            except OpcodeDispatchError as e:
                logger.error("Dispatch error for opcode '%s': %s", e.opcode, e.cause, exc_info=True)
                if strict:
                    raise
                result = OpcodeResult(entry, value=RawExpression(source=f"// Error: {e.cause}"))
                analysis.add_result(result)

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


    @staticmethod
    def compute_loop_ranges(entries: List[OpcodeEntry]) -> List[Tuple[int, int]]:
        """
        Cheaply derive loop-body address ranges from raw disassembly, ahead
        of (and independent from) full CFG/loop construction.

        Every jump-family opcode already has `target_address` populated by
        `OpcodeEntry._parse_comment()` from the `# Address: ...` marker. Any
        jump whose target is BEHIND its own address is - by definition - a
        backward branch, i.e. a loop back-edge: the bytecode between the
        target and the jump instruction is the loop body (this holds for
        `while`/`for`/`do-while`/`for-of`/`for-in` lowering alike, since
        they all compile down to a conditional or unconditional backward
        jump at the bottom of the loop).

        This is intentionally a static, single-pass, list-of-ranges result
        - not a general CFG. It only needs to answer one question later
        (`HermesAnalysis.defined_and_used_in_same_loop`): "are these two
        addresses inside the same loop body?".
        """
        ranges: List[Tuple[int, int]] = []

        for entry in entries:
            if entry.target_address is None:
                continue
            if entry.target_address < entry.address:
                ranges.append((entry.target_address, entry.address))

        return ranges