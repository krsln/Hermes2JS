import re

from hermes_decompiler.Logger import logger
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

_UNARY_REG_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')
_BINARY_REG_PATTERN = re.compile(r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+)$')
_CREATE_REGEXP_PATTERN = re.compile(
    r'^Reg\d+:\s*(\d+),\s*UInt32:\s*(\d+),\s*UInt32:\s*(\d+),\s*UInt32:\s*(\d+)$'
)
# Disassembler comments annotate string operands as: String: 'pattern' (...)
# CreateRegExp typically carries two such annotations (pattern, then flags).
_STRING_COMMENT_PATTERN = re.compile(r"String:\s*'([^']*)'")
_PUT_GETTER_SETTER_PATTERN = re.compile(
    r'^Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*Reg\d+:\s*(\d+),\s*UInt8:\s*(\d+)$'
)


# /// Arg1 = typeof Arg2.
# DEFINE_OPCODE_2(TypeOf, Reg8, Reg8)
# Example: <TypeOf>: <Reg8: 1, Reg8: 0>
class TypeOf(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _UNARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected two Reg8 arguments")

        dest_reg, src_reg = (int(x) for x in match.groups())
        src_val = self.GetValueByReg(analysis.results, src_reg) or f"r{src_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"typeof {src_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = (Arg2 instanceof Arg3).
# DEFINE_OPCODE_3(InstanceOf, Reg8, Reg8, Reg8)
# Example: <InstanceOf>: <Reg8: 2, Reg8: 0, Reg8: 1>
class InstanceOf(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, lhs_reg, rhs_reg = (int(x) for x in match.groups())
        lhs_val = self.GetValueByReg(analysis.results, lhs_reg) or f"r{lhs_reg}"
        rhs_val = self.GetValueByReg(analysis.results, rhs_reg) or f"r{rhs_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"{lhs_val} instanceof {rhs_val}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Arg1 = delete Arg2[Arg3].
# DEFINE_OPCODE_3(DelByVal, Reg8, Reg8, Reg8)
# Example: <DelByVal>: <Reg8: 2, Reg8: 0, Reg8: 1>
class DelByVal(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _BINARY_REG_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest_reg, obj_reg, prop_reg = (int(x) for x in match.groups())
        obj_val = self.GetValueByReg(analysis.results, obj_reg) or f"r{obj_reg}"
        prop_val = self.GetValueByReg(analysis.results, prop_reg) or f"r{prop_reg}"

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', f"delete {obj_val}[{prop_val}]")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


# /// Create a RegExp literal.
# /// Arg1 is the destination.
# /// Arg2 is the string_id of the pattern.
# /// Arg3 is the string_id of the flags.
# /// Arg4 is an index into the regexp bytecode table (compiled matcher; not
# ///      needed to reconstruct the source-level literal).
# DEFINE_OPCODE_4(CreateRegExp, Reg8, UInt32, UInt32, UInt32)
# Example: <CreateRegExp>: <Reg8: 0, UInt32: 12, UInt32: 13, UInt32: 0>  # String: '^\d+$'  String: 'g'
class CreateRegExp(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _CREATE_REGEXP_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected Reg8 and three UInt32 arguments")

        dest_reg, pattern_id, flags_id = (int(match.group(i)) for i in (1, 2, 3))

        pattern, flags = self._resolve_pattern_and_flags(analysis, entry, pattern_id, flags_id)
        if pattern is None:
            error = f'/* Error: could not resolve RegExp pattern (string_id {pattern_id}) */ undefined'
            return self.Exception(analysis, entry, error)

        js_regex = f"/{pattern}/{flags or ''}"
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_regex)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _resolve_pattern_and_flags(analysis, entry, pattern_id: int, flags_id: int):
        """
        Prefer the disassembler's own `String: '...'` comment annotations
        (present on real Hermes dumps for CreateRegExp), falling back to a
        stringTable lookup by id. Returns (pattern, flags), with either
        element possibly None if it could not be resolved.
        """
        comment_matches = _STRING_COMMENT_PATTERN.findall(entry.comment or "")
        if len(comment_matches) >= 2:
            return comment_matches[0], comment_matches[1]

        pattern = analysis.stringTable.get(str(pattern_id))
        flags = analysis.stringTable.get(str(flags_id))
        if pattern is None:
            logger.warning(
                f"CreateRegExp at address {entry.address}: unresolved pattern string_id {pattern_id}"
            )
        return pattern, flags


# /// Define an accessor (getter/setter) own property with a computed key.
# /// Arg1[Arg2] = { get: Arg3, set: Arg4, enumerable: Arg5, configurable: true }
# /// Arg5 (UInt8, 0 or 1) mirrors the `enumerable` flag recorded by the
# /// Hermes compiler for the property descriptor.
# DEFINE_OPCODE_5(PutOwnGetterSetterByVal, Reg8, Reg8, Reg8, Reg8, UInt8)
# Example: <PutOwnGetterSetterByVal>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 3, UInt8: 1>
class PutOwnGetterSetterByVal(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = _PUT_GETTER_SETTER_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(
                analysis, entry,
                "Expected four Reg8 arguments followed by a UInt8 enumerable flag",
            )

        obj_reg, key_reg, getter_reg, setter_reg, enumerable_flag = (int(x) for x in match.groups())

        obj_val = self.GetValueByReg(analysis.results, obj_reg) or f"r{obj_reg}"
        key_val = self.GetValueByReg(analysis.results, key_reg) or f"r{key_reg}"
        getter_val = self.GetValueByReg(analysis.results, getter_reg)
        setter_val = self.GetValueByReg(analysis.results, setter_reg)
        enumerable = "true" if int(enumerable_flag) != 0 else "false"

        descriptor_parts = []
        # A missing getter/setter register is legal (only one accessor may be
        # defined at a time); omit the corresponding descriptor entry rather
        # than emitting a misleading `undefined` accessor.
        if getter_val is not None:
            descriptor_parts.append(f"get: {getter_val}")
        if setter_val is not None:
            descriptor_parts.append(f"set: {setter_val}")
        descriptor_parts.append(f"enumerable: {enumerable}")
        descriptor_parts.append("configurable: true")

        descriptor = "{ " + ", ".join(descriptor_parts) + " }"
        value = f"Object.defineProperty({obj_val}, {key_val}, {descriptor})"

        variable = JSVariable(handler, entry.address, f'r{obj_reg}', value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)