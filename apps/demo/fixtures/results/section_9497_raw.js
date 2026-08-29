function weakMapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 2, string_id: 4746>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 6821>  # String: 'WeakMap' (Identifier)
    // USED → r2 = WeakMap;
    // CODE → addr: 28 | <CreateThisForNew>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = CreateThisForNew(r2);
    // CODE → addr: 32 | <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = CreateThisForNew(r2);
    // CODE → addr: 35 | <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new WeakMap();
    // CODE → addr: 39 | <SelectObject>: <Reg8: 6, Reg8: 3, Reg8: 2>
    r6 = new WeakMap()
    // CODE → addr: 43 | <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → addr: 45 | <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r3 = r6.set;
    // CODE → addr: 50 | <LoadConstString>: <Reg8: 2, string_id: 211>  # String: 'value' (Identifier)
    // USED → r2 = "value";
    // CODE → addr: 54 | <Call3>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 2>
    r2 = r6.set(r5, "value")
    // CODE → addr: 60 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 66 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 5, string_id: 11>  # String: 'has' (Identifier)
    // USED → r2 = r6.has;
    // CODE → addr: 76 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = r6.has(r5);
    // CODE → addr: 81 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr: 86 | <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr: 92 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 6, string_id: 49>  # String: 'get' (Identifier)
    // USED → r2 = r6.get;
    // CODE → addr:102 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = r6.get(r5);
    // CODE → addr:107 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → addr:112 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:118 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:123 | <LoadConstString>: <Reg8: 1, string_id: 3088>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → addr:127 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → addr:132 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr:134 | <Ret>: <Reg8: 0>
    return r0;
}