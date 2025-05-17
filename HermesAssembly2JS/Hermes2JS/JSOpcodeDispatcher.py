from typing import Optional

from HermesAssembly2JS.Hermes2JS.Handlers import Import_Handlers

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult


class JSOpcodeDispatcher:
    def __init__(self):
        self.Analysis: Optional[HermesAnalysis] = None
        Import_Handlers()
        # self.Handlers = OpcodeHandler.registry  # Handler Auto-Registration

    def Dispatch(self, line: OpcodeEntry) -> OpcodeResult:
        if not self.Analysis:
            return OpcodeResult(line, JSVariable("-", line.address, "", f'// Error: Analysis context is not set'))

        # print("analysis", self.Analysis)
        # print("line", line)

        handler = OpcodeHandler.GetHandler(line.opcode)
        # handler = self.Handlers.get(line.opcode)
        if handler:
            return handler.Handle(self.Analysis, line)
        else:
            print('TODO: NO HANDLER:\t', line.opcode, line)
            return OpcodeResult(line, JSVariable("-", line.address, "", f'// Unhandled opcode: {line.opcode}'))
