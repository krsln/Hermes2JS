function function_15058(param0, param1, param2, param3, param4, param5, param6, param7) {
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
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15059>  # Function: [#15059 ifTest of 241 bytes]: 2 params @ offset 0x002648ad
    // USED → r2 = ifTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 10728>  # String: 'ifTest' (Identifier)
    param6.ifTest = ifTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15060>  # Function: [#15060 ifElseChainTest of 231 bytes]: 3 params @ offset 0x0026499e
    // USED → r0 = ifElseChainTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 10719>  # String: 'ifElseChainTest' (Identifier)
    param6.ifElseChainTest = ifElseChainTest
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}