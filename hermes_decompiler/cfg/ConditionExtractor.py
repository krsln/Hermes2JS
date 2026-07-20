from hermes_decompiler.models.OpcodeResult import OpcodeResult


class ConditionExtractor:
    """
    Extracts high-level conditions from conditional jump instructions.

    This is intentionally isolated so support for additional Hermes
    jump opcodes can be added without affecting CFG reconstruction.
    """

    @staticmethod
    def extract(opcode: OpcodeResult) -> str:
        value = opcode.value.strip()

        if "if (" in value:
            return value.split("if (", 1)[1].split(")", 1)[0]

        return value