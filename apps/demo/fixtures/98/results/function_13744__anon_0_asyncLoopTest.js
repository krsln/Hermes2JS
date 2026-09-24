async function _anon_0_asyncLoopTest(param1) {
// ⚠ WARNING: this output is NOT valid JavaScript.
// Cause: a generator/async dispatch chain was recognized but this pass declined to fold it (see GeneratorStateDispatchCfgPass.run's own all-or-nothing contract - logged above at DEBUG).
// It contains raw `goto label_N;` / `if (...) goto label_N;` statements -
// `goto` is not a JavaScript keyword, so this will fail to parse as-is.
// If this is a generator/async function, re-run decompilation with batch_tables
// built from the full section directory (FileOperations.build_batch_tables) so
// its suspend/resume dispatch can be recognized before structuring runs.
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 9>
    // USED → r0 = r1[9];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[9];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    if (r0 === 2) {
        // ──────────────── Block 26 ──────────────── 
        // CODE → addr:484 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:487 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:490 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 0>
        r1[9] = 3
        // CODE → addr:494 | <LoadConstString>: <Reg8: 18, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r18 = "Generator functions may not be called on executing generators"
        // CODE → addr:498 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r18, r17)
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
        // USED → r0 = param2;
        // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
        // USED → r3 = param1;
        // CODE → addr: 26 | <Mov>: <Reg8: 14, Reg8: 2>
        r14 = r1[9]
        // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
        // USED → r7 = 3;
        // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // CODE → addr: 35 | <LoadConstZero>: <Reg8: 13>
        // USED → r13 = 0;
        // CODE → addr: 37 | <GetGlobalObject>: <Reg8: 12>
        // USED → r12 = globalThis;
        // CODE → addr: 39 | <LoadConstString>: <Reg8: 11, string_id: 4909>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/end' (String)
        // USED → r11 = "__BC:Functions/AsyncTests/asyncLoopTest/end";
        // CODE → addr: 43 | <LoadConstUndefined>: <Reg8: 10>
        // USED → r10 = undefined;
        // CODE → addr: 45 | <GetParentEnvironment>: <Reg8: 9, UInt8: 1>
        r9 = getParentEnvironment(1)
        // CODE → addr: 48 | <LoadConstString>: <Reg8: 8, string_id: 4910>  # String: '__BC:Functions/AsyncTests/asyncLoopTest/start' (String)
        // USED → r8 = "__BC:Functions/AsyncTests/asyncLoopTest/start";
        if (r14 === 3) {
            // Switch → START
            switch (param1) {
                case 1:
                    // ──────────────── Block 25 ──────────────── 
                    // CODE → addr:482 | <Throw>: <Reg8: 0>
                    throw param2;
                case 2:
                    // ──────────────── Block 24 ──────────────── 
                    // CODE → addr:470 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                    r3 = { "value": null, "done": true }
                    // CODE → addr:476 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                    r3.slot_0 = param2
                    // CODE → addr:480 | <Ret>: <Reg8: 3>
                    return r3;
                default:
                    // ──────────────── Block 23 ──────────────── 
                    // CODE → addr:462 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                    r3 = { "value": undefined, "done": true }
                    // CODE → addr:468 | <Ret>: <Reg8: 3>
                    return r3;
            }
            // Switch → END
        } else {
            // LOOP → START (while)
            while (true) {
                try {
                    // ──────────────── Block 2 ──────────────── 
                    // CODE → addr: 59 | <Mov>: <Reg8: 2, Reg8: 4>
                    r2 = 2
                    // CODE → addr: 62 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 4>
                    r1[9] = 2
                    // CODE → addr: 66 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 8>
                    r14 = r1[8]
                    // CODE → addr: 70 | <JStrictEqual>: <Addr8: 100, Reg8: 13, Reg8: 14>  # Address: 000000aa
                    if (0 === r14) goto label_170;
                } catch (caughtException) {
                    // ──────────────── Block 18 ──────────────── 
                    // CODE → addr:421 | <Mov>: <Reg8: 6, Reg8: 14>
                    // USED → r6 = caughtException;
                    // CODE → addr:424 | <StoreToEnvironment>: <Reg8: 1, UInt8: 7, Reg8: 14>
                    r1[7] = caughtException
                    // CODE → addr:428 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 6>
                    r14 = r1[6]
                    if (0 === r14) {
                        // ──────────────── Block 20 ──────────────── 
                        // CODE → addr:445 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:448 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
                        r1[9] = 3
                        // CODE → addr:452 | <Throw>: <Reg8: 6>
                        throw caughtException;
                    }
                    // ──────────────── Block 19 ──────────────── 
                    // CODE → addr:436 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 8, Reg8: 5>
                    r1[8] = 1
                }
            }
            // LOOP → END
            if (1 === r14) {
                // ──────────────── Block 9 ──────────────── 
                // CODE → addr:150 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 7>
                // USED → r14 = r1[7];
                // CODE → addr:154 | <Mov>: <Reg8: 6, Reg8: 14>
                r6 = r1[7]
                // CODE → addr:157 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 13>
                r1[6] = 0
                // CODE → addr:161 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 1>
                // USED → r15 = r1[1];
                // CODE → addr:165 | <IteratorClose>: <Reg8: 15, UInt8: 1>
                r1[1].return()
                // CODE → addr:168 | <Throw>: <Reg8: 14>
                throw r1[7];
            } else {
                // Switch → START
                switch (param1) {
                    case 1:
                        // ──────────────── Block 8 ──────────────── 
                        // CODE → addr:141 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:144 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
                        r1[9] = 3
                        // CODE → addr:148 | <Throw>: <Reg8: 0>
                        throw param2;
                    case 2:
                        // ──────────────── Block 7 ──────────────── 
                        // CODE → addr:111 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 13>
                        r1[6] = 0
                        // CODE → addr:115 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 1>
                        // USED → r14 = r1[1];
                        // CODE → addr:119 | <IteratorClose>: <Reg8: 14, UInt8: 0>
                        r1[1].return()
                        // CODE → addr:122 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:125 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
                        r1[9] = 3
                        // CODE → addr:129 | <NewObjectWithBuffer>: <Reg8: 14, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r14 = { "value": null, "done": true }
                        // CODE → addr:135 | <PutOwnBySlotIdx>: <Reg8: 14, Reg8: 0, UInt8: 0>
                        r14.slot_0 = param2
                        // CODE → addr:139 | <Ret>: <Reg8: 14>
                        return r14;
                    default:
                        // ──────────────── Block 6 ──────────────── 
                        // CODE → addr: 86 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 3>
                        // USED → r14 = r1[3];
                        // CODE → addr: 90 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 4>
                        // USED → r15 = r1[4];
                        // CODE → addr: 94 | <Add>: <Reg8: 14, Reg8: 14, Reg8: 0>
                        r14 = r1[3] + param2
                        // CODE → addr: 98 | <StoreToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 14>
                        r1[4][0] = r14
                        // CODE → addr:102 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 13>
                        r1[6] = 0
                        // CODE → addr:106 | <JmpLong>: <Addr32: 142>  # Address: 000000f8
                        goto label_248;
                        break;
                }
                // Switch → END
            }
            // ──────────────── Block 10 ──────────────── 
            // CODE → addr:170 | <JStrictEqualLong>: <Addr32: 240, Reg8: 3, Reg8: 5>  # Address: 0000019a
            if (param1 === 1) goto label_410;
            // ──────────────── Block 11 ──────────────── 
            // CODE → addr:177 | <JStrictEqualLong>: <Addr32: 214, Reg8: 3, Reg8: 4>  # Address: 00000187
            if (param1 === 2) goto label_391;
            // ──────────────── Block 12 ──────────────── 
            // CODE → addr:184 | <StoreToEnvironment>: <Reg8: 1, UInt8: 5, Reg8: 9>
            r1[5] = r9
            // CODE → addr:188 | <CreateTopLevelEnvironment>: <Reg8: 15, UInt32: 2>
            // USED → r15 = __environment__;
            // CODE → addr:194 | <StoreToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 15>
            r1[4] = __environment__
            // CODE → addr:198 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 0>
            // USED → r14 = r1[0];
            // CODE → addr:202 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 10>
            __environment__[0] = undefined
            // CODE → addr:206 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 1, Reg8: 10>
            __environment__[1] = undefined
            // CODE → addr:210 | <TryGetById>: <Reg8: 17, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
            // USED → r17 = console;
            // CODE → addr:216 | <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
            // USED → r16 = console.log;
            // CODE → addr:221 | <Call2>: <Reg8: 16, Reg8: 16, Reg8: 17, Reg8: 8>
            console.log("__BC:Functions/AsyncTests/asyncLoopTest/start")
            // CODE → addr:226 | <StoreNPToEnvironment>: <Reg8: 15, UInt8: 0, Reg8: 13>
            __environment__[0] = 0
            // CODE → addr:230 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 14>
            r1[2] = r1[0]
            // CODE → addr:234 | <Mov>: <Reg8: 15, Reg8: 14>
            r15 = r1[0]
            // CODE → addr:237 | <IteratorBegin>: <Reg8: 14, Reg8: 15>
            r14 = GetIterator(r15)
            // CODE → addr:240 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 15>
            r1[2] = r1[0]
            // CODE → addr:244 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 14>
            r1[1] = r14
            // ──────────────── Block 13 ──────────────── 
            // CODE → addr:248 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 2>
            r15 = r1[2]
            // CODE → addr:252 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 1>
            // USED → r14 = r1[1];
            // CODE → addr:256 | <IteratorNext>: <Reg8: 16, Reg8: 14, Reg8: 15>
            r16 = r1[1].next()
            // CODE → addr:260 | <StoreToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 14>
            r1[1] = r1[1]
            if (r14 === undefined) {
                // ──────────────── Block 15 ──────────────── 
                // CODE → addr:328 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 4>
                // USED → r14 = r1[4];
                // CODE → addr:332 | <TryGetById>: <Reg8: 17, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r17 = console;
                // CODE → addr:338 | <GetByIdShort>: <Reg8: 16, Reg8: 17, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r16 = console.log;
                // CODE → addr:343 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
                r15 = r1[4][0]
                // CODE → addr:347 | <Call2>: <Reg8: 15, Reg8: 16, Reg8: 17, Reg8: 15>
                console.log(r15)
                // CODE → addr:352 | <TryGetById>: <Reg8: 16, Reg8: 12, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r16 = console;
                // CODE → addr:358 | <GetByIdShort>: <Reg8: 15, Reg8: 16, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r15 = console.log;
                // CODE → addr:363 | <Call2>: <Reg8: 15, Reg8: 15, Reg8: 16, Reg8: 11>
                console.log("__BC:Functions/AsyncTests/asyncLoopTest/end")
                // CODE → addr:368 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 14, UInt8: 0>
                // USED → r15 = r1[4][0];
                // CODE → addr:372 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 3
                // CODE → addr:375 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
                r1[9] = 3
                // CODE → addr:379 | <NewObjectWithBuffer>: <Reg8: 14, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r14 = { "value": null, "done": true }
                // CODE → addr:385 | <PutOwnBySlotIdx>: <Reg8: 14, Reg8: 15, UInt8: 0>
                r14.slot_0 = r1[4][0]
                // CODE → addr:389 | <Ret>: <Reg8: 14>
                return r14;
            } else {
                // ──────────────── Block 14 ──────────────── 
                // CODE → addr:268 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 1, UInt8: 4>
                // USED → r14 = r1[4];
                // CODE → addr:272 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 1, UInt8: 5>
                // USED → r15 = r1[5];
                // CODE → addr:276 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 6, Reg8: 5>
                r1[6] = 1
                // CODE → addr:280 | <StoreToEnvironment>: <Reg8: 14, UInt8: 1, Reg8: 16>
                r1[4][1] = r16
                // CODE → addr:284 | <LoadFromEnvironment>: <Reg8: 16, Reg8: 14, UInt8: 0>
                // USED → r16 = r1[4][0];
                // CODE → addr:288 | <StoreToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 16>
                r1[3] = r1[4][0]
                // CODE → addr:292 | <LoadFromEnvironment>: <Reg8: 15, Reg8: 15, UInt8: 0>
                // USED → r15 = r1[5][0];
                // CODE → addr:296 | <LoadFromEnvironment>: <Reg8: 14, Reg8: 14, UInt8: 1>
                r14 = r1[4][1]
                // CODE → addr:300 | <Call2>: <Reg8: 15, Reg8: 15, Reg8: 13, Reg8: 14>
                r15 = r1[5][0].call(0, r14)
                // CODE → addr:305 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 8, Reg8: 4>
                r1[8] = 2
                // CODE → addr:309 | <Mov>: <Reg8: 2, Reg8: 5>
                r2 = 1
                // CODE → addr:312 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 5>
                r1[9] = 1
                // CODE → addr:316 | <NewObjectWithBuffer>: <Reg8: 14, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                r14 = { "value": null, "done": false }
                // CODE → addr:322 | <PutOwnBySlotIdx>: <Reg8: 14, Reg8: 15, UInt8: 0>
                r14.slot_0 = r15
                // CODE → addr:326 | <Ret>: <Reg8: 14>
                return r14;
            }
            // ──────────────── Block 16 ──────────────── 
            // CODE → addr:391 | <Mov>: <Reg8: 2, Reg8: 7>
            r2 = 3
            // CODE → addr:394 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
            r1[9] = 3
            // CODE → addr:398 | <NewObjectWithBuffer>: <Reg8: 14, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
            r14 = { "value": null, "done": true }
            // CODE → addr:404 | <PutOwnBySlotIdx>: <Reg8: 14, Reg8: 0, UInt8: 0>
            r14.slot_0 = param2
            // CODE → addr:408 | <Ret>: <Reg8: 14>
            return r14;
            // ──────────────── Block 17 ──────────────── 
            // CODE → addr:410 | <Mov>: <Reg8: 2, Reg8: 7>
            r2 = 3
            // CODE → addr:413 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 9, Reg8: 7>
            r1[9] = 3
            // CODE → addr:417 | <Throw>: <Reg8: 0>
            throw param2;
        }
    }
}