from typing import Optional, Dict
from warnings import catch_warnings

from HermesAssembly2JS.Hermes2JS.Handlers.Call import Call1, Call2, Call3, Call4
from HermesAssembly2JS.Hermes2JS.Handlers.Construct import Construct
from HermesAssembly2JS.Hermes2JS.Handlers.Create import CreateThis, CreateClosure
from HermesAssembly2JS.Hermes2JS.Handlers.Environment import GetEnvironment, LoadFromEnvironment
from HermesAssembly2JS.Hermes2JS.Handlers.Generators import StartGenerator, ResumeGenerator, CompleteGenerator, \
    SaveGenerator
from HermesAssembly2JS.Hermes2JS.Handlers.GetById import GetByIdShort, GetById, GetByIdLong, TryGetById
from HermesAssembly2JS.Hermes2JS.Handlers.GetGlobalObject import GetGlobalObject
from HermesAssembly2JS.Hermes2JS.Handlers.Jmp import Jmp, JmpTrue, JmpFalse, JmpUndefined
from HermesAssembly2JS.Hermes2JS.Handlers.Load import LoadParam, LoadConstString, LoadConstUndefined
from HermesAssembly2JS.Hermes2JS.Handlers.Mov import Mov
from HermesAssembly2JS.Hermes2JS.Handlers.New import NewObjectWithBuffer, NewObjectWithBufferLong
from HermesAssembly2JS.Hermes2JS.Handlers.Put import PutNewOwnByIdShort, PutById
from HermesAssembly2JS.Hermes2JS.Handlers.Ret import Ret
from HermesAssembly2JS.Hermes2JS.Handlers.SelectObject import SelectObject
from HermesAssembly2JS.Hermes2JS.Handlers.Throw import Throw

from HermesAssembly2JS.Hermes2JS.Models.HermesAnalysis import HermesAnalysis
from HermesAssembly2JS.Hermes2JS.Models.OpcodeResult import OpcodeResult
from HermesAssembly2JS.Hermes2JS.Models.JSVariable import JSVariable
from HermesAssembly2JS.Hermes2JS.Models.OpcodeEntry import OpcodeEntry
from HermesAssembly2JS.Hermes2JS.Models.OpcodeHandler import OpcodeHandler


class JSOpcodeDispatcher:
    def __init__(self):
        self.Analysis: Optional[HermesAnalysis] = None
        # self.Handlers = OpcodeHandler.registry  # Handler Auto-Registration
        # self.Handlers: Dict[str, OpcodeHandler] = {
        #     'Call1': Call1(),
        #     'Call2': Call2(),
        #     'Call3': Call3(),
        #     'Call4': Call4(),
        #     'Construct': Construct(),
        #     'CreateThis': CreateThis(),
        #
        #     'GetEnvironment': GetEnvironment(),
        #     'LoadFromEnvironment': LoadFromEnvironment(),
        #
        #     'StartGenerator': StartGenerator(),
        #     'ResumeGenerator': ResumeGenerator(),
        #     'CompleteGenerator': CompleteGenerator(),
        #     'SaveGenerator': SaveGenerator(),
        #
        #     'GetByIdShort': GetByIdShort(),
        #     'GetById': GetById(),
        #     'GetByIdLong': GetByIdLong(),
        #     'TryGetById': TryGetById(),
        #
        #     'GetGlobalObject': GetGlobalObject(),
        #
        #     'Jmp': Jmp(),
        #     'JmpTrue': JmpTrue(),
        #     'JmpFalse': JmpFalse(),
        #     'JmpUndefined': JmpUndefined(),
        #
        #     'LoadParam': LoadParam(),
        #     'LoadConstString': LoadConstString(),
        #     'LoadConstUndefined': LoadConstUndefined(),
        #
        #     'Mov': Mov(),
        #     'NewObjectWithBuffer': NewObjectWithBuffer(),
        #     'NewObjectWithBufferLong': NewObjectWithBufferLong(),
        #     'Ret': Ret(),
        #     'SelectObject': SelectObject(),
        # }

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
            print('TODO: NO HANDLER:\t', line.opcode)
            return OpcodeResult(line, JSVariable("-", line.address, "", f'// Unhandled opcode: {line.opcode}'))
