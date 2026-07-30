function function_15063(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 25>  # String: 'Object' (Identifier)
    // USED → r5 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 109>  # String: 'defineProperty' (Identifier)
    // USED → r4 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 206>  # String: 'value' (Identifier)
    // USED → r3 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 49>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    r2 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15064>  # Function: [#15064 forOfTest of 93 bytes]: 1 params @ offset 0x00264bd4
    // USED → r2 = forOfTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 10789>  # String: 'forOfTest' (Identifier)
    param6.forOfTest = forOfTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15065>  # Function: [#15065 forInTest of 102 bytes]: 1 params @ offset 0x00264c31
    // USED → r0 = forInTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 8463>  # String: 'forInTest' (Identifier)
    param6.forInTest = forInTest
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}