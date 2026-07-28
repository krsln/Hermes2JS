import re

from hermes_decompiler.handlers import OpcodeHandler
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult, ControlFlowType
from hermes_decompiler.analysis.regions import SwitchGotoStatement
from hermes_decompiler.runtime import HermesAnalysis


class SwitchImm(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg\d+:\s*(\d+)")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_value(analysis, selector_reg)

        targets = []

        for offset in re.compile(r"Addr\d+:\s*(-?\d+)").findall(entry.args):
            target = entry.address + int(offset)
            analysis.gotoList.append(target)
            targets.append(target)

        statement = SwitchGotoStatement(selector=selector, targets=tuple(targets))
        flow = ControlFlowType.TERMINATOR

        # NOTE (fix): the original never set `control_flow`, defaulting
        # to NORMAL despite having multiple successors and no
        # fallthrough - same class of bug already fixed for JCompareX.
        # pure control flow: no operand value of its own
        result = OpcodeResult(
            entry, value=None, statement=statement, dest_reg=None, extra_gotos=targets, control_flow=flow
        )
        analysis.add_result(result)

        return result


# UIntSwitchImm
#
# Same instruction family as SwitchImm (a jump table keyed by an
# integer selector register, `Addr` targets parsed the same way) --
# the "UInt" distinction is about how Hermes encodes/bounds-checks the
# selector *inside the VM* (unsigned vs. signed immediate comparisons
# against the jump table's min/max), not about the disassembled text
# shape this handler parses. `entry.args` for both opcodes follows the
# same `Reg<N>: <selector>  Addr<N>: <offset> ...` textual layout, so
# the existing regex-based parsing in SwitchImm applies unchanged.
class UIntSwitchImm(SwitchImm):
    pass
