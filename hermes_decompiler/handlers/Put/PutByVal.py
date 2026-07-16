from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler

from hermes_decompiler.handlers._shared_patterns import REG, sequence


# /// Set a property by value (dynamic key) — the "put" counterpart of
# /// GetByVal, the same way PutById complements GetById.
# /// Arg1[Arg2] = Arg3.
# DEFINE_OPCODE_3(PutByVal, Reg8, Reg8, Reg8)
# Example: <PutByVal>: <Reg8: 98, Reg8: 2, Reg8: 0>
class PutByVal(OpcodeHandler):
    """
    Unlike PutById/PutOwnByIndex, the key here is a *register* (dynamic),
    not a statically known string/index — so the mutation can't be safely
    folded into a tracked object/array literal the way those do (there's no
    way to know, at decompile time, which literal slot a runtime key
    actually targets). This emits a standalone assignment statement instead.

    Deliberately does NOT call analysis.AddResult keyed to `obj_reg`: doing
    so would overwrite that register's tracked expression (used for later
    `.prop`/`[key]` chaining) with this statement's text, corrupting any
    subsequent access through the same register. The result is recorded
    under an empty register key instead — a side-effect-only statement with
    no downstream chainable value (same convention as Ret/Throw).
    """

    _PATTERN = sequence(REG, REG, REG)

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.InvalidArgs(analysis, entry, "Expected three Reg8 arguments")

        obj_reg, key_reg, value_reg = map(int, match.groups())

        obj_val = self.GetValueByReg(analysis, obj_reg) or f"r{obj_reg}"
        key_val = self.GetValueByReg(analysis, key_reg) or f"r{key_reg}"
        value_val = self.GetValueByReg(analysis, value_reg) or f"r{value_reg}"

        statement = f"{obj_val}[{key_val}] = {value_val}"
        variable = JSVariable(handler, entry.address, "", statement)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)