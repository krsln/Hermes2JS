function simpleGeneratorTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 2>
    // USED → r1 = __environment__;
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12482>  # Function: [#12482 simpleGeneratorTest of 398 bytes]: 1 params @ offset 0x00243eaf
    // USED → r1 = createGenerator(__environment__, simpleGeneratorTest);
    // CODE → <Ret>: <Reg8: 1>
    return createGenerator(__environment__, simpleGeneratorTest);
}