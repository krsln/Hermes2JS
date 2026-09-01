function function_15158(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15159>  # Function: [#15159 restOnlyTest of 126 bytes]: 1 params @ offset 0x0026ac88
    // USED → r4 = restOnlyTest();
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 4>
    r0[0] = restOnlyTest()
    // CODE → addr: 14 | <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15160>  # Function: [#15160 restAfterRequiredTest of 149 bytes]: 3 params @ offset 0x0026ad06
    // USED → r3 = restAfterRequiredTest(param1, param2);
    // CODE → addr: 19 | <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 3>
    r0[1] = restAfterRequiredTest(param1, param2)
    // CODE → addr: 23 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15161>  # Function: [#15161 legacyArgumentsTest of 109 bytes]: 1 params @ offset 0x0026ad9b
    // USED → r2 = legacyArgumentsTest();
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 0, UInt8: 2, Reg8: 2>
    r0[2] = legacyArgumentsTest()
    // CODE → addr: 32 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr: 34 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr: 40 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr: 45 | <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → addr: 47 | <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → addr: 49 | <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r5 = "__esModule";
    // CODE → addr: 57 | <Call4>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 5, Reg8: 6>
    r5 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → addr: 64 | <PutById>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 11235>  # String: 'restOnlyTest' (Identifier)
    param6.restOnlyTest = restOnlyTest()
    // CODE → addr: 70 | <PutById>: <Reg8: 1, Reg8: 3, UInt8: 2, string_id: 11230>  # String: 'restAfterRequiredTest' (Identifier)
    param6.restAfterRequiredTest = restAfterRequiredTest(param1, param2)
    // CODE → addr: 76 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 3, string_id: 9022>  # String: 'legacyArgumentsTest' (Identifier)
    param6.legacyArgumentsTest = legacyArgumentsTest()
    // CODE → addr: 82 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15162>  # Function: [#15162 callRestParameterTests of 119 bytes]: 1 params @ offset 0x0026ae08
    // USED → r0 = callRestParameterTests();
    // CODE → addr: 87 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11222>  # String: 'callRestParameterTests' (Identifier)
    param6.callRestParameterTests = callRestParameterTests()
    // CODE → addr: 93 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 95 | <Ret>: <Reg8: 0>
    return r0;
}