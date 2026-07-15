from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler
from hermes_decompiler.models.OpcodeResult import OpcodeResult

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# /// Allocate the `this` object for a constructor call, ahead of the actual
# /// Construct/CallDirect invocation that follows.
# /// Arg1 is the destination register.
# /// Arg2 is the closure (used to look up its .prototype).
# /// Arg3 is the `new.target` (the constructor actually being `new`'d, which
# ///      may differ from Arg2 in a derived-class / Reflect.construct call).
# DEFINE_OPCODE_3(CreateThis, Reg8, Reg8, Reg8)
# Example: <CreateThis>: <Reg8: 3, Reg8: 3, Reg8: 2>
class CreateThis(OpcodeHandler):
    """Represents `this` object allocation prior to a constructor call."""

    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        dest, func, new_target = (int(x) for x in match.groups())

        func_name = self.GetValueByReg(analysis.results, func) or f"r{func}"
        new_target_name = self.GetValueByReg(analysis.results, new_target) or f"r{new_target}"

        variable = JSVariable(
            handler,
            entry.address,
            f'r{dest}',
            f"createThis(prototype={func_name}, constructor={new_target_name})",
        )

        # variable = JSVariable(handler, entry.address, f'r{dest}', f"createThis({func_name}, {new_target_name});")
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
