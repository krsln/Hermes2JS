import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


class SwitchImm(OpcodeHandler):
    _PATTERN = re.compile(r'^Reg\d+:\s*(\d+)')

    def Handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__
        args = entry.args.strip()

        selector_match = self._PATTERN.match(args)
        if not selector_match:
            return self.InvalidArgs(analysis, entry, "Expected a leading Reg8 selector argument")

        selector_reg = int(selector_match.group(1))
        selector_val = self.GetValueByReg(analysis, selector_reg) or f"r{selector_reg}"

        target_addrs = []
        for offset_str in re.compile(r'Addr\d+:\s*(-?\d+)').findall(args):
            target_addr = entry.address + int(offset_str)
            analysis.gotoList.append(target_addr)
            target_addrs.append(target_addr)

        if target_addrs:
            targets = ", ".join(f"label_{addr}" for addr in target_addrs)
            value = (
                f"/* TODO: SwitchImm({selector_val}) — jump table not reconstructed; "
                f"candidate targets: {targets} */"
            )
        else:
            value = (
                f"/* TODO: SwitchImm({selector_val}) — jump table not reconstructed; "
                f"no Addr operands found to recover targets from */"
            )

        variable = JSVariable(handler, entry.address, "", value)
        analysis.AddResult(entry, variable)

        return OpcodeResult(entry, variable)
