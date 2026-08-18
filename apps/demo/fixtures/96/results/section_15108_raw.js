function callDestructuringTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 0, string_id: 4805>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/start' (String)
    // USED → r0 = "__BC:Objects/DestructuringTests/callDestructuringTests/start";
    // CODE → <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/start")
    // CODE → <GetEnvironment>: <Reg8: 2, UInt8: 0>
    r2 = getEnvironment(0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 2>
    // USED → r3 = r2[2];
    // CODE → <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = r2[2].call(r0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 3>
    // USED → r3 = r2[3];
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = r2[3].call(r0)
    // CODE → <LoadFromEnvironment>: <Reg8: 3, Reg8: 2, UInt8: 4>
    // USED → r3 = r2[4];
    // CODE → <Call1>: <Reg8: 3, Reg8: 3, Reg8: 0>
    r3 = r2[4].call(r0)
    // CODE → <LoadFromEnvironment>: <Reg8: 5, Reg8: 2, UInt8: 5>
    // USED → r5 = r2[5];
    // CODE → <NewObject>: <Reg8: 4>
    // USED → r4 = {  };
    // CODE → <LoadConstUInt8>: <Reg8: 3, UInt8: 7>
    // USED → r3 = 7;
    // CODE → <PutNewOwnByIdShort>: <Reg8: 4, Reg8: 3, string_id: 29>  # String: 'id' (Identifier)
    r4.id = 7
    // CODE → <NewArrayWithBuffer>: <Reg8: 3, UInt16: 2, UInt16: 2, UInt16: 23660>  # Array: [9, 10]
    // USED → r3 = [9, 10];
    // CODE → <Call3>: <Reg8: 3, Reg8: 5, Reg8: 0, Reg8: 4, Reg8: 3>
    r3 = r2[5].call(r0, r4, r3)
    // CODE → <LoadFromEnvironment>: <Reg8: 2, Reg8: 2, UInt8: 6>
    // USED → r2 = r2[6];
    // CODE → <Call1>: <Reg8: 2, Reg8: 2, Reg8: 0>
    r2 = r2[6].call(r0)
    // CODE → <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → <LoadConstString>: <Reg8: 1, string_id: 4291>  # String: '__BC:Objects/DestructuringTests/callDestructuringTests/end' (String)
    // USED → r1 = "__BC:Objects/DestructuringTests/callDestructuringTests/end";
    // CODE → <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Objects/DestructuringTests/callDestructuringTests/end")
    // CODE → <Ret>: <Reg8: 0>
    return undefined;
}