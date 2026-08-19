function function_15171(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → addr:  5 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  8 | <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → addr: 11 | <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15172>  # Function: [#15172 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → addr: 16 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15173>  # Function: [#15173 delay of 24 bytes]: 2 params @ offset 0x0026b22b
    // USED → r0 = delay(param1);
    // CODE → addr: 21 | <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 0>
    r2[2] = delay(param1)
    // CODE → addr: 25 | <CreateClosure>: <Reg8: 8, Reg8: 2, function_id: 15174>  # Function: [#15174 simpleAsyncTest of 30 bytes]: 1 params @ offset 0x00244d86
    // USED → r8 = simpleAsyncTest();
    // CODE → addr: 30 | <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 8>
    r2[3] = simpleAsyncTest()
    // CODE → addr: 34 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15175>  # Function: [#15175 _simpleAsyncTest of 53 bytes]: 1 params @ offset 0x0026b243
    // USED → r0 = _simpleAsyncTest();
    // CODE → addr: 39 | <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 0>
    r2[4] = _simpleAsyncTest()
    // CODE → addr: 43 | <CreateClosure>: <Reg8: 7, Reg8: 2, function_id: 15178>  # Function: [#15178 asyncTryCatchTest of 30 bytes]: 1 params @ offset 0x00244e78
    // USED → r7 = asyncTryCatchTest();
    // CODE → addr: 48 | <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 7>
    r2[5] = asyncTryCatchTest()
    // CODE → addr: 52 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15179>  # Function: [#15179 _asyncTryCatchTest of 53 bytes]: 1 params @ offset 0x0026b2e6
    // USED → r0 = _asyncTryCatchTest();
    // CODE → addr: 57 | <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 0>
    r2[6] = _asyncTryCatchTest()
    // CODE → addr: 61 | <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 15182>  # Function: [#15182 asyncLoopTest of 30 bytes]: 2 params @ offset 0x0025ab5e
    // USED → r6 = asyncLoopTest(param1);
    // CODE → addr: 66 | <StoreToEnvironment>: <Reg8: 2, UInt8: 7, Reg8: 6>
    r2[7] = asyncLoopTest(param1)
    // CODE → addr: 70 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15183>  # Function: [#15183 _asyncLoopTest of 53 bytes]: 1 params @ offset 0x0026b40f
    // USED → r0 = _asyncLoopTest();
    // CODE → addr: 75 | <StoreToEnvironment>: <Reg8: 2, UInt8: 8, Reg8: 0>
    r2[8] = _asyncLoopTest()
    // CODE → addr: 79 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15186>  # Function: [#15186 parallelAwaitTest of 30 bytes]: 1 params @ offset 0x0025aeb3
    // USED → r0 = parallelAwaitTest();
    // CODE → addr: 84 | <StoreToEnvironment>: <Reg8: 2, UInt8: 9, Reg8: 0>
    r2[9] = parallelAwaitTest()
    // CODE → addr: 88 | <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15187>  # Function: [#15187 _parallelAwaitTest of 53 bytes]: 1 params @ offset 0x0026b4da
    // USED → r9 = _parallelAwaitTest();
    // CODE → addr: 93 | <StoreToEnvironment>: <Reg8: 2, UInt8: 10, Reg8: 9>
    r2[10] = _parallelAwaitTest()
    // CODE → addr: 97 | <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15191>  # Function: [#15191 _callAsyncTests of 53 bytes]: 1 params @ offset 0x0026b5bf
    // USED → r9 = _callAsyncTests();
    // CODE → addr:102 | <StoreToEnvironment>: <Reg8: 2, UInt8: 11, Reg8: 9>
    r2[11] = _callAsyncTests()
    // CODE → addr:106 | <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → addr:108 | <TryGetById>: <Reg8: 12, Reg8: 9, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r12 = Object;
    // CODE → addr:114 | <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r11 = Object.defineProperty;
    // CODE → addr:119 | <NewObject>: <Reg8: 10>
    // USED → r10 = {  };
    // CODE → addr:121 | <LoadConstTrue>: <Reg8: 9>
    // USED → r9 = true;
    // CODE → addr:123 | <PutNewOwnByIdShort>: <Reg8: 10, Reg8: 9, string_id: 205>  # String: 'value' (Identifier)
    r10.value = true
    // CODE → addr:127 | <LoadConstString>: <Reg8: 9, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r9 = "__esModule";
    // CODE → addr:131 | <Call4>: <Reg8: 9, Reg8: 11, Reg8: 12, Reg8: 1, Reg8: 9, Reg8: 10>
    r9 = Object.defineProperty(param6, "__esModule", r10)
    // CODE → addr:138 | <PutById>: <Reg8: 1, Reg8: 8, UInt8: 1, string_id: 11171>  # String: 'simpleAsyncTest' (Identifier)
    param6.simpleAsyncTest = simpleAsyncTest()
    // CODE → addr:144 | <PutById>: <Reg8: 1, Reg8: 7, UInt8: 2, string_id: 7300>  # String: 'asyncTryCatchTest' (Identifier)
    param6.asyncTryCatchTest = asyncTryCatchTest()
    // CODE → addr:150 | <PutById>: <Reg8: 1, Reg8: 6, UInt8: 3, string_id: 11144>  # String: 'asyncLoopTest' (Identifier)
    param6.asyncLoopTest = asyncLoopTest(param1)
    // CODE → addr:156 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11161>  # String: 'parallelAwaitTest' (Identifier)
    param6.parallelAwaitTest = parallelAwaitTest()
    // CODE → addr:162 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15190>  # Function: [#15190 callAsyncTests of 30 bytes]: 1 params @ offset 0x00225544
    // USED → r0 = callAsyncTests();
    // CODE → addr:167 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 9338>  # String: 'callAsyncTests' (Identifier)
    param6.callAsyncTests = callAsyncTests()
    // CODE → addr:173 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr:175 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    // USED → r1 = param7[r0];
    // CODE → addr:179 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:181 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr:186 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:191 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r1
    // CODE → addr:195 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr:198 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → addr:202 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr:207 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:212 | <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    r2[1] = r1
    // CODE → addr:216 | <Ret>: <Reg8: 0>
    return undefined;
}