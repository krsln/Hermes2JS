from hermes_decompiler.ir import CallExpression, Identifier, MemberExpression
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
        iterable = self.get_register_value(analysis, iterable_reg)

        # Named pseudo-call, same convention as getEnvironment()/
        # HermesPropertyIterator() elsewhere - GetIterator() is not
        # real JS syntax but a VM-level operation.
        value = CallExpression(callee=Identifier(name="GetIterator"), arguments=(iterable,))

        variable = JSVariable(handler, entry.address, f"r{iterator_reg}", value)
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
        iterator = self.get_register_value(analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="next"))
        value = CallExpression(callee=callee, arguments=())

        variable = JSVariable(handler, entry.address, f"r{result_reg}", value)
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
        iterator = self.get_register_value(analysis, iterator_reg)

        callee = MemberExpression(iterator, Identifier(name="return"))
        value = CallExpression(callee=callee, arguments=())

        variable = JSVariable(handler, entry.address, "", value)
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


# DEFINE_OPCODE_4(GetPNameList, Reg8, Reg8, Reg8, Reg8)
class GetPNameList(OpcodeHandler):
    _PATTERN = sequence(REG, REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected four Reg8 arguments")

        dest_reg, obj_reg, _index_reg, _size_reg = map(int, match.groups())
        obj = self.get_register_value(analysis, obj_reg)

        value = CallExpression(callee=Identifier(name="HermesPropertyIterator"), arguments=(obj,))

        # for-in property list
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
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
        list_val = self.get_register_value(analysis, list_reg)

        callee = MemberExpression(list_val, Identifier(name="next"))
        value = CallExpression(callee=callee, arguments=())

        # for-in step
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)