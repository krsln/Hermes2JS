import re
import json

from hermes_decompiler.ir.Expressions import CallExpression, MemberExpression, ComputedMemberExpression
from hermes_decompiler.ir.Values import ObjectLiteralValue, IdentifierValue
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT16, sequence


# DEFINE_OPCODE_5(NewObjectWithBuffer, Reg8, UInt16, UInt16, UInt16, UInt16)
# Example: < NewObjectWithBuffer >: < Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182 >  # Object: {'message': 'You have joined the list', 'type': 'success'}
class NewObjectWithBuffer(OpcodeHandler):
    """Create an object from a static map of values using buffer."""
    _PATTERN = sequence(REG, UINT16, UINT16, UINT16, UINT16)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        object_value = self._parse_object_from_comment(entry.comment)

        if not object_value:
            error = f'// Warning: No valid object parsed from comment: {entry.comment}'
            return self.build_exception_result(analysis, entry, error)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', object_value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _parse_object_from_comment(comment: str) -> ObjectLiteralValue:
        """Extract and parse Object: {...} from opcode comment."""
        if not comment:
            return ObjectLiteralValue({})

        object_matches = re.findall(r"Object:\s*(\{[^}]+})", comment)
        for obj_str in object_matches:
            try:
                # Clean and convert to valid JSON
                clean_str = obj_str.replace("'", '"').rstrip(",").strip()
                return json.loads(clean_str)
            except json.JSONDecodeError:
                continue  # try next match
        return ObjectLiteralValue({})


class NewObjectWithBufferLong(NewObjectWithBuffer):
    """Long variant."""
    pass


class NewObject(OpcodeHandler):
    """Create a new empty object: {}"""
    _PATTERN = sequence(REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', ObjectLiteralValue({}))
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


# Example: <NewObjectWithParent>: <Reg8: 1, Reg8: 14>
class NewObjectWithParent(OpcodeHandler):
    """Create a new object with the specified prototype."""

    _PATTERN = sequence(REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, parent_reg = map(int, match.groups())

        parent = self.get_register_value(analysis, parent_reg) or f"r{parent_reg}"

        value = CallExpression(
            callee=MemberExpression(
                IdentifierValue("Object"),
                IdentifierValue("create"),
            ),
            arguments=[parent],
        )
        variable = JSVariable(handler, entry.address, f"r{dest_reg}", value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)


class SelectObject(OpcodeHandler):
    """Select a property by dynamic key: obj[key]"""
    _PATTERN = sequence(REG, REG, REG)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        obj = self.get_register_value(analysis, obj_reg)
        selector = self.get_register_value(analysis, selector_reg)

        value = ComputedMemberExpression(
            object=obj,
            property=selector,
        )

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', value)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
