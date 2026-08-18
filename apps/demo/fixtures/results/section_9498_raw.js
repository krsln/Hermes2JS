function callMapSetTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetParentEnvironment>: <Reg8: 3, UInt8: 0>
    r3 = getParentEnvironment(0)
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 6, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r6 = console;
    // CODE → <GetByIdShort>: <Reg8: 5, Reg8: 6, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r5 = console.log;
    // CODE → <LoadConstString>: <Reg8: 4, string_id: 4736>  # String: '__BC:Collections/MapSetTests/callMapSetTests/start' (String)
    // USED → r4 = "__BC:Collections/MapSetTests/callMapSetTests/start";
    // CODE → <Call2>: <Reg8: 4, Reg8: 5, Reg8: 6, Reg8: 4>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/start")
    // CODE → <LoadFromEnvironment>: <Reg8: 4, Reg8: 3, UInt8: 0>
    // USED → r4 = r3[0];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 1, Reg8: 4, Reg8: 0>
    r1 = r3[0].call(r0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = r3[1];
    // CODE → <Call1>: <Reg8: 1, Reg8: 3, Reg8: 0>
    r1 = r3[1].call(r0)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4746>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 2, UInt8: 2, string_id: 6821>  # String: 'WeakMap' (Identifier)
    // USED → r3 = WeakMap;
    // CODE → <CreateThisForNew>: <Reg8: 4, Reg8: 3, UInt8: 3>
    // USED → r4 = CreateThisForNew(r3);
    // CODE → <Mov>: <Reg8: 10, Reg8: 4>
    // USED → r10 = CreateThisForNew(r3);
    // CODE → <Construct>: <Reg8: 3, Reg8: 3, UInt8: 1>
    // USED → r3 = new WeakMap();
    // CODE → <SelectObject>: <Reg8: 7, Reg8: 4, Reg8: 3>
    r7 = new WeakMap()
    // CODE → <NewObject>: <Reg8: 6>
    // USED → r6 = {  };
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 7, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r4 = r7.set;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 211>  # String: 'value' (Identifier)
    // USED → r3 = "value";
    // CODE → <Call3>: <Reg8: 3, Reg8: 4, Reg8: 7, Reg8: 6, Reg8: 3>
    r3 = r7.set(r6, "value")
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 5, string_id: 11>  # String: 'has' (Identifier)
    // USED → r3 = r7.has;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    // USED → r3 = r7.has(r6);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 7, UInt8: 6, string_id: 49>  # String: 'get' (Identifier)
    // USED → r3 = r7.get;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 7, Reg8: 6>
    // USED → r3 = r7.get(r6);
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 3088>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r3 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 293>  # String: '__BC:Collections/MapSetTests/callMapSetTests/end' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/callMapSetTests/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/callMapSetTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}