function function_15152() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
    // USED → r0 = r0[0];
    // CODE → addr:  7 | <Ret>: <Reg8: 0>
    return r0[0];
}