from typing import Dict, Any, Optional, List

from Hermes2JS.Models.JSVariable import JSVariable
from Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from Hermes2JS.Models.OpcodeResult import OpcodeResult


class HermesAnalysis:
    metadata: Dict[str, Any]
    stringTable: Dict[str, str]

    def __init__(self, metadata: Dict[str, Any] = None, stringTable: Dict[str, str] = None):
        """
        Initialize the Hermes analysis context.

        Args:
            metadata (Dict[str, Any], optional): Metadata from .hbc file.
            stringTable (Dict[str, str], optional): String mappings for string_id.
        """
        self.metadata = metadata if metadata is not None else {}
        self.stringTable = stringTable if stringTable is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def AddResult(self, entry: OpcodeEntry, variable: JSVariable, goto: Optional[int] = None):
        """Add a variable, tracking multiple assignments."""
        self.results.append(OpcodeResult(entry, variable, goto))
        # self.AddVariable(variable)

    # def AddVariable(self, variable: JSVariable):
    #     """Add a variable, tracking multiple assignments."""
    #     self.variables.append(variable)
    #     if variable.name:
    #         if variable.name not in self.variable_map:
    #             self.variable_map[variable.name] = []
    #         self.variable_map[variable.name].append(variable)

    def GenerateJS_OLD(self):
        verbose = True
        # verbose = False

        js_code = []
        for item in self.results:
            line = item.Opcode
            result = item.result
            goto = item.GoTo
            bytecode = line.bytecode

            if self.gotoList.count(line.address) > 0:
                js_code.append(f'\nlabel_{line.address}:')

            if verbose:
                after_first_colon = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()
                js_code.append(f'    // CODE -> {after_first_colon}')

            if not item.Variable.used:
                js_code.append(f'    {result}')
            elif verbose:
                js_code.append(f'    // USED -> {result}')

            if goto:
                js_code.append(f'goto label_{goto};')

        return js_code

    def GenerateJS(self, verbose: bool = True) -> List[str]:
        """
        Generate structured JavaScript code from the analysis results.

        Returns:
            List[str]: The generated JavaScript code lines.
        """
        output = []
        indent_lvl = 1  # Track indentation for nested blocks
        indent = lambda lvl: '    ' * lvl

        visited = set()  # Track processed instruction indices
        return_points = set()  # Track return statements to avoid duplicates
        open_blocks = []  # Stack of open if blocks with their end addresses

        def Formatter(used: bool, txt: str):
            if not used:
                return txt
            return f'// USED -> {txt}' if verbose else ''

        i = 0
        try:
            while i < len(self.results):
                item = self.results[i]
                goto = item.GoTo

                variable = item.Variable
                handler = variable.handler
                addr = variable.address

                bytecode = item.Opcode.bytecode
                # bytecode -> after first colon
                original_bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                # Debug: Log each instruction
                # print(f"Processing index={i}, addr={addr}, handler={handler}, value={variable.value if variable and variable.value else None}, goto={goto}")

                # Close blocks if the current address is a jump target
                while open_blocks and any(block["end_addr"] == addr for block in open_blocks):
                    for block in open_blocks[:]:
                        if block["end_addr"] == addr:
                            indent_lvl -= 1
                            output.append(indent(indent_lvl) + "}")
                            open_blocks.remove(block)
                            # Debug: Log block closure
                            # print(f"Closed block at addr={addr}, open_blocks={open_blocks}")

                # Skip if already visited
                if i in visited:
                    # Debug: Log skipped instruction
                    print(f"Skipping visited index={i}, addr={addr}")
                    i += 1
                    continue
                visited.add(i)

                # Add label if the address is a jump target
                if addr in self.gotoList:
                    output.append(indent(indent_lvl) + f"label_{addr}:")

                # Handle instructions
                if handler == "CompleteGenerator":
                    i += 1
                    continue  # Skip CompleteGenerator
                elif variable and variable.value and not variable.value.startswith("//"):
                    line = variable.value.strip()

                    if verbose:
                        output.append(indent(indent_lvl) + f'// CODE -> {original_bytecode}')

                    # Handle special opcodes
                    if handler == "SaveGenerator":
                        # print(item)
                        output.append(indent(indent_lvl) + f"await yield; // Resume at label_{goto}")
                    elif handler == "ResumeGenerator":
                        # print(item)
                        formatted = Formatter(variable.used, item.result)
                        if formatted != '':
                            output.append(indent(indent_lvl) + f"{formatted}; // Resume generator")
                    elif handler == "Ret" and addr not in return_points:
                        return_points.add(addr)
                        value = line.split("return ")[1].strip() if "return " in line else line
                        output.append(indent(indent_lvl) + f"return {value}")
                    elif "/* jump to" in line and goto is not None:
                        # Handle conditional jumps (e.g., JmpTrue)
                        try:
                            condition = line.split("if (")[1].split(")")[0].strip()
                            output.append(indent(indent_lvl) + f"if ({condition}) {{")
                            indent_lvl += 1
                            open_blocks.append({"end_addr": goto, "start_idx": i})
                            # Debug: Log conditional
                            # print(f"Opened if block at addr={addr}, condition={condition}, end_addr={goto}")
                        except IndexError:
                            # Malformed condition; emit as regular line
                            output.append(indent(indent_lvl) + line)
                    else:
                        # Regular instruction (e.g., assignments, calls)
                        formatted = Formatter(variable.used, item.result)
                        if formatted != '':
                            output.append(indent(indent_lvl) + formatted)

                        # Handle jumps for SaveGenerator
                if goto is not None and handler == "SaveGenerator":
                    target_idx = next((j for j, r in enumerate(self.results) if r.Opcode.address == goto), i + 1)
                    # print(goto, target_idx)
                    if target_idx not in visited and target_idx < len(self.results):
                        # Debug: Log jump
                        # print(f"Jumping from addr={addr} to target_idx={target_idx}, goto={goto}")
                        i = target_idx
                        continue

                i += 1
        except Exception as e:
            print('GenerateJS', e)
            print(self.results[i].to_dict())

        # Close any remaining open blocks
        while open_blocks:
            indent_lvl -= 1
            output.append(indent(indent_lvl) + "}")
            open_blocks.pop()

        return output

    def __str__(self):
        return f"HermesAnalysis(globalObjects={self.globalObjects}, gotoList={self.gotoList}, results={[var.to_dict() for var in self.results]})"

    def to_dict(self):
        """Convert the HermesAnalysis object to a dictionary."""
        return {
            "metadata": self.metadata,
            "stringMap": self.stringTable,
            "globalObjects": self.globalObjects,
            "gotoList": self.gotoList,
            "results": [var.to_dict() for var in self.results],
        }
