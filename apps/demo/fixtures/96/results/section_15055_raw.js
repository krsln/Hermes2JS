function function_15055(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r4 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r3 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 2, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r2.value = true
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0, Reg8: 2>
    r0 = globalThis.Object.defineProperty(r1, "__esModule", r2)
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15056>  # Function: [#15056 switchTest of 192 bytes]: 2 params @ offset 0x00267e53
    // USED → r0 = switchTest(param0, param1);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 8729>  # String: 'switchTest' (Identifier)
    param6.switchTest = switchTest(param0, param1)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}