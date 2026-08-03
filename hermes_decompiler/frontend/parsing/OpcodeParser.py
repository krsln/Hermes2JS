import re

from hermes_decompiler.frontend.opcode import OpcodeEntry
from hermes_decompiler.core.logging import get_logger

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
        headers, etc.), not an error. Genuine parsing failures (regex matched
        but downstream construction blew up) are logged and also return None,
        matching prior behavior, but now via logger instead of print so callers
        can control verbosity/output destination.
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
            logger.warning("Failed to construct OpcodeEntry from line %r: %s", line, e)
            return None
