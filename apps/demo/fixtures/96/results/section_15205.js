function function_15205(param0, param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 5>
    // USED → r5 = createEnvironment();
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED → r6 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 7>
    // USED → r7 = param7;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15206>  # Function: [#15206 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r4 = _interopDefault;
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15207>  # Function: [#15207 _privateHelper2 of 59 bytes]: 1 params @ offset 0x0026bc3f
    // USED → r0 = _privateHelper2;
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 11, Reg8: 0>
    createEnvironment()[11] = _privateHelper2
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r9 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r8 = globalThis.Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    // USED → r3 = { value: true };
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 8, Reg8: 9, Reg8: 1, Reg8: 0, Reg8: 3>
    r0 = globalThis.Object.defineProperty(param6, "__esModule", { value: true })
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15208>  # Function: [#15208 privateStaticTest of 262 bytes]: 1 params @ offset 0x0026bc7a
    // USED → r0 = privateStaticTest;
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
    param6.privateStaticTest = privateStaticTest
    // CODE → <LoadConstZero>: <Reg8: 0>
    // USED → r0 = 0;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 0>
    // USED → r1 = param7[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[0]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[0]));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 1>
    createEnvironment()[0] = _interopDefault.call(undefined, param2.call(undefined, param7[0]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    // USED → r1 = 1;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[1]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[1]));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 1>
    createEnvironment()[1] = _interopDefault.call(undefined, param2.call(undefined, param7[1]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    // USED → r1 = 2;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[2];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[2]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[2]));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 2, Reg8: 1>
    createEnvironment()[2] = _interopDefault.call(undefined, param2.call(undefined, param7[2]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    // USED → r1 = 3;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[3];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[3]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[3]));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 3, Reg8: 1>
    createEnvironment()[3] = _interopDefault.call(undefined, param2.call(undefined, param7[3]))
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    // USED → r1 = 4;
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[4];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, param7[4]);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4]));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 4, Reg8: 1>
    createEnvironment()[4] = _interopDefault.call(undefined, param2.call(undefined, param7[4]))
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    // USED → r3 = 5;
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 3>
    // USED → r3 = param7[5];
    // CODE → <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 3>
    // USED → r3 = param2.call(undefined, param7[5]);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    // USED → r3 = _interopDefault.call(undefined, param2.call(undefined, param7[5]));
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r4 = "count";
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    // USED → r4 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "count");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 5, Reg8: 4>
    createEnvironment()[5] = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "count")
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1521>  # String: 'instances' (String)
    // USED → r4 = "instances";
    // CODE → <Call2>: <Reg8: 9, Reg8: 6, Reg8: 0, Reg8: 4>
    // USED → r9 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "instances");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 6, Reg8: 9>
    createEnvironment()[6] = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "instances")
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5021>  # String: 'privateHelper' (String)
    // USED → r4 = "privateHelper";
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    // USED → r4 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "privateHelper");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 7, Reg8: 4>
    createEnvironment()[7] = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "privateHelper")
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15209>  # Function: [#15209  of 166 bytes]: 1 params @ offset 0x0026bd80
    // USED → r4 = function_15209;
    // CODE → <Call1>: <Reg8: 6, Reg8: 4, Reg8: 0>
    // USED → r6 = function_15209.call(undefined);
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 8, Reg8: 6>
    createEnvironment()[8] = function_15209.call(undefined)
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = globalThis.Object.defineProperty;
    // CODE → <NewObjectWithBuffer>: <Reg8: 4, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 45>  # Object: {'writable': true, 'value': 0}
    // USED → r4 = { "writable": true, "value": 0 };
    // CODE → <Call4>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 9, Reg8: 4>
    r4 = globalThis.Object.defineProperty(function_15209.call(undefined), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "instances"), { "writable": true, "value": 0 })
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 100>
    // USED → r4 = 100;
    // CODE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 11547>  # String: 'MAX' (Identifier)
    function_15209.call(undefined).MAX = 100
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 7671>  # String: 'label' (Identifier)
    // USED → r3 = "label";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    // USED → r3 = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 9, Reg8: 3>
    createEnvironment()[9] = _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15217>  # Function: [#15217  of 81 bytes]: 2 params @ offset 0x0026c046
    // USED → r4 = function_15217;
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 0, Reg8: 6>
    // USED → r4 = function_15217.call(undefined, function_15209.call(undefined));
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 10, Reg8: 4>
    createEnvironment()[10] = function_15217.call(undefined, function_15209.call(undefined))
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = globalThis.Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = globalThis.Object.defineProperty;
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 219>  # Object: {'writable': true, 'value': 'configured'}
    // USED → r5 = { "writable": true, "value": "configured" };
    // CODE → <Call4>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 4, Reg8: 3, Reg8: 5>
    r5 = globalThis.Object.defineProperty(function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"), { "writable": true, "value": "configured" })
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2815>  # String: '__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block' (String)
    // USED → r2 = "__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    r2 = globalThis.console.log("__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block")
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 4, Reg8: 3>
    // USED → r2 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"));
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 4, Reg8: 3>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"));
    // CODE → <GetByVal>: <Reg8: 4, Reg8: 1, Reg8: 3>
    // USED → r4 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"))[_interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")];
    // CODE → <GetById>: <Reg8: 1, Reg8: 4, UInt8: 6, string_id: 10961>  # String: 'toUpperCase' (Identifier)
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"))[_interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")].toUpperCase;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 4>
    // USED → r1 = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"))[_interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")].toUpperCase();
    // CODE → <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"))[_interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")] = _interopDefault.call(undefined, param2.call(undefined, param7[4])).default.call(undefined, function_15217.call(undefined, function_15209.call(undefined)), _interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label"))[_interopDefault.call(undefined, param2.call(undefined, param7[5])).default.call(undefined, "label")].toUpperCase()
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}