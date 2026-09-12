async function* anon_15193() {
    // ──────────────── Block 1 ──────────────── 
    // CODE → addr: 10 | <GetGlobalObject>: <Reg8: 6>
    // USED → r6 = globalThis;
    // CODE → addr: 12 | <TryGetById>: <Reg8: 3, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r3 = console;
    // CODE → addr: 18 | <GetByIdShort>: <Reg8: 2, Reg8: 3, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r2 = console.log;
    // CODE → addr: 23 | <LoadConstString>: <Reg8: 1, string_id: 4759>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
    // USED → r1 = "__BC:Functions/AsyncTests/callAsyncTests/start";
    // CODE → addr: 27 | <Call2>: <Reg8: 1, Reg8: 2, Reg8: 3, Reg8: 1>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
    // CODE → addr: 32 | <GetEnvironment>: <Reg8: 4, UInt8: 2>
    r4 = getEnvironment(2)
    // CODE → addr: 35 | <LoadFromEnvironment>: <Reg8: 1, Reg8: 4, UInt8: 3>
    // USED → r1 = r4[3];
    // CODE → addr: 39 | <LoadConstUndefined>: <Reg8: 5>
    // USED → r5 = undefined;
    // CODE → addr: 45 | <SaveGenerator>: <Addr8: 4>  # Address: 00000031
    yield await r4[3].call(r5)
    // ──────────────── Block 4 ──────────────── 
    // CODE → addr: 55 | <LoadFromEnvironment>: <Reg8: 2, Reg8: 4, UInt8: 5>
    // USED → r2 = r4[5];
    // CODE → addr: 63 | <SaveGenerator>: <Addr8: 4>  # Address: 00000043
    yield await r4[5].call(r5)
    // ──────────────── Block 7 ──────────────── 
    // CODE → addr: 73 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 4, UInt8: 7>
    // USED → r7 = r4[7];
    // CODE → addr: 77 | <NewArrayWithBuffer>: <Reg8: 3, UInt16: 3, UInt16: 3, UInt16: 23374>  # Array: [1, 2, 3]
    r3 = [1, 2, 3]
    // CODE → addr: 90 | <SaveGenerator>: <Addr8: 4>  # Address: 0000005e
    yield await r4[7].call(r5, r3)
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:100 | <LoadFromEnvironment>: <Reg8: 4, Reg8: 4, UInt8: 9>
    // USED → r4 = r4[9];
    // CODE → addr:108 | <SaveGenerator>: <Addr8: 4>  # Address: 00000070
    yield await r4[9].call(r5)
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:118 | <TryGetById>: <Reg8: 8, Reg8: 6, UInt8: 1, string_id: 99>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:124 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 2, string_id: 90>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:129 | <LoadConstString>: <Reg8: 6, string_id: 2895>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
    // USED → r6 = "__BC:Functions/AsyncTests/callAsyncTests/end";
    // CODE → addr:133 | <Call2>: <Reg8: 6, Reg8: 7, Reg8: 8, Reg8: 6>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
    // CODE → addr:139 | <Ret>: <Reg8: 5>
    return undefined;
}