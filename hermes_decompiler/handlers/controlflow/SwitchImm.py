import re

from hermes_decompiler.analysis.terminators import TerminatorSwitch
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

        terminator = TerminatorSwitch(selector=selector, targets=tuple(targets))
        # TODO: remove → statement | flow
        statement = SwitchGotoStatement(selector=selector, targets=tuple(targets))
        flow = ControlFlowType.TERMINATOR

        # NOTE (fix): the original never set `control_flow`, defaulting
        # to NORMAL despite having multiple successors and no
        # fallthrough - same class of bug already fixed for JCompareX.
        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, terminator=terminator, dest_reg=None,
                              statement=statement, control_flow=flow)
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


# DEFINE_OPCODE_5(StringSwitchImm, Reg8, UInt32, UInt32, Addr32, UInt32)
#   [confirmed, facebook/hermes BytecodeList.def, tag hermes-v260318099.0.1]
#
#   "All-string switch (switch all of whose case labels are string
#    literals).
#    Arg 1 is the value to be branched upon
#    Arg 2 is a global index for this StringSwitchImm instruction in
#      the bytecode file.
#    Arg 3 is the relative offset of the string switch table. A string
#      switch table is a sequence of pairs:
#      <UInt32 string table index, UInt32 jump targets>
#    Arg 4 is the relative offset for the "default" jump.
#    Arg 5 is the size of the string switch table.
#
#    Given the above, the jump table entry for a given value (that is
#    in range) is located at offset ip + arg3. Note that Arg3 is
#    *unaligned*; it is dynamically aligned at runtime."
#
# Structurally different from SwitchImm/UIntSwitchImm: those encode
# jump targets as a flat sequence of `Addr` operands directly in
# `entry.args` (parsed via the `Addr\d+:\s*(-?\d+)` regex), which is
# why SwitchImm's existing parsing works unchanged for UIntSwitchImm.
# StringSwitchImm instead points at an *out-of-line table* (Arg3: an
# offset to a sequence of <string_id, jump_target> pairs elsewhere in
# the bytecode) plus a separate `Addr32` default-jump operand (Arg4) --
# the individual case targets are NOT expected to appear as `Addr`
# tokens in this opcode's own disassembled `entry.args` text the way
# SwitchImm's are. Whether this decompiler's disassembler/OpcodeEntry
# layer already resolves that out-of-line table into inline `Addr`-like
# annotations (the way it resolves string_ids into
# `entry.identifier_name`) is unknown -- if it does, this can reuse
# SwitchImm's regex-based target extraction; if it doesn't, this
# handler alone can't recover the actual jump table without a new
# capability which is not yet implemented.
#
# NOT extending SwitchImm here (unlike UIntSwitchImm) because the
# operand shape is genuinely different, not just a VM-internal bounds-
# check detail -- reusing SwitchImm.handle would silently mis-parse
# Arg2 (bytecode-file-global switch index) as a selector register.
#
# VERIFY: whether entry.args/entry.comment exposes the resolved
# <string, target> pairs for this opcode before trusting the "default
# only" fallback below.
class StringSwitchImm(OpcodeHandler):
    """All-string `switch` statement. Case targets come from an out-of-line table this handler can't yet resolve."""

    _PATTERN = re.compile(r"^Reg\d+:\s*(\d+)")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis, entry, "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_value(analysis, selector_reg)

        # Case targets live in an out-of-line string-switch table (Arg3
        # offset) that this handler does not resolve -- see module
        # comment. Only the default-jump (Addr32, Arg4) is picked up if
        # the disassembler surfaces it as a plain `Addr` token, same as
        # SwitchImm's existing regex.
        targets = []
        for offset in re.compile(r"Addr\d+:\s*(-?\d+)").findall(entry.args):
            target = entry.address + int(offset)
            analysis.gotoList.append(target)
            targets.append(target)

        terminator = TerminatorSwitch(selector=selector, targets=tuple(targets))
        # TODO: remove → statement | flow
        statement = SwitchGotoStatement(selector=selector, targets=tuple(targets))
        flow = ControlFlowType.TERMINATOR

        result = OpcodeResult(
            entry, value=None, terminator=terminator, dest_reg=None,
            statement=statement, control_flow=flow
        )
        analysis.add_result(result)

        return result
