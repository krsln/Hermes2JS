import re
from typing import ClassVar, Tuple

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.handlers.Jmp import JmpFalse

# Two-register conditional jumps: <Addr, Reg8 (lhs), Reg8 (rhs)>.
# Example (Hermes disasm): <JLess>: <Addr8: 12, Reg8: 3, Reg8: 4>  # Address: 00000021
_COMPARE_PATTERN = re.compile(r'^Addr\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')


class JCompareX(OpcodeHandler):
    """
    Shared base for two-register conditional-branch opcodes
    (JLess, JNotLess, JEqual, JStrictEqual, JStrictNotEqual, ...).

    Subclasses only need to set `operator` (the JS operator to emit) and,
    optionally, override `describe` for a custom comment. This mirrors the
    "no-op-payload, only comparison semantics differ" shape of the real
    Hermes bytecode definitions (DEFINE_JUMP_3 family).
    """

    #: JS operator emitted between the two operands, e.g. "<", "===".
    operator: ClassVar[str] = "=="

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _COMPARE_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(
                analysis, entry,
                f"Expected 'Addr, Reg, Reg' arguments for {handler}",
            )

        addr_offset, lhs_reg, rhs_reg = self._parse_operands(match)
        target_addr = entry.address + addr_offset
        analysis.gotoList.append(target_addr)

        lhs_val = self.GetValueByReg(analysis.results, lhs_reg)
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg)
        if lhs_val is None or rhs_val is None:
            logger.warning(
                f"{handler}: unresolved operand register(s) at address {entry.address} "
                f"(r{lhs_reg}={lhs_val!r}, r{rhs_reg}={rhs_val!r})"
            )
            lhs_val = lhs_val if lhs_val is not None else f"r{lhs_reg}"
            rhs_val = rhs_val if rhs_val is not None else f"r{rhs_reg}"

        value = (
            f"if ({lhs_val} {self.operator} {rhs_val}) "
            f"{{ /* jump to label_{target_addr} */ }}"
        )

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable, goto=target_addr)

        return OpcodeResult(entry, variable, goto=target_addr)

    @staticmethod
    def _parse_operands(match: "re.Match[str]") -> Tuple[int, int, int]:
        addr_offset, lhs_reg, rhs_reg = (int(x) for x in match.groups())
        return addr_offset, lhs_reg, rhs_reg


# /// Arg1 = (Arg2 < Arg3), then jump if true.
# DEFINE_JUMP_3(JLess)
class JLess(JCompareX):
    operator = "<"


# /// Negation of JLess: jump if !(Arg2 < Arg3).
# DEFINE_JUMP_3(JNotLess)
class JNotLess(JCompareX):
    operator = ">="


# /// Loose equality jump: jump if Arg2 == Arg3.
# DEFINE_JUMP_3(JEqual)
class JEqual(JCompareX):
    operator = "=="


# /// Strict equality jump: jump if Arg2 === Arg3.
# DEFINE_JUMP_3(JStrictEqual)
class JStrictEqual(JCompareX):
    operator = "==="


# /// Strict inequality jump: jump if Arg2 !== Arg3.
# DEFINE_JUMP_3(JStrictNotEqual)
class JStrictNotEqual(JCompareX):
    operator = "!=="


# /// Long-offset (Addr32) variant of JmpFalse. Semantics are identical to
# /// JmpFalse; only the branch-offset encoding width differs, and the shared
# /// `Addr\d+` pattern in Jmp.py's parser already accepts both widths — so
# /// this simply reuses JmpFalse's Handle() the same way JmpTrueLong reuses
# /// JmpTrue's.
# DEFINE_JUMP_2(JmpFalseLong)
class JmpFalseLong(JmpFalse):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)