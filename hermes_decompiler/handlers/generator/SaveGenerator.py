from hermes_decompiler.analysis.terminators import TerminatorJump
from hermes_decompiler.frontend.opcode import OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, OpcodeContext, sequence, ADDR


# Addr8 (total size 1)
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

    def handle(self, ctx: OpcodeContext) -> OpcodeResult:

        match = self._PATTERN.match(ctx.entry.args.strip())
        if not match:
            return self.build_invalid_args_result(ctx.analysis, ctx.entry)

        offset = int(match.group(1))

        target = ctx.entry.target_address
        if target is None:
            target = ctx.entry.address + offset

        ctx.analysis.gotoList.append(target)

        terminator = TerminatorJump(target=target)

        # pure control flow: no operand value of its own
        result = OpcodeResult(ctx.entry, value=None, terminator=terminator, dest_reg=target)
        ctx.analysis.add_result(result)

        return result


# Addr32 (total size 4)
class SaveGeneratorLong(SaveGenerator):
    pass
