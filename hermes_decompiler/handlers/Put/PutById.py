import re
from typing import Dict, List, Tuple, Any

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, UINT8, STRING_ID, sequence


# DEFINE_OPCODE_4(PutById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(PutByIdLong, Reg8, Reg8, UInt8, UInt32)
# Example: <PutById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 12270>  # String: 'fetchMovieDetails' (Identifier)
class PutById(OpcodeHandler):
    """Set an object property by string index."""
    _PATTERN = sequence(REG, REG, UINT8, STRING_ID)

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(analysis, entry)

        dest_reg, value_reg, _cache, string_id = map(int, match.groups())

        prop_name = self.resolve_property_name(analysis, entry, string_id)
        reg_var = self.get_register_variable(analysis, value_reg)
        reg_value = reg_var.value if reg_var and reg_var.value is not None else 'undefined'

        obj = self.parse_existing_object(analysis, dest_reg)
        obj[prop_name] = reg_value

        js_obj = self._format_object_literal(obj)

        updated_var = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.add_result(entry, updated_var)

        return OpcodeResult(entry, updated_var)

    def parse_existing_object(self, analysis: HermesAnalysis, dest_reg: int) -> Dict[str, Any]:
        dest_var = self.get_register_variable(analysis, dest_reg)
        if not dest_var or dest_var.value in (None, '{}', ''):
            return {}

        obj_str = dest_var.value.strip()
        if not (obj_str.startswith('{') and obj_str.endswith('}')):
            return {}

        try:
            inner = obj_str[1:-1].strip()
            return dict(PutById._parse_object_pairs(inner)) if inner else {}
        except Exception as e:
            print(f"[WARNING] Failed to parse object in r{dest_reg}: {e}")
            return {}

    @staticmethod
    def _parse_object_pairs(obj_str: str) -> List[Tuple[str, str]]:
        pairs: List[Tuple[str, str]] = []
        if not obj_str:
            return pairs

        parts = []
        buffer = []
        in_quotes = in_template = False
        i = 0
        while i < len(obj_str):
            char = obj_str[i]
            if char in '"\'' and (i == 0 or obj_str[i - 1] != '\\'):
                in_quotes = not in_quotes
                buffer.append(char)
            elif char == '`' and (i == 0 or obj_str[i - 1] != '\\'):
                in_template = not in_template
                buffer.append(char)
            elif char == ',' and not in_quotes and not in_template:
                parts.append(''.join(buffer).strip())
                buffer = []
            else:
                buffer.append(char)
            i += 1
        if buffer:
            parts.append(''.join(buffer).strip())

        for part in parts:
            match = re.match(r'^\s*([a-zA-Z_$][a-zA-Z0-9_$]*|["`][^"`]*["`])\s*:\s*(.+?)\s*$', part)
            if match:
                key, value = match.groups()
                if key[0] in '"`':
                    key = key[1:-1]
                pairs.append((key, value))
        return pairs

    @staticmethod
    def _format_object_literal(obj: Dict[str, Any]) -> str:
        def is_valid_identifier(k: str) -> bool:
            return bool(re.match(r'^[a-zA-Z_$][a-zA-Z0-9_$]*$', k))

        parts = []
        for key, value in obj.items():
            formatted_key = key if is_valid_identifier(key) else f'"{key}"'
            parts.append(f'{formatted_key}: {value}')
        return '{ ' + ', '.join(parts) + ' }'


class PutByIdLong(PutById):
    pass
