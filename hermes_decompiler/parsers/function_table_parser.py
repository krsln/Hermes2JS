import re
from typing import Dict, List

_FUNC_RE = re.compile(r'\[#(\d+)(?:\s+(\w+))?\s+of\s+\d+\s+bytes]')


def parse_function_map(lines: List[str]) -> Dict[str, str]:
    """
    Parse function references like:
        [#11947 fetchMovies of 29 bytes]
        [#11944 of 37 bytes] (anonymous)
    """
    function_map: Dict[str, str] = {}
    for line in lines:
        match = _FUNC_RE.search(line)
        if match:
            function_id, function_name = match.groups()
            function_map[function_id] = function_name if function_name else f"function_{function_id}"
    return function_map
