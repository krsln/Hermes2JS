import re
import json
from typing import Any, Dict

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

        parsed_obj = self._parse_object_from_comment(entry.comment)

        if not parsed_obj:
            error = f'// Warning: No valid object parsed from comment: {entry.comment}'
            return self.build_exception_result(analysis, entry, error)

        # Format as JS object literal
        js_obj = self._format_object_literal(parsed_obj)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _parse_object_from_comment(comment: str) -> Dict[str, Any]:
        """Extract and parse Object: {...} from opcode comment."""
        if not comment:
            return {}

        object_matches = re.findall(r"Object:\s*(\{[^}]+})", comment)
        for obj_str in object_matches:
            try:
                # Clean and convert to valid JSON
                clean_str = obj_str.replace("'", '"').rstrip(",").strip()
                return json.loads(clean_str)
            except json.JSONDecodeError:
                continue  # try next match
        return {}

    @staticmethod
    def _format_object_literal(obj: Dict[str, Any]) -> str:
        """Convert dict to JS object literal string."""
        if not obj:
            return "{}"

        parts = []
        for k, v in obj.items():
            # Handle different value types
            if isinstance(v, str):
                val_str = f'"{v}"'
            elif v is None:
                val_str = "null"
            elif isinstance(v, bool):
                val_str = "true" if v else "false"
            else:
                val_str = str(v)
            parts.append(f'{k}: {val_str}')

        return "{ " + ", ".join(parts) + " }"


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

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', "{}")
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

        variable = JSVariable(handler, entry.address, f"r{dest_reg}", f"Object.create({parent})")
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

        variable = JSVariable(
            handler, entry.address,
            f'r{dest_reg}', f"r{obj_reg}[r{selector_reg}]"
        )
        analysis.add_result(entry, variable)

        return OpcodeResult(entry, variable)
