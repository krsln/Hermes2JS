function function_15143(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 0, UInt8: 0>
    // USED → r1 = r0[0];
    // CODE → addr:  7 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr: 10 | <Mul>: <Reg8: 0, Reg8: 0, Reg8: 1>
    r0 = param1 * r0[0]
    // CODE → addr: 14 | <Ret>: <Reg8: 0>
    return r0;
}