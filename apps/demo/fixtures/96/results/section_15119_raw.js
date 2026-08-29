function spreadObjectTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4529>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadObjectTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/start")
    // CODE → addr: 22 | <NewObject>: <Reg8: 4>
    // USED → r4 = {  };
    // CODE → addr: 24 | <NewObjectWithBuffer>: <Reg8: 6, UInt16: 2, UInt16: 2, UInt16: 317, UInt16: 19852>  # Object: {'x': 1, 'y': 2}
    r6 = { "x": 1, "y": 2 }
    // CODE → addr: 34 | <Mov>: <Reg8: 7, Reg8: 4>
    r7 = r4
    // CODE → addr: 37 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 3>  # Built-in function: [#44 copyDataProperties]
    r0 = copyDataProperties(r-3, r-2, r-1)
    // CODE → addr: 41 | <LoadConstUInt8>: <Reg8: 2, UInt8: 3>
    // USED → r2 = 3;
    // CODE → addr: 44 | <LoadConstString>: <Reg8: 0, string_id: 7612>  # String: 'z' (Identifier)
    // USED → r0 = "z";
    // CODE → addr: 48 | <PutOwnByVal>: <Reg8: 4, Reg8: 2, Reg8: 0, UInt8: 1>
    r4["z"] = 3
    // CODE → addr: 53 | <TryGetById>: <Reg8: 2, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r2 = console;
    // CODE → addr: 59 | <GetByIdShort>: <Reg8: 0, Reg8: 2, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r0 = console.log;
    // CODE → addr: 64 | <Call2>: <Reg8: 0, Reg8: 0, Reg8: 2, Reg8: 4>
    console.log(r4)
    // CODE → addr: 69 | <GetByIdShort>: <Reg8: 5, Reg8: 4, UInt8: 3, string_id: 41>  # String: 'x' (Identifier)
    // USED → r5 = r4.x;
    // CODE → addr: 74 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr: 77 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 1>
    r2 = r0[1]
    // CODE → addr: 81 | <GetByIdShort>: <Reg8: 3, Reg8: 2, UInt8: 4, string_id: 107>  # String: 'default' (Identifier)
    // USED → r3 = r2.default;
    // CODE → addr: 86 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 0, UInt8: 0>
    // USED → r2 = r0[0];
    // CODE → addr: 90 | <LoadConstUndefined>: <Reg8: 0>
    r0 = undefined
    // CODE → addr: 92 | <Call3>: <Reg8: 4, Reg8: 3, Reg8: 0, Reg8: 4, Reg8: 2>
    // USED → r4 = r2.default.call(r0, r4, r2);
    // CODE → addr: 98 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:104 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:109 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r4.x, r4)
    // CODE → addr:115 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:126 | <LoadConstString>: <Reg8: 1, string_id: 4527>  # String: '__BC:Arrays/SpreadTests/spreadObjectTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadObjectTest/end";
    // CODE → addr:130 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Arrays/SpreadTests/spreadObjectTest/end")
    // CODE → addr:135 | <Ret>: <Reg8: 0>
    return r0;
}