function function_15101(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → addr:  5 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  8 | <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → addr: 11 | <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15102>  # Function: [#15102 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → addr: 16 | <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15103>  # Function: [#15103 nestedObjectDestructureTest of 157 bytes]: 1 params @ offset 0x0026979f
    // USED → r9 = nestedObjectDestructureTest();
    // CODE → addr: 21 | <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 9>
    r2[2] = nestedObjectDestructureTest()
    // CODE → addr: 25 | <CreateClosure>: <Reg8: 8, Reg8: 2, function_id: 15104>  # Function: [#15104 renamedDefaultDestructureTest of 111 bytes]: 1 params @ offset 0x0026983c
    // USED → r8 = renamedDefaultDestructureTest();
    // CODE → addr: 30 | <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 8>
    r2[3] = renamedDefaultDestructureTest()
    // CODE → addr: 34 | <CreateClosure>: <Reg8: 7, Reg8: 2, function_id: 15105>  # Function: [#15105 nestedArrayDestructureTest of 241 bytes]: 1 params @ offset 0x002698ab
    // USED → r7 = nestedArrayDestructureTest();
    // CODE → addr: 39 | <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 7>
    r2[4] = nestedArrayDestructureTest()
    // CODE → addr: 43 | <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 15106>  # Function: [#15106 parameterDestructureTest of 131 bytes]: 3 params @ offset 0x0026999c
    // USED → r6 = parameterDestructureTest(param1, param2);
    // CODE → addr: 48 | <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 6>
    r2[5] = parameterDestructureTest(param1, param2)
    // CODE → addr: 52 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15107>  # Function: [#15107 swapViaDestructureTest of 91 bytes]: 1 params @ offset 0x00269a1f
    // USED → r0 = swapViaDestructureTest();
    // CODE → addr: 57 | <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 0>
    r2[6] = swapViaDestructureTest()
    // CODE → addr: 61 | <GetGlobalObject>: <Reg8: 10>
    // USED → r10 = globalThis;
    // CODE → addr: 63 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r13 = Object;
    // CODE → addr: 69 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r12 = Object.defineProperty;
    // CODE → addr: 74 | <NewObject>: <Reg8: 11>
    r11 = {  }
    // CODE → addr: 76 | <LoadConstTrue>: <Reg8: 10>
    // USED → r10 = true;
    // CODE → addr: 78 | <PutNewOwnByIdShort>: <Reg8: 11, Reg8: 10, string_id: 205>  # String: 'value' (Identifier)
    r11.value = true
    // CODE → addr: 82 | <LoadConstString>: <Reg8: 10, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r10 = "__esModule";
    // CODE → addr: 86 | <Call4>: <Reg8: 10, Reg8: 12, Reg8: 13, Reg8: 1, Reg8: 10, Reg8: 11>
    r10 = Object.defineProperty(param6, "__esModule", r11)
    // CODE → addr: 93 | <PutById>: <Reg8: 1, Reg8: 9, UInt8: 1, string_id: 11263>  # String: 'nestedObjectDestructureTest' (Identifier)
    param6.nestedObjectDestructureTest = nestedObjectDestructureTest()
    // CODE → addr: 99 | <PutById>: <Reg8: 1, Reg8: 8, UInt8: 2, string_id: 11276>  # String: 'renamedDefaultDestructureTest' (Identifier)
    param6.renamedDefaultDestructureTest = renamedDefaultDestructureTest()
    // CODE → addr:105 | <PutById>: <Reg8: 1, Reg8: 7, UInt8: 3, string_id: 11259>  # String: 'nestedArrayDestructureTest' (Identifier)
    param6.nestedArrayDestructureTest = nestedArrayDestructureTest()
    // CODE → addr:111 | <PutById>: <Reg8: 1, Reg8: 6, UInt8: 4, string_id: 11272>  # String: 'parameterDestructureTest' (Identifier)
    param6.parameterDestructureTest = parameterDestructureTest(param1, param2)
    // CODE → addr:117 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 11280>  # String: 'swapViaDestructureTest' (Identifier)
    param6.swapViaDestructureTest = swapViaDestructureTest()
    // CODE → addr:123 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15108>  # Function: [#15108 callDestructuringTests of 108 bytes]: 1 params @ offset 0x00269a7a
    // USED → r0 = callDestructuringTests();
    // CODE → addr:128 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 6, string_id: 10657>  # String: 'callDestructuringTests' (Identifier)
    param6.callDestructuringTests = callDestructuringTests()
    // CODE → addr:134 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr:136 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    r1 = param7[r0]
    // CODE → addr:140 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:142 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:147 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:152 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r1
    // CODE → addr:156 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr:159 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr:163 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:168 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:173 | <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    r2[1] = r1
    // CODE → addr:177 | <Ret>: <Reg8: 0>
    return undefined;
}