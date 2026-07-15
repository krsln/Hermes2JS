import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


# /// Set an object property by string index.
# /// Arg1[stringtable[Arg4]] = Arg2.
# DEFINE_OPCODE_4(PutById, Reg8, Reg8, UInt8, UInt16)
# DEFINE_OPCODE_4(PutByIdLong, Reg8, Reg8, UInt8, UInt32)
# OPERAND_STRING_ID(PutById, 4)
# OPERAND_STRING_ID(PutByIdLong, 4)
# Example: <PutById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 12270>  # String: 'fetchMovieDetails' (Identifier)
class PutById(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: Reg8 (dest), Reg8 (value), UInt8 (cache), string_id
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*UInt8:\s*(\d+),\s*string_id:\s*(\d+)', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, value_reg, cache, string_id = map(int, match.groups())

        # Extract property name
        prop_name = ''
        comment_match = re.search(r"String:\s*'([^']+)'\s*\(Identifier\)", entry.comment)
        if comment_match:
            prop_name = comment_match.group(1)
        else:
            try:
                prop_name = analysis.stringTable.get(str(string_id))
            except (AttributeError, KeyError):
                prop_name = f'string_{string_id}'

        # Retrieve the value
        value_var = self.GetVariableByReg(analysis.results, value_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        # Initialize object
        obj = {}
        # Retrieve the destination object
        dest_var = self.GetVariableByReg(analysis.results, dest_reg)

        if dest_var.value != '{}':
            obj_str = dest_var.value.strip()
            # Check if the value is an object literal
            if not (obj_str.startswith('{') and obj_str.endswith('}')):
                obj = {}
            else:
                try:
                    # Parse object literal
                    obj_str = obj_str[1:-1].strip()
                    if obj_str:
                        pairs = self._parse_object_pairs(self, obj_str)
                        obj = {k: v for k, v in pairs}
                except Exception as e:
                    error = f'/* Error: Failed to parse object in r{dest_reg}: {dest_var.value} - {str(e)} */ undefined'
                    return self.Exception(analysis, entry, error)

        # Update or set the property
        obj[prop_name] = value

        # Generate JavaScript object literal
        js_obj = self._format_object_literal(obj)

        # Update the JSVariable
        updated_var = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, updated_var)

        return OpcodeResult(entry, updated_var)

    @staticmethod
    def _parse_object_pairs(self, obj_str: str) -> list[tuple[str, str]]:
        """
        Parse a JavaScript object literal string into key-value pairs.
        Handles valid identifiers, quoted keys, and complex string values.
        """
        pairs = []
        if not obj_str:
            return pairs

        # Split on commas outside of quotes
        parts = []
        buffer = []
        in_quotes = False
        in_template = False
        i = 0
        while i < len(obj_str):
            char = obj_str[i]
            if char == '"' and (i == 0 or obj_str[i - 1] != '\\'):
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

        # Process each key-value pair
        for part in parts:
            match = re.match(r'^\s*([a-zA-Z_$][a-zA-Z0-9_$]*|\"[^\"]*\"|\`[^\`]*\`)\s*:\s*(.+?)\s*$', part)
            if not match:
                raise ValueError(f"Invalid key-value pair: {part}")
            key, value = match.groups()
            if key.startswith('"') and key.endswith('"') or key.startswith('`') and key.endswith('`'):
                key = key[1:-1]
            pairs.append((key, value))

        return pairs

    @staticmethod
    def _format_object_literal(obj: dict) -> str:
        """
        Format a dictionary as a JavaScript object literal.
        """

        def is_valid_identifier(key: str) -> bool:
            return bool(re.match(r'^[a-zA-Z_$][a-zA-Z0-9_$]*$', key))

        parts = []
        for key, value in obj.items():
            formatted_key = key if is_valid_identifier(key) else f'"{key}"'
            parts.append(f'{formatted_key}: {value}')
        return '{ ' + ', '.join(parts) + ' }'


class PutByIdLong(PutById): pass


# /// Create a new own property on an object. This is similar to PutById, but
# /// the destination must be an object, it only deals with own properties,
# /// ignoring the prototype chain, and the property must not already be defined.
# /// Similarly to PutById, the property name cannot be a valid array index.
# /// Arg1 is the destination object, which is known to be an object.
# /// Arg2 is the value to write.
# /// Arg3 is the string table ID of the property name.
# /// Arg1[stringTable[Arg3]] = Arg2
# DEFINE_OPCODE_3(PutNewOwnByIdShort, Reg8, Reg8, UInt8)
# DEFINE_OPCODE_3(PutNewOwnById, Reg8, Reg8, UInt16)
# DEFINE_OPCODE_3(PutNewOwnByIdLong, Reg8, Reg8, UInt32)
# OPERAND_STRING_ID(PutNewOwnByIdShort, 3)
# OPERAND_STRING_ID(PutNewOwnById, 3)
# OPERAND_STRING_ID(PutNewOwnByIdLong, 3)

# Example: <PutNewOwnById>: <Reg8: 4, Reg8: 5, string_id: 8626>  # String: 'Authorization' (Identifier)
# Example: <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 6, string_id: 158>  # String: 'method' (Identifier)
class PutNewOwnByIdX(OpcodeHandler):
    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        # Parse arguments: Reg8 (dest), Reg8 (value), string_id
        match = re.match(r'Reg8:\s*(\d+),\s*Reg8:\s*(\d+),\s*string_id:\s*(\d+)', entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry)

        dest_reg, value_reg, string_id = map(int, match.groups())

        # Extract property name from comment (e.g., String: 'headers')
        prop_name = None
        comment_match = re.search(r"String:\s*'([^']+)'\s*\(Identifier\)", entry.comment)
        if comment_match:
            prop_name = comment_match.group(1)
        else:
            # Fallback to string table lookup
            try:
                prop_name = analysis.stringTable.get(str(string_id))
            except (AttributeError, KeyError):
                prop_name = f'string_{string_id}'  # Fallback if lookup fails

        # Retrieve the destination object from the analysis context
        dest_var = self.GetVariableByReg(analysis.results, dest_reg)
        if not dest_var or not dest_var.value:
            error = f'/* Error: No valid object in r{dest_reg} */ undefined'
            return self.Exception(analysis, entry, error)

            # Retrieve the value from the analysis context
        value_var = self.GetVariableByReg(analysis.results, value_reg)
        value = value_var.value if value_var and value_var.value else 'undefined'

        # Initialize or update the object state
        obj = {}
        if dest_var.value and dest_var.value != '{}':
            obj_str = dest_var.value.strip()
            if not (obj_str.startswith('{') and obj_str.endswith('}')):
                error = f'/* Error: Invalid object format in r{dest_reg}: {dest_var.value} */ undefined'
                return self.Exception(analysis, entry, error)
            try:
                obj_str = obj_str[1:-1].strip()
                if obj_str:
                    pairs = self._parse_object_pairs(self, obj_str)
                    obj = {k: v for k, v in pairs}
            except Exception as e:
                error = f'/* Error: Invalid object format in r{dest_reg}: {dest_var.value} */ undefined'
                return self.Exception(analysis, entry, error)

        # Add the new property
        obj[prop_name] = value

        # Generate the JavaScript object literal
        js_obj = self._format_object_literal(obj)

        # Update the JSVariable for the destination object
        variable = JSVariable(handler, entry.address, f'r{dest_reg}', js_obj)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)

    @staticmethod
    def _parse_object_pairs(self, obj_str: str) -> list[tuple[str, str]]:
        """
        Parse a JavaScript object literal string into key-value pairs.
        Handles valid identifiers, quoted keys, and complex string values, with validation.
        """
        pairs = []
        obj_str = obj_str.strip()
        if not obj_str:
            return pairs

        # Split on commas outside of quotes
        parts = []
        buffer = []
        in_quotes = False
        in_template = False
        i = 0
        while i < len(obj_str):
            char = obj_str[i]
            if char == '"' and (i == 0 or obj_str[i - 1] != '\\'):
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

        # Process each key-value pair
        for part in parts:
            # Match key: value, where key can be identifier or quoted string
            match = re.match(r'^\s*([a-zA-Z_$][a-zA-Z0-9_$]*|\"[^\"]*\"|\`[^\`]*\`)\s*:\s*(.+?)\s*$', part)
            if not match:
                raise ValueError(f"Invalid key-value pair: {part}")
            key, value = match.groups()
            # Remove quotes or backticks from key
            if key.startswith('"') and key.endswith('"') or key.startswith('`') and key.endswith('`'):
                key = key[1:-1]
            # Validate value (basic check for unclosed quotes)
            if value.startswith('"') and not value.endswith('"') and not value.endswith('`"'):
                raise ValueError(f"Unclosed string in value: {value}")
            pairs.append((key, value))

        return pairs

    @staticmethod
    def _format_object_literal(obj: dict) -> str:
        """
        Format a dictionary as a JavaScript object literal, avoiding quotes for valid identifiers.
        """

        def is_valid_identifier(key: str) -> bool:
            # Check if the key is a valid JavaScript identifier
            return bool(re.match(r'^[a-zA-Z_$][a-zA-Z0-9_$]*$', key))

        parts = []
        for key, value in obj.items():
            # Only quote the key if it's not a valid identifier
            formatted_key = key if is_valid_identifier(key) else f'"{key}"'
            # Use the value as-is, assuming it's a valid JavaScript expression
            parts.append(f'{formatted_key}: {value}')
        return '{ ' + ', '.join(parts) + ' }'


class PutNewOwnByIdShort(PutNewOwnByIdX): pass


class PutNewOwnById(PutNewOwnByIdX): pass


class PutNewOwnByIdLong(PutNewOwnByIdX): pass
