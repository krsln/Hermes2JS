import re

from hermes_decompiler.Logger import get_logger

logger = get_logger(__name__)

_NAME_RE = re.compile(r'\[Function #(\d+) "([^"]*)" of (\d+) bytes]')
_PARAMS_RE = re.compile(r'(\d+) params')
_OFFSET_RE = re.compile(r'@ offset (0x[0-9a-fA-F]+)')
_KV_RE = re.compile(r'(.+)=(\d+)')


def parse_hbc_metadata(metadata_line: str) -> dict:
    """
    Parse the metadata line of a .hbc file.

    Args:
        metadata_line: e.g. '[Function #9594 "?anon_0_" of 105 bytes] ...'

    Returns:
        Dictionary containing parsed metadata. Missing/unrecognized fields
        are logged as warnings rather than raising, matching prior
        behavior where the caller (JSConverter) applies sensible defaults
        via `.get(key, default)`.
    """
    metadata = {}

    metadata_line = metadata_line.strip()
    metadata_line = re.sub(r'^\s*=>\s*', '', metadata_line)

    name_match = _NAME_RE.match(metadata_line)
    if name_match:
        metadata['function_id'] = int(name_match.group(1))
        metadata['function_name'] = name_match.group(2) or f"function_{metadata['function_id']}"
        metadata['byte_size'] = int(name_match.group(3))
    else:
        logger.warning('Could not parse metadata header line: %r', metadata_line)

    try:
        content_after_bracket = metadata_line.split(']', 1)[1].strip(': ')
    except IndexError:
        logger.warning("No content after function metadata bracket in: %r", metadata_line)
        content_after_bracket = ""

    segments = [segment.strip() for segment in content_after_bracket.split(',')]
    if segments and '@ offset' in segments[-1]:
        last_segment = segments.pop()
        offset_split = last_segment.split('@ offset')
        if len(offset_split) > 1:
            segments.append(offset_split[0].strip())
            segments.append(f'@ offset {offset_split[1].strip()}')

    for segment in segments:
        if not segment:
            continue

        params_match = _PARAMS_RE.match(segment)
        if params_match:
            metadata['param_count'] = int(params_match.group(1))
            continue

        offset_match = _OFFSET_RE.match(segment)
        if offset_match:
            metadata['offset'] = offset_match.group(1)
            continue

        kv_match = _KV_RE.match(segment)
        if kv_match:
            key, value = kv_match.groups()
            key = key.strip().replace(' ', '_').lower()
            metadata[key] = int(value)
        else:
            logger.warning("Unrecognized metadata segment: %r", segment)

    return metadata
