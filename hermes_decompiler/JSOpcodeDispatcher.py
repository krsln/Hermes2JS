from typing import Optional

from hermes_decompiler.handlers import Import_Handlers

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult


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
