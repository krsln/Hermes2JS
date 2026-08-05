function value(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 0>
    // USED → r0 = getEnvironment(0)[0];
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[0];
}