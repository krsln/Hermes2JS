async function* ?anon_0_asyncLoopTest(param1) {
    // ──────────────── Block 20 ──────────────── 
    // CODE → addr:445 | <Mov>: <Reg8: 2, Reg8: 7>
    r2 = 3
    // CODE → addr:448 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
    r1[9] = 3
    // CODE → addr:452 | <Throw>: <Reg8: 6>
    throw r6;
}