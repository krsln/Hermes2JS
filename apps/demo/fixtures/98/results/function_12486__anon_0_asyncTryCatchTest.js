function* ?anon_0_asyncTryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 5>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 0>
    __environment__[4] = 0
    // CODE → addr: 13 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → addr: 17 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 13743>  # Function: [#13743 ?anon_0_asyncTryCatchTest of 534 bytes]: 1 params @ offset 0x002611a8
    r1 = createGenerator(__environment__, ?anon_0_asyncTryCatchTest)
    // CODE → addr: 22 | <Ret>: <Reg8: 1>
    return r1;
}