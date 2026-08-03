from hermes_decompiler.frontend.opcode import OpcodeEntry, OpcodeResult
from hermes_decompiler.handlers import OpcodeHandler, sequence, REG, UINT16
from hermes_decompiler.ir.Operators import AssignmentOperator
from hermes_decompiler.ir.expressions import (
    ArrayExpression,
    CallExpression,
    AssignmentExpression,
    Identifier,
    MemberExpression,
    SpreadElement,
)
from hermes_decompiler.runtime import HermesAnalysis


# FastArray is a React-Native/Hermes-specific typed array-storage
# optimization (`FastArray.h`/`FastArray.cpp`) distinct from a regular
# JS Array, but not observable as a different type from JS source - it's
# purely an engine-internal representation Hermes' compiler picks for
# arrays it can prove are dense/homogeneous enough. Operand roles below
# are verified against `lib/VM/Interpreter.cpp`
# (hermes-v260318099.0.1, CASE(NewFastArray)/CASE(FastArrayLength)/...),
# not guessed from the opcode name alone.


# Reg8, UInt16 (total size 3)
# DEFINE_OPCODE_2(NewFastArray, Reg8, UInt16)
# Arg1 = new FastArray(Arg2)  [Arg2 is a size hint, not a visible value]
class NewFastArray(OpcodeHandler):
    """Create a new FastArray. The UInt16 size hint has no JS-visible effect."""

    _PATTERN = sequence(REG, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected Reg8, UInt16")

        dest_reg, _size_hint = map(int, match.groups())

        result = OpcodeResult(entry, value=ArrayExpression(elements=()), dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(FastArrayLength, Reg8, Reg8)
# Arg1 = Arg2.length
class FastArrayLength(OpcodeHandler):
    """Get the length of a FastArray."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, array_reg = map(int, match.groups())

        array_value = self.get_register_expression(analysis, array_reg)
        expression = MemberExpression(receiver=array_value, member=Identifier(name="length"), computed=False)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(FastArrayLoad, Reg8, Reg8, Reg8)
# Arg1 = Arg2[Arg3]
class FastArrayLoad(OpcodeHandler):
    """Load an element from a FastArray by index."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, array_reg, index_reg = map(int, match.groups())

        array_value = self.get_register_expression(analysis, array_reg)
        index_value = self.get_register_expression(analysis, index_reg)
        expression = MemberExpression(receiver=array_value, member=index_value, computed=True)

        result = OpcodeResult(entry, value=expression, dest_reg=dest_reg)
        analysis.add_result(result)

        return result


# Reg8, Reg8, Reg8 (total size 3)
# DEFINE_OPCODE_3(FastArrayStore, Reg8, Reg8, Reg8)
# Arg1[Arg2] = Arg3  (NOTE: operand order differs from FastArrayLoad -
class FastArrayStore(OpcodeHandler):
    """Store a value into a FastArray by index."""

    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected three Reg8 arguments")

        array_reg, index_reg, value_reg = map(int, match.groups())

        array_value = self.get_register_expression(analysis, array_reg)
        index_value = self.get_register_expression(analysis, index_reg)
        right = self.get_register_expression(analysis, value_reg)

        left = MemberExpression(receiver=array_value, member=index_value, computed=True)
        expression = AssignmentExpression(left=left, operator=AssignmentOperator.ASSIGN, right=right)

        # No destination register: statement-only, same pattern as PutById.
        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(FastArrayPush, Reg8, Reg8)
# Arg1.push(Arg2)
class FastArrayPush(OpcodeHandler):
    """Push a single element onto the end of a FastArray."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        array_reg, value_reg = map(int, match.groups())

        array_value = self.get_register_expression(analysis, array_reg)
        value = self.get_register_expression(analysis, value_reg)

        callee = MemberExpression(receiver=array_value, member=Identifier(name="push"), computed=False)
        expression = CallExpression(callee=callee, arguments=(value,))

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result


# Reg8, Reg8 (total size 2)
# DEFINE_OPCODE_2(FastArrayAppend, Reg8, Reg8)
# Arg1.push(...Arg2)  (append all of Arg2's elements onto Arg1)
class FastArrayAppend(OpcodeHandler):
    """Append every element of one FastArray onto another."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry, "Expected two Reg8 arguments")

        dest_array_reg, src_array_reg = map(int, match.groups())

        dest_array = self.get_register_expression(analysis, dest_array_reg)
        src_array = self.get_register_expression(analysis, src_array_reg)

        callee = MemberExpression(receiver=dest_array, member=Identifier(name="push"), computed=False)
        expression = CallExpression(callee=callee, arguments=(SpreadElement(argument=src_array),))

        result = OpcodeResult(entry, value=expression, dest_reg=None)
        analysis.add_result(result)

        return result
