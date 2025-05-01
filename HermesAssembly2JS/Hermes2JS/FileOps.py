import os
import re
from typing import Tuple, Optional, List

from HermesAssembly2JS.Hermes2JS.JSConverter import JSConverter
from HermesAssembly2JS.Hermes2JS.Logger import logger

# Define the filename pattern for section_<number>.hbc
filename_pattern = re.compile(r'section_(\d+)\.hbc')

def GetFiles(input_dir: str, output_dir: str, start: Optional[int] = None, end: Optional[int] = None) -> List[
    Tuple[str, int]]:
    """
    Retrieve and sort .hbc files from input_dir that match the section_<number>.hbc pattern
    and fall within the specified range [start, end].

    Args:
        input_dir: Directory containing .hbc files.
        output_dir: Directory to store output (created if it doesn't exist).
        start: Optional starting section index (inclusive).
        end: Optional ending section index (inclusive).

    Returns:
        A sorted list of tuples (filename, section_index) for matching files.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Filter and sort .hbc files within the specified range
    files = []
    for f in os.listdir(input_dir):
        if not f.endswith('.hbc'):
            continue
        match = filename_pattern.match(f)
        if not match:
            logger.debug(f"Filename does not match section_<number>.hbc pattern: {f}")
            continue
        section_index = int(match.group(1))
        if (start is not None and section_index < start) or (end is not None and section_index > end):
            continue
        files.append((f, section_index))

    # Sort files by section index
    files.sort(key=lambda x: x[1])
    if not files:
        logger.warning(f"No section_<number>.hbc files found in {input_dir} within range {start}-{end}")
    return files


def ProcessFile(section_index: int, file_path: str, output_dir: str) -> bool:
    """
    Process a .hbc file by reading its content, converting it to JavaScript, and writing to output_dir.

    Args:
        section_index: Section index of the file (e.g., 9594 for section_9594.hbc).
        file_path: Path to the .hbc file.
        output_dir: Directory to store the output .js file.

    Returns:
        bool: True if the file was processed and written successfully, False otherwise.
    """

    # Check if the file exists
    if not os.path.exists(file_path):
        logger.error(f"File does not exist: {file_path}")
        return False

    logger.info(f"Processing {file_path}")

    # Read file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            hbc_content = f.read()
        if not hbc_content.strip():
            logger.error(f"File is empty: {file_path}")
            return False
    except Exception as e:
        logger.error(f"Error reading {file_path}: {str(e)}")
        return False

    # Process content
    try:
        js_code = JSConverter.convert(hbc_content, section_index)
    except Exception as e:
        logger.error(f"Error processing content of {file_path}: {str(e)}")
        return False

    # Write output
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"section_{section_index}.js")
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(js_code)
        logger.info(f"Successfully wrote output to {output_path}\n")
        return True
    except Exception as e:
        logger.error(f"Error writing to {output_path}: {str(e)}")
        return False
