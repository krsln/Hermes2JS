import re


def Parse_HbcMetadata(metadata_line: str) -> dict:
    """
    Parse the metadata line of a .hbc file.

    Args:
        metadata_line: The metadata string (e.g., '[Function #9594 "?anon_0_" of 105 bytes]...').

    Returns:
        Dictionary containing parsed metadata.
    """
    metadata = {}

    # Remove any leading prefix (e.g., '=>') and normalize whitespace
    metadata_line = metadata_line.strip()
    metadata_line = re.sub(r'^\s*=>\s*', '', metadata_line)  # Remove '=>' prefix

    # Extract function name, ID, and byte size
    name_match = re.match(r'\[Function #(\d+) "([^"]*)" of (\d+) bytes]', metadata_line)

    if name_match:
        metadata['function_id'] = int(name_match.group(1))
        metadata['function_name'] = name_match.group(2) or f"func_{metadata['function_id']}"
        metadata['byte_size'] = int(name_match.group(3))
    else:
        print('Could not parse metadata line "{}"'.format(metadata_line))

    # Extract everything after the initial function metadata (after ']')
    try:
        content_after_bracket = metadata_line.split(']', 1)[1].strip(': ')
    except IndexError:
        print("Warning: No content after function metadata bracket")
        content_after_bracket = ""

    # Split by commas, but also handle the offset which may be space-separated
    segments = [segment.strip() for segment in content_after_bracket.split(',')]
    # Handle offset separately if it’s space-separated
    if segments and '@ offset' in segments[-1]:
        last_segment = segments.pop()  # Remove the last segment
        offset_split = last_segment.split('@ offset')
        if len(offset_split) > 1:
            segments.append(offset_split[0].strip())  # Add back any part before offset
            segments.append(f'@ offset {offset_split[1].strip()}')  # Add offset as separate segment

    # Process each segment
    for segment in segments:
        if not segment:
            continue

        # Handle 'X params'
        params_match = re.match(r'(\d+) params', segment)
        if params_match:
            metadata['param_count'] = int(params_match.group(1))
            continue

        # Handle '@ offset 0x...'
        offset_match = re.match(r'@ offset (0x[0-9a-fA-F]+)', segment)
        if offset_match:
            metadata['offset'] = offset_match.group(1)  # Keep as hex string
            continue

        # Handle key=value pairs
        kv_match = re.match(r'(.+)=(\d+)', segment)
        if kv_match:
            key, value = kv_match.groups()
            # Clean and normalize key (replace spaces with underscores)
            key = key.strip().replace(' ', '_').lower()
            metadata[key] = int(value)
        else:
            print(f"Warning: Unrecognized segment: {segment}")

    return metadata
