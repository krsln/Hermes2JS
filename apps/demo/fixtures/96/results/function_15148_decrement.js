function decrement() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    r0 = r1[0]
    // CODE → addr:  7 | <Dec>: <Reg8: 0, Reg8: 0>
    // USED → r0 = r0 - 1;
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    r1[0] = r0 - 1
    // CODE → addr: 14 | <Ret>: <Reg8: 0>
    return r0 - 1;
}