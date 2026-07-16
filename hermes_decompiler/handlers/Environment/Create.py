from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, sequence

from .Base import EnvironmentAccess


class CreateEnvironment(EnvironmentAccess):
    """
    Allocate a new lexical environment.

    Hermes uses environment objects to store variables
    captured by nested closures.
    """

    _PATTERN = sequence(REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        variable = JSVariable(self.__class__.__name__, entry.address, f"r{dest_reg}", "createEnvironment()")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
