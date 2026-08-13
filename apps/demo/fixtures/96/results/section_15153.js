function function_15153(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15154>  # Function: [#15154 defaultParameterTest of 121 bytes]: 2 params @ offset 0x0026aa9c
    // USED → r3 = defaultParameterTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 3>
    createEnvironment()[0] = defaultParameterTest
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15155>  # Function: [#15155 defaultWithRestTest of 169 bytes]: 1 params @ offset 0x0026ab15
    // USED → r2 = defaultWithRestTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 2>
    createEnvironment()[1] = defaultWithRestTest
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 4>
    // USED → r4 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 4, string_id: 205>  # String: 'value' (Identifier)
    r5.value = true
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r4 = "__esModule";
    // CODE → <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 1, Reg8: 4, Reg8: 5>
    r4 = globalThis.Object.defineProperty(r1, "__esModule", r5)
    // CODE → <PutById>: <Reg8: 1, Reg8: 3, UInt8: 1, string_id: 11191>  # String: 'defaultParameterTest' (Identifier)
    param6.defaultParameterTest = defaultParameterTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11193>  # String: 'defaultWithRestTest' (Identifier)
    param6.defaultWithRestTest = defaultWithRestTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15157>  # Function: [#15157 callDefaultParameterTests of 105 bytes]: 1 params @ offset 0x0026abbe
    // USED → r0 = callDefaultParameterTests;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 11182>  # String: 'callDefaultParameterTests' (Identifier)
    param6.callDefaultParameterTests = callDefaultParameterTests
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}