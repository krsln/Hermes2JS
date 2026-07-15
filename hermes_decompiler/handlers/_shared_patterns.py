import re

REG = r'Reg\d+:\s*(\d+)'
ADDR = r'Addr\d+:\s*(\d+)'
UINT8 = r'UInt8:\s*(\d+)'
UINT16 = r'UInt16:\s*(\d+)'
UINT32 = r'UInt32:\s*(\d+)'
STRING_ID = r'string_id:\s*(\d+)'
FUNCTION_ID = r'function_id:\s*(\d+)'


def sequence(*parts: str) -> "re.Pattern[str]":
    """Build an anchored, comma-separated operand pattern from fragments."""
    return re.compile(r'^' + r',\s*'.join(parts) + r'$')
