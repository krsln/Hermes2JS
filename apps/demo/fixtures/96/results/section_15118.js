function spreadArrayTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetGlobalObject>: <Reg8: 1>
    // USED → r1 = globalThis;
    // CODE → addr:  2 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:  8 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 13 | <LoadConstString>: <Reg8: 0, string_id: 4523>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/start' (String)
    // USED → r0 = "__BC:Arrays/SpreadTests/spreadArrayTest/start";
    // CODE → addr: 17 | <Call2>: <Reg8: 0, Reg8: 2, Reg8: 3, Reg8: 0>
    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/start")
    // CODE → addr: 22 | <NewArrayWithBuffer>: <Reg8: 2, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
    r2 = [1, 2, 3]
    // CODE → addr: 30 | <NewArray>: <Reg8: 3, UInt16: 0>
    // USED → r3 = [];
    // CODE → addr: 34 | <LoadConstZero>: <Reg8: 0>
    r0 = 0
    // CODE → addr: 42 | <LoadConstZero>: <Reg8: 7>
    r7 = 0
    // CODE → addr: 44 | <CallBuiltin>: <Reg8: 7, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r7 = arraySpread(r3, r4, r5, r6)
    // CODE → addr: 48 | <NewArrayWithBuffer>: <Reg8: 8, UInt16: 3, UInt16: 3, UInt16: 23671>  # Array: [4, 5, 6]
    r8 = [4, 5, 6]
    // CODE → addr: 59 | <CallBuiltin>: <Reg8: 4, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r4 = arraySpread(r0, r1, r2, r3)
    // CODE → addr: 63 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr: 69 | <GetByIdShort>: <Reg8: 4, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r4 = console.log;
    // CODE → addr: 74 | <Call2>: <Reg8: 4, Reg8: 4, Reg8: 5, Reg8: 3>
    console.log(r3)
    // CODE → addr: 79 | <NewArrayWithBuffer>: <Reg8: 6, UInt16: 2, UInt16: 1, UInt16: 18648>  # Array: [0]
    // USED → r6 = [0];
    // CODE → addr: 87 | <LoadConstUInt8>: <Reg8: 4, UInt8: 1>
    // USED → r4 = 1;
    // CODE → addr: 90 | <Mov>: <Reg8: 9, Reg8: 6>
    r9 = r6
    // CODE → addr: 93 | <Mov>: <Reg8: 8, Reg8: 2>
    r8 = r2
    // CODE → addr: 96 | <Mov>: <Reg8: 7, Reg8: 4>
    r7 = 1
    // CODE → addr: 99 | <CallBuiltin>: <Reg8: 2, UInt8: 46, UInt8: 4>  # Built-in function: [#46 arraySpread]
    r2 = arraySpread(r-2, r-1, r0, r1)
    // CODE → addr:103 | <LoadConstUInt8>: <Reg8: 5, UInt8: 99>
    // USED → r5 = 99;
    // CODE → addr:106 | <PutOwnByVal>: <Reg8: 6, Reg8: 5, Reg8: 2, UInt8: 1>
    r6[r2] = 99
    // CODE → addr:111 | <Add>: <Reg8: 2, Reg8: 2, Reg8: 4>
    r2 = r2 + 1
    // CODE → addr:115 | <TryGetById>: <Reg8: 5, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r5 = console;
    // CODE → addr:121 | <GetByIdShort>: <Reg8: 2, Reg8: 5, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:126 | <Call2>: <Reg8: 2, Reg8: 2, Reg8: 5, Reg8: 6>
    console.log(r6)
    // CODE → addr:131 | <GetByVal>: <Reg8: 5, Reg8: 3, Reg8: 0>
    // USED → r5 = r3[r0];
    // CODE → addr:135 | <GetEnvironment>: <Reg8: 0, UInt8: 0>
    r0 = getEnvironment(0)
    // CODE → addr:138 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 0, UInt8: 2>
    r0 = r0[2]
    // CODE → addr:142 | <GetByIdShort>: <Reg8: 2, Reg8: 0, UInt8: 3, string_id: 107>  # String: 'default' (Identifier)
    // USED → r2 = r0.default;
    // CODE → addr:147 | <LoadConstUndefined>: <Reg8: 0>
    // USED → r0 = undefined;
    // CODE → addr:149 | <Call2>: <Reg8: 3, Reg8: 2, Reg8: 0, Reg8: 3>
    r3 = r0.default(r3)
    // CODE → addr:154 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 4, string_id: 227>  # String: 'slice' (Identifier)
    // USED → r2 = r3.slice;
    // CODE → addr:159 | <Call2>: <Reg8: 4, Reg8: 2, Reg8: 3, Reg8: 4>
    // USED → r4 = r3.slice(1);
    // CODE → addr:164 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:170 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:175 | <Call3>: <Reg8: 2, Reg8: 2, Reg8: 3, Reg8: 5, Reg8: 4>
    console.log(r5, r4)
    // CODE → addr:181 | <TryGetById>: <Reg8: 3, Reg8: 1, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr:187 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr:192 | <LoadConstString>: <Reg8: 1, string_id: 4521>  # String: '__BC:Arrays/SpreadTests/spreadArrayTest/end' (String)
    // USED → r1 = "__BC:Arrays/SpreadTests/spreadArrayTest/end";
    // CODE → addr:196 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Arrays/SpreadTests/spreadArrayTest/end")
    // CODE → addr:201 | <Ret>: <Reg8: 0>
    return undefined;
}