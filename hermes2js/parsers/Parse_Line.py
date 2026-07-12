import re

from hermes2js.models.OpcodeEntry import OpcodeEntry


def Parse_Line(line: str) -> OpcodeEntry | None:
    try:
        match = re.match(r"^==>\s*([0-9a-fA-F]+):\s*<(\w+)>:\s*<([^>]*)>", line.strip())
        if match:
            # Using ternary expression to extract and print the comment part
            comment = re.search(r"\s*#\s*(.*)", line.strip()).group(1) \
                if re.search(r"\s*#\s*(.*)", line.strip()) else ""

            hex_address, opcode, args = match.groups()

            return OpcodeEntry(bytecode=line, hex_address=hex_address, opcode=opcode, args=args, comment=comment)
        else:
            return None

    except Exception as e:
        # Fallback if something goes wrong during parsing
        print(f"Error parsing line: {line}\n{e}")
        return None
