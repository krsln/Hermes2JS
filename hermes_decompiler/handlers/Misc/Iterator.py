from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


class IteratorBegin(OpcodeHandler):
    """Begin iteration over an iterable."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        iterator_reg, iterable_reg = map(int, match.groups())

        iterable = self.get_register_value(analysis, iterable_reg) or f"r{iterable_reg}"

        variable = JSVariable(
            handler,
            entry.address,
            f"r{iterator_reg}",
            f"GetIterator({iterable})"
        )

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class IteratorNext(OpcodeHandler):
    """Advance iterator."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        result_reg, iterator_reg, _ = map(int, match.groups())

        iterator = self.get_register_value(analysis, iterator_reg) or f"r{iterator_reg}"

        variable = JSVariable(handler, entry.address, f"r{result_reg}", f"{iterator}.next()")

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class IteratorClose(OpcodeHandler):
    """Close iterator."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        iterator_reg = int(match.group(1))

        iterator = self.get_register_value(
            analysis,
            iterator_reg
        ) or f"r{iterator_reg}"

        variable = JSVariable(handler, entry.address, "", f"{iterator}.return()")

        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# CFG (control-flow graph) ->
# IteratorBegin
# IteratorNext
# JmpTrue
# IteratorClose
#
# to
#
# for (const item of iterable)


# ⚠️ VERIFICATION NEEDED: the operand counts/order below are reconstructed
# from general knowledge of how Hermes lowers `for...in` loops (build a
# property-name list, then repeatedly pull the next name until `undefined`),
# not from a confirmed real disassembly sample the way most other handlers
# in this codebase were written. Before relying on this, grep a real `.hbc`
# dump for `<GetPNameList>` / `<GetNextPName>` and confirm the argument
# shape matches `_PATTERN` below; adjust if it doesn't.


# /// Begin a for-in enumeration: build the list of enumerable property
# /// names for Arg2, using Arg3/Arg4 as scratch iteration state (index,
# /// size) that the paired GetNextPName instructions consume.
# DEFINE_OPCODE_4(GetPNameList, Reg8, Reg8, Reg8, Reg8)
class GetPNameList(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected four Reg8 arguments")

        dest_reg, obj_reg, _index_reg, _size_reg = map(int, match.groups())
        obj_val = self.get_register_value(analysis, obj_reg) or f"r{obj_reg}"

        variable = JSVariable(
            handler, entry.address, f"r{dest_reg}",
            f"Object.keys({obj_val}) /* for-in property list */", )
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# DEFINE_OPCODE_5(GetNextPName, Reg8, Reg8, Reg8, Reg8, Reg8)
class GetNextPName(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected five Reg8 arguments")

        dest_reg, list_reg, _obj_reg, _index_reg, _size_reg = map(int, match.groups())
        list_val = self.get_register_value(analysis, list_reg) or f"r{list_reg}"

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"{list_val}.next() /* for-in step */")
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
