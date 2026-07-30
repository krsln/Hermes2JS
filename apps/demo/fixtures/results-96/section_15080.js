function function_15080(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    // USED → r2 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15081>  # Function: [#15081 _interopDefault of 28 bytes]: 2 params @ offset 0x001017eb
    // USED → r3 = _interopDefault;
    // CODE → <NewArrayWithBuffer>: <Reg8: 0, UInt16: 1, UInt16: 1, UInt16: 23509>  # Array: ['x']
    // USED → r0 = ["x"];
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 0>
    createEnvironment()[0] = ["x"]
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
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15082>  # Function: [#15082 spreadArrayTest of 203 bytes]: 1 params @ offset 0x002651cd
    // USED → r0 = spreadArrayTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10645>  # String: 'spreadArrayTest' (Identifier)
    param6.spreadArrayTest = spreadArrayTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15083>  # Function: [#15083 spreadObjectTest of 137 bytes]: 1 params @ offset 0x00265298
    // USED → r0 = spreadObjectTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 2, string_id: 10651>  # String: 'spreadObjectTest' (Identifier)
    param6.spreadObjectTest = spreadObjectTest
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15084>  # Function: [#15084 spreadFunctionArgsTest of 99 bytes]: 1 params @ offset 0x00265321
    // USED → r0 = spreadFunctionArgsTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10648>  # String: 'spreadFunctionArgsTest' (Identifier)
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