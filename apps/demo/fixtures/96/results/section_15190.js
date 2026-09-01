function callAsyncTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:  2 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr:  5 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 11>
    r3 = r1[11]
    // CODE → addr:  9 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 65>  # String: 'apply' (Identifier)
    // USED → r2 = r3.apply;
    // CODE → addr: 14 | <ReifyArguments>: <Reg8: 0>
    // USED → r0 = arguments;
    // CODE → addr: 16 | <Mov>: <Reg8: 1, Reg8: 0>
    r1 = arguments
    // CODE → addr: 19 | <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → addr: 22 | <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    r0 = r3.apply(this, r1)
    // CODE → addr: 28 | <Ret>: <Reg8: 0>
    return r0;
}