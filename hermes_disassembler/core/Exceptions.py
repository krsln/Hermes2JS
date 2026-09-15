"""
Exception hierarchy for hermes_disassembler.

Mirrors `hermes_decompiler.core.Exceptions`'s rationale: a malformed or
unsupported bytecode file should raise a specific, catchable error - not
a bare `struct.error` or `IndexError` that's indistinguishable from a
programming bug in this package.
"""


class HermesBytecodeError(Exception):
    """Base class for all recoverable hermes_disassembler errors."""


class InvalidMagicError(HermesBytecodeError):
    """The file does not start with the Hermes bytecode magic number."""

    def __init__(self, found: int, expected: int):
        self.found = found
        self.expected = expected
        super().__init__(
            f"Not a Hermes bytecode file: magic {found:#x} != expected {expected:#x}"
        )


class TruncatedFileError(HermesBytecodeError):
    """The file is shorter than a structure being read requires."""

    def __init__(self, what: str, needed: int, available: int):
        self.what = what
        self.needed = needed
        self.available = available
        super().__init__(
            f"Truncated file while reading {what}: needed {needed} bytes, "
            f"only {available} available"
        )


class UnsupportedBytecodeVersionError(HermesBytecodeError):
    """The file's bytecode version has no known layout in this package yet."""

    def __init__(self, version: int, known_versions: tuple[int, ...]):
        self.version = version
        self.known_versions = known_versions
        super().__init__(
            f"Bytecode version {version} is not supported yet "
            f"(known: {', '.join(map(str, known_versions))}). "
            f"See tools/hermes/versions.json and hermes_disassembler/format/."
        )
