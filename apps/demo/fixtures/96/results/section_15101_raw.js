function function_15101(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15102>  # Function: [#15102 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15103>  # Function: [#15103 nestedObjectDestructureTest of 157 bytes]: 1 params @ offset 0x0026979f
    // USED → r9 = nestedObjectDestructureTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 9>
    r2[2] = nestedObjectDestructureTest()
    // CODE → <CreateClosure>: <Reg8: 8, Reg8: 2, function_id: 15104>  # Function: [#15104 renamedDefaultDestructureTest of 111 bytes]: 1 params @ offset 0x0026983c
    // USED → r8 = renamedDefaultDestructureTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 8>
    r2[3] = renamedDefaultDestructureTest()
    // CODE → <CreateClosure>: <Reg8: 7, Reg8: 2, function_id: 15105>  # Function: [#15105 nestedArrayDestructureTest of 241 bytes]: 1 params @ offset 0x002698ab
    // USED → r7 = nestedArrayDestructureTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 7>
    r2[4] = nestedArrayDestructureTest()
    // CODE → <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 15106>  # Function: [#15106 parameterDestructureTest of 131 bytes]: 3 params @ offset 0x0026999c
    // USED → r6 = parameterDestructureTest(param1, param2);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 6>
    r2[5] = parameterDestructureTest(param1, param2)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15107>  # Function: [#15107 swapViaDestructureTest of 91 bytes]: 1 params @ offset 0x00269a1f
    // USED → r0 = swapViaDestructureTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 0>
    r2[6] = swapViaDestructureTest()
    // CODE → <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r13 = Object;
    // CODE → <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r12 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 11>
    // USED → r11 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 10>
    // USED → r10 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 11, Reg8: 10, string_id: 205>  # String: 'value' (Identifier)
    r11.value = true
    // CODE → <LoadConstString>: <Reg8: 10, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r10 = "__esModule";
    // CODE → <Call4>: <Reg8: 10, Reg8: 12, Reg8: 13, Reg8: 1, Reg8: 10, Reg8: 11>
    r10 = Object.defineProperty(param6, "__esModule", r11)
    // CODE → <PutById>: <Reg8: 1, Reg8: 9, UInt8: 1, string_id: 11263>  # String: 'nestedObjectDestructureTest' (Identifier)
    param6.nestedObjectDestructureTest = nestedObjectDestructureTest()
    // CODE → <PutById>: <Reg8: 1, Reg8: 8, UInt8: 2, string_id: 11276>  # String: 'renamedDefaultDestructureTest' (Identifier)
    param6.renamedDefaultDestructureTest = renamedDefaultDestructureTest()
    // CODE → <PutById>: <Reg8: 1, Reg8: 7, UInt8: 3, string_id: 11259>  # String: 'nestedArrayDestructureTest' (Identifier)
    param6.nestedArrayDestructureTest = nestedArrayDestructureTest()
    // CODE → <PutById>: <Reg8: 1, Reg8: 6, UInt8: 4, string_id: 11272>  # String: 'parameterDestructureTest' (Identifier)
    param6.parameterDestructureTest = parameterDestructureTest(param1, param2)
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 11280>  # String: 'swapViaDestructureTest' (Identifier)
    param6.swapViaDestructureTest = swapViaDestructureTest()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15108>  # Function: [#15108 callDestructuringTests of 108 bytes]: 1 params @ offset 0x00269a7a
    // USED → r0 = callDestructuringTests();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 6, string_id: 10657>  # String: 'callDestructuringTests' (Identifier)
    param6.callDestructuringTests = callDestructuringTests()
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    // USED → r1 = param7[r0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    r2[1] = r1
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}