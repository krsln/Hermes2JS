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


class CodeGenerationError(HbcDecompilerError):
    """The code-generation stage (CodeGenerationStage) failed for this section."""

    def __init__(self, section_index: int, cause: BaseException):
        self.section_index = section_index
        self.cause = cause
        super().__init__(f"Code generation failed for section {section_index}: {cause}")
