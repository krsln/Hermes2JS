function weakMapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 1, string_id: 4562>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → addr: 22 | <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 7238>  # String: 'WeakMap' (Identifier)
    // USED → r1 = WeakMap;
    // CODE → addr: 28 | <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = WeakMap.prototype;
    // CODE → addr: 33 | <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 1>
    // USED → r2 = CreateThis(r2);
    // CODE → addr: 37 | <Mov>: <Reg8: 8, Reg8: 2>
    // USED → r8 = CreateThis(r2);
    // CODE → addr: 40 | <Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>
    // USED → r1 = new WeakMap();
    // CODE → addr: 44 | <SelectObject>: <Reg8: 5, Reg8: 2, Reg8: 1>
    r5 = new WeakMap()
    // CODE → addr: 48 | <NewObject>: <Reg8: 4>
    r4 = {  }
    // CODE → addr: 50 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r2 = r5.set;
    // CODE → addr: 55 | <LoadConstString>: <Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r1 = "value";
    // CODE → addr: 59 | <Call3>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 4, Reg8: 1>
    r1 = r5.set(r4, "value")
    // CODE → addr: 65 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 71 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 76 | <GetByIdShort>: <Reg8: 1, Reg8: 5, UInt8: 6, string_id: 153>  # String: 'has' (Identifier)
    // USED → r1 = r5.has;
    // CODE → addr: 81 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 5, Reg8: 4>
    r1 = r5.has(r4)
    // CODE → addr: 86 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr: 91 | <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 97 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:102 | <GetByIdShort>: <Reg8: 1, Reg8: 5, UInt8: 7, string_id: 50>  # String: 'get' (Identifier)
    // USED → r1 = r5.get;
    // CODE → addr:107 | <Call2>: <Reg8: 1, Reg8: 1, Reg8: 5, Reg8: 4>
    r1 = r5.get(r4)
    // CODE → addr:112 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log(r1)
    // CODE → addr:117 | <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr:123 | <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = console.log;
    // CODE → addr:128 | <LoadConstString>: <Reg8: 0, string_id: 4560>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → addr:132 | <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → addr:137 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:139 | <Ret>: <Reg8: 0>
    return undefined;
}