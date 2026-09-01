function _loop(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 1>
    // USED → r1 = param1;
    // CODE → addr:  5 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 1>
    r0[0] = param1
    // CODE → addr:  9 | <GetEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getEnvironment(0)
    // CODE → addr: 12 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 1, UInt8: 0>
    r2 = r1[0]
    // CODE → addr: 16 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 207>  # String: 'push' (Identifier)
    // USED → r1 = r2.push;
    // CODE → addr: 21 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15152>  # Function: [#15152  of 9 bytes]: 1 params @ offset 0x000f7bb4
    // USED → r0 = function_15152();
    // CODE → addr: 26 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = r2.push(function_15152())
    // CODE → addr: 31 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 33 | <Ret>: <Reg8: 0>
    return undefined;
}