function generatorTryFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = __environment__;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12484>  # Function: [#12484 generatorTryFinallyTest of 436 bytes]: 1 params @ offset 0x002441cc
    // USED → r1 = createGenerator(__environment__, generatorTryFinallyTest);
    // CODE → <Ret>: <Reg8: 1>
    return createGenerator(__environment__, generatorTryFinallyTest);
}