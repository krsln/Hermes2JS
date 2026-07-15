from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class IteratorBegin(OpcodeHandler):
    """Begin iteration over an iterable."""

    _PATTERN = sequence(REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        iterator_reg, iterable_reg = map(int, match.groups())

        iterable = self.GetValueByReg(
            analysis.results,
            iterable_reg
        ) or f"r{iterable_reg}"

        variable = JSVariable(
            handler,
            entry.address,
            f"r{iterator_reg}",
            f"GetIterator({iterable})"
        )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class IteratorNext(OpcodeHandler):
    """Advance iterator."""

    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        result_reg, iterator_reg, _ = map(int, match.groups())

        iterator = self.GetValueByReg(
            analysis.results,
            iterator_reg
        ) or f"r{iterator_reg}"

        variable = JSVariable(
            handler,
            entry.address,
            f"r{result_reg}",
            f"{iterator}.next()"
        )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class IteratorClose(OpcodeHandler):
    """Close iterator."""

    _PATTERN = sequence(REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        iterator_reg = int(match.group(1))

        iterator = self.GetValueByReg(
            analysis.results,
            iterator_reg
        ) or f"r{iterator_reg}"

        variable = JSVariable(
            handler,
            entry.address,
            "",
            f"{iterator}.return()"
        )

        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

# CFG (control-flow graph) analizinde
# IteratorBegin
# IteratorNext
# JmpTrue
# IteratorClose
#
# kalıbını yakalayıp
#
# for (const item of iterable)
