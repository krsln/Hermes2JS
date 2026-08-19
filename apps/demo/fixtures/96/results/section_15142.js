function makeMultiplier(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → addr:  5 | <StoreNPToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    r0[0] = 3
    // CODE → addr:  9 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15143>  # Function: [#15143  of 16 bytes]: 2 params @ offset 0x001ec067
    // USED → r0 = function_15143(param1);
    // CODE → addr: 14 | <Ret>: <Reg8: 0>
    return function_15143(param1);
}