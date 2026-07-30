function function_15105(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15106>  # Function: [#15106 _interopDefault of 28 bytes]: 2 params @ offset 0x001017eb
    // USED → r3 = _interopDefault;
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 25>  # String: 'Object' (Identifier)
    // USED → r8 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 109>  # String: 'defineProperty' (Identifier)
    // USED → r7 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 0, string_id: 206>  # String: 'value' (Identifier)
    // USED → r6 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 49>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 0, Reg8: 6>
    r0 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15107>  # Function: [#15107 classTest of 193 bytes]: 1 params @ offset 0x002658b0
    // USED → r0 = classTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10666>  # String: 'classTest' (Identifier)
    param6.classTest = classTest
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
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[2];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[2]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[2]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 1>
    createEnvironment()[2] = _interopDefault.call(undefined, param2.call(undefined, param7[2]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[3];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[3]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[3]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 1>
    createEnvironment()[3] = _interopDefault.call(undefined, param2.call(undefined, param7[3]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    // USED → r1 = 4;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[4];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[4]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 1>
    createEnvironment()[4] = _interopDefault.call(undefined, param2.call(undefined, param7[4]))
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15108>  # Function: [#15108  of 83 bytes]: 1 params @ offset 0x00265971
    // USED → r1 = function_15108;
    // CODE → <Call1>: <Reg8: 3, Reg8: 1, Reg8: 0>
    // USED → r3 = function_15108.call(undefined);
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 3>
    createEnvironment()[5] = function_15108.call(undefined)
    // CODE → <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15112>  # Function: [#15112  of 106 bytes]: 2 params @ offset 0x00265a83
    // USED → r1 = function_15112;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 3>
    // USED → r1 = function_15112.call(undefined, function_15108.call(undefined));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 1>
    createEnvironment()[6] = function_15112.call(undefined, function_15108.call(undefined))
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}