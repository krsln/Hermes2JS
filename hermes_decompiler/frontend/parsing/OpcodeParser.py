import re

from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.core.Exceptions import OpcodeConstructionError
from hermes_decompiler.core.logging import get_logger

__all__ = ["OpcodeParser"]

logger = get_logger(__name__)


class OpcodeParser:
    """Parses Hermes bytecode listing lines into OpcodeEntry instances."""

    _LINE_RE = re.compile(
        r"^==>\s*([0-9a-fA-F]+):\s*<(\w+)>:\s*<([^>]*)>"
    )
    _COMMENT_RE = re.compile(r"\s*#\s*(.*)")

    @classmethod
    def parse(cls, line: str) -> OpcodeEntry | None:
        """
        Parse one bytecode-listing line into an OpcodeEntry.

        Returns None (not an exception) when the line simply doesn't match the
        opcode grammar - that's an expected, common case (blank lines, section
        headers, etc.), not an error.

        Raises OpcodeConstructionError if the grammar matched but building the
        OpcodeEntry from the matched groups failed - that's not an expected
        input variation, it's a bug in this parser, and swallowing it would
        make it indistinguishable from a plain non-opcode line. Callers decide
        whether to log-and-continue or let it propagate.
        """
        stripped = line.strip()
        match = cls._LINE_RE.match(stripped)
        if not match:
            return None

        try:
            comment_match = cls._COMMENT_RE.search(stripped)
            comment = comment_match.group(1) if comment_match else ""

            hex_address, opcode, args = match.groups()
            return OpcodeEntry(bytecode=line, hex_address=hex_address, opcode=opcode, args=args, comment=comment)
        except Exception as e:
            raise OpcodeConstructionError(line, e) from e
