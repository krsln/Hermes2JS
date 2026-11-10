async function _anon_0_callAsyncTests() {
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0);
    // CODE → addr:395 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1);
    // CODE → addr:398 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
    r1[0] = r7;
    // CODE → addr:402 | <GetGlobalObject>: <Reg8: 8>
    // USED → r8 = globalThis;
    // CODE → addr:404 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:410 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:415 | <LoadConstString>: <Reg8: 8, string_id: 4920>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
    // USED → r8 = "__BC:Functions/AsyncTests/callAsyncTests/start";
    // CODE → addr:419 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/start");
    // CODE → addr:424 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 1>
    r8 = r7[1];
    // CODE → addr:428 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:430 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
    await r8();
    // ──────────────── Block 23 ──────────────── 
    // CODE → addr:319 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:323 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 2>
    // USED → r8 = r1[0][2];
    // CODE → addr:327 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:329 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
    await r1[0][2].call(undefined);
    // ──────────────── Block 18 ──────────────── 
    // CODE → addr:237 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:241 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 3>
    // USED → r9 = r1[0][3];
    // CODE → addr:245 | <LoadConstUndefined>: <Reg8: 8>
    // USED → r8 = undefined;
    // CODE → addr:247 | <NewArrayWithBuffer>: <Reg8: 7, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
    r7 = [1, 2, 3];
    // CODE → addr:255 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 8, Reg8: 7>
    await r1[0][3].call(undefined, r7);
    // ──────────────── Block 13 ──────────────── 
    // CODE → addr:161 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
    // USED → r7 = r1[0];
    // CODE → addr:165 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 4>
    // USED → r8 = r1[0][4];
    // CODE → addr:169 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:171 | <Call1>: <Reg8: 8, Reg8: 8, Reg8: 7>
    await r1[0][4].call(undefined);
    // ──────────────── Block 8 ──────────────── 
    // CODE → addr: 88 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr: 90 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r9 = console;
    // CODE → addr: 96 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r8 = console.log;
    // CODE → addr:101 | <LoadConstString>: <Reg8: 7, string_id: 4919>  # String: '__BC:Functions/AsyncTests/callAsyncTests/end' (String)
    // USED → r7 = "__BC:Functions/AsyncTests/callAsyncTests/end";
    // CODE → addr:105 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    console.log("__BC:Functions/AsyncTests/callAsyncTests/end");
    // CODE → addr:117 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r7 = { "value": undefined, "done": true };
    // CODE → addr:123 | <Ret>: <Reg8: 7>
    return r7;
}