function function_15194(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 4, UInt8: 2>
    // USED → r4 = param2;
    // CODE → addr:  5 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  8 | <LoadParam>: <Reg8: 5, UInt8: 7>
    // USED → r5 = param7;
    // CODE → addr: 11 | <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15195>  # Function: [#15195 _interopDefault of 28 bytes]: 2 params @ offset 0x00104cff
    // USED → r3 = _interopDefault(param1);
    // CODE → addr: 16 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr: 18 | <TryGetById>: <Reg8: 8, Reg8: 0, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr: 24 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr: 29 | <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → addr: 31 | <LoadConstTrue>: <Reg8: 0>
    // USED → r0 = true;
    // CODE → addr: 33 | <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 0, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → addr: 37 | <LoadConstString>: <Reg8: 0, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r0 = "__esModule";
    // CODE → addr: 41 | <Call4>: <Reg8: 0, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 0, Reg8: 6>
    r0 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → addr: 48 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15196>  # Function: [#15196 classTest of 193 bytes]: 1 params @ offset 0x0026b75b
    // USED → r0 = classTest();
    // CODE → addr: 53 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 1, string_id: 10812>  # String: 'classTest' (Identifier)
    param6.classTest = classTest()
    // CODE → addr: 59 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 61 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 0>
    // USED → r1 = param7[r0];
    // CODE → addr: 65 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 67 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr: 72 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr: 77 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r1
    // CODE → addr: 81 | <LoadConstUInt8>: <Reg8: 1, UInt8: 1>
    r1 = 1
    // CODE → addr: 84 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → addr: 88 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr: 93 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr: 98 | <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 1>
    r2[1] = r1
    // CODE → addr:102 | <LoadConstUInt8>: <Reg8: 1, UInt8: 2>
    r1 = 2
    // CODE → addr:105 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → addr:109 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr:114 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:119 | <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 1>
    r2[2] = r1
    // CODE → addr:123 | <LoadConstUInt8>: <Reg8: 1, UInt8: 3>
    r1 = 3
    // CODE → addr:126 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → addr:130 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr:135 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:140 | <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 1>
    r2[3] = r1
    // CODE → addr:144 | <LoadConstUInt8>: <Reg8: 1, UInt8: 4>
    r1 = 4
    // CODE → addr:147 | <GetByVal>: <Reg8: 1, Reg8: 5, Reg8: 1>
    // USED → r1 = param7[r1];
    // CODE → addr:151 | <Call2>: <Reg8: 1, Reg8: 4, Reg8: 0, Reg8: 1>
    // USED → r1 = param2.call(undefined, r1);
    // CODE → addr:156 | <Call2>: <Reg8: 1, Reg8: 3, Reg8: 0, Reg8: 1>
    r1 = _interopDefault(param1).call(undefined, r1)
    // CODE → addr:161 | <StoreToEnvironment>: <Reg8: 2, UInt8: 4, Reg8: 1>
    r2[4] = r1
    // CODE → addr:165 | <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15197>  # Function: [#15197  of 83 bytes]: 1 params @ offset 0x0026b81c
    // USED → r1 = function_15197();
    // CODE → addr:170 | <Call1>: <Reg8: 3, Reg8: 1, Reg8: 0>
    // USED → r3 = function_15197().call(undefined);
    // CODE → addr:174 | <StoreToEnvironment>: <Reg8: 2, UInt8: 5, Reg8: 3>
    r2[5] = r3
    // CODE → addr:178 | <CreateClosure>: <Reg8: 1, Reg8: 2, function_id: 15201>  # Function: [#15201  of 106 bytes]: 2 params @ offset 0x0026b92e
    // USED → r1 = function_15201(param1);
    // CODE → addr:183 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 0, Reg8: 3>
    r1 = function_15201(param1).call(undefined, r3)
    // CODE → addr:188 | <StoreToEnvironment>: <Reg8: 2, UInt8: 6, Reg8: 1>
    r2[6] = r1
    // CODE → addr:192 | <Ret>: <Reg8: 0>
    return undefined;
}