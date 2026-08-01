function function_15171(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15172>  # Function: [#15172 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15173>  # Function: [#15173 delay of 24 bytes]: 2 params @ offset 0x0026b22b
    // USED → r0 = delay;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 0>
    createEnvironment()[2] = delay
    // CODE → <CreateClosure>: <Reg8: 8, Reg8: 2, function_id: 15174>  # Function: [#15174 simpleAsyncTest of 30 bytes]: 1 params @ offset 0x00244d86
    // USED → r8 = simpleAsyncTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 8>
    createEnvironment()[3] = simpleAsyncTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15175>  # Function: [#15175 _simpleAsyncTest of 53 bytes]: 1 params @ offset 0x0026b243
    // USED → r0 = _simpleAsyncTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 0>
    createEnvironment()[4] = _simpleAsyncTest
    // CODE → <CreateClosure>: <Reg8: 7, Reg8: 2, function_id: 15178>  # Function: [#15178 asyncTryCatchTest of 30 bytes]: 1 params @ offset 0x00244e78
    // USED → r7 = asyncTryCatchTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 7>
    createEnvironment()[5] = asyncTryCatchTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15179>  # Function: [#15179 _asyncTryCatchTest of 53 bytes]: 1 params @ offset 0x0026b2e6
    // USED → r0 = _asyncTryCatchTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 0>
    createEnvironment()[6] = _asyncTryCatchTest
    // CODE → <CreateClosure>: <Reg8: 6, Reg8: 2, function_id: 15182>  # Function: [#15182 asyncLoopTest of 30 bytes]: 2 params @ offset 0x0025ab5e
    // USED → r6 = asyncLoopTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 7, Reg8: 6>
    createEnvironment()[7] = asyncLoopTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15183>  # Function: [#15183 _asyncLoopTest of 53 bytes]: 1 params @ offset 0x0026b40f
    // USED → r0 = _asyncLoopTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 8, Reg8: 0>
    createEnvironment()[8] = _asyncLoopTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15186>  # Function: [#15186 parallelAwaitTest of 30 bytes]: 1 params @ offset 0x0025aeb3
    // USED → r0 = parallelAwaitTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 9, Reg8: 0>
    createEnvironment()[9] = parallelAwaitTest
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15187>  # Function: [#15187 _parallelAwaitTest of 53 bytes]: 1 params @ offset 0x0026b4da
    // USED → r9 = _parallelAwaitTest;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 10, Reg8: 9>
    createEnvironment()[10] = _parallelAwaitTest
    // CODE → <CreateClosure>: <Reg8: 9, Reg8: 2, function_id: 15191>  # Function: [#15191 _callAsyncTests of 53 bytes]: 1 params @ offset 0x0026b5bf
    // USED → r9 = _callAsyncTests;
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 11, Reg8: 9>
    createEnvironment()[11] = _callAsyncTests
    // CODE → <GetGlobalObject>: <Reg8: 9>
    // USED → r9 = globalThis;
    // CODE → <TryGetById>: <Reg8: 12, Reg8: 9, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r12 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 11, Reg8: 12, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r11 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 10>
    // USED → r10 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 9>
    // USED → r9 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 10, Reg8: 9, string_id: 205>  # String: 'value' (Identifier)
    // USED → r10 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 9, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r9 = "__esModule";
    // CODE → <Call4>: <Reg8: 9, Reg8: 11, Reg8: 12, Reg8: 1, Reg8: 9, Reg8: 10>
    r9 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <PutById>: <Reg8: 1, Reg8: 8, UInt8: 1, string_id: 11171>  # String: 'simpleAsyncTest' (Identifier)
    param6.simpleAsyncTest = simpleAsyncTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 7, UInt8: 2, string_id: 7300>  # String: 'asyncTryCatchTest' (Identifier)
    param6.asyncTryCatchTest = asyncTryCatchTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 6, UInt8: 3, string_id: 11144>  # String: 'asyncLoopTest' (Identifier)
    param6.asyncLoopTest = asyncLoopTest
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 11161>  # String: 'parallelAwaitTest' (Identifier)
    param6.parallelAwaitTest = parallelAwaitTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15190>  # Function: [#15190 callAsyncTests of 30 bytes]: 1 params @ offset 0x00225544
    // USED → r0 = callAsyncTests;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 5, string_id: 9338>  # String: 'callAsyncTests' (Identifier)
    param6.callAsyncTests = callAsyncTests
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    // USED → r1 = param7[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[0]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[0]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    createEnvironment()[0] = _interopDefault.call(undefined, param2.call(undefined, param7[0]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[1]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[1]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    createEnvironment()[1] = _interopDefault.call(undefined, param2.call(undefined, param7[1]))
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}