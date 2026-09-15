function _loop(param1) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateTopLevelEnvironment>: <Reg8: 2, UInt32: 1>
    // USED → r2 = __environment__;
    // CODE → addr:  6 | <LoadParam>: <Reg8: 0, UInt8: 1>
    // USED → r0 = param1;
    // CODE → addr:  9 | <StoreNPToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    __environment__[0] = param1
    // CODE → addr: 13 | <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → addr: 16 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
    r4 = r3[0]
    // CODE → addr: 20 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 0, string_id: 88>  # String: 'push' (Identifier)
    // USED → r3 = r4.push;
    // CODE → addr: 25 | <CreateClosure>: <Reg8: 2, Reg8: 2, function_id: 13741>  # Function: [#13741  of 9 bytes]: 1 params @ offset 0x00193d54
    // USED → r2 = function_13741();
    // CODE → addr: 30 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    r2 = r4.push(function_13741())
    // CODE → addr: 35 | <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → addr: 37 | <Ret>: <Reg8: 1>
    return undefined;
}