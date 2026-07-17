"""
Exception hierarchy for hermes_decompiler.

Rationale: bare `except Exception` in the old code meant a genuine bug
(e.g., an IndexError from a programming mistake) was indistinguishable
from an expected parsing failure (e.g., hermes-dis emitted an unfamiliar
line format). These types let callers decide, per-exception-type, whether
to log-and-continue or fail fast.
"""


class HbcDecompilerError(Exception):
    """Base class for all recoverable decompiler errors."""


class MetadataParseError(HbcDecompilerError):
    """The .hbc metadata header line could not be parsed."""


# class LineParseError(HbcDecompilerError):
#     """A single bytecode listing line did not match the expected grammar."""
#
#     def __init__(self, line: str, reason: str = ""):
#         self.line = line
#         self.reason = reason
#         super().__init__(f"Could not parse line: {line!r} ({reason})" if reason else f"Could not parse line: {line!r}")


class OpcodeDispatchError(HbcDecompilerError):
    """A registered handler raised while processing an opcode."""

    def __init__(self, opcode: str, entry_bytecode: str, cause: BaseException):
        self.opcode = opcode
        self.entry_bytecode = entry_bytecode
        self.cause = cause
        super().__init__(f"Opcode '{opcode}' handler failed on {entry_bytecode!r}: {cause}")


class NoHandlerError(HbcDecompilerError):
    """No OpcodeHandler is registered for the given opcode."""

    def __init__(self, opcode: str):
        self.opcode = opcode
        super().__init__(f"No handler registered for opcode '{opcode}'")


class AnalysisContextError(HbcDecompilerError):
    """Dispatch was attempted without a valid HermesAnalysis context."""


# class CodeGenerationError(HbcDecompilerError):
#     """JS code generation (HermesAnalysis.GenerateJS) failed unexpectedly."""
