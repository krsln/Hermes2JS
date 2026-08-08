function weakMapTest(param0) {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 0>
    // USED → r0 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4562>  # String: '__BC:Collections/MapSetTests/weakMapTest/start' (String)
    // USED → r1 = "__BC:Collections/MapSetTests/weakMapTest/start";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log("__BC:Collections/MapSetTests/weakMapTest/start")
    // CODE → <TryGetById>: <Reg8: 1, Reg8: 0, UInt8: 3, string_id: 7238>  # String: 'WeakMap' (Identifier)
    // USED → r1 = globalThis.WeakMap;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 1, UInt8: 4, string_id: 206>  # String: 'prototype' (Identifier)
    // USED → r2 = globalThis.WeakMap.prototype;
    // CODE → <CreateThis>: <Reg8: 2, Reg8: 2, Reg8: 1>
    // USED → r2 = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap);
    // CODE → <Mov>: <Reg8: 8, Reg8: 2>
    r8 = createThis(globalThis.WeakMap.prototype, globalThis.WeakMap)
    // CODE → <Construct>: <Reg8: 1, Reg8: 1, UInt8: 1>
    // USED → r1 = new globalThis.WeakMap();
    // CODE → <SelectObject>: <Reg8: 5, Reg8: 2, Reg8: 1>
    // USED → r5 = new globalThis.WeakMap();
    // CODE → <NewObject>: <Reg8: 4>
    r4 = {  }
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 5, string_id: 185>  # String: 'set' (Identifier)
    // USED → r2 = new globalThis.WeakMap().set;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 205>  # String: 'value' (Identifier)
    // USED → r1 = "value";
    // CODE → <Call3>: <Reg8: 1, Reg8: 2, Reg8: 5, Reg8: 4, Reg8: 1>
    r1 = new globalThis.WeakMap().set(r4, "value")
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 5, UInt8: 6, string_id: 153>  # String: 'has' (Identifier)
    // USED → r1 = new globalThis.WeakMap().has;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 5, Reg8: 4>
    // USED → r1 = new globalThis.WeakMap().has(r4);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log(new globalThis.WeakMap().has(r4))
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = globalThis.console.log;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 5, UInt8: 7, string_id: 50>  # String: 'get' (Identifier)
    // USED → r1 = new globalThis.WeakMap().get;
    // CODE → <Call2>: <Reg8: 1, Reg8: 1, Reg8: 5, Reg8: 4>
    // USED → r1 = new globalThis.WeakMap().get(r4);
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    r1 = globalThis.console.log(new globalThis.WeakMap().get(r4))
    // CODE → <TryGetById>: <Reg8: 2, Reg8: 0, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = globalThis.console;
    // CODE → <GetByIdShort>: <Reg8: 1, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r1 = globalThis.console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4560>  # String: '__BC:Collections/MapSetTests/weakMapTest/end' (String)
    // USED → r0 = "__BC:Collections/MapSetTests/weakMapTest/end";
    // CODE → <Call2>: <Reg8: 0, Reg8: 1, Reg8: 2, Reg8: 0>
    r0 = globalThis.console.log("__BC:Collections/MapSetTests/weakMapTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}