function anon_12487(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 10>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  6 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 2>
    __environment__[0] = param1
    // CODE → addr: 10 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 12 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 8, Reg8: 0>
    __environment__[8] = 0
    // CODE → addr: 16 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 0>
    __environment__[9] = 0
    // CODE → addr: 20 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 0>
    __environment__[6] = 0
    // CODE → addr: 24 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 13744>  # Function: [#13744 ?anon_0_asyncLoopTest of 502 bytes]: 2 params @ offset 0x002613be
    r1 = createGenerator(__environment__, ?anon_0_asyncLoopTest)
    // CODE → addr: 29 | <Ret>: <Reg8: 1>
    return r1;
}