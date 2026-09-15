function generatorWithLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → addr:  6 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 2>
    __environment__[0] = param1
    // CODE → addr: 10 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr: 12 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
    __environment__[2] = 0
    // CODE → addr: 16 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → addr: 20 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12483>  # Function: [#12483 generatorWithLoopTest of 399 bytes]: 2 params @ offset 0x0024403d
    r1 = createGenerator(__environment__, generatorWithLoopTest)
    // CODE → addr: 25 | <Ret>: <Reg8: 1>
    return r1;
}