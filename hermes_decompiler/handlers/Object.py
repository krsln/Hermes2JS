import re
import json
from typing import Any, Dict

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from ._shared_patterns import REG, UINT16, sequence

# Pre-compiled patterns
NEW_OBJECT_WITH_BUFFER_PATTERN = sequence(REG, UINT16, UINT16, UINT16, UINT16)
NEW_OBJECT_PATTERN = sequence(REG)
NEW_ARRAY_WITH_BUFFER_PATTERN = sequence(REG, UINT16, UINT16, UINT16)
SELECT_PATTERN = sequence(REG, REG, REG)


# Create an object from a static map of values, as for var={'a': 3}.
# Any non-constant elements can be set afterwards with PutOwnByInd.
# Arg1 is the destination.
# Arg2 is a preallocation size hint.
# Arg3 is the number of static elements.
# Arg4 is the index in the object key buffer table.
# Arg5 is the index in the object val buffer table.
# DEFINE_OPCODE_5(NewObjectWithBuffer, Reg8, UInt16, UInt16, UInt16, UInt16)
# Example: < NewObjectWithBuffer >: < Reg8: 2, UInt16: 2, UInt16: 2, UInt16: 4743, UInt16: 24182 >  # Object: {'message': 'You have joined the list', 'type': 'success'}
class NewObjectWithBuffer(OpcodeHandler):
    """Create an object from a static map of values using buffer."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = NEW_OBJECT_WITH_BUFFER_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        parsed_obj = self._parse_object_from_comment(entry.comment)

        if not parsed_obj:
            error = f'// Warning: No valid object parsed from comment: {entry.comment}'
            return self.Exception(analysis, entry, error)

        # Format as JS object literal
        js_obj = self._format_object_literal(parsed_obj)

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    def _parse_object_from_comment(self, comment: str) -> Dict[str, Any]:
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
    """Long variant - reuses same logic."""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        return super().Handle(analysis, entry)


class NewObject(OpcodeHandler):
    """Create a new empty object: {}"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = NEW_OBJECT_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg = int(match.group(1))

        variable = JSVariable(handler, entry.address, f'r{dest_reg}', "{}")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)


class SelectObject(OpcodeHandler):
    """Select a property by dynamic key: obj[key]"""

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = SELECT_PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, obj_reg, selector_reg = map(int, match.groups())

        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest_reg}',
            f"r{obj_reg}[r{selector_reg}]"
        )
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
