function function_15057(param0, param1, param2, param3, param4, param5, param6, param7) {
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
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15058>  # Function: [#15058 nestedLoopTest of 130 bytes]: 1 params @ offset 0x00267f47
    // USED → r0 = nestedLoopTest(param0);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10944>  # String: 'nestedLoopTest' (Identifier)
    param6.nestedLoopTest = nestedLoopTest(param0)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}