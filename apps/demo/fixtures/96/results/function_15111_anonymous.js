function function_15111(param1, param2) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 0, UInt8: 2>
    // USED → r0 = param2;
    // CODE → addr:  6 | <Sub>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 - param2;
    // CODE → addr: 10 | <Ret>: <Reg8: 0>
    return param1 - param2;
}