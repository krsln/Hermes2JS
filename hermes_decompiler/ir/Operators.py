from enum import StrEnum
from typing import Final


class VariableKind(StrEnum):
    VAR = "var"
    LET = "let"
    CONST = "const"


class LogicalOperator(StrEnum):
    AND = "&&"
    OR = "||"
    NULLISH = "??"


class AssignmentOperator(StrEnum):
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
    INCREMENT = "++"
    DECREMENT = "--"


class UnaryOperator(StrEnum):
    PLUS = "+"
    MINUS = "-"

    LOGICAL_NOT = "!"
    BITWISE_NOT = "~"

    TYPEOF = "typeof "
    VOID = "void "
    DELETE = "delete "
    # TYPEOF = "typeof"
    # VOID = "void"
    # DELETE = "delete"


class BinaryOperator(StrEnum):
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

    # Shifts
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


_OPERATOR_PRECEDENCE = {
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


_BINARY_PRECEDENCE: Final[dict[BinaryOperator, int]] = {...}

_LOGICAL_PRECEDENCE: Final[dict[LogicalOperator, int]] = {...}

_ASSIGNMENT_PRECEDENCE: Final[dict[AssignmentOperator, int]] = {...}

def precedence(operator: BinaryOperator | LogicalOperator | AssignmentOperator) -> int:
    ...


def is_commutative(operator: BinaryOperator) -> bool:
    ...


def is_associative(operator: BinaryOperator) -> bool:
    ...
