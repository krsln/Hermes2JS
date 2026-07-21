import re

from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


class SwitchImm(OpcodeHandler):
    _PATTERN = re.compile(r'^Reg\d+:\s*(\d+)')

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__
        args = entry.args.strip()

        selector_match = self._PATTERN.match(args)
        if not selector_match:
            return self.build_invalid_args_result(analysis, entry, "Expected a leading Reg8 selector argument")

        selector_reg = int(selector_match.group(1))
        selector_val = self.get_register_value(analysis, selector_reg) or f"r{selector_reg}"

        target_addr_list = []
        for offset_str in re.compile(r'Addr\d+:\s*(-?\d+)').findall(args):
            target_addr = entry.address + int(offset_str)
            analysis.gotoList.append(target_addr)
            target_addr_list.append(target_addr)

        if target_addr_list:
            targets = ", ".join(f"label_{addr}" for addr in target_addr_list)
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

        # `extra_gotos` wires every case target into the CFG as a real
        # edge (see ControlFlowGraphBuilder._connect / BasicBlockBuilder
        # leader-finding). Without this, any case block only reachable
        # via the switch (not also a fallthrough/other jump target) is
        # structurally unreachable and trips CFGValidator - it doesn't
        # yet reconstruct a `switch { }` statement (that's SwitchRegion,
        # not implemented), but it does stop the CFG from silently
        # dropping those blocks.
        analysis.add_result(entry, variable, extra_gotos=target_addr_list)

        return OpcodeResult(entry, variable, extra_gotos=target_addr_list)
