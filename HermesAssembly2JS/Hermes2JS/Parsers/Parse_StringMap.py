import re
from typing import Dict


def Parse_StringMap(lines: list[str]) -> dict[str, str]:
    stringMap: Dict[str, str] = {}
    for line in lines:
        match = re.search(r'string_id: (\d+).*?# String: \'(.*?)\'', line)
        if match:
            string_id, string_value = match.groups()
            stringMap[string_id] = string_value

    return stringMap
