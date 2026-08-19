function simpleGeneratorTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 2>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
    __environment__[0] = 0
    // CODE → addr: 13 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 12482>  # Function: [#12482 simpleGeneratorTest of 398 bytes]: 1 params @ offset 0x00243eaf
    r1 = createGenerator(__environment__, simpleGeneratorTest)
    // CODE → addr: 18 | <Ret>: <Reg8: 1>
    return r1;
}