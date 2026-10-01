function decrement() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 2, UInt8: 0>
    r1 = r2[0]
    // CODE → addr:  7 | <LoadConstUInt8>: <Reg8: 0, UInt8: 1>
    // USED → r0 = 1;
    // CODE → addr: 10 | <SubN>: <Reg8: 0, Reg8: 1, Reg8: 0>
    // USED → r0 = r1 - 1;
    // CODE → addr: 14 | <StoreNPToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    r2[0] = r1 - 1
    // CODE → addr: 18 | <Ret>: <Reg8: 0>
    return r1 - 1;
}