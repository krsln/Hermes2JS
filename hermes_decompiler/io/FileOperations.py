from __future__ import annotations

import os
import re
from typing import List, Optional, Tuple

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.core.Exceptions import CodeGenerationError
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
                False covers every recoverable failure for THIS section (missing/empty
                file, unparseable metadata, code-generation failure, write error) - the
                caller can safely loop over many sections without wrapping this call in
                its own try/except.

        Note on `strict`:
            `strict` only affects opcode-dispatch behavior inside `Decompiler.build_context`.
            When True, a dispatch failure raises `OpcodeDispatchError`/`NoHandlerError`
            (subclasses of `HbcDecompilerError`), which this method intentionally does
            NOT catch - that is the whole point of `--strict`, and it is the caller's
            responsibility to decide whether that should abort the batch.
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
            context = Decompiler.build_context(hbc_content, section_index, strict=strict)

            # Render the raw representation first, as it preserves the complete
            # low-level output before any presentation-oriented formatting.
            js_code_raw = Decompiler.render(context, verbose=True, raw=True) if raw else None

            # Render the standard JavaScript output.
            js_code = Decompiler.render(context, verbose=verbose, raw=False)
        except (ValueError, CodeGenerationError):
            # Bad/unparseable input, or a code-generation bug, for THIS section
            # only - not a `strict`-related failure. Log and return False so
            # one broken section never aborts the rest of a batch; matches the
            # documented bool contract above.
            logger.error("Failed to convert %s", file_path, exc_info=True)
            return False
        # Note: HbcDecompilerError subclasses (OpcodeDispatchError, NoHandlerError, ...)
        # raised here when `strict=True` are deliberately left uncaught - see the
        # `strict` note in the docstring above.

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
