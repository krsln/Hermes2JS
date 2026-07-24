import re

from hermes_decompiler.ir.Expressions import SwitchStatement
from hermes_decompiler.models.HermesAnalysis import HermesAnalysis
from hermes_decompiler.models.OpcodeResult import OpcodeResult
from hermes_decompiler.models.JSVariable import JSVariable
from hermes_decompiler.models.OpcodeEntry import OpcodeEntry
from hermes_decompiler.models.OpcodeHandler import OpcodeHandler


class SwitchImm(OpcodeHandler):
    _PATTERN = re.compile(r"^Reg\d+:\s*(\d+)")

    def handle(self, analysis: HermesAnalysis, entry: OpcodeEntry) -> OpcodeResult:
        handler = self.__class__.__name__

        match = self._PATTERN.match(entry.args.strip())
        if not match:
            return self.build_invalid_args_result(
                analysis,
                entry,
                "Expected a leading Reg selector",
            )

        selector_reg = int(match.group(1))
        selector = self.get_register_value(analysis, selector_reg)

        targets = []

        for offset in re.compile(r"Addr\d+:\s*(-?\d+)").findall(entry.args):
            target = entry.address + int(offset)
            analysis.gotoList.append(target)
            targets.append(target)

        variable = JSVariable(
            handler,
            entry.address,
            "",
            SwitchStatement(selector, targets),
        )

        analysis.add_result(entry, variable, extra_gotos=targets)

        return OpcodeResult(entry, variable, extra_gotos=targets)
