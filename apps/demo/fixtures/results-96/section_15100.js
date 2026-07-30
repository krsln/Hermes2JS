function function_15100(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15101>  # Function: [#15101 defaultParameterTest of 121 bytes]: 2 params @ offset 0x00265663
    // USED → r3 = defaultParameterTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 3>
    createEnvironment()[0] = defaultParameterTest
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15102>  # Function: [#15102 defaultWithRestTest of 169 bytes]: 1 params @ offset 0x002656dc
    // USED → r2 = defaultWithRestTest;
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 2>
    createEnvironment()[1] = defaultWithRestTest
    // CODE → <GetGlobalObject>: <Reg8: 4>
    // USED → r4 = globalThis;
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 4, UInt8: 1, string_id: 25>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 109>  # String: 'defineProperty' (Identifier)
    // USED → r6 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 4>
    // USED → r4 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 5, Reg8: 4, string_id: 206>  # String: 'value' (Identifier)
    // USED → r5 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 49>  # String: '__esModule' (Identifier)
    // USED → r4 = "__esModule";
    // CODE → <Call4>: <Reg8: 4, Reg8: 6, Reg8: 7, Reg8: 1, Reg8: 4, Reg8: 5>
    r4 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <PutById>: <Reg8: 1, Reg8: 3, UInt8: 1, string_id: 10785>  # String: 'defaultParameterTest' (Identifier)
    param6.defaultParameterTest = defaultParameterTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 10787>  # String: 'defaultWithRestTest' (Identifier)
    param6.defaultWithRestTest = defaultWithRestTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15104>  # Function: [#15104 callDefaultParameterTests of 105 bytes]: 1 params @ offset 0x00265785
    // USED → r0 = callDefaultParameterTests;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10781>  # String: 'callDefaultParameterTests' (Identifier)
    param6.callDefaultParameterTests = callDefaultParameterTests
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}