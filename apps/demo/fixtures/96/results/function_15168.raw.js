function generatorTryFinallyTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 15169>  # Function: [#15169 ?anon_0_generatorTryFinallyTest of 158 bytes]: 1 params @ offset 0x0026afdf
    r0 = createGenerator(r0, ?anon_0_generatorTryFinallyTest)
    // CODE → addr:  7 | <Ret>: <Reg8: 0>
    return r0;
}