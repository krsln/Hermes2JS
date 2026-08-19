function function_15052(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r4 = Object;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r3 = Object.defineProperty;
    // CODE → addr: 16 | <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → addr: 18 | <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → addr: 20 | <PutNewOwnByIdShort>: <Reg8: 2, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r2.value = true
    // CODE → addr: 24 | <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → addr: 28 | <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0, Reg8: 2>
    r0 = Object.defineProperty(param6, "__esModule", r2)
    // CODE → addr: 35 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr: 37 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15053>  # Function: [#15053 forEachTest of 71 bytes]: 1 params @ offset 0x00267d8a
    // USED → r0 = forEachTest();
    // CODE → addr: 42 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10885>  # String: 'forEachTest' (Identifier)
    param6.forEachTest = forEachTest()
    // CODE → addr: 48 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 50 | <Ret>: <Reg8: 0>
    return undefined;
}