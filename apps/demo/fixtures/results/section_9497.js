function weakMapTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4746>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r2 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 2, string_id: 6821>  # String: 'WeakMap' (Identifier)
    // USED → r2 = globalThis.WeakMap;
    // CODE → <CreateThisForNew>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = CreateThisForNew(r2);
    // CODE → <Mov>: <Reg8: 9, Reg8: 3>
    // USED → r9 = CreateThisForNew(r2);
    // CODE → <Construct>: <Reg8: 2, Reg8: 2, UInt8: 1>
    // USED → r2 = new globalThis.WeakMap();
    // CODE → <SelectObject>: <Reg8: 6, Reg8: 3, Reg8: 2>
    // USED → r6 = new globalThis.WeakMap();
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 6, UInt8: 4, string_id: 55>  # String: 'set' (Identifier)
    // USED → r3 = new globalThis.WeakMap().set;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 211>  # String: 'value' (Identifier)
    // USED → r2 = "value";
    // CODE → <Call3>: <Reg8: 2, Reg8: 3, Reg8: 6, Reg8: 5, Reg8: 2>
    r2 = new globalThis.WeakMap().set(r5, "value")
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 5, string_id: 11>  # String: 'has' (Identifier)
    // USED → r2 = new globalThis.WeakMap().has;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = new globalThis.WeakMap().has(r5);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 6, UInt8: 6, string_id: 49>  # String: 'get' (Identifier)
    // USED → r2 = new globalThis.WeakMap().get;
    // CODE → <Call2>: <Reg8: 2, Reg8: 2, Reg8: 6, Reg8: 5>
    // USED → r2 = new globalThis.WeakMap().get(r5);
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log(r2)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 3088>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}