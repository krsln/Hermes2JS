function generatorWithLoopTest(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 15167>  # Function: [#15167 ?anon_0_generatorWithLoopTest of 123 bytes]: 2 params @ offset 0x0026af5b
    r0 = createGenerator(r0, ?anon_0_generatorWithLoopTest)
    // CODE → addr:  7 | <Ret>: <Reg8: 0>
    return r0;
}