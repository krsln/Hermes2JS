import re

from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class FunctionMetadataParser:
    _NAME_RE = re.compile(r'\[Function #(\d+) "([^"]*)" of (\d+) bytes]')
    _PARAMS_RE = re.compile(r'(\d+) params')
    _OFFSET_RE = re.compile(r'@ offset (0x[0-9a-fA-F]+)')
    _KV_RE = re.compile(r'(.+)=(\d+)')
    _EXCEPTION_HANDLER_RE = re.compile(
        r"\[start=(0x[0-9a-fA-F]+),\s*end=(0x[0-9a-fA-F]+),\s*target=(0x[0-9a-fA-F]+)]"
    )

    @classmethod
    def parse(cls, line: str) -> dict:
        """
        Parse the metadata line of a .hbc file.

        Args:
            line: e.g. '[Function #9594 "?anon_0_" of 105 bytes] ...'

        Returns:
            Dictionary containing parsed metadata. Missing/unrecognized fields
            are logged as warnings rather than raising, matching prior
            behavior where the caller (JSConverter) applies sensible defaults
            via `.get(key, default)`.
        """
        metadata = {}

        metadata_line = line.strip()
        metadata_line = re.sub(r'^\s*=>\s*', '', metadata_line)

        name_match = cls._NAME_RE.match(metadata_line)
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

            params_match = cls._PARAMS_RE.match(segment)
            if params_match:
                metadata['param_count'] = int(params_match.group(1))
                continue

            offset_match = cls._OFFSET_RE.match(segment)
            if offset_match:
                metadata['offset'] = offset_match.group(1)
                continue

            kv_match = cls._KV_RE.match(segment)
            if kv_match:
                key, value = kv_match.groups()
                key = key.strip().replace(' ', '_').lower()
                metadata[key] = int(value)
            else:
                logger.warning("Unrecognized metadata segment: %r", segment)

        return metadata

    @classmethod
    def parse_exception_handlers(cls, line: str) -> list[dict]:
        """
        Parse a Hermes exception handler line.

        Example:
            [Exception handlers: [start=0x19, end=0x2f, target=0x35]
                                 [start=0xbc, end=0x138, target=0x13a] ]

        Returns:
            [
                {"start": 25, "end": 47, "target": 53},
                {"start": 188, "end": 312, "target": 314},
            ]
        """

        handlers = []

        if not line:
            return handlers

        for start, end, target in cls._EXCEPTION_HANDLER_RE.findall(line):
            handlers.append({
                "start": int(start, 16),
                "end": int(end, 16),
                "target": int(target, 16),
            })

        return handlers
