function makeMultiplier(param0, param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <StoreNPToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    createEnvironment()[0] = 3
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15143>  # Function: [#15143  of 16 bytes]: 2 params @ offset 0x001ec067
    // USED → r0 = function_15143(param0, param1);
    // CODE → <Ret>: <Reg8: 0>
    return function_15143(param0, param1);
}