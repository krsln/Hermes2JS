function function_15205(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 5>
    r5 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 6, UInt8: 2>
    // USED → r6 = param2;
    // CODE → addr:  5 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  8 | <LoadParam>: <Reg8: 7, UInt8: 7>
    // USED → r7 = param7;
    // CODE → addr: 11 | <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15206>  # Function: [#15206 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r4 = _interopDefault(param1);
    // CODE → addr: 16 | <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15207>  # Function: [#15207 _privateHelper2 of 59 bytes]: 1 params @ offset 0x0026bc3f
    // USED → r0 = _privateHelper2();
    // CODE → addr: 21 | <StoreToEnvironment>: <Reg8: 5, UInt8: 11, Reg8: 0>
    r5[11] = _privateHelper2()
    // CODE → addr: 25 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr: 27 | <TryGetById>: <Reg8: 9, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r9 = Object;
    // CODE → addr: 33 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r8 = Object.defineProperty;
    // CODE → addr: 38 | <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → addr: 40 | <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → addr: 42 | <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r3.value = true
    // CODE → addr: 46 | <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → addr: 50 | <Call4>: <Reg8: 0, Reg8: 8, Reg8: 9, Reg8: 1, Reg8: 0, Reg8: 3>
    r0 = Object.defineProperty(param6, "__esModule", r3)
    // CODE → addr: 57 | <CreateClosure>: <Reg8: 0, Reg8: 5, function_id: 15208>  # Function: [#15208 privateStaticTest of 262 bytes]: 1 params @ offset 0x0026bc7a
    // USED → r0 = privateStaticTest();
    // CODE → addr: 62 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10854>  # String: 'privateStaticTest' (Identifier)
    param6.privateStaticTest = privateStaticTest()
    // CODE → addr: 68 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 70 | <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 0>
    r1 = param7[r0]
    // CODE → addr: 74 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 76 | <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr: 81 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr: 86 | <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 1>
    r5[0] = r1
    // CODE → addr: 90 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr: 93 | <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr: 97 | <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:102 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:107 | <StoreToEnvironment>: <Reg8: 5, UInt8: 1, Reg8: 1>
    r5[1] = r1
    // CODE → addr:111 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    r1 = 2
    // CODE → addr:114 | <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr:118 | <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:123 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:128 | <StoreToEnvironment>: <Reg8: 5, UInt8: 2, Reg8: 1>
    r5[2] = r1
    // CODE → addr:132 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    r1 = 3
    // CODE → addr:135 | <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr:139 | <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:144 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:149 | <StoreToEnvironment>: <Reg8: 5, UInt8: 3, Reg8: 1>
    r5[3] = r1
    // CODE → addr:153 | <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    r1 = 4
    // CODE → addr:156 | <GetByVal>: <Reg8: 1, Reg8: 7, Reg8: 1>
    r1 = param7[r1]
    // CODE → addr:160 | <Call2>: <Reg8: 1, Reg8: 6, Reg8: 0, Reg8: 1>
    r1 = param2.call(undefined, r1)
    // CODE → addr:165 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:170 | <StoreToEnvironment>: <Reg8: 5, UInt8: 4, Reg8: 1>
    r5[4] = r1
    // CODE → addr:174 | <LoadConstUInt8>: <Reg8: 3, UInt8: 5>
    r3 = 5
    // CODE → addr:177 | <GetByVal>: <Reg8: 3, Reg8: 7, Reg8: 3>
    r3 = param7[r3]
    // CODE → addr:181 | <Call2>: <Reg8: 3, Reg8: 6, Reg8: 0, Reg8: 3>
    r3 = param2.call(undefined, r3)
    // CODE → addr:186 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = _interopDefault(param1).call(undefined, r3)
    // CODE → addr:191 | <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → addr:196 | <LoadConstString>: <Reg8: 4, string_id: 7735>  # String: 'count' (Identifier)
    // USED → r4 = "count";
    // CODE → addr:200 | <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    r4 = r3.default.call(r0, "count")
    // CODE → addr:205 | <StoreToEnvironment>: <Reg8: 5, UInt8: 5, Reg8: 4>
    r5[5] = r4
    // CODE → addr:209 | <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → addr:214 | <LoadConstString>: <Reg8: 4, string_id: 1521>  # String: 'instances' (String)
    // USED → r4 = "instances";
    // CODE → addr:218 | <Call2>: <Reg8: 9, Reg8: 6, Reg8: 0, Reg8: 4>
    r9 = r3.default.call(r0, "instances")
    // CODE → addr:223 | <StoreToEnvironment>: <Reg8: 5, UInt8: 6, Reg8: 9>
    r5[6] = r9
    // CODE → addr:227 | <GetByIdShort>: <Reg8: 6, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r6 = r3.default;
    // CODE → addr:232 | <LoadConstString>: <Reg8: 4, string_id: 5021>  # String: 'privateHelper' (String)
    // USED → r4 = "privateHelper";
    // CODE → addr:236 | <Call2>: <Reg8: 4, Reg8: 6, Reg8: 0, Reg8: 4>
    r4 = r3.default.call(r0, "privateHelper")
    // CODE → addr:241 | <StoreToEnvironment>: <Reg8: 5, UInt8: 7, Reg8: 4>
    r5[7] = r4
    // CODE → addr:245 | <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15209>  # Function: [#15209  of 166 bytes]: 1 params @ offset 0x0026bd80
    // USED → r4 = function_15209();
    // CODE → addr:250 | <Call1>: <Reg8: 6, Reg8: 4, Reg8: 0>
    r6 = function_15209().call(undefined)
    // CODE → addr:254 | <StoreToEnvironment>: <Reg8: 5, UInt8: 8, Reg8: 6>
    r5[8] = r6
    // CODE → addr:258 | <TryGetById>: <Reg8: 8, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr:264 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr:269 | <NewObjectWithBuffer>: <Reg8: 4, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 45>  # Object: {'writable': true, 'value': 0}
    r4 = { "writable": true, "value": 0 }
    // CODE → addr:279 | <Call4>: <Reg8: 4, Reg8: 7, Reg8: 8, Reg8: 6, Reg8: 9, Reg8: 4>
    r4 = Object.defineProperty(r6, r9, r4)
    // CODE → addr:286 | <LoadConstUInt8>: <Reg8: 4, UInt8: 100>
    // USED → r4 = 100;
    // CODE → addr:289 | <PutById>: <Reg8: 6, Reg8: 4, UInt8: 2, string_id: 11547>  # String: 'MAX' (Identifier)
    r6.MAX = 100
    // CODE → addr:295 | <GetByIdShort>: <Reg8: 4, Reg8: 3, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r4 = r3.default;
    // CODE → addr:300 | <LoadConstString>: <Reg8: 3, string_id: 7671>  # String: 'label' (Identifier)
    // USED → r3 = "label";
    // CODE → addr:304 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 0, Reg8: 3>
    r3 = r3.default.call(r0, "label")
    // CODE → addr:309 | <StoreToEnvironment>: <Reg8: 5, UInt8: 9, Reg8: 3>
    r5[9] = r3
    // CODE → addr:313 | <CreateClosure>: <Reg8: 4, Reg8: 5, function_id: 15217>  # Function: [#15217  of 81 bytes]: 2 params @ offset 0x0026c046
    // USED → r4 = function_15217(param1);
    // CODE → addr:318 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 0, Reg8: 6>
    r4 = function_15217(param1).call(undefined, r6)
    // CODE → addr:323 | <StoreToEnvironment>: <Reg8: 5, UInt8: 10, Reg8: 4>
    r5[10] = r4
    // CODE → addr:327 | <TryGetById>: <Reg8: 7, Reg8: 2, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r7 = Object;
    // CODE → addr:333 | <GetByIdShort>: <Reg8: 6, Reg8: 7, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r6 = Object.defineProperty;
    // CODE → addr:338 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 2, UInt16: 2, UInt16: 43, UInt16: 219>  # Object: {'writable': true, 'value': 'configured'}
    r5 = { "writable": true, "value": "configured" }
    // CODE → addr:348 | <Call4>: <Reg8: 5, Reg8: 6, Reg8: 7, Reg8: 4, Reg8: 3, Reg8: 5>
    r5 = Object.defineProperty(r4, r3, r5)
    // CODE → addr:355 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 4, string_id: 99>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr:361 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 5, string_id: 90>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr:366 | <LoadConstString>: <Reg8: 2, string_id: 2815>  # String: '__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block' (String)
    // USED → r2 = "__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block";
    // CODE → addr:370 | <Call2>: <Reg8: 2, Reg8: 5, Reg8: 6, Reg8: 2>
    console.log("__BC:Classes/PrivateStaticTests/ConfiguredCounter/static-block")
    // CODE → addr:375 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r1.default;
    // CODE → addr:380 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 0, Reg8: 4, Reg8: 3>
    r2 = r1.default.call(r0, r4, r3)
    // CODE → addr:386 | <GetByIdShort>: <Reg8: 1, Reg8: 1, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r1 = r1.default;
    // CODE → addr:391 | <Call3>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 4, Reg8: 3>
    r1 = r1.default.call(r0, r4, r3)
    // CODE → addr:397 | <GetByVal>: <Reg8: 4, Reg8: 1, Reg8: 3>
    r4 = r1[r3]
    // CODE → addr:401 | <GetById>: <Reg8: 1, Reg8: 4, UInt8: 6, string_id: 10961>  # String: 'toUpperCase' (Identifier)
    // USED → r1 = r4.toUpperCase;
    // CODE → addr:407 | <Call1>: <Reg8: 1, Reg8: 1, Reg8: 4>
    r1 = r4.toUpperCase()
    // CODE → addr:411 | <PutByVal>: <Reg8: 2, Reg8: 3, Reg8: 1>
    r2[r3] = r1
    // CODE → addr:415 | <Ret>: <Reg8: 0>
    return r0;
}