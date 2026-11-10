async function _anon_0_asyncLoopTest(param1) {
    // ──────────────── Block 28 ──────────────── 
    // CODE → addr: 45 | <GetParentEnvironment>: <Reg8: 9, UInt8: 1>
    r9 = getParentEnvironment(1);
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0);
    try {
        // ──────────────── Block 12 ──────────────── 
        // CODE → addr:184 | <StoreToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 9>
        r1[5] = r9;
        // CODE → addr:188 | <CreateTopLevelEnvironment>: <Reg8: 15, UInt32: 2>
        // USED → r15 = __environment__;
        // CODE → addr:194 | <StoreToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 15>
        r1[4] = __environment__;
        // CODE → addr:198 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 0>
        r14 = r1[0];
        // CODE → addr:202 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 10>
        __environment__[0] = undefined;
        // CODE → addr:206 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 1, Reg8: 10>
        __environment__[1] = undefined;
        // CODE → addr:210 | <TryGetById>: <Reg8: 17, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r17 = console;
        // CODE → addr:216 | <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r16 = console.log;
        // CODE → addr:221 | <Call2>: <Reg8: 16, Reg8: 16, Reg8: 17, Reg8: 8>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/start");
        // CODE → addr:226 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 13>
        __environment__[0] = 0;
        // CODE → addr:230 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 14>
        r1[2] = r14;
        // CODE → addr:234 | <Mov>: <Reg8: 15, Reg8: 14>
        r15 = r14;
        // CODE → addr:237 | <IteratorBegin>: <Reg8: 14, Reg8: 15>
        r14 = GetIterator(r15);
        // CODE → addr:240 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 15>
        r1[2] = r15;
        // CODE → addr:244 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 14>
        r1[1] = r14;
        // LOOP → START (while)
        while (!(r14 === undefined)) {
            // ──────────────── Block 13 ──────────────── 
            // CODE → addr:248 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 2>
            r15 = r1[2];
            // CODE → addr:252 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 1>
            r14 = r1[1];
            // CODE → addr:256 | <IteratorNext>: <Reg8: 16, Reg8: 14, Reg8: 15>
            r16 = r1[1].next();
            // CODE → addr:260 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 14>
            r1[1] = r1[1];
            // ──────────────── Block 6 ──────────────── 
            // CODE → addr: 86 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 3>
            // USED → r14 = r1[3];
            // CODE → addr: 90 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 4>
            // USED → r15 = r1[4];
            // CODE → addr: 94 | <Add>: <Reg8: 14, Reg8: 14, Reg8: 0>
            r14 = r1[3] + param2;
            // CODE → addr: 98 | <StoreToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 14>
            r1[4][0] = r14;
            // CODE → addr:102 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 13>
            r1[6] = 0;
            // ──────────────── Block 14 ──────────────── 
            // CODE → addr:268 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 4>
            // USED → r14 = r1[4];
            // CODE → addr:272 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 5>
            // USED → r15 = r1[5];
            // CODE → addr:276 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 5>
            r1[6] = 1;
            // CODE → addr:280 | <StoreToEnvironment>: <Reg8: 14, UInt8: 1, Reg8: 16>
            r1[4][1] = r16;
            // CODE → addr:284 | <LoadFromEnvironment>: <Reg8: 16, Reg8: 14, UInt8: 0>
            // USED → r16 = r1[4][0];
            // CODE → addr:288 | <StoreToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 16>
            r1[3] = r1[4][0];
            // CODE → addr:292 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 15, UInt8: 0>
            // USED → r15 = r1[5][0];
            // CODE → addr:296 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 14, UInt8: 1>
            r14 = r1[4][1];
            // CODE → addr:300 | <Call2>: <Reg8: 15, Reg8: 15, Reg8: 13, Reg8: 14>
            await r1[5][0].call(0, r14);
        }
        // LOOP → END
        // ──────────────── Block 15 ──────────────── 
        // CODE → addr:328 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 4>
        r14 = r1[4];
        // CODE → addr:332 | <TryGetById>: <Reg8: 17, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r17 = console;
        // CODE → addr:338 | <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r16 = console.log;
        // CODE → addr:343 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
        r15 = r1[4][0];
        // CODE → addr:347 | <Call2>: <Reg8: 15, Reg8: 16, Reg8: 17, Reg8: 15>
        console.log(r15);
        // CODE → addr:352 | <TryGetById>: <Reg8: 16, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
        // USED → r16 = console;
        // CODE → addr:358 | <GetByIdShort>: <Reg8: 15, Reg8: 16, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
        // USED → r15 = console.log;
        // CODE → addr:363 | <Call2>: <Reg8: 15, Reg8: 15, Reg8: 16, Reg8: 11>
        console.log("__BC:Functions/AsyncTests/asyncLoopTest/end");
        // CODE → addr:368 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
        // USED → r15 = r14[0];
        // CODE → addr:379 | <NewObjectWithBuffer>: <Reg8: 14, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
        // USED → r14 = { "value": null, "done": true };
        // CODE → addr:385 | <PutOwnBySlotIdx>: <Reg8: 14, Reg8: 15, UInt8: 0>
        r14 = { "value": r14[0], "done": true };
        // CODE → addr:389 | <Ret>: <Reg8: 14>
        return r14;
    } catch (caughtException) {
        // ──────────────── Block 18 ──────────────── 
        // CODE → addr:421 | <Mov>: <Reg8: 6, Reg8: 14>
        // USED → r6 = caughtException;
        // CODE → addr:424 | <StoreToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 14>
        r1[7] = caughtException;
        // CODE → addr:428 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 6>
        r14 = r1[6];
        if (0 === r14) {
            // ──────────────── Block 20 ──────────────── 
            // CODE → addr:452 | <Throw>: <Reg8: 6>
            throw caughtException;
        } else {
            // ──────────────── Block 27 ──────────────── 
            // CODE → addr:150 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 7>
            // USED → r14 = r1[7];
            // CODE → addr:154 | <Mov>: <Reg8: 6, Reg8: 14>
            r6 = r1[7];
            // CODE → addr:157 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 13>
            r1[6] = 0;
            // CODE → addr:161 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 1>
            // USED → r15 = r1[1];
            // CODE → addr:165 | <IteratorClose>: <Reg8: 15, UInt8: 1>
            r1[1].return();
            // CODE → addr:168 | <Throw>: <Reg8: 14>
            throw r1[7];
        }
    }
}