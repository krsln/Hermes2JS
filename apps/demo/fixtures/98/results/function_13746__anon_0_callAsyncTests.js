function ?anon_0_callAsyncTests() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 2>
    // USED → r0 = r1[2];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[2];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    if (r0 === 2) {
        // ──────────────── Block 37 ──────────────── 
        // CODE → addr:529 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:532 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:535 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 0>
        r1[2] = 3
        // CODE → addr:539 | <LoadConstString>: <Reg8: 11, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r11 = "Generator functions may not be called on executing generators"
        // CODE → addr:543 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r11, r10)
    } else if (r5 === 3) {
        // ──────────────── Block 32 ──────────────── 
        // CODE → addr:496 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // Switch → START
        switch (param1) {
            case 1:
                // ──────────────── Block 36 ──────────────── 
                // CODE → addr:527 | <Throw>: <Reg8: 0>
                throw param2;
            case 2:
                // ──────────────── Block 35 ──────────────── 
                // CODE → addr:515 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:521 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                r3.slot_0 = param2
                // CODE → addr:525 | <Ret>: <Reg8: 3>
                return r3;
            default:
                // ──────────────── Block 34 ──────────────── 
                // CODE → addr:507 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:513 | <Ret>: <Reg8: 3>
                return r3;
        }
        // Switch → END
    } else {
        try {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
            r2 = 2
            // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 4>
            r1[2] = 2
            // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 1>
            r7 = r1[1]
            // CODE → addr: 50 | <LoadConstZero>: <Reg8: 5>
            // USED → r5 = 0;
            // Switch → START
            switch (r7) {
                case 0:
                    // ──────────────── Block 26 ──────────────── 
                    // CODE → addr:384 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
                    // USED → r5 = 1;
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 30 ──────────────── 
                            // CODE → addr:483 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 29 ──────────────── 
                            // CODE → addr:464 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r5 = { "value": null, "done": true }
                            // CODE → addr:470 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                            r5.slot_0 = param2
                            // CODE → addr:474 | <Ret>: <Reg8: 5>
                            return r5;
                        default:
                            // ──────────────── Block 28 ──────────────── 
                            // CODE → addr:395 | <GetParentEnvironment>: <Reg8: 7, UInt8: 1>
                            r7 = getParentEnvironment(1)
                            // CODE → addr:398 | <StoreToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                            r1[0] = r7
                            // CODE → addr:402 | <GetGlobalObject>: <Reg8: 8>
                            // USED → r8 = globalThis;
                            // CODE → addr:404 | <TryGetById>: <Reg8: 10, Reg8: 8, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                            // USED → r10 = console;
                            // CODE → addr:410 | <GetByIdShort>: <Reg8: 9, Reg8: 10, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                            // USED → r9 = console.log;
                            // CODE → addr:415 | <LoadConstString>: <Reg8: 8, string_id: 4920>  # String: '__BC:Functions/AsyncTests/callAsyncTests/start' (String)
                            // USED → r8 = "__BC:Functions/AsyncTests/callAsyncTests/start";
                            // CODE → addr:419 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 10, Reg8: 8>
                            console.log("__BC:Functions/AsyncTests/callAsyncTests/start")
                            // CODE → addr:424 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 1>
                            // USED → r8 = r7[1];
                            // CODE → addr:428 | <LoadConstUndefined>: <Reg8: 7>
                            r7 = undefined
                            // CODE → addr:430 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
                            r7 = r7[1]()
                            // CODE → addr:434 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
                            r1[1] = 1
                            // CODE → addr:438 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:441 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
                            r1[2] = 1
                            // CODE → addr:445 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                            r5 = { "value": null, "done": false }
                            // CODE → addr:451 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
                            r5.slot_0 = r7
                            // CODE → addr:455 | <Ret>: <Reg8: 5>
                            return r5;
                    }
                    // Switch → END
                    break;
                case 1:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 25 ──────────────── 
                            // CODE → addr:382 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 24 ──────────────── 
                            // CODE → addr:363 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r5 = { "value": null, "done": true }
                            // CODE → addr:369 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                            r5.slot_0 = param2
                            // CODE → addr:373 | <Ret>: <Reg8: 5>
                            return r5;
                        default:
                            // ──────────────── Block 23 ──────────────── 
                            // CODE → addr:319 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
                            // USED → r7 = r1[0];
                            // CODE → addr:323 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 2>
                            // USED → r8 = r1[0][2];
                            // CODE → addr:327 | <LoadConstUndefined>: <Reg8: 7>
                            // USED → r7 = undefined;
                            // CODE → addr:329 | <Call1>: <Reg8: 7, Reg8: 8, Reg8: 7>
                            r7 = r1[0][2].call(undefined)
                            // CODE → addr:333 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
                            r1[1] = 2
                            // CODE → addr:337 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:340 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
                            r1[2] = 1
                            // CODE → addr:344 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                            r5 = { "value": null, "done": false }
                            // CODE → addr:350 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 7, UInt8: 0>
                            r5.slot_0 = r7
                            // CODE → addr:354 | <Ret>: <Reg8: 5>
                            return r5;
                    }
                    // Switch → END
                    break;
                case 2:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 20 ──────────────── 
                            // CODE → addr:309 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 19 ──────────────── 
                            // CODE → addr:290 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:296 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
                            r7.slot_0 = param2
                            // CODE → addr:300 | <Ret>: <Reg8: 7>
                            return r7;
                        default:
                            // ──────────────── Block 18 ──────────────── 
                            // CODE → addr:237 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
                            // USED → r7 = r1[0];
                            // CODE → addr:241 | <LoadFromEnvironment>: <Reg8: 9, Reg8: 7, UInt8: 3>
                            // USED → r9 = r1[0][3];
                            // CODE → addr:245 | <LoadConstUndefined>: <Reg8: 8>
                            // USED → r8 = undefined;
                            // CODE → addr:247 | <NewArrayWithBuffer>: <Reg8: 7, UInt16: 3, UInt16: 3, UInt16: 19164>  # Array: [1, 2, 3]
                            r7 = [1, 2, 3]
                            // CODE → addr:255 | <Call2>: <Reg8: 8, Reg8: 9, Reg8: 8, Reg8: 7>
                            r8 = r1[0][3].call(undefined, r7)
                            // CODE → addr:260 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 6>
                            r1[1] = 3
                            // CODE → addr:264 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:267 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
                            r1[2] = 1
                            // CODE → addr:271 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                            r7 = { "value": null, "done": false }
                            // CODE → addr:277 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 8, UInt8: 0>
                            r7.slot_0 = r8
                            // CODE → addr:281 | <Ret>: <Reg8: 7>
                            return r7;
                    }
                    // Switch → END
                    break;
                case 3:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 15 ──────────────── 
                            // CODE → addr:227 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 14 ──────────────── 
                            // CODE → addr:208 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:214 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
                            r7.slot_0 = param2
                            // CODE → addr:218 | <Ret>: <Reg8: 7>
                            return r7;
                        default:
                            // ──────────────── Block 13 ──────────────── 
                            // CODE → addr:161 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 0>
                            // USED → r7 = r1[0];
                            // CODE → addr:165 | <LoadFromEnvironment>: <Reg8: 8, Reg8: 7, UInt8: 4>
                            // USED → r8 = r1[0][4];
                            // CODE → addr:169 | <LoadConstUndefined>: <Reg8: 7>
                            // USED → r7 = undefined;
                            // CODE → addr:171 | <Call1>: <Reg8: 8, Reg8: 8, Reg8: 7>
                            r8 = r1[0][4].call(undefined)
                            // CODE → addr:175 | <LoadConstUInt8>: <Reg8: 7, UInt8: 4>
                            // USED → r7 = 4;
                            // CODE → addr:178 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 7>
                            r1[1] = 4
                            // CODE → addr:182 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:185 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 5>
                            r1[2] = 1
                            // CODE → addr:189 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18061>  # Object: {'value': null, 'done': false}
                            r7 = { "value": null, "done": false }
                            // CODE → addr:195 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 8, UInt8: 0>
                            r7.slot_0 = r8
                            // CODE → addr:199 | <Ret>: <Reg8: 7>
                            return r7;
                    }
                    // Switch → END
                    break;
                default:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 10 ──────────────── 
                            // CODE → addr:151 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 9 ──────────────── 
                            // CODE → addr:132 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:138 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
                            r7.slot_0 = param2
                            // CODE → addr:142 | <Ret>: <Reg8: 7>
                            return r7;
                        default:
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
                            console.log("__BC:Functions/AsyncTests/callAsyncTests/end")
                            // CODE → addr:117 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:123 | <Ret>: <Reg8: 7>
                            return r7;
                    }
                    // Switch → END
                    break;
            }
            // Switch → END
        } finally {
            // ──────────────── Block 31 ──────────────── 
            // CODE → addr:487 | <Mov>: <Reg8: 2, Reg8: 6>
            r2 = 3
            // CODE → addr:490 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 6>
            r1[2] = 3
        }
    }
}