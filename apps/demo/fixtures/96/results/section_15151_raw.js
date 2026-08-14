function _loop(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    createEnvironment()[0] = param1
    // CODE → <GetEnvironment>: <Reg8: 1, UInt8: 0>
    // USED → r1 = getEnvironment(0);
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    // USED → r2 = getEnvironment(0)[0];
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 207>  # String: 'push' (Identifier)
    // USED → r1 = getEnvironment(0)[0].push;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15152>  # Function: [#15152  of 9 bytes]: 1 params @ offset 0x000f7bb4
    // USED → r0 = function_15152();
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = getEnvironment(0)[0].push(function_15152())
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}