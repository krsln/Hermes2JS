function function_15133(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 0>
    r0 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateClosure>: <Reg8: 5, Reg8: 0, function_id: 15134>  # Function: [#15134 basicRegExpTest of 129 bytes]: 2 params @ offset 0x0026a53e
    // USED → r5 = basicRegExpTest(param1);
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 5>
    r0[0] = basicRegExpTest(param1)
    // CODE → addr: 14 | <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15135>  # Function: [#15135 regExpFlagsTest of 169 bytes]: 2 params @ offset 0x0026a5bf
    // USED → r4 = regExpFlagsTest(param1);
    // CODE → addr: 19 | <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 4>
    r0[1] = regExpFlagsTest(param1)
    // CODE → addr: 23 | <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15136>  # Function: [#15136 regExpSingleQuotePatternTest of 139 bytes]: 2 params @ offset 0x0026a668
    // USED → r3 = regExpSingleQuotePatternTest(param1);
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 0, UInt8: 2, Reg8: 3>
    r0[2] = regExpSingleQuotePatternTest(param1)
    // CODE → addr: 32 | <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15137>  # Function: [#15137 regExpGroupsAndReplaceTest of 120 bytes]: 2 params @ offset 0x0026a6f3
    // USED → r2 = regExpGroupsAndReplaceTest(param1);
    // CODE → addr: 37 | <StoreToEnvironment>: <Reg8: 0, UInt8: 3, Reg8: 2>
    r0[3] = regExpGroupsAndReplaceTest(param1)
    // CODE → addr: 41 | <GetGlobalObject>: <Reg8: 6>
    // USED → r6 = globalThis;
    // CODE → addr: 43 | <TryGetById>: <Reg8: 9, Reg8: 6, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r9 = Object;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r8 = Object.defineProperty;
    // CODE → addr: 54 | <NewObject>: <Reg8: 7>
    // USED → r7 = {  };
    // CODE → addr: 56 | <LoadConstTrue>: <Reg8: 6>
    // USED → r6 = true;
    // CODE → addr: 58 | <PutNewOwnByIdShort>: <Reg8: 7, Reg8: 6, string_id: 205>  # String: 'value' (Identifier)
    r7.value = true
    // CODE → addr: 62 | <LoadConstString>: <Reg8: 6, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r6 = "__esModule";
    // CODE → addr: 66 | <Call4>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 1, Reg8: 6, Reg8: 7>
    r6 = Object.defineProperty(param6, "__esModule", r7)
    // CODE → addr: 73 | <PutById>: <Reg8: 1, Reg8: 5, UInt8: 1, string_id: 7656>  # String: 'basicRegExpTest' (Identifier)
    param6.basicRegExpTest = basicRegExpTest(param1)
    // CODE → addr: 79 | <PutById>: <Reg8: 1, Reg8: 4, UInt8: 2, string_id: 11315>  # String: 'regExpFlagsTest' (Identifier)
    param6.regExpFlagsTest = regExpFlagsTest(param1)
    // CODE → addr: 85 | <PutById>: <Reg8: 1, Reg8: 3, UInt8: 3, string_id: 11325>  # String: 'regExpSingleQuotePatternTest' (Identifier)
    param6.regExpSingleQuotePatternTest = regExpSingleQuotePatternTest(param1)
    // CODE → addr: 91 | <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 11321>  # String: 'regExpGroupsAndReplaceTest' (Identifier)
    param6.regExpGroupsAndReplaceTest = regExpGroupsAndReplaceTest(param1)
    // CODE → addr: 97 | <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15138>  # Function: [#15138 callRegExpTests of 101 bytes]: 1 params @ offset 0x0026a76b
    // USED → r0 = callRegExpTests();
    // CODE → addr:102 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 11311>  # String: 'callRegExpTests' (Identifier)
    param6.callRegExpTests = callRegExpTests()
    // CODE → addr:108 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:110 | <Ret>: <Reg8: 0>
    return undefined;
}