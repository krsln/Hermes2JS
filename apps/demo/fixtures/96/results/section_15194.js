function function_15194(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15195>  # Function: [#15195 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 0, Reg8: 6>
    r0 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15196>  # Function: [#15196 classTest of 193 bytes]: 1 params @ offset 0x0026b75b
    // USED → r0 = classTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10812>  # String: 'classTest' (Identifier)
    param6.classTest = classTest()
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    // USED → r1 = param7[r0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault(param1).call(undefined, r1);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    createEnvironment()[0] = _interopDefault(param1).call(undefined, r1)
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault(param1).call(undefined, r1);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    createEnvironment()[1] = _interopDefault(param1).call(undefined, r1)
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    r1 = 2
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault(param1).call(undefined, r1);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 1>
    createEnvironment()[2] = _interopDefault(param1).call(undefined, r1)
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    r1 = 3
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault(param1).call(undefined, r1);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 1>
    createEnvironment()[3] = _interopDefault(param1).call(undefined, r1)
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    r1 = 4
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault(param1).call(undefined, r1);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 1>
    createEnvironment()[4] = _interopDefault(param1).call(undefined, r1)
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15197>  # Function: [#15197  of 83 bytes]: 1 params @ offset 0x0026b81c
    // USED → r1 = function_15197();
    // CODE → <Call1>: <Reg8: 3, Reg8: 1, Reg8: 0>
    // USED → r3 = function_15197().call(undefined);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 3>
    createEnvironment()[5] = function_15197().call(undefined)
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15201>  # Function: [#15201  of 106 bytes]: 2 params @ offset 0x0026b92e
    // USED → r1 = function_15201(param1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 3>
    // USED → r1 = function_15201(param1).call(undefined, r3);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 1>
    createEnvironment()[6] = function_15201(param1).call(undefined, r3)
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}