function function_15141(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  3 | <LoadConstUInt8>: <Reg8: 0, UInt8: 2>
    // USED → r0 = 2;
    // CODE → addr:  6 | <Mul>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = param1 * 2;
    // CODE → addr: 10 | <Ret>: <Reg8: 0>
    return param1 * 2;
}