function asyncTryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 1, UInt8: 6>
    // USED → r3 = getEnvironment(0)[6];
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 65>  # String: 'apply' (Identifier)
    // USED → r2 = getEnvironment(0)[6].apply;
    // CODE → <ReifyArguments>: <Reg8: 0>
    // USED → r0 = arguments;
    // CODE → <Mov>: <Reg8: 1, Reg8: 0>
    // USED → r1 = arguments;
    // CODE → <LoadParam>: <Reg8: 0, UInt8: 0>
    // USED → r0 = this;
    // CODE → <Call3>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r0 = getEnvironment(0)[6].apply(this, r1);
    // CODE → <Ret>: <Reg8: 0>
    return getEnvironment(0)[6].apply(this, r1);
}