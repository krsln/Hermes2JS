function value() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    // USED → r0 = r1[0];
    // CODE → addr:  7 | <Ret>: <Reg8: 0>
    return r1[0];
}