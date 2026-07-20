from __future__ import annotations

from typing import ClassVar, Tuple

from hermes_decompiler.handlers._shared_patterns import ADDR, REG, sequence
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

_COMPARE_PATTERN = sequence(ADDR, REG, REG)


def _parse_compare(entry: OpcodeEntry) -> Tuple[int, int, int]:
    """
    Parse comparison jump arguments.

        Addr, Reg, Reg
    """

    match = _COMPARE_PATTERN.match(entry.args.strip())

    if not match:
        raise ValueError(
            f"Invalid arguments for {entry.opcode}: {entry.args}"
        )

    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3)),
    )


class JCompareX(OpcodeHandler):
    """
    Base class for every comparison jump opcode.
    """

    operator: ClassVar[str] = "=="

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry, ) -> OpcodeResult:
        try:
            offset, lhs_reg, rhs_reg = _parse_compare(entry)
        except ValueError as exc:
            return self.build_invalid_args_result(analysis, entry, str(exc))

        target = entry.address + offset
        analysis.gotoList.append(target)

        lhs = self.get_register_value(analysis, lhs_reg) or f"r{lhs_reg}"
        rhs = self.get_register_value(analysis, rhs_reg) or f"r{rhs_reg}"

        expression = (
            f"if ({lhs} {self.operator} {rhs}) "
            f"{{ /* jump to label_{target} */ }}"
        )

        variable = JSVariable(
            self.__class__.__name__,
            entry.address,
            "",
            expression,
        )

        analysis.add_result(entry, variable, goto=target)

        return OpcodeResult(entry, variable, goto=target)


# @formatter:off
# Equality
# ---------
class JEqual(JCompareX): operator = "=="
class JEqualLong(JEqual): pass
class JNotEqual(JCompareX): operator = "!="
class JNotEqualLong(JNotEqual): pass

class JStrictEqual(JCompareX): operator = "==="
class JStrictEqualLong(JStrictEqual): pass
class JStrictNotEqual(JCompareX): operator = "!=="
class JStrictNotEqualLong(JStrictNotEqual): pass

# Less
# ----
class JLess(JCompareX): operator = "<"
class JLessLong(JLess): pass
class JLessN(JLess): pass
class JLessNLong(JLess): pass

class JLessEqual(JCompareX): operator = "<="
class JLessEqualLong(JLessEqual): pass
class JLessEqualN(JLessEqual): pass

class JNotLess(JCompareX): operator = ">="
class JNotLessLong(JNotLess): pass
class JNotLessN(JNotLess): pass
class JNotLessNLong(JNotLess): pass

class JNotLessEqual(JCompareX): operator = ">"
class JNotLessEqualLong(JNotLessEqual): pass
class JNotLessEqualN(JNotLessEqual): pass
class JNotLessEqualNLong(JNotLessEqual): pass

# Greater
# -------
class JGreater(JCompareX): operator = ">"
class JGreaterLong(JGreater): pass
class JGreaterN(JGreater): pass
class JGreaterNLong(JGreater): pass

class JGreaterEqual(JCompareX): operator = ">="
class JGreaterEqualLong(JGreaterEqual): pass
class JGreaterEqualN(JGreaterEqual): pass
class JGreaterEqualNLong(JGreaterEqual): pass

class JNotGreater(JCompareX):  operator = "<="
class JNotGreaterLong(JNotGreater): pass
class JNotGreaterN(JNotGreater): pass
class JNotGreaterNLong(JNotGreater): pass

class JNotGreaterEqual(JCompareX): operator = "<"
class JNotGreaterEqualLong(JNotGreaterEqual): pass
class JNotGreaterEqualN(JNotGreaterEqual): pass
class JNotGreaterEqualNLong(JNotGreaterEqual): pass
# @formatter:on
