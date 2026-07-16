import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

_LEADING_REG_PATTERN = re.compile(r'^Reg\d+:\s*(\d+)')
_ADDR_TOKEN_PATTERN = re.compile(r'Addr\d+:\s*(-?\d+)')


# /// Switch on a small integer value using an inline jump table, generated
# /// for `switch` statements whose cases are dense small integers (sparse
# /// or non-integer `switch` cases compile to a chain of comparisons + Jmp
# /// instead, which this opcode is not involved in).
# ///
# /// ⚠️ NOT VERIFIED — unlike every other handler in this codebase, the
# /// exact operand layout (how many UInt32/Addr32 fields, what each bound
# /// means, and — critically — whether the jump-table entries themselves
# /// even appear inline in `entry.args`, or live in a separate bytecode
# /// region the text disassembly doesn't expose per-instruction) was not
# /// confirmed against a real `<SwitchImm>` disassembly line.
# ///
# /// Given that uncertainty, this handler deliberately does NOT attempt to
# /// reconstruct a `switch { ... }` statement — fabricating plausible-
# /// looking-but-wrong control flow here would be worse than an honest
# /// gap. It only extracts the selector register and any jump-table
# /// addresses it can find via a generic scan, registers them as goto
# /// targets (so downstream label/control-flow handling doesn't silently
# /// break), and leaves the rest as an explicit TODO comment in the output.
# ///
# /// Before relying on this for real: grep a `.hbc` dump for `<SwitchImm>`,
# /// paste an actual example line into this header comment (matching every
# /// other handler's convention), and rewrite Handle() against the real
# /// operand shape — most likely a UInt32 jump-table offset, a default
# /// Addr32 target, and UInt32 min/max case bounds, per Hermes's C++
# /// SwitchImm definition, but that needs confirming against real output.
# DEFINE_OPCODE_N(SwitchImm, ...)  # exact arity intentionally left unconfirmed
class SwitchImm(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__
        args = entry.args.strip()

        selector_match = _LEADING_REG_PATTERN.match(args)
        if not selector_match:
            return self.InvalidArgs(analysis, entry, "Expected a leading Reg8 selector argument")

        selector_reg = int(selector_match.group(1))
        selector_val = self.GetValueByReg(analysis.results, selector_reg) or f"r{selector_reg}"

        target_addrs = []
        for offset_str in _ADDR_TOKEN_PATTERN.findall(args):
            target_addr = entry.address + int(offset_str)
            analysis.gotoList.append(target_addr)
            target_addrs.append(target_addr)

        if target_addrs:
            targets = ", ".join(f"label_{addr}" for addr in target_addrs)
            value = (
                f"/* TODO: SwitchImm({selector_val}) — jump table not reconstructed; "
                f"candidate targets: {targets} */"
            )
        else:
            value = (
                f"/* TODO: SwitchImm({selector_val}) — jump table not reconstructed; "
                f"no Addr operands found to recover targets from */"
            )

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)