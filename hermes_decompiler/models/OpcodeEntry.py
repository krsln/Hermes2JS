from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)


class OpcodeEntry:
    """Represents a single opcode entry in Hermes bytecode, including its bytecode, address, and metadata."""
    bytecode: str
    comment: str = ""
    offset: str = ""
    address: int = 0  # instruction offset
    opcode: str = ""
    args: str = ""

    def __init__(self, bytecode: str, hex_address: str, comment: str = "", opcode: str = "", args: str = ""):
        self.bytecode = bytecode
        self.offset = hex_address
        self.address = self._safe_parse_address(hex_address)
        self.comment = comment
        self.opcode = opcode
        self.args = args

    @staticmethod
    def _safe_parse_address(hex_address: str) -> int:
        """
        Safely convert a hexadecimal address string to an integer.

        Returns 0 if the input is empty or invalid.
        """

        if not hex_address:
            return 0
        try:
            return int(hex_address, 16)
        except ValueError:
            logger.warning("Invalid hex address %r, defaulting to 0", hex_address)
            return 0

    def __str__(self):
        return (f"OpcodeEntry(bytecode='{self.bytecode}', offset={self.offset}, address={self.address}, "
                f"opcode='{self.opcode}', args='{self.args}', comment='{self.comment}')")

    def to_dict(self):
        """Converts the OpcodeEntry object to a dictionary for JSON serialization."""
        return {
            "bytecode": self.bytecode,
            "offset": self.offset,
            "address": self.address,
            "comment": self.comment,
            "opcode": self.opcode,
            "args": self.args
        }
