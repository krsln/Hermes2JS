function anon_12488() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 5>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 0>
    __environment__[4] = 0
    // CODE → addr: 13 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 13745>  # Function: [#13745 ?anon_0_parallelAwaitTest of 500 bytes]: 1 params @ offset 0x002615b4
    r1 = createGenerator(__environment__, ?anon_0_parallelAwaitTest)
    // CODE → addr: 18 | <Ret>: <Reg8: 1>
    return r1;
}