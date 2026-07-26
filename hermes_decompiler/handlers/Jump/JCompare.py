from __future__ import annotations

from typing import ClassVar, Tuple

from hermes_decompiler.handlers import OpcodeHandler, REG, ADDR, sequence
from hermes_decompiler.ir.Operators import BinaryOperator
from hermes_decompiler.ir.expressions import BinaryExpression
from hermes_decompiler.opcode import OpcodeEntry, OpcodeResult, ControlFlowType
from hermes_decompiler.analysis.regions import IfGotoStatement
from hermes_decompiler.runtime import HermesAnalysis


def _parse_compare(entry: OpcodeEntry) -> Tuple[int, int, int]:
    """
    Parse comparison jump arguments.

        Addr, Reg, Reg
    """

    _PATTERN = sequence(ADDR, REG, REG)
    match = _PATTERN.match(entry.args.strip())

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

    `operator` is a `BinaryOperator` enum member - the string names of
    the historical `JNotLess`/`JNotGreater`/... family already encode
    Hermes' inverted-jump semantics (e.g. `JNotLess` jumps when the
    values are NOT less, i.e. `>=`), which is preserved unchanged here;
    only the representation (string -> BinaryOperator) changed.
    """

    operator: ClassVar[BinaryOperator] = BinaryOperator.EQUAL

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        try:
            offset, lhs_reg, rhs_reg = _parse_compare(entry)
        except ValueError as exc:
            return self.build_invalid_args_result(analysis, entry, str(exc))

        target = entry.target_address
        if target is None:
            target = entry.address + offset

        analysis.gotoList.append(target)

        lhs = self.get_register_value(analysis, lhs_reg)
        rhs = self.get_register_value(analysis, rhs_reg)

        condition = BinaryExpression(left=lhs, operator=self.operator, right=rhs)
        statement = IfGotoStatement(condition=condition, target=target)
        flow = ControlFlowType.CONDITIONAL

        # pure control flow: no operand value of its own
        result = OpcodeResult(entry, value=None, statement=statement, dest_reg=None, goto=target, control_flow=flow)
        analysis.add_result(result)

        return result


# @formatter:off
# Equality
# ---------
class JEqual(JCompareX): operator = BinaryOperator.EQUAL
class JEqualLong(JEqual): pass
class JNotEqual(JCompareX): operator = BinaryOperator.NOT_EQUAL
class JNotEqualLong(JNotEqual): pass

class JStrictEqual(JCompareX): operator = BinaryOperator.STRICT_EQUAL
class JStrictEqualLong(JStrictEqual): pass
class JStrictNotEqual(JCompareX): operator = BinaryOperator.STRICT_NOT_EQUAL
class JStrictNotEqualLong(JStrictNotEqual): pass

# Less
# ----
class JLess(JCompareX): operator = BinaryOperator.LESS_THAN
class JLessLong(JLess): pass
class JLessN(JLess): pass
class JLessNLong(JLess): pass

class JLessEqual(JCompareX): operator = BinaryOperator.LESS_EQUAL
class JLessEqualLong(JLessEqual): pass
class JLessEqualN(JLessEqual): pass

class JNotLess(JCompareX): operator = BinaryOperator.GREATER_EQUAL
class JNotLessLong(JNotLess): pass
class JNotLessN(JNotLess): pass
class JNotLessNLong(JNotLess): pass

class JNotLessEqual(JCompareX): operator = BinaryOperator.GREATER_THAN
class JNotLessEqualLong(JNotLessEqual): pass
class JNotLessEqualN(JNotLessEqual): pass
class JNotLessEqualNLong(JNotLessEqual): pass

# Greater
# -------
class JGreater(JCompareX): operator = BinaryOperator.GREATER_THAN
class JGreaterLong(JGreater): pass
class JGreaterN(JGreater): pass
class JGreaterNLong(JGreater): pass

class JGreaterEqual(JCompareX): operator = BinaryOperator.GREATER_EQUAL
class JGreaterEqualLong(JGreaterEqual): pass
class JGreaterEqualN(JGreaterEqual): pass
class JGreaterEqualNLong(JGreaterEqual): pass

class JNotGreater(JCompareX):  operator = BinaryOperator.LESS_EQUAL
class JNotGreaterLong(JNotGreater): pass
class JNotGreaterN(JNotGreater): pass
class JNotGreaterNLong(JNotGreater): pass

class JNotGreaterEqual(JCompareX): operator = BinaryOperator.LESS_THAN
class JNotGreaterEqualLong(JNotGreaterEqual): pass
class JNotGreaterEqualN(JNotGreaterEqual): pass
class JNotGreaterEqualNLong(JNotGreaterEqual): pass
# @formatter:on