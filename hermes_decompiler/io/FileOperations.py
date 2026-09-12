from __future__ import annotations

import os
import re

from hermes_decompiler.Decompiler import Decompiler
from hermes_decompiler.core.Exceptions import CodeGenerationError
from hermes_decompiler.core.logging import get_logger

logger = get_logger(__name__)


class FileOperations:
    """
    Filesystem I/O for the `.hasm` -> `.js` pipeline: discovering input
    function files and writing converted output. Grouped under `core/`
    since - like `Pipeline`/`PipelineStage` - this is orchestration
    plumbing around the frontend/handlers/backend phases, not one of the
    phases itself.
    """

    #: `function_<number>_<name>.hasm`  (e.g. function_15042_runAllTests.hasm)
    _FUNCTION_FILENAME_RE = re.compile(r'function_(\d+)_.+\.hasm')

    @classmethod
    def get_section_files(
            cls,
            input_dir: str,
            output_dir: str,
            start: int | None = None,
            end: int | None = None,
    ) -> list[tuple[str, int]]:
        """
        Retrieve and sort .hasm files from input_dir that match the
        function_<number>_<name>.hasm pattern and fall within the
        specified range [start, end].

        Returns list of (filename, function_index) tuples, sorted by index.
        """
        os.makedirs(output_dir, exist_ok=True)

        files = []
        for f in os.listdir(input_dir):
            if not f.endswith('.hasm'):
                continue
            match = cls._FUNCTION_FILENAME_RE.match(f)
            if not match:
                logger.debug(
                    "Filename does not match function_<number>_<name>.hasm pattern: %s", f
                )
                continue
            function_index = int(match.group(1))
            if (start is not None and function_index < start) or (
                    end is not None and function_index > end
            ):
                continue
            files.append((f, function_index))

        files.sort(key=lambda x: x[1])
        if not files:
            logger.warning(
                "No function_<number>_<name>.hasm files found in %s within range %s-%s",
                input_dir, start, end,
            )
        return files

    @classmethod
    def process_section(
            cls,
            section_index: int,
            file_path: str,
            output_dir: str,
            filename: str,
            verbose: bool,
            raw: bool,
            strict: bool,
    ) -> bool:
        """
        Process a *.hasm file by reading its content, converting it to
        JavaScript, and writing to output_dir.

        Args:
            section_index: Function index of the file (e.g. 15042 for
                function_15042_runAllTests.hasm).
            file_path: Path to the .hasm file.
            output_dir: Directory to store the output .js file.
            filename: filename of the .js file (without extension).
            verbose: If True, annotate generated JS with `// CODE ->` source comments.
            raw: If True, also generates function_{section_index}_raw.js.
            strict: If True, raise immediately on the first opcode
                    dispatch failure.

        Returns:
            bool: True if the file was processed and written successfully,
                False otherwise. False covers every recoverable failure for
                THIS function (missing/empty file, unparseable metadata,
                code-generation failure, write error) - the caller can
                safely loop over many functions without wrapping this call
                in its own try/except.

        Note on `strict`:
            `strict` only affects opcode-dispatch behavior inside
            `Decompiler.build_context`. When True, a dispatch failure raises
            `OpcodeDispatchError`/`NoHandlerError` (subclasses of
            `HasmDecompilerError`), which this method intentionally does NOT
            catch - that is the whole point of `--strict`, and it is the
            caller's responsibility to decide whether that should abort the batch.
        """
        if not os.path.exists(file_path):
            logger.error("File does not exist: %s", file_path)
            return False

        basename = os.path.basename(file_path)
        logger.info("Processing function #%s: %s", section_index, basename)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                hasm_content = f.read()
            if not hasm_content.strip():
                logger.error("File is empty: %s", file_path)
                return False
        except OSError as e:
            logger.error("Error reading %s: %s", file_path, e)
            return False

        try:
            context = Decompiler.build_context(hasm_content, section_index, strict=strict)

            # Render the raw representation first, as it preserves the complete
            # low-level output before any presentation-oriented formatting.
            js_code_raw = Decompiler.render(context, verbose=True, raw=True) if raw else None

            # Render the standard JavaScript output.
            js_code = Decompiler.render(context, verbose=verbose, raw=False)
        except (ValueError, CodeGenerationError):
            # Bad/unparseable input, or an ordinary code-generation failure,
            # for THIS function only - not a `strict`-related failure and not
            # a decompiler-internal bug (see below). Log and return False so
            # one broken function never aborts the rest of a batch; matches
            # the documented bool contract above.
            logger.error("Failed to convert %s", file_path, exc_info=True)
            return False
        # Note: HasmDecompilerError subclasses raised here are deliberately
        # left uncaught in two distinct cases, both intentional:
        #   - OpcodeDispatchError/NoHandlerError, when `strict=True` - that
        #     is the whole point of `--strict`; see the note above.
        #   - StructurerInvariantError, regardless of `strict` - it signals
        #     a bug in the decompiler itself rather than a per-function input
        #     failure, so it must never be logged-and-continued past like an
        #     ordinary CodeGenerationError; see that exception's docstring
        #     and `Decompiler.render()`.

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{filename}.js")
        output_path_raw = os.path.join(output_dir, f"function_{section_index}_raw.js")
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(js_code)
            if raw and js_code_raw is not None:
                with open(output_path_raw, 'w', encoding='utf-8') as f:
                    f.write(js_code_raw)
            logger.debug("Successfully wrote output %s", f"{filename}.js")
            return True
        except OSError as e:
            logger.error("Error writing to %s: %s", output_path, e)
            return False
