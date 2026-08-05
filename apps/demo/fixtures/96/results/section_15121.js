function sum(param0, param1, param2, param3) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    r1 = param1
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 2>
    r0 = param2
    // CODE → <Add>: <Reg8: 1, Reg8: 1, Reg8: 0>
    r1 = r1 + r0
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 3>
    r0 = param3
    // CODE → <Add>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = r1 + r0;
    // CODE → <Ret>: <Reg8: 0>
    return r1 + r0;
}