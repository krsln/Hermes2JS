import re

from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, sequence
from hermes_decompiler.ir.expressions import AwaitExpression, YieldExpression, RawExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult, ControlFlowType
from hermes_decompiler.regions.models.Statements import GotoStatement
from hermes_decompiler.runtime import HermesAnalysis


# Example: <StartGenerator>: <>
class StartGenerator(OpcodeHandler):
    """Initialize generator execution."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        if not self._PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        # No JS-observable effect of its own; kept as a bare comment
        # marker via RawExpression, same as before.
        expression = RawExpression(source="// StartGenerator")

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Example: <ResumeGenerator>: <Reg8: 0, Reg8: 2>
class ResumeGenerator(OpcodeHandler):
    """Resume a suspended generator."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, _flag_reg = map(int, match.groups())

        # `await yield` is real, expressible JS - modeled directly
        # instead of the previous comment-annotated string.
        expression = AwaitExpression(argument=YieldExpression())

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Example: <CompleteGenerator>: <>
class CompleteGenerator(OpcodeHandler):
    """Mark the generator as completed."""

    _PATTERN = re.compile(r'^(?:<>)?$')

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        if not self._PATTERN.match(entry.args.strip()):
            return self.build_invalid_args_result(analysis, entry)

        expression = RawExpression(source="// CompleteGenerator")

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


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

        statement = GotoStatement(target=target)
        flow = ControlFlowType.UNCONDITIONAL

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, statement=statement, dest_reg=target, goto=target, control_flow=flow)
        analysis.add_result(result)

        return result
