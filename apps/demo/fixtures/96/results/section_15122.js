function function_15122(param1, param2, param3, param4, param5, param6, param7) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <CreateEnvironment>: <Reg8: 2>
    r2 = createEnvironment()
    // CODE → addr:  2 | <LoadParam>: <Reg8: 1, UInt8: 6>
    // USED → r1 = param6;
    // CODE → addr:  5 | <CreateClosure>: <Reg8: 4, Reg8: 2, function_id: 15123>  # Function: [#15123 mapTest of 311 bytes]: 1 params @ offset 0x00269f5f
    // USED → r4 = mapTest();
    // CODE → addr: 10 | <StoreToEnvironment>: <Reg8: 2, UInt8: 1, Reg8: 4>
    r2[1] = mapTest()
    // CODE → addr: 14 | <CreateClosure>: <Reg8: 3, Reg8: 2, function_id: 15124>  # Function: [#15124 setTest of 217 bytes]: 1 params @ offset 0x0026a096
    // USED → r3 = setTest();
    // CODE → addr: 19 | <StoreToEnvironment>: <Reg8: 2, UInt8: 2, Reg8: 3>
    r2[2] = setTest()
    // CODE → addr: 23 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15125>  # Function: [#15125 weakMapTest of 141 bytes]: 1 params @ offset 0x0026a16f
    // USED → r0 = weakMapTest();
    // CODE → addr: 28 | <StoreToEnvironment>: <Reg8: 2, UInt8: 3, Reg8: 0>
    r2[3] = weakMapTest()
    // CODE → addr: 32 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr: 34 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 1, string_id: 24>  # String: 'Object' (Identifier)
    // USED → r8 = Object;
    // CODE → addr: 40 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 108>  # String: 'defineProperty' (Identifier)
    // USED → r7 = Object.defineProperty;
    // CODE → addr: 45 | <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → addr: 47 | <LoadConstTrue>: <Reg8: 5>
    // USED → r5 = true;
    // CODE → addr: 49 | <PutNewOwnByIdShort>: <Reg8: 6, Reg8: 5, string_id: 205>  # String: 'value' (Identifier)
    r6.value = true
    // CODE → addr: 53 | <LoadConstString>: <Reg8: 5, string_id: 48>  # String: '__esModule' (Identifier)
    // USED → r5 = "__esModule";
    // CODE → addr: 57 | <Call4>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 1, Reg8: 5, Reg8: 6>
    r5 = Object.defineProperty(param6, "__esModule", r6)
    // CODE → addr: 64 | <PutById>: <Reg8: 1, Reg8: 4, UInt8: 1, string_id: 10859>  # String: 'mapTest' (Identifier)
    param6.mapTest = mapTest()
    // CODE → addr: 70 | <PutById>: <Reg8: 1, Reg8: 3, UInt8: 2, string_id: 10864>  # String: 'setTest' (Identifier)
    param6.setTest = setTest()
    // CODE → addr: 76 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 10868>  # String: 'weakMapTest' (Identifier)
    param6.weakMapTest = weakMapTest()
    // CODE → addr: 82 | <CreateClosure>: <Reg8: 0, Reg8: 2, function_id: 15126>  # Function: [#15126 callMapSetTests of 73 bytes]: 1 params @ offset 0x0026a1fc
    // USED → r0 = callMapSetTests();
    // CODE → addr: 87 | <PutById>: <Reg8: 1, Reg8: 0, UInt8: 4, string_id: 7228>  # String: 'callMapSetTests' (Identifier)
    param6.callMapSetTests = callMapSetTests()
    // CODE → addr: 93 | <LoadParam>: <Reg8: 1, UInt8: 7>
    // USED → r1 = param7;
    // CODE → addr: 96 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 98 | <GetByVal>: <Reg8: 3, Reg8: 1, Reg8: 0>
    r3 = param7[r0]
    // CODE → addr:102 | <LoadParam>: <Reg8: 1, UInt8: 2>
    // USED → r1 = param2;
    // CODE → addr:105 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:107 | <Call2>: <Reg8: 4, Reg8: 1, Reg8: 0, Reg8: 3>
    r4 = param2.call(undefined, r3)
    // → r4 = param2.call(undefined, r3)
    if (!r4) {
        // ──────────────── Block 2 ──────────────── 
        // CODE → addr:126 | <NewObject>: <Reg8: 3>
        r3 = {  }
        // CODE → addr:128 | <PutNewOwnByIdShort>: <Reg8: 3, Reg8: 4, string_id: 107>  # String: 'default' (Identifier)
        r3.default = r4
        // CODE → addr:132 | <Mov>: <Reg8: 1, Reg8: 3>
        // USED → r1 = r3;
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr:115 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 3, string_id: 48>  # String: '__esModule' (Identifier)
        // USED → r3 = r4.__esModule;
        // CODE → addr:120 | <Mov>: <Reg8: 1, Reg8: 4>
        r1 = r4
    }
    // ──────────────── Block 3 ──────────────── 
    // CODE → addr:135 | <StoreToEnvironment>: <Reg8: 2, UInt8: 0, Reg8: 1>
    r2[0] = r3
    // CODE → addr:139 | <Ret>: <Reg8: 0>
    return undefined;
}