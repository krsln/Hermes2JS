function* ?anon_0_runAllTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateFunctionEnvironment>: <Reg8: 1, UInt8: 3>
    // USED → r1 = __environment__;
    // CODE → addr:  3 | <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 0>
    __environment__[1] = 0
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
    __environment__[2] = 0
    // CODE → addr: 13 | <CreateGenerator>: <Reg8: 1, Reg8: 1, function_id: 13737>  # Function: [#13737 ?anon_0_runAllTests of 1070 bytes]: 1 params @ offset 0x00260bf9
    r1 = createGenerator(__environment__, ?anon_0_runAllTests)
    // CODE → addr: 18 | <Ret>: <Reg8: 1>
    return r1;
}