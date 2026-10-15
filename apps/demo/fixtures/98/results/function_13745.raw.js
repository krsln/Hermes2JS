async function _anon_0_parallelAwaitTest() {
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0);
    // CODE → addr:299 | <CreateTopLevelEnvironment>: <Reg8: 8, UInt32: 2>
    // USED → r8 = __environment__;
    // CODE → addr:305 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 8>
    r1[2] = __environment__;
    // CODE → addr:309 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:311 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 7>
    __environment__[0] = undefined;
    // CODE → addr:315 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 1, Reg8: 7>
    __environment__[1] = undefined;
    // CODE → addr:319 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:321 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:327 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:332 | <LoadConstString>: <Reg8: 8, string_id: 4922>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
    // USED → r8 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
    // CODE → addr:336 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start");
    // CODE → addr:341 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 26>  # String: 'Promise' (Identifier)
    // USED → r9 = Promise;
    // CODE → addr:347 | <GetById>: <Reg8: 8, Reg8: 9, UInt8: 3, string_id: 6842>  # String: 'all' (Identifier)
    // USED → r8 = Promise.all;
    // CODE → addr:353 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1);
    // CODE → addr:356 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 0>
    // USED → r10 = r7[0];
    // CODE → addr:360 | <Call2>: <Reg8: 12, Reg8: 10, Reg8: 11, Reg8: 5>
    r12 = r7[0].call(0, 1);
    // CODE → addr:365 | <NewArray>: <Reg8: 7, UInt16: 2>
    // USED → r7 = [];
    // CODE → addr:369 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 12, UInt8: 0>
    r7 = [r12];
    // CODE → addr:373 | <Call2>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 4>
    r10 = r7[0].call(0, 2);
    // CODE → addr:378 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 10, UInt8: 1>
    r7[1] = r10;
    // CODE → addr:382 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    await Promise.all(r7);
    // ──────────────── Block 5 ──────────────── 
    // CODE → addr: 80 | <Mov>: <Reg8: 5, Reg8: 0>
    r5 = param2;
    // CODE → addr: 83 | <IteratorBegin>: <Reg8: 8, Reg8: 5>
    [r1[2][0], r1[2][1]] = r5;
    // ──────────────── Block 12 ──────────────── 
    // CODE → addr:191 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 2>
    // USED → r7 = r1[2];
    // CODE → addr:195 | <GetGlobalObject>: <Reg8: 5>
    // USED → r5 = globalThis;
    // CODE → addr:197 | <TryGetById>: <Reg8: 10, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:203 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:208 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 0>
    r8 = r1[2][0];
    // CODE → addr:212 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 7, UInt8: 1>
    r7 = r1[2][1];
    // CODE → addr:216 | <Call3>: <Reg8: 7, Reg8: 9, Reg8: 10, Reg8: 8, Reg8: 7>
    console.log(r8, r7);
    // CODE → addr:222 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r8 = console;
    // CODE → addr:228 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r7 = console.log;
    // CODE → addr:233 | <LoadConstString>: <Reg8: 5, string_id: 4921>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
    // USED → r5 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
    // CODE → addr:237 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end");
    // CODE → addr:249 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r5 = { "value": undefined, "done": true };
    // CODE → addr:255 | <Ret>: <Reg8: 5>
    return r5;
}