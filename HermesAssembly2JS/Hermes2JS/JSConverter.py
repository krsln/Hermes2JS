import re
from typing import List, Dict, Any, Optional

from Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from Hermes2JS.JSOpcodeDispatcher import JSOpcodeDispatcher
from Hermes2JS.Models.OpcodeResult import OpcodeResult
from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Parsers.Parse_HasmMetadata import Parse_HasmMetadata
from Hermes2JS.Parsers.Parse_Line import Parse_Line
from Hermes2JS.Parsers.Parse_StringMap import Parse_StringMap


class JSConverter:
    @staticmethod
    def convert(assembly_content: str, section_index: int) -> str:
        """
        Convert .hbc assembly content to JavaScript code.

        Args:
            assembly_content (str): The .hbc assembly content.
            section_index (int): The section index for naming anonymous functions.

        Returns:
            str: The generated JavaScript code.

        Raises:
            ValueError: If the assembly content is invalid or metadata is missing.
        """
        if not assembly_content.strip():
            raise ValueError("Empty assembly content")

        lines = assembly_content.strip().split('\n')
        analysis = HermesAnalysis()

        # Parse the metadata from the first line
        try:
            analysis.metadata = Parse_HasmMetadata(lines[0])
        except Exception as e:
            raise ValueError(f"Failed to parse metadata: {str(e)}")

        # ----
        # Generate JavaScript function signature
        function_name = analysis.metadata.get('function_name', f'func_{section_index}')
        if function_name.startswith('?anon_'):
            function_name = f'anon_{analysis.metadata.get("function_id", section_index)}'

        param_count = analysis.metadata.get('param_count', 0)
        params = [f'param{i}' for i in range(param_count)]

        # Check if the function is async (detect if <StartGenerator> is in the content)
        is_async = '<StartGenerator>' in ''.join(lines)  # Check for generator start indicator
        js_code = [f'{"async function* " if is_async else "function "}{function_name}({", ".join(params)}) {{']
        # ----

        # Placeholder for bytecode parsing
        bytecode_start = next((i for i, line in enumerate(lines) if "Bytecode listing" in line), -1)
        bytecode_lines = lines[bytecode_start + 1:] if bytecode_start >= 0 else []

        if bytecode_lines:
            analysis.stringTable = Parse_StringMap(bytecode_lines)
            results = Dispatcher(bytecode_lines, analysis)

            # print(analysis)
            # js_code.extend(analysis.GenerateJS_OLD())
            # js_code.append('\n\n//------------------------------------------------\n// new\n\n')

            js_code.extend(analysis.GenerateJS(True))
            # js_code.extend(analysis.GenerateJS(False))
        else:
            js_code.append('    // No bytecode provided')

        # for var in analysis.variables:
        #     print(var)

        # Close function
        js_code.append('}')

        return '\n'.join(js_code)


def Dispatcher(bytecode_lines: List[str], analysis: HermesAnalysis) -> List[OpcodeResult]:
    """
    Dispatch bytecode lines to opcode handlers.

    Args:
        bytecode_lines (List[str]): The bytecode lines to process.
        analysis (HermesAnalysis): The analysis context.

    Returns:
        List[OpcodeResult]: The processed opcode results.
    """
    handler = JSOpcodeDispatcher()
    handler.Analysis = analysis

    resList: List[OpcodeResult] = []

    # Preprocess lines
    cleaned_lines = [line.strip() for line in bytecode_lines if line.strip()]

    for line in cleaned_lines:
        try:
            parsedLine = Parse_Line(line)
            if parsedLine:
                dispatched = handler.Dispatch(parsedLine)
                # print(dispatched)
                resList.append(dispatched)
            else:
                newLine = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")
                result = OpcodeResult(newLine, JSVariable("", 0, "", f'// Unparsed: {line}'))
                analysis.results.append(result)

                resList.append(result)
        except Exception as e:
            newLine = OpcodeEntry(bytecode=line, hex_address="", opcode="", args="", comment="")
            result = OpcodeResult(newLine, JSVariable("", 0, "", f'// Error: {str(e)}'))
            analysis.results.append(result)

            # analysis.add_instruction(result)
            resList.append(result)

    return resList
