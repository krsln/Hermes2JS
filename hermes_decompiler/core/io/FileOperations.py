from __future__ import annotations

import os
import re
from typing import List, Optional, Tuple

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class FileOperations:
    """
    Filesystem I/O for the `.hbc` -> `.js` pipeline: discovering input
    section files and writing converted output. Grouped under `core/`
    since - like `Pipeline`/`PipelineStage` - this is orchestration
    plumbing around the frontend/handlers/backend phases, not one of the
    phases itself.
    """

    #: `section_<number>.hbc`
    _SECTION_FILENAME_RE = re.compile(r'section_(\d+)\.hbc')

    @classmethod
    def get_section_files(
            cls,
            input_dir: str,
            output_dir: str,
            start: Optional[int] = None,
            end: Optional[int] = None,
    ) -> List[Tuple[str, int]]:
        """
        Retrieve and sort .hbc files from input_dir that match the
        section_<number>.hbc pattern and fall within the specified range
        [start, end].
        """
        os.makedirs(output_dir, exist_ok=True)

        files = []
        for f in os.listdir(input_dir):
            if not f.endswith('.hbc'):
                continue
            match = cls._SECTION_FILENAME_RE.match(f)
            if not match:
                logger.debug("Filename does not match section_<number>.hbc pattern: %s", f)
                continue
            section_index = int(match.group(1))
            if (start is not None and section_index < start) or (end is not None and section_index > end):
                continue
            files.append((f, section_index))

        files.sort(key=lambda x: x[1])
        if not files:
            logger.warning("No section_<number>.hbc files found in %s within range %s-%s", input_dir, start, end)
        return files

    @classmethod
    def process_section(
            cls,
            section_index: int,
            file_path: str,
            output_dir: str,
            verbose: bool,
            raw: bool,
            strict: bool,
    ) -> bool:
        """
        Process a *.hbc file by reading its content, converting it to
        JavaScript, and writing to output_dir.

        Args:
            section_index: Section index of the file (e.g., 9594 for section_9594.hbc).
            file_path: Path to the .hbc file.
            output_dir: Directory to store the output .js file.
            verbose: If True, annotate generated JS with `// CODE ->`source comments.
            raw: If True, generates section_{section_index}_raw.js.
            strict: If True, rise immediately on the first opcode
                    dispatch failure

        Returns:
            bool: True if the file was processed and written successfully, False otherwise.
        """
        if not os.path.exists(file_path):
            logger.error("File does not exist: %s", file_path)
            return False

        logger.info("Processing section #%s: %s", section_index, f"\t~/section_{section_index}.hbc")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                hbc_content = f.read()
            if not hbc_content.strip():
                logger.error("File is empty: %s", file_path)
                return False
        except OSError as e:
            logger.error("Error reading %s: %s", file_path, e)
            return False

        try:
            js_code = Decompiler.convert(hbc_content, section_index, verbose=verbose, raw=False, strict=strict)
            js_code_raw = None
            if raw:
                js_code_raw = Decompiler.convert(hbc_content, section_index, verbose=True, raw=True, strict=strict)
        except ValueError:
            # Bad/unparseable input for this specific section - log and let the
            # caller decide whether to continue with the rest of the batch.
            logger.error("Failed to convert %s", file_path, exc_info=True)
            raise

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"section_{section_index}.js")
        output_path_raw = os.path.join(output_dir, f"section_{section_index}_raw.js")
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(js_code)
            if raw and js_code_raw is not None:
                with open(output_path_raw, 'w', encoding='utf-8') as f:
                    f.write(js_code_raw)
            logger.debug("Successfully wrote output %s", f"\t~/section_{section_index}.js")
            return True
        except OSError as e:
            logger.error("Error writing to %s: %s", output_path, e)
            return False
