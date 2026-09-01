function function_15113(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  3 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:  6 | <Greater>: <Reg8: 0, Reg8: 1, Reg8: 0>
    r0 = param1 > 3
    // CODE → addr: 10 | <Ret>: <Reg8: 0>
    return r0;
}