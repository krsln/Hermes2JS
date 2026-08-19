function spreadObjectTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → <GetGlobalObject>: <Reg8: 2>
    // USED → r2 = globalThis;
    // CODE → <TryGetById>: <Reg8: 5, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → <LoadConstString>: <Reg8: 3, string_id: 4722>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/start' (String)
    // USED → r3 = "__BC:Arrays/SpreadTests/spreadObjectTest/start";
    // CODE → <Call2>: <Reg8: 3, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/start")
    // CODE → <NewObject>: <Reg8: 5>
    // USED → r5 = {  };
    // CODE → <NewObjectWithBuffer>: <Reg8: 8, UInt16: 61, UInt16: 42665>  # Object: {'x': 1, 'y': 2}
    r8 = { "x": 1, "y": 2 }
    // CODE → <Mov>: <Reg8: 9, Reg8: 5>
    r9 = r5
    // CODE → <CallBuiltin>: <Reg8: 3, UInt8: 46, UInt8: 3>  # Built-in function: [#46 copyDataProperties]
    r3 = copyDataProperties(r0, r1, r2)
    // CODE → <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
    // USED → r0 = 3;
    // CODE → <DefineOwnById>: <Reg8: 5, Reg8: 0, UInt8: 0, UInt16: 6711>
    r5.string_6711 = 3
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <Call2>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 5>
    console.log(r5)
    // CODE → <GetByIdShort>: <Reg8: 6, Reg8: 5, UInt8: 2, string_id: 30>  # String: 'x' (Identifier)
    // USED → r6 = r5.x;
    // CODE → <NewObject>: <Reg8: 9>
    r9 = {  }
    // CODE → <LoadConstNull>: <Reg8: 1>
    // USED → r1 = null;
    // CODE → <NewObjectWithBufferAndParent>: <Reg8: 7, Reg8: 1, UInt32: 1118, UInt32: 17298>
    r7 = {  }
    // CODE → <Mov>: <Reg8: 8, Reg8: 5>
    r8 = r5
    // CODE → <CallBuiltin>: <Reg8: 5, UInt8: 46, UInt8: 4>  # Built-in function: [#46 copyDataProperties]
    // USED → r5 = copyDataProperties(r1, r2, r3, r4);
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <Call3>: <Reg8: 3, Reg8: 3, Reg8: 4, Reg8: 6, Reg8: 5>
    console.log(r5.x, r5)
    // CODE → <TryGetById>: <Reg8: 4, Reg8: 2, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r4 = console;
    // CODE → <GetByIdShort>: <Reg8: 3, Reg8: 4, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r3 = console.log;
    // CODE → <LoadConstString>: <Reg8: 2, string_id: 4721>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/end' (String)
    // USED → r2 = "__BC:Arrays/SpreadTests/spreadObjectTest/end";
    // CODE → <Call2>: <Reg8: 2, Reg8: 3, Reg8: 4, Reg8: 2>
    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/end")
    // CODE → <LoadConstUndefined>: <Reg8: 1>
    // USED → r1 = undefined;
    // CODE → <Ret>: <Reg8: 1>
    return undefined;
}