function generatorWithLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 4>
    // USED → r1 = __environment__;
    // CODE → <LoadParam>: <Reg8: 2, UInt8: 1>
    // USED → r2 = param1;
    // CODE → <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 2>
    __environment__[0] = param1
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
    __environment__[2] = 0
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 0>
    __environment__[3] = 0
    // CODE → <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12483>  # Function: [#12483 generatorWithLoopTest of 399 bytes]: 2 params @ offset 0x0024403d
    // USED → r1 = createGenerator(__environment__, generatorWithLoopTest);
    // CODE → <Ret>: <Reg8: 1>
    return createGenerator(__environment__, generatorWithLoopTest);
}