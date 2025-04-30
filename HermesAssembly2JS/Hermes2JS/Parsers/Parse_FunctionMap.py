import re
from typing import Dict, List

def Parse_FunctionMap(lines: List[str]) -> Dict[str, str]:
    function_map: Dict[str, str] = {}
    for line in lines:
        # Match examples like:
        # [#11947 fetchMovies of 29 bytes]
        # [#11944  of 37 bytes] (no name)
        match = re.search(r'\[#(\d+)(?:\s+(\w+))?\s+of\s+\d+\s+bytes\]', line)
        if match:
            function_id, function_name = match.groups()
            if function_name:
                function_map[function_id] = function_name
            else:
                function_map[function_id] = f"function_{function_id}"
    return function_map
