function generatorTryFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → addr: 13 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → addr: 17 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12484>  # Function: [#12484 generatorTryFinallyTest of 436 bytes]: 1 params @ offset 0x002441cc
    r1 = createGenerator(__environment__, generatorTryFinallyTest)
    // CODE → addr: 22 | <Ret>: <Reg8: 1>
    return r1;
}