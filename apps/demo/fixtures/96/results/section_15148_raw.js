function decrement(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    r0 = getEnvironment(0)[0]
    // CODE → <Dec>: <Reg8: 0, Reg8: 0>
    // USED → r0 = r0 - 1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    getEnvironment(0)[0] = r0 - 1
    // CODE → <Ret>: <Reg8: 0>
    return r0 - 1;
}