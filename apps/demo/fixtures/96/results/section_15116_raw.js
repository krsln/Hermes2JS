function function_15116(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15117>  # Function: [#15117 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault;
    // CODE → <NewArrayWithBuffer>: <Reg8: 0, UInt16: 1, UInt16: 1, UInt16: 23669>  # Array: ['x']
    // USED → r0 = ["x"];
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    createEnvironment()[0] = ["x"]
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    // USED → r6 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 0, Reg8: 6>
    r0 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15118>  # Function: [#15118 spreadArrayTest of 203 bytes]: 1 params @ offset 0x00269d08
    // USED → r0 = spreadArrayTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10787>  # String: 'spreadArrayTest' (Identifier)
    param6.spreadArrayTest = spreadArrayTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15119>  # Function: [#15119 spreadObjectTest of 137 bytes]: 1 params @ offset 0x00269dd3
    // USED → r0 = spreadObjectTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 10795>  # String: 'spreadObjectTest' (Identifier)
    param6.spreadObjectTest = spreadObjectTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15120>  # Function: [#15120 spreadFunctionArgsTest of 99 bytes]: 1 params @ offset 0x00269e5c
    // USED → r0 = spreadFunctionArgsTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10792>  # String: 'spreadFunctionArgsTest' (Identifier)
    param6.spreadFunctionArgsTest = spreadFunctionArgsTest
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
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    createEnvironment()[1] = _interopDefault.call(undefined, param2.call(undefined, param7[0]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[1]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[1]));
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 1>
    createEnvironment()[2] = _interopDefault.call(undefined, param2.call(undefined, param7[1]))
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}