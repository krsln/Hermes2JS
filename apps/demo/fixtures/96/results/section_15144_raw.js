function function_15144(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = globalThis.Object.defineProperty(r1, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15145>  # Function: [#15145 closureTest of 112 bytes]: 1 params @ offset 0x0026a8f2
    // USED → r2 = closureTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 10113>  # String: 'closureTest' (Identifier)
    param6.closureTest = closureTest()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15150>  # Function: [#15150 closureLoopTest of 124 bytes]: 1 params @ offset 0x0026a9ab
    // USED → r0 = closureLoopTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 11176>  # String: 'closureLoopTest' (Identifier)
    param6.closureLoopTest = closureLoopTest()
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}