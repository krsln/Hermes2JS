function function_15205(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 5>
    r5 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED → r6 = param2;
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <LoadParam>: <Reg8: 7, UInt8: 7>
    // USED → r7 = param7;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15206>  # Function: [#15206 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r4 = _interopDefault(param1);
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15207>  # Function: [#15207 _privateHelper2 of 59 bytes]: 1 params @ offset 0x0026bc3f
    // USED → r0 = _privateHelper2();
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 11, Reg8: 0>
    r5[11] = _privateHelper2()
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 9, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r9 = Object;
    // CODE → <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r8 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 3>
    // USED → r3 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → <Call4>: <Reg8: 0, Reg8: 8, Reg8: 9, Reg8: 1, Reg8: 0, Reg8: 3>
    r0 = Object.defineProperty(param6, "__esModule", r3)
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15208>  # Function: [#15208 privateStaticTest of 262 bytes]: 1 params @ offset 0x0026bc7a
    // USED → r0 = privateStaticTest();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
    param6.privateStaticTest = privateStaticTest()
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 0>
    // USED → r1 = param7[r0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 1>
    r5[0] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 1>
    r5[1] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    r1 = 2
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 2, Reg8: 1>
    r5[2] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    r1 = 3
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 3, Reg8: 1>
    r5[3] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    r1 = 4
    // CODE → <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 4, Reg8: 1>
    r5[4] = r1
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    r3 = 5
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 3>
    // USED → r3 = param7[r3];
    // CODE → <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 3>
    // USED → r3 = param2.call(undefined, r3);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = _interopDefault(param1).call(undefined, r3)
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r4 = "count";
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    r4 = r3.default.call(r0, "count")
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 5, Reg8: 4>
    r5[5] = r4
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 1521>  # String: 'instances' (String)
    // USED → r4 = "instances";
    // CODE → <Call2>: <Reg8: 9, Reg8: 6, Reg8: 0, Reg8: 4>
    // USED → r9 = r3.default.call(r0, "instances");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 6, Reg8: 9>
    r5[6] = r9
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 5021>  # String: 'privateHelper' (String)
    // USED → r4 = "privateHelper";
    // CODE → <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    r4 = r3.default.call(r0, "privateHelper")
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 7, Reg8: 4>
    r5[7] = r4
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15209>  # Function: [#15209  of 166 bytes]: 1 params @ offset 0x0026bd80
    // USED → r4 = function_15209();
    // CODE → <Call1>: <Reg8: 6, Reg8: 4, Reg8: 0>
    // USED → r6 = function_15209().call(undefined);
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 8, Reg8: 6>
    r5[8] = r6
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → <NewObjectWithBuffer>: <Reg8: 4, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 45>  # Object: {'writable': true, 'value': 0}
    // USED → r4 = { "writable": true, "value": 0 };
    // CODE → <Call4>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 9, Reg8: 4>
    r4 = Object.defineProperty(r6, r9, r4)
    // CODE → <LoadConstUInt8>: <Reg8: 4, UInt8: 100>
    // USED → r4 = 100;
    // CODE → <PutById>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 11547>  # String: 'MAX' (Identifier)
    r6.MAX = 100
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = r3.default;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 7671>  # String: 'label' (Identifier)
    // USED → r3 = "label";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    // USED → r3 = r3.default.call(r0, "label");
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 9, Reg8: 3>
    r5[9] = r3
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15217>  # Function: [#15217  of 81 bytes]: 2 params @ offset 0x0026c046
    // USED → r4 = function_15217(param1);
    // CODE → <Call2>: <Reg8: 4, Reg8: 4, Reg8: 0, Reg8: 6>
    // USED → r4 = function_15217(param1).call(undefined, r6);
    // CODE → <StoreToEnvironment>: <Reg8: 5, UInt8: 10, Reg8: 4>
    r5[10] = r4
    // CODE → <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = Object;
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = Object.defineProperty;
    // CODE → <NewObjectWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 219>  # Object: {'writable': true, 'value': 'configured'}
    // USED → r5 = { "writable": true, "value": "configured" };
    // CODE → <Call4>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 4, Reg8: 3, Reg8: 5>
    r5 = Object.defineProperty(r4, r3, r5)
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 2815>  # String: '__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block' (String)
    // USED → r2 = "__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block";
    // CODE → <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log("__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block")
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r1.default;
    // CODE → <Call3>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 4, Reg8: 3>
    r2 = r1.default.call(r0, r4, r3)
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r1.default;
    // CODE → <Call3>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 4, Reg8: 3>
    r1 = r1.default.call(r0, r4, r3)
    // CODE → <GetByVal>: <Reg8: 4, Reg8: 1, Reg8: 3>
    r4 = r1[r3]
    // CODE → <GetById>: <Reg8: 1, Reg8: 4, UInt8: 6, string_id: 10961>  # String: 'toUpperCase' (Identifier)
    // USED → r1 = r4.toUpperCase;
    // CODE → <Call1>: <Reg8: 1, Reg8: 1, Reg8: 4>
    r1 = r4.toUpperCase()
    // CODE → <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    r2[r3] = r1
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}