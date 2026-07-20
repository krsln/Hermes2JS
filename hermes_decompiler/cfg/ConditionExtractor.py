from hermes_decompiler.models.OpcodeResult import OpcodeResult


class ConditionExtractor:
    """
    Extracts high-level conditions from conditional jump instructions.
    """

    @classmethod
    def extract(cls, opcode: OpcodeResult) -> str:

        value = opcode.value.strip()

        if value.startswith("if ("):
            return value[4:value.rfind(")")]

        if value.startswith("if (!"):
            return value[5:value.rfind(")")]

        return value
