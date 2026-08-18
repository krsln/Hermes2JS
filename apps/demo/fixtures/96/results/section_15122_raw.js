function function_15122(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 15123>  # Function: [#15123 mapTest of 311 bytes]: 1 params @ offset 0x00269f5f
    // USED → r4 = mapTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 4>
    r2[1] = mapTest()
    // CODE → <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15124>  # Function: [#15124 setTest of 217 bytes]: 1 params @ offset 0x0026a096
    // USED → r3 = setTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 3>
    r2[2] = setTest()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15125>  # Function: [#15125 weakMapTest of 141 bytes]: 1 params @ offset 0x0026a16f
    // USED → r0 = weakMapTest();
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 0>
    r2[3] = weakMapTest()
    // CODE → <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r5 = "__esModule";
    // CODE → <Call4>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 5, Reg8: 6>
    r5 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → <PutById>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 10859>  # String: 'mapTest' (Identifier)
    param6.mapTest = mapTest()
    // CODE → <PutById>: <Reg8: 1, Reg8: 3, UInt8: 2, string_id: 10864>  # String: 'setTest' (Identifier)
    param6.setTest = setTest()
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10868>  # String: 'weakMapTest' (Identifier)
    param6.weakMapTest = weakMapTest()
    // CODE → <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15126>  # Function: [#15126 callMapSetTests of 73 bytes]: 1 params @ offset 0x0026a1fc
    // USED → r0 = callMapSetTests();
    // CODE → <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 7228>  # String: 'callMapSetTests' (Identifier)
    param6.callMapSetTests = callMapSetTests()
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 7>
    // USED → r1 = param7;
    // CODE → <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 0>
    // USED → r3 = param7[r0];
    // CODE → <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call2>: <Reg8: 4, Reg8: 1, Reg8: 0, Reg8: 3>
    r4 = param2.call(undefined, r3)
    // CODE → <JmpFalse>: <Addr8: 14, Reg8: 4>  # Address: 0000007e
    // → r4 = param2.call(undefined, r3)
    if (!r4) goto label_126;
    // ──────────────── Block 1 ──────────────── 
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r3 = r4.__esModule;
    // CODE → <Mov>: <Reg8: 1, Reg8: 4>
    r1 = r4
    // CODE → <JmpTrue>: <Addr8: 12, Reg8: 3>  # Address: 00000087
    if (r4.__esModule) goto label_135;
    // ──────────────── Block 2 ──────────────── 
    // CODE → <NewObject>: <Reg8: 3>
    r3 = {  }
    // CODE → <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 4, string_id: 107>  # String: 'default' (Identifier)
    r3.default = r4
    // CODE → <Mov>: <Reg8: 1, Reg8: 3>
    // USED → r1 = r3;
    // ──────────────── Block 3 ──────────────── 
    // CODE → <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r3
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}