from hermes_decompiler.analysis.terminators import TerminatorJump
from hermes_decompiler.handlers import OpcodeHandler, ADDR, sequence
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.runtime import HermesAnalysis


# Example: <SaveGenerator>: <Addr8: 4>  # Address: 00000095
class SaveGenerator(OpcodeHandler):
    """
    Save generator state and yield.

    CFG-wise this is an unconditional jump (like Jmp) to the resume
    point, so it's represented the same way: `GotoStatement`. The
    generator-specific `await yield` semantics is synthesized
    separately by `Dispatcher._handle_generator_await`, which wraps the
    *previous* instruction's value in an `AwaitExpression` once it sees
    a `SaveGenerator` follows it.
    """

    _PATTERN = sequence(ADDR)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        offset = int(match.group(1))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        terminator = TerminatorJump(target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=target)
        analysis.add_result(result)

        return result
