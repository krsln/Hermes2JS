function function_15153(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15154>  # Function: [#15154 defaultParameterTest of 121 bytes]: 2 params @ offset 0x0026aa9c
    // USED → r3 = defaultParameterTest(param1);
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 3>
    r0[0] = defaultParameterTest(param1)
    // CODE → addr: 14 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15155>  # Function: [#15155 defaultWithRestTest of 169 bytes]: 1 params @ offset 0x0026ab15
    // USED → r2 = defaultWithRestTest();
    // CODE → addr: 19 | <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 2>
    r0[1] = defaultWithRestTest()
    // CODE → addr: 23 | <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → addr: 25 | <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = Object;
    // CODE → addr: 31 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = Object.defineProperty;
    // CODE → addr: 36 | <NewObject>: <Reg8: 5>
    r5 = {  }
    // CODE → addr: 38 | <LoadConstTrue>: <Reg8: 4>
    // USED → r4 = true;
    // CODE → addr: 40 | <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 4, string_id: 205>  # String: 'value' (Identifier)
    r5.value = true
    // CODE → addr: 44 | <LoadConstString>: <Reg8: 4, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r4 = "__esModule";
    // CODE → addr: 48 | <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 1, Reg8: 4, Reg8: 5>
    r4 = Object.defineProperty(param6, "__esModule", r5)
    // CODE → addr: 55 | <PutById>: <Reg8: 1, Reg8: 3, UInt8: 1, string_id: 11191>  # String: 'defaultParameterTest' (Identifier)
    param6.defaultParameterTest = defaultParameterTest(param1)
    // CODE → addr: 61 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 11193>  # String: 'defaultWithRestTest' (Identifier)
    param6.defaultWithRestTest = defaultWithRestTest()
    // CODE → addr: 67 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15157>  # Function: [#15157 callDefaultParameterTests of 105 bytes]: 1 params @ offset 0x0026abbe
    // USED → r0 = callDefaultParameterTests();
    // CODE → addr: 72 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 11182>  # String: 'callDefaultParameterTests' (Identifier)
    param6.callDefaultParameterTests = callDefaultParameterTests()
    // CODE → addr: 78 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 80 | <Ret>: <Reg8: 0>
    return undefined;
}