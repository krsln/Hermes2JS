function simpleGeneratorTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateGenerator>: <Reg8: 0, Reg8: 0, function_id: 15165>  # Function: [#15165 ?anon_0_simpleGeneratorTest of 105 bytes]: 1 params @ offset 0x0026aee9
    r0 = createGenerator(r0, ?anon_0_simpleGeneratorTest)
    // CODE → <Ret>: <Reg8: 0>
    return r0;
}