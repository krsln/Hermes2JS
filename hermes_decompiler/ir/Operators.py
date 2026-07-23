from enum import Enum


class UnaryOperator(Enum):
    NEGATE = "-"
    NOT = "!"
    BIT_NOT = "~"

    TYPEOF = "typeof "
    VOID = "void "


class BinaryOperator(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    MOD = "%"

    EQ = "=="
    STRICT_EQ = "==="

    NOT_EQ = "!="
    STRICT_NOT_EQ = "!=="

    LT = "<"
    LTE = "<="
    GT = ">"
    GTE = ">="

    AND = "&&"
    OR = "||"

    BIT_AND = "&"
    BIT_OR = "|"
    BIT_XOR = "^"

    SHL = "<<"
    SHR = ">>"
    USHR = ">>>"

    INSTANCEOF = "instanceof"
    IN = "in"
