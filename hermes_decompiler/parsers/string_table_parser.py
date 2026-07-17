import re
from typing import Dict

from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)

# Allow escaped single quotes inside the string value (\') so a string like
# 'It\'s ready' doesn't truncate at the first apostrophe. The old regex
# `'(.*?)'` had no escape awareness and would cut such strings short.
_STRING_RE = re.compile(r"string_id: (\d+).*?# String: '((?:\\.|[^'\\])*)'")


def parse_string_map(lines: list[str]) -> Dict[str, str]:
    string_map: Dict[str, str] = {}
    for line in lines:
        match = _STRING_RE.search(line)
        if match:
            string_id, string_value = match.groups()
            if string_id in string_map and string_map[string_id] != string_value:
                logger.debug(
                    "string_id %s redefined: %r -> %r", string_id, string_map[string_id], string_value
                )
            string_map[string_id] = string_value

    return string_map
