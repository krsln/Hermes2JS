async function _anon_0_asyncTryCatchTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 4>
    // USED → r0 = r1[4];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[4];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    if (r0 === 2) {
        // ──────────────── Block 30 ──────────────── 
        // CODE → addr:516 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:519 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:522 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 0>
        r1[4] = 3
        // CODE → addr:526 | <LoadConstString>: <Reg8: 23, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r23 = "Generator functions may not be called on executing generators"
        // CODE → addr:530 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r24, r23)
    } else {
        // ──────────────── Block 1 ──────────────── 
        // CODE → addr: 20 | <LoadParam>: <Reg8: 0, UInt8: 2>
        // USED → r0 = param2;
        // CODE → addr: 23 | <LoadParam>: <Reg8: 3, UInt8: 1>
        // USED → r3 = param1;
        // CODE → addr: 26 | <Mov>: <Reg8: 18, Reg8: 2>
        r18 = r1[4]
        // CODE → addr: 29 | <LoadConstUInt8>: <Reg8: 7, UInt8: 3>
        // USED → r7 = 3;
        // CODE → addr: 32 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // CODE → addr: 35 | <LoadConstZero>: <Reg8: 17>
        // USED → r17 = 0;
        // CODE → addr: 37 | <LoadConstUndefined>: <Reg8: 16>
        // USED → r16 = undefined;
        // CODE → addr: 39 | <GetGlobalObject>: <Reg8: 15>
        // USED → r15 = globalThis;
        // CODE → addr: 41 | <LoadConstString>: <Reg8: 14, string_id: 4918>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/start' (String)
        // USED → r14 = "__BC:Functions/AsyncTests/asyncTryCatchTest/start";
        // CODE → addr: 45 | <GetParentEnvironment>: <Reg8: 13, UInt8: 1>
        r13 = getParentEnvironment(1)
        // CODE → addr: 48 | <LoadConstString>: <Reg8: 12, string_id: 4915>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/finally' (String)
        // USED → r12 = "__BC:Functions/AsyncTests/asyncTryCatchTest/finally";
        // CODE → addr: 52 | <LoadConstString>: <Reg8: 11, string_id: 4914>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/end' (String)
        // USED → r11 = "__BC:Functions/AsyncTests/asyncTryCatchTest/end";
        // CODE → addr: 56 | <LoadConstString>: <Reg8: 10, string_id: 4912>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/caught' (String)
        // USED → r10 = "__BC:Functions/AsyncTests/asyncTryCatchTest/caught";
        // CODE → addr: 60 | <LoadConstString>: <Reg8: 9, string_id: 2660>  # String: 'post-await failure' (String)
        // USED → r9 = "post-await failure";
        // CODE → addr: 64 | <LoadConstString>: <Reg8: 8, string_id: 4911>  # String: '__BC:Functions/AsyncTests/asyncTryCatchTest/awaited' (String)
        // USED → r8 = "__BC:Functions/AsyncTests/asyncTryCatchTest/awaited";
        if (r18 === 3) {
            // Switch → START
            switch (param1) {
                case 1:
                    // ──────────────── Block 29 ──────────────── 
                    // CODE → addr:514 | <Throw>: <Reg8: 0>
                    throw param2;
                case 2:
                    // ──────────────── Block 28 ──────────────── 
                    // CODE → addr:502 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                    r3 = { "value": null, "done": true }
                    // CODE → addr:508 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                    r3.slot_0 = param2
                    // CODE → addr:512 | <Ret>: <Reg8: 3>
                    return r3;
                default:
                    // ──────────────── Block 27 ──────────────── 
                    // CODE → addr:494 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                    r3 = { "value": null, "done": true }
                    // CODE → addr:500 | <Ret>: <Reg8: 3>
                    return r3;
            }
            // Switch → END
        } else {
            // LOOP → START (while)
            while (true) {
                try {
                    // ──────────────── Block 2 ──────────────── 
                    // CODE → addr: 75 | <Mov>: <Reg8: 2, Reg8: 4>
                    r2 = 2
                    // CODE → addr: 78 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 4>
                    r1[4] = 2
                    // CODE → addr: 82 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 1>
                    r18 = r1[1]
                    // CODE → addr: 86 | <JStrictEqualLong>: <Addr32: 250, Reg8: 17, Reg8: 18>  # Address: 00000150
                    if (0 === r18) goto label_336;
                } catch (caughtException) {
                    // ──────────────── Block 20 ──────────────── 
                    // CODE → addr:440 | <Mov>: <Reg8: 6, Reg8: 18>
                    // USED → r6 = caughtException;
                    // CODE → addr:443 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 18>
                    r1[2] = caughtException
                    // CODE → addr:447 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 3>
                    r18 = r1[3]
                    if (0 === r18) {
                        // ──────────────── Block 24 ──────────────── 
                        // CODE → addr:477 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:480 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                        r1[4] = 3
                        // CODE → addr:484 | <Throw>: <Reg8: 6>
                        throw caughtException;
                    }
                    if (1 === r18) {
                        // ──────────────── Block 23 ──────────────── 
                        // CODE → addr:468 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
                        r1[1] = 1
                    } else {
                        // ──────────────── Block 22 ──────────────── 
                        // CODE → addr:459 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
                        r1[1] = 2
                    }
                }
            }
            // LOOP → END
            if (1 === r18) {
                // ──────────────── Block 14 ──────────────── 
                // CODE → addr:307 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 2>
                // USED → r18 = r1[2];
                // CODE → addr:311 | <Mov>: <Reg8: 6, Reg8: 18>
                r6 = r1[2]
                // CODE → addr:314 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
                r1[3] = 0
                // CODE → addr:318 | <TryGetById>: <Reg8: 20, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r20 = console;
                // CODE → addr:324 | <GetByIdShort>: <Reg8: 19, Reg8: 20, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r19 = console.log;
                // CODE → addr:329 | <Call2>: <Reg8: 19, Reg8: 19, Reg8: 20, Reg8: 12>
                console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
                // CODE → addr:334 | <Throw>: <Reg8: 18>
                throw r1[2];
            } else {
                if (2 === r18) {
                    // ──────────────── Block 12 ──────────────── 
                    // CODE → addr:232 | <LoadFromEnvironment>: <Reg8: 6, Reg8: 1, UInt8: 2>
                    r6 = r1[2]
                    // CODE → addr:236 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
                    r1[3] = 1
                    // CODE → addr:240 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r19 = console;
                    // CODE → addr:246 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r18 = console.log;
                    // CODE → addr:251 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 10>
                    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/caught")
                } else {
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 11 ──────────────── 
                            // CODE → addr:223 | <Mov>: <Reg8: 2, Reg8: 7>
                            r2 = 3
                            // CODE → addr:226 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                            r1[4] = 3
                            // CODE → addr:230 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 10 ──────────────── 
                            // CODE → addr:184 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
                            r1[3] = 0
                            // CODE → addr:188 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                            // USED → r19 = console;
                            // CODE → addr:194 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                            // USED → r18 = console.log;
                            // CODE → addr:199 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 12>
                            console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
                            // CODE → addr:204 | <Mov>: <Reg8: 2, Reg8: 7>
                            r2 = 3
                            // CODE → addr:207 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                            r1[4] = 3
                            // CODE → addr:211 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r18 = { "value": null, "done": true }
                            // CODE → addr:217 | <PutOwnBySlotIdx>: <Reg8: 18, Reg8: 0, UInt8: 0>
                            r18.slot_0 = param2
                            // CODE → addr:221 | <Ret>: <Reg8: 18>
                            return r18;
                        default:
                            // ──────────────── Block 7 ──────────────── 
                            // CODE → addr:115 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 1, UInt8: 0>
                            // USED → r18 = r1[0];
                            // CODE → addr:119 | <StoreToEnvironment>: <Reg8: 18, UInt8: 0, Reg8: 0>
                            r1[0][0] = param2
                            // CODE → addr:123 | <TryGetById>: <Reg8: 21, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                            // USED → r21 = console;
                            // CODE → addr:129 | <GetByIdShort>: <Reg8: 20, Reg8: 21, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                            // USED → r20 = console.log;
                            // CODE → addr:134 | <LoadFromEnvironment>: <Reg8: 19, Reg8: 18, UInt8: 0>
                            r19 = r1[0][0]
                            // CODE → addr:138 | <Call3>: <Reg8: 19, Reg8: 20, Reg8: 21, Reg8: 8, Reg8: 19>
                            console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/awaited", r19)
                            // CODE → addr:144 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 18, UInt8: 0>
                            r18 = r1[0][0]
                            if (r18 === 1) {
                                // ──────────────── Block 9 ──────────────── 
                                // CODE → addr:158 | <TryGetById>: <Reg8: 18, Reg8: 15, UInt8: 2, string_id: 9>  # String: 'Error' (Identifier)
                                // USED → r18 = Error;
                                // CODE → addr:164 | <CreateThisForNew>: <Reg8: 19, Reg8: 18, UInt8: 3>
                                r19 = CreateThisForNew(r18)
                                // CODE → addr:168 | <Mov>: <Reg8: 24, Reg8: 19>
                                r24 = r19
                                // CODE → addr:171 | <Mov>: <Reg8: 23, Reg8: 9>
                                r23 = "post-await failure"
                                // CODE → addr:174 | <Construct>: <Reg8: 18, Reg8: 18, UInt8: 2>
                                // USED → r18 = new Error(r23);
                                // CODE → addr:178 | <SelectObject>: <Reg8: 18, Reg8: 19, Reg8: 18>
                                // USED → r18 = new Error(r23);
                                // CODE → addr:182 | <Throw>: <Reg8: 18>
                                throw new Error(r23);
                            } else {
                                // ──────────────── Block 8 ──────────────── 
                                // CODE → addr:152 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
                                r1[3] = 1
                                // CODE → addr:156 | <Jmp>: <Addr8: 100>  # Address: 00000100
                                goto label_256;
                            }
                            break;
                    }
                    // Switch → END
                }
                // ──────────────── Block 13 ──────────────── 
                // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 17>
                r1[3] = 0
                // CODE → addr:260 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r19 = console;
                // CODE → addr:266 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r18 = console.log;
                // CODE → addr:271 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 12>
                console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/finally")
                // CODE → addr:276 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r19 = console;
                // CODE → addr:282 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r18 = console.log;
                // CODE → addr:287 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 11>
                console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/end")
                // CODE → addr:292 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 3
                // CODE → addr:295 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                r1[4] = 3
                // CODE → addr:299 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                r18 = { "value": null, "done": true }
                // CODE → addr:305 | <Ret>: <Reg8: 18>
                return r18;
            }
            // Switch → START
            switch (param1) {
                case 1:
                    // ──────────────── Block 19 ──────────────── 
                    // CODE → addr:429 | <Mov>: <Reg8: 2, Reg8: 7>
                    r2 = 3
                    // CODE → addr:432 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                    r1[4] = 3
                    // CODE → addr:436 | <Throw>: <Reg8: 0>
                    throw param2;
                case 2:
                    // ──────────────── Block 18 ──────────────── 
                    // CODE → addr:410 | <Mov>: <Reg8: 2, Reg8: 7>
                    r2 = 3
                    // CODE → addr:413 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 7>
                    r1[4] = 3
                    // CODE → addr:417 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                    r18 = { "value": null, "done": true }
                    // CODE → addr:423 | <PutOwnBySlotIdx>: <Reg8: 18, Reg8: 0, UInt8: 0>
                    r18.slot_0 = param2
                    // CODE → addr:427 | <Ret>: <Reg8: 18>
                    return r18;
                default:
                    // ──────────────── Block 17 ──────────────── 
                    // CODE → addr:344 | <CreateTopLevelEnvironment>: <Reg8: 18, UInt32: 1>
                    // USED → r18 = __environment__;
                    // CODE → addr:350 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 18>
                    r1[0] = __environment__
                    // CODE → addr:354 | <StoreNPToEnvironment>: <Reg8: 18, UInt8: 0, Reg8: 16>
                    __environment__[0] = undefined
                    // CODE → addr:358 | <TryGetById>: <Reg8: 19, Reg8: 15, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                    // USED → r19 = console;
                    // CODE → addr:364 | <GetByIdShort>: <Reg8: 18, Reg8: 19, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                    // USED → r18 = console.log;
                    // CODE → addr:369 | <Call2>: <Reg8: 18, Reg8: 18, Reg8: 19, Reg8: 14>
                    console.log("__BC:Functions/AsyncTests/asyncTryCatchTest/start")
                    // CODE → addr:374 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 4>
                    r1[3] = 2
                    // CODE → addr:378 | <LoadFromEnvironment>: <Reg8: 18, Reg8: 13, UInt8: 0>
                    // USED → r18 = r13[0];
                    // CODE → addr:382 | <Call2>: <Reg8: 19, Reg8: 18, Reg8: 17, Reg8: 5>
                    r19 = r13[0].call(r17, 1)
                    // CODE → addr:387 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 7>
                    r1[1] = 3
                    // CODE → addr:391 | <Mov>: <Reg8: 2, Reg8: 5>
                    r2 = 1
                    // CODE → addr:394 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 4, Reg8: 5>
                    r1[4] = 1
                    // CODE → addr:398 | <NewObjectWithBuffer>: <Reg8: 18, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                    r18 = { "value": null, "done": false }
                    // CODE → addr:404 | <PutOwnBySlotIdx>: <Reg8: 18, Reg8: 19, UInt8: 0>
                    r18.slot_0 = r19
                    // CODE → addr:408 | <Ret>: <Reg8: 18>
                    return r18;
            }
            // Switch → END
        }
    }
}