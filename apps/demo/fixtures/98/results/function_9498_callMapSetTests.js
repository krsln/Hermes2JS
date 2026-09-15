function callMapSetTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → addr:  3 | <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → addr:  5 | <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → addr: 11 | <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → addr: 16 | <LoadConstString>: <Reg8: 4, string_id: 4736>  # String: '__BC:Collections/MapSetTests/callMapSetTests/start' (String)
    // USED → r4 = "__BC:Collections/MapSetTests/callMapSetTests/start";
    // CODE → addr: 20 | <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/start")
    // CODE → addr: 25 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
    // USED → r4 = r3[0];
    // CODE → addr: 29 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr: 31 | <Call1>: <Reg8: 1, Reg8: 4, Reg8: 0>
    r1 = r3[0].call(r0)
    // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = r3[1];
    // CODE → addr: 39 | <Call1>: <Reg8: 1, Reg8: 3, Reg8: 0>
    r1 = r3[1].call(r0)
    // CODE → addr: 43 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 49 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 54 | <LoadConstString>: <Reg8: 3, string_id: 4746>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → addr: 58 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → addr: 63 | <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 6821>  # String: 'WeakMap' (Identifier)
    // USED → r3 = WeakMap;
    // CODE → addr: 69 | <CreateThisForNew>: <Reg8: 4, Reg8: 3, UInt8: 3>
    // USED → r4 = CreateThisForNew(r3);
    // CODE → addr: 73 | <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = CreateThisForNew(r3);
    // CODE → addr: 76 | <Construct>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = new WeakMap();
    // CODE → addr: 80 | <SelectObject>: <Reg8: 7, Reg8: 4, Reg8: 3>
    r7 = new WeakMap()
    // CODE → addr: 84 | <NewObject>: <Reg8: 6>
    r6 = {  }
    // CODE → addr: 86 | <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r4 = r7.set;
    // CODE → addr: 91 | <LoadConstString>: <Reg8: 3, string_id: 211>  # String: 'value' (Identifier)
    // USED → r3 = "value";
    // CODE → addr: 95 | <Call3>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 6, Reg8: 3>
    r3 = r7.set(r6, "value")
    // CODE → addr:101 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:107 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:112 | <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 5, string_id: 11>  # String: 'has' (Identifier)
    // USED → r3 = r7.has;
    // CODE → addr:117 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    r3 = r7.has(r6)
    // CODE → addr:122 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → addr:127 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:133 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:138 | <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 6, string_id: 49>  # String: 'get' (Identifier)
    // USED → r3 = r7.get;
    // CODE → addr:143 | <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    r3 = r7.get(r6)
    // CODE → addr:148 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → addr:153 | <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:159 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr:164 | <LoadConstString>: <Reg8: 3, string_id: 3088>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → addr:168 | <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → addr:173 | <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → addr:179 | <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → addr:184 | <LoadConstString>: <Reg8: 2, string_id: 293>  # String: '__BC:Collections/MapSetTests/callMapSetTests/end' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/callMapSetTests/end";
    // CODE → addr:188 | <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/end")
    // CODE → addr:193 | <Ret>: <Reg8: 0>
    return undefined;
}