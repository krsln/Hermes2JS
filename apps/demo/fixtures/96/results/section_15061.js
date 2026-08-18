function function_15061(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r5 = Object;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r4 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 2>
    // USED → r2 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 2, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r2 = "__esModule";
    // CODE → <Call4>: <Reg8: 2, Reg8: 4, Reg8: 5, Reg8: 1, Reg8: 2, Reg8: 3>
    Object.defineProperty(param6, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15062>  # Function: [#15062 ifTest of 241 bytes]: 2 params @ offset 0x0026812c
    // USED → r2 = ifTest(param1);
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 1, string_id: 8596>  # String: 'ifTest' (Identifier)
    param6.ifTest = ifTest(param1)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15063>  # Function: [#15063 ifElseChainTest of 231 bytes]: 3 params @ offset 0x0026821d
    // USED → r0 = ifElseChainTest(param1, param2);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 10899>  # String: 'ifElseChainTest' (Identifier)
    param6.ifElseChainTest = ifElseChainTest(param1, param2)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}