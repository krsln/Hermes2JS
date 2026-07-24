from enum import Enum, StrEnum


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


class UpdateOperator(StrEnum):
    INCREMENT = "++"
    DECREMENT = "--"


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
