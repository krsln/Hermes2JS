from __future__ import annotations

from enum import StrEnum
from typing import Final

__all__ = [
    "VariableKind",
    "LogicalOperator",
    "AssignmentOperator",
    "UpdateOperator",
    "UnaryOperator",
    "BinaryOperator",
    "precedence",
    "is_commutative",
    "is_associative",
]


# ============================================================================
# Variable Declaration
# ============================================================================


class VariableKind(StrEnum):
    """Represents a JavaScript variable declaration kind."""

    VAR = "var"
    LET = "let"
    CONST = "const"


# ============================================================================
# Operators
# ============================================================================


class LogicalOperator(StrEnum):
    """Logical operators."""

    AND = "&&"
    OR = "||"
    NULLISH = "??"


class AssignmentOperator(StrEnum):
    """Assignment operators."""

    ASSIGN = "="

    ADD_ASSIGN = "+="
    SUBTRACT_ASSIGN = "-="
    MULTIPLY_ASSIGN = "*="
    DIVIDE_ASSIGN = "/="
    MODULO_ASSIGN = "%="

    BITWISE_AND_ASSIGN = "&="
    BITWISE_OR_ASSIGN = "|="
    BITWISE_XOR_ASSIGN = "^="

    LEFT_SHIFT_ASSIGN = "<<="
    RIGHT_SHIFT_ASSIGN = ">>="
    UNSIGNED_RIGHT_SHIFT_ASSIGN = ">>>="

    LOGICAL_AND_ASSIGN = "&&="
    LOGICAL_OR_ASSIGN = "||="
    NULLISH_ASSIGN = "??="


class UpdateOperator(StrEnum):
    """Update operators."""

    INCREMENT = "++"
    DECREMENT = "--"


class UnaryOperator(StrEnum):
    """Unary operators."""

    PLUS = "+"
    MINUS = "-"

    LOGICAL_NOT = "!"
    BITWISE_NOT = "~"

    # TODO: remove space suffix later
    TYPEOF = "typeof "
    VOID = "void "
    DELETE = "delete "


class BinaryOperator(StrEnum):
    """Binary operators."""

    # Arithmetic
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MODULO = "%"
    EXPONENT = "**"

    # Bitwise
    BITWISE_AND = "&"
    BITWISE_OR = "|"
    BITWISE_XOR = "^"

    # Shift
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"
    UNSIGNED_RIGHT_SHIFT = ">>>"

    # Comparison
    LESS_THAN = "<"
    LESS_EQUAL = "<="
    GREATER_THAN = ">"
    GREATER_EQUAL = ">="

    EQUAL = "=="
    NOT_EQUAL = "!="
    STRICT_EQUAL = "==="
    STRICT_NOT_EQUAL = "!=="

    # Others
    INSTANCEOF = "instanceof"
    IN = "in"


# ============================================================================
# Precedence
# ============================================================================


_BINARY_PRECEDENCE: Final[dict[BinaryOperator, int]] = {
    BinaryOperator.EXPONENT: 15,

    BinaryOperator.MULTIPLY: 14,
    BinaryOperator.DIVIDE: 14,
    BinaryOperator.MODULO: 14,

    BinaryOperator.ADD: 13,
    BinaryOperator.SUBTRACT: 13,

    BinaryOperator.LEFT_SHIFT: 12,
    BinaryOperator.RIGHT_SHIFT: 12,
    BinaryOperator.UNSIGNED_RIGHT_SHIFT: 12,

    BinaryOperator.LESS_THAN: 11,
    BinaryOperator.LESS_EQUAL: 11,
    BinaryOperator.GREATER_THAN: 11,
    BinaryOperator.GREATER_EQUAL: 11,
    BinaryOperator.INSTANCEOF: 11,
    BinaryOperator.IN: 11,

    BinaryOperator.EQUAL: 10,
    BinaryOperator.NOT_EQUAL: 10,
    BinaryOperator.STRICT_EQUAL: 10,
    BinaryOperator.STRICT_NOT_EQUAL: 10,
}

_LOGICAL_PRECEDENCE: Final[dict[LogicalOperator, int]] = {
    LogicalOperator.AND: 6,
    LogicalOperator.OR: 5,
    LogicalOperator.NULLISH: 5,
}

_ASSIGNMENT_PRECEDENCE: Final[dict[AssignmentOperator, int]] = {
    operator: 3
    for operator in AssignmentOperator
}


def precedence(
    operator: BinaryOperator | LogicalOperator | AssignmentOperator,
) -> int:
    """Returns the JavaScript operator precedence."""

    if isinstance(operator, BinaryOperator):
        return _BINARY_PRECEDENCE[operator]

    if isinstance(operator, LogicalOperator):
        return _LOGICAL_PRECEDENCE[operator]

    return _ASSIGNMENT_PRECEDENCE[operator]


# ============================================================================
# Operator Properties
# ============================================================================


_COMMUTATIVE: Final[frozenset[BinaryOperator]] = frozenset({
    BinaryOperator.ADD,
    BinaryOperator.MULTIPLY,
    BinaryOperator.BITWISE_AND,
    BinaryOperator.BITWISE_OR,
    BinaryOperator.BITWISE_XOR,
    BinaryOperator.EQUAL,
    BinaryOperator.NOT_EQUAL,
    BinaryOperator.STRICT_EQUAL,
    BinaryOperator.STRICT_NOT_EQUAL,
})


_ASSOCIATIVE: Final[frozenset[BinaryOperator]] = frozenset({
    BinaryOperator.ADD,
    BinaryOperator.MULTIPLY,
    BinaryOperator.BITWISE_AND,
    BinaryOperator.BITWISE_OR,
    BinaryOperator.BITWISE_XOR,
})


def is_commutative(operator: BinaryOperator) -> bool:
    """Returns whether the operator is commutative."""

    return operator in _COMMUTATIVE


def is_associative(operator: BinaryOperator) -> bool:
    """Returns whether the operator is associative."""

    return operator in _ASSOCIATIVE