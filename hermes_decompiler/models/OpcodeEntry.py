import re
from dataclasses import dataclass

from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)

_TARGET_ADDRESS_RE = re.compile(r"Address:\s*([0-9A-Fa-f]+)")
_FUNCTION_RE = re.compile(
    r'Function:\s*\[#(\d+)\s+"?([^"]*)"?\s+of\s+(\d+)\s+bytes]'
    r'(?:\s*:\s*(\d+)\s+params)?'
    r'(?:\s*@\s*offset\s*(0x[0-9A-Fa-f]+))?'
)
_IDENTIFIER_RE = re.compile(
    r"String:\s*'([^']*)'\s*\(Identifier\)"
)

_STRING_RE = re.compile(
    r"String:\s*'([^']*)'\s*\(String\)"
)
# ==> 0000007d: <CreateRegExp>: <Reg8: 2, string_id: 7509, string_id: 11399, UInt32: 199>  # String: '\\(eval code' (String)  # String: 'g' (Identifier)
_REGEX_STRINGS_RE = re.compile(r"String:\s*'([^']*)'")


@dataclass(slots=True)
class FunctionReference:
    id: int
    name: str
    byte_size: int
    param_count: int | None = None
    offset: str | None = None


class OpcodeEntry:
    """Represents a single opcode entry in Hermes bytecode, including its bytecode, address, and metadata."""
    bytecode: str
    comment: str = ""
    offset: str = ""
    address: int = 0  # instruction offset
    opcode: str = ""
    args: str = ""

    target_address: int | None = None
    identifier_name: str | None = None
    string_literal: str | None = None
    function: FunctionReference | None = None

    def __init__(self, bytecode: str, hex_address: str, comment: str = "", opcode: str = "", args: str = ""):
        self.bytecode = bytecode
        self.offset = hex_address
        self.address = self._safe_parse_address(hex_address)
        self.comment = comment
        self.opcode = opcode
        self.args = args
        self._parse_comment()

    def _parse_comment(self):

        if not self.comment:
            return

        if match := _TARGET_ADDRESS_RE.search(self.comment):
            self.target_address = int(match.group(1), 16)

        if match := _IDENTIFIER_RE.search(self.comment):
            self.identifier_name = match.group(1)

        if match := _STRING_RE.search(self.comment):
            self.string_literal = match.group(1)

        if match := _FUNCTION_RE.search(self.comment):
            self.function = FunctionReference(
                id=int(match.group(1)),
                name=match.group(2),
                byte_size=int(match.group(3)),
                param_count=int(match.group(4)) if match.group(4) else None,
                offset=match.group(5),
            )

    def resolve_pattern_and_flags(self) -> tuple[str | None, str | None]:
        matches = _REGEX_STRINGS_RE.findall(self.comment)

        if len(matches) >= 2:
            return matches[0], matches[1]

        return None, None

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
