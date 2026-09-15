function function_15116(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → addr:  5 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  8 | <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → addr: 11 | <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15117>  # Function: [#15117 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → addr: 16 | <NewArrayWithBuffer>: <Reg8: 0, UInt16: 1, UInt16: 1, UInt16: 23669>  # Array: ['x']
    r0 = ["x"]
    // CODE → addr: 24 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    r2[0] = r0
    // CODE → addr: 28 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 30 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr: 36 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr: 41 | <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → addr: 43 | <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → addr: 45 | <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → addr: 49 | <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → addr: 53 | <Call4>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 0, Reg8: 6>
    r0 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → addr: 60 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15118>  # Function: [#15118 spreadArrayTest of 203 bytes]: 1 params @ offset 0x00269d08
    // USED → r0 = spreadArrayTest();
    // CODE → addr: 65 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10787>  # String: 'spreadArrayTest' (Identifier)
    param6.spreadArrayTest = spreadArrayTest()
    // CODE → addr: 71 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15119>  # Function: [#15119 spreadObjectTest of 137 bytes]: 1 params @ offset 0x00269dd3
    // USED → r0 = spreadObjectTest();
    // CODE → addr: 76 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 10795>  # String: 'spreadObjectTest' (Identifier)
    param6.spreadObjectTest = spreadObjectTest()
    // CODE → addr: 82 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15120>  # Function: [#15120 spreadFunctionArgsTest of 99 bytes]: 1 params @ offset 0x00269e5c
    // USED → r0 = spreadFunctionArgsTest();
    // CODE → addr: 87 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10792>  # String: 'spreadFunctionArgsTest' (Identifier)
    param6.spreadFunctionArgsTest = spreadFunctionArgsTest()
    // CODE → addr: 93 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 95 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    r1 = param7[r0]
    // CODE → addr: 99 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:101 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:106 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:111 | <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    r2[1] = r1
    // CODE → addr:115 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr:118 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr:122 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:127 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:132 | <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 1>
    r2[2] = r1
    // CODE → addr:136 | <Ret>: <Reg8: 0>
    return r0;
}