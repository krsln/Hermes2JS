function function_15043(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 0, UInt8: 1, string_id: 25>  # String: 'Object' (Identifier)
    // USED → r4 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 2, string_id: 109>  # String: 'defineProperty' (Identifier)
    // USED → r3 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 2>
    // USED → r2 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 2, Reg8: 0, string_id: 206>  # String: 'value' (Identifier)
    // USED → r2 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 49>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 3, Reg8: 4, Reg8: 1, Reg8: 0, Reg8: 2>
    r0 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15044>  # Function: [#15044 whileTest of 117 bytes]: 1 params @ offset 0x00264329
    // USED → r0 = whileTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10754>  # String: 'whileTest' (Identifier)
    param6.whileTest = whileTest
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}