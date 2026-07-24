from enum import Enum


class UnaryOperator(Enum):
    PLUS = "+"
    NEGATE = "-"
    NOT = "!"
    BIT_NOT = "~"

    TYPEOF = "typeof "
    VOID = "void "
    DELETE = "delete "


class BinaryOperator(Enum):
    # Arithmetic
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    MOD = "%"

    # Comparison
    EQ = "=="
    STRICT_EQ = "==="
    NOT_EQ = "!="
    STRICT_NOT_EQ = "!=="

    LT = "<"
    LTE = "<="
    GT = ">"
    GTE = ">="

    # Logical
    AND = "&&"
    OR = "||"

    # Bitwise
    BIT_AND = "&"
    BIT_OR = "|"
    BIT_XOR = "^"

    # Shifts
    SHL = "<<"
    SHR = ">>"
    USHR = ">>>"

    # Others
    INSTANCEOF = "instanceof"
    IN = "in"
