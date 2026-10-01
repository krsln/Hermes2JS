function function_12474(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  6 | <Greater>: <Reg8: 1, Reg8: 2, Reg8: 0>
    // USED → r1 = param1 > 3;
    // CODE → addr: 10 | <Ret>: <Reg8: 1>
    return param1 > 3;
}