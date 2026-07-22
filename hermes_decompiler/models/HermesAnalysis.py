from typing import Dict, Any, Optional, List

from hermes_decompiler.cfg import BasicBlockBuilder, ControlFlowGraphBuilder, CFGValidator
from hermes_decompiler.cfg.CFGAnalysis import CFGAnalysis
from hermes_decompiler.emitter.JavaScriptEmitter import JavaScriptEmitter
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.Logger import get_logger
from hermes_decompiler.regions.building.RegionBuilder import RegionBuilder

logger = get_logger(__name__)


class Output:
    indent: int = 0
    content: str = ""

    used: Optional[bool] = None
    var: Optional[JSVariable] = None

    def __init__(self, lvl: int, content: str, used: Optional[bool] = False, var: Optional[JSVariable] = None) -> None:
        self.indent = lvl
        self.content = content
        self.used = used
        self.var = var


class HermesAnalysis:
    metadataList: List[Dict[str, Any]]
    metadata: Dict[str, Any]

    def __init__(
            self,
            metadata: Optional[dict[str, Any]] = None,
            stringTable: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Initialize the Hermes analysis context.

        This object is created fresh per `JSConverter.convert()` call and is
        the sole owner of state for one conversion pass (registers, results,
        string/function tables). It should never be reused or shared across
        conversions - see core/registry.py for how cross-section data
        (function names) is shared explicitly instead.
        """
        self.registers: dict[str, JSVariable] = {}
        self.metadataList = []
        self.metadata = metadata if metadata is not None else {}

        self.globalObjects: Optional[int] = None
        self.gotoList: List[int] = []

        self.results: List[OpcodeResult] = []

    def add_result(
            self,
            entry: OpcodeEntry,
            variable: JSVariable,
            goto: Optional[int] = None,
            extra_gotos: Optional[List[int]] = None,
    ):
        """
        Add a variable, tracking multiple assignments.

        `extra_gotos` is for instructions with more than one possible
        jump target that isn't a plain fallthrough - today that's only
        SwitchImm (one target per case label). See OpcodeResult for
        why this is a separate parameter instead of making `goto` a
        list.
        """
        result = OpcodeResult(entry, variable, goto, extra_gotos)
        self.results.append(result)

        if variable.name:
            self.registers[variable.name] = variable

    def generate_js(self, verbose: bool = False) -> list[str]:
        return self.generate_js_v1_new(verbose)

    def generate_js_v2(self, verbose: bool = False) -> list[str]:
        #
        # CFG
        #

        blocks = BasicBlockBuilder.build(self.results)

        cfg = ControlFlowGraphBuilder.build(blocks, metadata=self.metadata)

        #
        # Analyses
        #

        analysis = CFGAnalysis(
            cfg=cfg,
            metadata=self.metadata,
        )

        #
        # Regions
        #

        region = RegionBuilder.build(analysis)

        #
        # Emit
        #

        emitter = JavaScriptEmitter(verbose)

        return emitter.emit(region)

    def generate_js_v1(self, verbose: bool = True) -> List[str]:
        outputList: List[Output] = []

        indent_lvl = 1  # Track indentation for nested blocks
        indent = lambda lvl: '    ' * lvl

        visited = set()  # Track processed instruction indices
        return_points = set()  # Track return statements to avoid duplicates
        open_blocks = []  # Stack of open if blocks with their end addresses

        i = 0
        try:
            while i < len(self.results):
                item = self.results[i]
                variable = item.variable

                bytecode = item.opcode.bytecode
                # bytecode -> after first colon
                original_bytecode = bytecode.split(":", 1)[1].strip() if ":" in bytecode else bytecode.strip()

                output: Output = Output(indent_lvl, "", used=variable.used, var=variable)

                # Close blocks if the current address is a jump target
                while open_blocks and any(block["end_addr"] == variable.address for block in open_blocks):
                    for block in open_blocks[:]:
                        if block["end_addr"] == variable.address:
                            indent_lvl -= 1
                            outputList.append(Output(indent_lvl, "}"))
                            open_blocks.remove(block)

                # Skip if already visited
                if i in visited:
                    logger.debug("Skipping visited index=%s, addr=%s", i, variable.address)
                    i += 1
                    continue

                visited.add(i)

                # -----------------------------------------------------
                # -----------------------------------------------------

                if verbose:
                    outputList.append(Output(indent_lvl, f'// CODE → {original_bytecode}'))

                # Add label if the address is a jump target
                if variable.address in self.gotoList:
                    outputList.append(Output(indent_lvl, f"label_{variable.address}:"))

                if variable.handler == "CompleteGenerator":
                    i += 1
                    continue  # Skip CompleteGenerator
                else:
                    valueRaw = variable.value.strip()

                    # Handle special opcodes
                    if variable.handler == "SaveGenerator":
                        output.indent = indent_lvl
                        output.content = f"// await yield; // check: OpcodeDispatcher.dispatch_all // Resume at label_{item.goto}"
                    elif variable.handler == "ResumeGenerator":
                        output.indent = indent_lvl
                        output.content = f'{item.result}; // Resume generator'
                    elif variable.handler == "Ret" and variable.address not in return_points:
                        return_points.add(variable.address)
                        value = valueRaw.split("return ")[1].strip() if "return " in valueRaw else valueRaw
                        output.indent = indent_lvl
                        output.content = f"return {value}"
                    elif "/* jump to" in valueRaw and item.goto is not None:
                        # Handle conditional jumps (e.g., JmpTrue)
                        try:
                            condition = valueRaw.split("if (")[1].split(")")[0].strip()
                            output.indent = indent_lvl
                            output.content = f"if ({condition}) {{"
                            indent_lvl += 1
                            open_blocks.append({"end_addr": item.goto, "start_idx": i})
                        except IndexError:
                            # Malformed condition; emit as regular line
                            logger.warning("Malformed jump condition at address %s: %r", variable.address, valueRaw)
                            outputList.append(Output(indent_lvl, valueRaw))
                    else:
                        # Regular instruction (e.g., assignments, calls)
                        output.content = item.result
                        output.indent = indent_lvl

                # -----------------------------------------------------
                # -----------------------------------------------------
                outputList.append(output)

                if item.goto is not None and variable.handler == "SaveGenerator":
                    target_idx = next((j for j, r in enumerate(self.results) if r.opcode.address == item.goto), i + 1)
                    if target_idx not in visited and target_idx < len(self.results):
                        i = target_idx
                        continue

                i += 1
        except Exception as e:
            logger.error("GenerateJS failed at index=%s: %s", i, e, exc_info=True)
            if 0 <= i < len(self.results):
                logger.error("Failing result: %s", self.results[i].to_dict())

        # Close any remaining open blocks
        while open_blocks:
            indent_lvl -= 1
            outputList.append(Output(indent_lvl, "}"))
            open_blocks.pop()

        # -----------------------------------------------------
        # -----------------------------------------------------

        result = []
        for item in outputList:
            if item.var is not None:
                if verbose and item.used:
                    result.append(f"{indent(item.indent)}// USED → {item.content}")
                elif item.used:
                    pass
                else:
                    result.append(f"{indent(item.indent)}{item.content}")
            else:
                if verbose and item.content.startswith("label_"):
                    result.append(f"{indent(item.indent)}// {item.content}")
                elif verbose is False and item.content.startswith("label_"):
                    pass
                else:
                    result.append(f"{indent(item.indent)}{item.content}")

        return result

    def generate_js_v1_new(self, verbose: bool = False) -> List[str]:

        from hermes_decompiler.regions_new.cfg.CFG import CFG
        from hermes_decompiler.regions_new.building.StructuralAnalyzer import StructuralAnalyzer
        from hermes_decompiler.regions_new.render.JSRenderer import JSRenderer

        cfg = CFG.from_results(self.results)

        cfg.verify()

        cfg.compute_dominators()

        cfg.compute_post_dominators()

        analyzer = StructuralAnalyzer(cfg)

        root = analyzer.build()

        renderer = JSRenderer(verbose=verbose)

        return renderer.render(root)

    def __str__(self):
        return f"HermesAnalysis(globalObjects={self.globalObjects}, gotoList={self.gotoList}, results={[var.to_dict() for var in self.results]})"

    def to_dict(self):
        """Convert the HermesAnalysis object to a dictionary."""
        return {
            "metadata": self.metadata,
            "globalObjects": self.globalObjects,
            "gotoList": self.gotoList,
            "results": [var.to_dict() for var in self.results],
        }
