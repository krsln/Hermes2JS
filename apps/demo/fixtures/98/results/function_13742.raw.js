async function _anon_0_simpleAsyncTest() {
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 67 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 0>
    // USED → r5 = r1[0];
    // CODE → addr: 71 | <StoreToEnvironment>: <Reg8: 5, UInt8: 0, Reg8: 0>
    r1[0][0] = param2
    // CODE → addr: 75 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr: 77 | <TryGetById>: <Reg8: 11, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r11 = console;
    // CODE → addr: 83 | <GetByIdShort>: <Reg8: 10, Reg8: 11, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r10 = console.log;
    // CODE → addr: 88 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 5, UInt8: 0>
    r8 = r1[0][0]
    // CODE → addr: 92 | <Call2>: <Reg8: 8, Reg8: 10, Reg8: 11, Reg8: 8>
    console.log(r8)
    // CODE → addr: 97 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:103 | <GetByIdShort>: <Reg8: 8, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:108 | <LoadConstString>: <Reg8: 7, string_id: 4923>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/end' (String)
    // USED → r7 = "__BC:Functions/AsyncTests/simpleAsyncTest/end";
    // CODE → addr:112 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 10, Reg8: 7>
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/end")
    // CODE → addr:117 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 5, UInt8: 0>
    // USED → r7 = r1[0][0];
    // CODE → addr:121 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:124 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:128 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:134 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
    r5.slot_0 = r1[0][0]
    // CODE → addr:138 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 10 ──────────────── 
    // CODE → addr:179 | <CreateTopLevelEnvironment>: <Reg8: 8, UInt32: 1>
    // USED → r8 = __environment__;
    // CODE → addr:185 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 8>
    r1[0] = __environment__
    // CODE → addr:189 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:191 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 7>
    __environment__[0] = undefined
    // CODE → addr:195 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:197 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:203 | <GetByIdShort>: <Reg8: 8, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:208 | <LoadConstString>: <Reg8: 7, string_id: 568>  # String: '__BC:Functions/AsyncTests/simpleAsyncTest/start' (String)
    // USED → r7 = "__BC:Functions/AsyncTests/simpleAsyncTest/start";
    // CODE → addr:212 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 10, Reg8: 7>
    console.log("__BC:Functions/AsyncTests/simpleAsyncTest/start")
    // CODE → addr:217 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1)
    // CODE → addr:220 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 0>
    // USED → r8 = r7[0];
    // CODE → addr:224 | <LoadConstUInt8>: <Reg8: 7, UInt8: 42>
    // USED → r7 = 42;
    // CODE → addr:227 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    await r7[0].call(r9, 42)
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:283 | <Catch>: <Reg8: 5>
    r5 = caughtException
    // CODE → addr:285 | <Mov>: <Reg8: 2, Reg8: 6>
    r2 = 3
    // CODE → addr:288 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
    r1[2] = 3
    // CODE → addr:292 | <Throw>: <Reg8: 5>
    throw r5;
}