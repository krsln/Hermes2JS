from typing import Dict, Any, Optional, List

from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult


class HermesAnalysis:
    metadataList: List[Dict[str, Any]]
    metadata: Dict[str, Any]
    stringTable: Dict[str, str]
    functionTable: Dict[str, str]

    def __init__(self,
                 metadata: Dict[str, Any] = None,
                 stringTable: Dict[str, str] = None,
                 functionTable: Dict[str, str] = None):
        """
        Initialize the Hermes analysis context.

        Args:
            metadata (Dict[str, Any], optional): Metadata from .hbc file.
            stringTable (Dict[str, str], optional): String mappings for string_id.
        """
        self.metadataList = []
        self.metadata = metadata if metadata is not None else {}
        self.stringTable = stringTable if stringTable is not None else {}
        self.functionTable = functionTable if functionTable is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def AddResult(self, entry: OpcodeEntry, variable: JSVariable, goto: Optional[int] = None):
        """Add a variable, tracking multiple assignments."""
        self.results.append(OpcodeResult(entry, variable, goto))
        # self.AddVariable(variable)

    def GenerateJS(self, verbose: bool = True) -> List[str]:
        # Use a list of dictionaries instead of a plain list
        output_dicts = []  # Each entry: {"content": str, "indent_lvl": int}
        indent_lvl = 1  # Track indentation for nested blocks
        indent = lambda lvl: '    ' * lvl

        visited = set()  # Track processed instruction indices
        return_points = set()  # Track return statements to avoid duplicates
        open_blocks = []  # Stack of open if blocks with their end addresses

        i = 0
        try:
            while i < len(self.results):
                item = self.results[i]
                variable = item.Variable

                bytecode = item.Opcode.bytecode
                # bytecode -> after first colon
                original_bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                # Close blocks if the current address is a jump target
                while open_blocks and any(block["end_addr"] == variable.address for block in open_blocks):
                    for block in open_blocks[:]:
                        if block["end_addr"] == variable.address:
                            indent_lvl -= 1
                            output_dicts.append({"content": "}", "indent_lvl": indent_lvl})
                            open_blocks.remove(block)

                # Skip if already visited
                if i in visited:
                    # Debug: Log skipped instruction
                    print(f"Skipping visited index={i}, addr={variable.address}")
                    i += 1
                    continue

                # -----------------------------------------------------
                visited.add(i)
                # -----------------------------------------------------

                if verbose:
                    output_dicts.append({"content": f'// CODE -> {original_bytecode}', "indent_lvl": indent_lvl})

                # Add label if the address is a jump target
                if variable.address in self.gotoList:
                    output_dicts.append({"content": f"label_{variable.address}:", "indent_lvl": indent_lvl})

                if variable.handler == "CompleteGenerator":
                    i += 1
                    continue  # Skip CompleteGenerator
                else:
                    valueRaw = variable.value.strip()

                    # Handle special opcodes
                    if variable.handler == "SaveGenerator":
                        output_dicts.append({"content": f"// TODO: await yield; // Resume at label_{item.GoTo}",
                                             "indent_lvl": indent_lvl})
                    elif variable.handler == "ResumeGenerator":
                        if not variable.used:
                            output_dicts.append(
                                {"content": f'{item.result}; // Resume generator', "indent_lvl": indent_lvl})
                        elif verbose:
                            output_dicts.append(
                                {"content": f'// USED -> {item.result}; // Resume generator', "indent_lvl": indent_lvl})
                    elif variable.handler == "Ret" and variable.address not in return_points:
                        return_points.add(variable.address)
                        value = valueRaw.split("return ")[1].strip() if "return " in valueRaw else valueRaw
                        output_dicts.append({"content": f"return {value}", "indent_lvl": indent_lvl})
                    elif "/* jump to" in valueRaw and item.GoTo is not None:
                        # Handle conditional jumps (e.g., JmpTrue)
                        try:
                            condition = valueRaw.split("if (")[1].split(")")[0].strip()
                            output_dicts.append({"content": f"if ({condition}) {{", "indent_lvl": indent_lvl})
                            indent_lvl += 1
                            open_blocks.append({"end_addr": item.GoTo, "start_idx": i})
                        except IndexError:
                            # Malformed condition; emit as regular line
                            output_dicts.append({"content": valueRaw, "indent_lvl": indent_lvl})
                    else:
                        # Regular instruction (e.g., assignments, calls)
                        if not variable.used:
                            output_dicts.append({"content": item.result, "indent_lvl": indent_lvl})
                        elif verbose:
                            output_dicts.append({"content": f'// USED -> {item.result}', "indent_lvl": indent_lvl})

                # -----------------------------------------------------
                # -----------------------------------------------------

                if item.GoTo is not None and variable.handler == "SaveGenerator":
                    target_idx = next((j for j, r in enumerate(self.results) if r.Opcode.address == item.GoTo), i + 1)
                    if target_idx not in visited and target_idx < len(self.results):
                        i = target_idx
                        continue

                i += 1
        except Exception as e:
            print('GenerateJS', e)
            print(self.results[i].to_dict())

        # Close any remaining open blocks
        while open_blocks:
            indent_lvl -= 1
            output_dicts.append({"content": "}", "indent_lvl": indent_lvl})
            open_blocks.pop()

        # Convert the list of dictionaries to a string array with proper indentation
        output = [indent(item["indent_lvl"]) + item["content"] for item in output_dicts]

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
