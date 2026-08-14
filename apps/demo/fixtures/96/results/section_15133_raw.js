function function_15133(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 0>
    // USED → r0 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateClosure>: <Reg8: 5, Reg8: 0, function_id: 15134>  # Function: [#15134 basicRegExpTest of 129 bytes]: 2 params @ offset 0x0026a53e
    // USED → r5 = basicRegExpTest(param0, param1);
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 0, Reg8: 5>
    createEnvironment()[0] = basicRegExpTest(param0, param1)
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 0, function_id: 15135>  # Function: [#15135 regExpFlagsTest of 169 bytes]: 2 params @ offset 0x0026a5bf
    // USED → r4 = regExpFlagsTest(param0, param1);
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 1, Reg8: 4>
    createEnvironment()[1] = regExpFlagsTest(param0, param1)
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 0, function_id: 15136>  # Function: [#15136 regExpSingleQuotePatternTest of 139 bytes]: 2 params @ offset 0x0026a668
    // USED → r3 = regExpSingleQuotePatternTest(param0, param1);
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 2, Reg8: 3>
    createEnvironment()[2] = regExpSingleQuotePatternTest(param0, param1)
    // CODE → <CreateClosure>: <Reg8: 2, Reg8: 0, function_id: 15137>  # Function: [#15137 regExpGroupsAndReplaceTest of 120 bytes]: 2 params @ offset 0x0026a6f3
    // USED → r2 = regExpGroupsAndReplaceTest(param0, param1);
    // CODE → <StoreToEnvironment>: <Reg8: 0, UInt8: 3, Reg8: 2>
    createEnvironment()[3] = regExpGroupsAndReplaceTest(param0, param1)
    // CODE → <GetGlobalObject>: <Reg8: 6>
    // USED → r6 = globalThis;
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 6, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r9 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r8 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 7>
    // USED → r7 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 6>
    // USED → r6 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 7, Reg8: 6, string_id: 205>  # String: 'value' (Identifier)
    r7.value = true
    // CODE → <LoadConstString>: <Reg8: 6, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r6 = "__esModule";
    // CODE → <Call4>: <Reg8: 6, Reg8: 8, Reg8: 9, Reg8: 1, Reg8: 6, Reg8: 7>
    r6 = globalThis.Object.defineProperty(r1, "__esModule", r7)
    // CODE → <PutById>: <Reg8: 1, Reg8: 5, UInt8: 1, string_id: 7656>  # String: 'basicRegExpTest' (Identifier)
    param6.basicRegExpTest = basicRegExpTest(param0, param1)
    // CODE → <PutById>: <Reg8: 1, Reg8: 4, UInt8: 2, string_id: 11315>  # String: 'regExpFlagsTest' (Identifier)
    param6.regExpFlagsTest = regExpFlagsTest(param0, param1)
    // CODE → <PutById>: <Reg8: 1, Reg8: 3, UInt8: 3, string_id: 11325>  # String: 'regExpSingleQuotePatternTest' (Identifier)
    param6.regExpSingleQuotePatternTest = regExpSingleQuotePatternTest(param0, param1)
    // CODE → <PutById>: <Reg8: 1, Reg8: 2, UInt8: 4, string_id: 11321>  # String: 'regExpGroupsAndReplaceTest' (Identifier)
    param6.regExpGroupsAndReplaceTest = regExpGroupsAndReplaceTest(param0, param1)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 0, function_id: 15138>  # Function: [#15138 callRegExpTests of 101 bytes]: 1 params @ offset 0x0026a76b
    // USED → r0 = callRegExpTests(param0);
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 11311>  # String: 'callRegExpTests' (Identifier)
    param6.callRegExpTests = callRegExpTests(param0)
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}