async function _anon_0_parallelAwaitTest() {
    try {
        // ──────────────── Block 5 ──────────────── 
        // CODE → addr: 76 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
        r1[0] = param2
        // CODE → addr: 80 | <Mov>: <Reg8: 5, Reg8: 0>
        r5 = param2
        // CODE → addr: 83 | <IteratorBegin>: <Reg8: 8, Reg8: 5>
        r8 = GetIterator(r5)
        // CODE → addr: 86 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
        r1[0] = param2
        // CODE → addr: 90 | <LoadConstUndefined>: <Reg8: 9>
        // USED → r9 = undefined;
        // CODE → addr: 92 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 9>
        r1[1] = undefined
        // CODE → addr: 99 | <IteratorNext>: <Reg8: 5, Reg8: 7, Reg8: 5>
        r5 = r8.next()
        // CODE → addr:103 | <Mov>: <Reg8: 12, Reg8: 7>
        // USED → r12 = r8;
        // CODE → addr:106 | <StrictEq>: <Reg8: 7, Reg8: 12, Reg8: 9>
        // USED → r7 = r8 === undefined;
        if (r8 !== undefined) {
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr:113 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
            r1[1] = r5
        }
        // ──────────────── Block 7 ──────────────── 
        // CODE → addr:117 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 2>
        // USED → r8 = r1[2];
        // CODE → addr:121 | <LoadFromEnvironment>: <Reg8: 5, Reg8: 1, UInt8: 1>
        // USED → r5 = r1[1];
        // CODE → addr:125 | <StoreToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 5>
        r1[2][0] = r1[1]
        // CODE → addr:129 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 9>
        r1[1] = undefined
        // CODE → addr:133 | <Mov>: <Reg8: 5, Reg8: 12>
        r5 = r8
        if (r8 !== undefined) {
            // ──────────────── Block 8 ──────────────── 
            // CODE → addr:139 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 1, UInt8: 0>
            r10 = r1[0]
            // CODE → addr:143 | <Mov>: <Reg8: 8, Reg8: 12>
            // USED → r8 = r8;
            // CODE → addr:146 | <IteratorNext>: <Reg8: 10, Reg8: 8, Reg8: 10>
            r10 = r8.next()
            // CODE → addr:150 | <StrictEq>: <Reg8: 9, Reg8: 8, Reg8: 9>
            // USED → r9 = r8 === undefined;
            // CODE → addr:154 | <Mov>: <Reg8: 7, Reg8: 9>
            r7 = r8 === undefined
            // CODE → addr:157 | <Mov>: <Reg8: 5, Reg8: 8>
            r5 = r8
            if (r8 !== undefined) {
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr:163 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 10>
                r1[1] = r10
                // CODE → addr:167 | <Mov>: <Reg8: 7, Reg8: 9>
                // USED → r7 = r8 === undefined;
                // CODE → addr:170 | <Mov>: <Reg8: 5, Reg8: 8>
                // USED → r5 = r8;
            }
        }
        // ──────────────── Block 10 ──────────────── 
        // CODE → addr:173 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 1, UInt8: 2>
        // USED → r9 = r1[2];
        // CODE → addr:177 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 1, UInt8: 1>
        // USED → r8 = r1[1];
        // CODE → addr:181 | <StoreToEnvironment>: <Reg8: 9, UInt8: 1, Reg8: 8>
        r1[2][1] = r1[1]
        if (r8 !== undefined) {
            // ──────────────── Block 11 ──────────────── 
            // CODE → addr:188 | <IteratorClose>: <Reg8: 5, UInt8: 0>
            r8.return()
        }
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
        r8 = r1[2][0]
        // CODE → addr:212 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 7, UInt8: 1>
        r7 = r1[2][1]
        // CODE → addr:216 | <Call3>: <Reg8: 7, Reg8: 9, Reg8: 10, Reg8: 8, Reg8: 7>
        console.log(r8, r7)
        // CODE → addr:222 | <TryGetById>: <Reg8: 8, Reg8: 5, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r8 = console;
        // CODE → addr:228 | <GetByIdShort>: <Reg8: 7, Reg8: 8, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r7 = console.log;
        // CODE → addr:233 | <LoadConstString>: <Reg8: 5, string_id: 4921>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/end' (String)
        // USED → r5 = "__BC:Functions/AsyncTests/parallelAwaitTest/end";
        // CODE → addr:237 | <Call2>: <Reg8: 5, Reg8: 7, Reg8: 8, Reg8: 5>
        console.log("__BC:Functions/AsyncTests/parallelAwaitTest/end")
    } finally {
        // ──────────────── Block 20 ──────────────── 
        // CODE → addr:440 | <Mov>: <Reg8: 2, Reg8: 6>
        r2 = 3
        // CODE → addr:443 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 6>
        r1[4] = 3
    }
    // ──────────────── Block 21 ──────────────── 
    // CODE → addr:249 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
    r5 = { "value": null, "done": true }
    // CODE → addr:255 | <Ret>: <Reg8: 5>
    return r5;
    // ──────────────── Block 17 ──────────────── 
    // CODE → addr:299 | <CreateTopLevelEnvironment>: <Reg8: 8, UInt32: 2>
    // USED → r8 = __environment__;
    // CODE → addr:305 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 8>
    r1[2] = __environment__
    // CODE → addr:309 | <LoadConstUndefined>: <Reg8: 7>
    // USED → r7 = undefined;
    // CODE → addr:311 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 0, Reg8: 7>
    __environment__[0] = undefined
    // CODE → addr:315 | <StoreNPToEnvironment>: <Reg8: 8, UInt8: 1, Reg8: 7>
    __environment__[1] = undefined
    // CODE → addr:319 | <GetGlobalObject>: <Reg8: 7>
    // USED → r7 = globalThis;
    // CODE → addr:321 | <TryGetById>: <Reg8: 10, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
    // USED → r10 = console;
    // CODE → addr:327 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
    // USED → r9 = console.log;
    // CODE → addr:332 | <LoadConstString>: <Reg8: 8, string_id: 4922>  # String: '__BC:Functions/AsyncTests/parallelAwaitTest/start' (String)
    // USED → r8 = "__BC:Functions/AsyncTests/parallelAwaitTest/start";
    // CODE → addr:336 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
    console.log("__BC:Functions/AsyncTests/parallelAwaitTest/start")
    // CODE → addr:341 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 2, string_id: 26>  # String: 'Promise' (Identifier)
    // USED → r9 = Promise;
    // CODE → addr:347 | <GetById>: <Reg8: 8, Reg8: 9, UInt8: 3, string_id: 6842>  # String: 'all' (Identifier)
    // USED → r8 = Promise.all;
    // CODE → addr:353 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
    r7 = getParentEnvironment(1)
    // CODE → addr:356 | <LoadFromEnvironment>: <Reg8: 10, Reg8: 7, UInt8: 0>
    // USED → r10 = r7[0];
    // CODE → addr:360 | <Call2>: <Reg8: 12, Reg8: 10, Reg8: 11, Reg8: 5>
    r12 = r7[0].call(r11, 1)
    // CODE → addr:365 | <NewArray>: <Reg8: 7, UInt16: 2>
    r7 = []
    // CODE → addr:369 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 12, UInt8: 0>
    r7[0] = r12
    // CODE → addr:373 | <Call2>: <Reg8: 10, Reg8: 10, Reg8: 11, Reg8: 4>
    r10 = r7[0].call(r11, 2)
    // CODE → addr:378 | <DefineOwnInDenseArray>: <Reg8: 7, Reg8: 10, UInt8: 1>
    r7[1] = r10
    // CODE → addr:382 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
    await Promise.all(r7)
}