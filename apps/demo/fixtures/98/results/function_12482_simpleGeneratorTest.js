function simpleGeneratorTest() {
    // ──────────────── Block 0 ──────────────── 
    // CODE → addr:  0 | <GetParentEnvironment>: <Reg8: 1, UInt8: 0>
    r1 = getParentEnvironment(0)
    // CODE → addr:  3 | <LoadFromEnvironment>: <Reg8: 0, Reg8: 1, UInt8: 0>
    // USED → r0 = r1[0];
    // CODE → addr:  7 | <Mov>: <Reg8: 2, Reg8: 0>
    // USED → r2 = r1[0];
    // CODE → addr: 10 | <LoadConstUInt8>: <Reg8: 4, UInt8: 2>
    // USED → r4 = 2;
    if (r0 === 2) {
        // ──────────────── Block 31 ──────────────── 
        // CODE → addr:380 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:383 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:386 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
        r1[0] = 3
        // CODE → addr:390 | <LoadConstString>: <Reg8: 10, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r10 = "Generator functions may not be called on executing generators"
        // CODE → addr:394 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r10, r9)
    } else if (r5 === 3) {
        // ──────────────── Block 26 ──────────────── 
        // CODE → addr:347 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
        // USED → r5 = 1;
        // Switch → START
        switch (param1) {
            case 1:
                // ──────────────── Block 30 ──────────────── 
                // CODE → addr:378 | <Throw>: <Reg8: 0>
                throw param2;
            case 2:
                // ──────────────── Block 29 ──────────────── 
                // CODE → addr:366 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:372 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                r3.slot_0 = param2
                // CODE → addr:376 | <Ret>: <Reg8: 3>
                return r3;
            default:
                // ──────────────── Block 28 ──────────────── 
                // CODE → addr:358 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:364 | <Ret>: <Reg8: 3>
                return r3;
        }
        // Switch → END
    } else {
        try {
            // ──────────────── Block 2 ──────────────── 
            // CODE → addr: 39 | <Mov>: <Reg8: 2, Reg8: 4>
            r2 = 2
            // CODE → addr: 42 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
            r1[0] = 2
            // CODE → addr: 46 | <LoadFromEnvironment>: <Reg8: 7, Reg8: 1, UInt8: 1>
            r7 = r1[1]
            // CODE → addr: 50 | <LoadConstZero>: <Reg8: 5>
            // USED → r5 = 0;
            // Switch → START
            switch (r7) {
                case 0:
                    // ──────────────── Block 20 ──────────────── 
                    // CODE → addr:256 | <LoadConstUInt8>: <Reg8: 5, UInt8: 1>
                    // USED → r5 = 1;
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 24 ──────────────── 
                            // CODE → addr:334 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 23 ──────────────── 
                            // CODE → addr:315 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r5 = { "value": null, "done": true }
                            // CODE → addr:321 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                            r5.slot_0 = param2
                            // CODE → addr:325 | <Ret>: <Reg8: 5>
                            return r5;
                        default:
                            // ──────────────── Block 22 ──────────────── 
                            // CODE → addr:267 | <GetGlobalObject>: <Reg8: 7>
                            // USED → r7 = globalThis;
                            // CODE → addr:269 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                            // USED → r9 = console;
                            // CODE → addr:275 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                            // USED → r8 = console.log;
                            // CODE → addr:280 | <LoadConstString>: <Reg8: 7, string_id: 4949>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/start' (String)
                            // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/start";
                            // CODE → addr:284 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
                            console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/start")
                            // CODE → addr:289 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
                            r1[1] = 1
                            // CODE → addr:293 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:296 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
                            r1[0] = 1
                            // CODE → addr:300 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 48810>  # Object: {'value': 1, 'done': false}
                            r5 = { "value": 1, "done": false }
                            // CODE → addr:306 | <Ret>: <Reg8: 5>
                            return r5;
                    }
                    // Switch → END
                    break;
                case 1:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 19 ──────────────── 
                            // CODE → addr:254 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 18 ──────────────── 
                            // CODE → addr:235 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r5 = { "value": null, "done": true }
                            // CODE → addr:241 | <PutOwnBySlotIdx>: <Reg8: 5, Reg8: 0, UInt8: 0>
                            r5.slot_0 = param2
                            // CODE → addr:245 | <Ret>: <Reg8: 5>
                            return r5;
                        default:
                            // ──────────────── Block 17 ──────────────── 
                            // CODE → addr:209 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
                            r1[1] = 2
                            // CODE → addr:213 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:216 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
                            r1[0] = 1
                            // CODE → addr:220 | <NewObjectWithBuffer>: <Reg8: 5, UInt16: 1047, UInt16: 1525>  # Object: {'value': 2, 'done': false}
                            r5 = { "value": 2, "done": false }
                            // CODE → addr:226 | <Ret>: <Reg8: 5>
                            return r5;
                    }
                    // Switch → END
                    break;
                case 2:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 14 ──────────────── 
                            // CODE → addr:199 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 13 ──────────────── 
                            // CODE → addr:180 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:186 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
                            r7.slot_0 = param2
                            // CODE → addr:190 | <Ret>: <Reg8: 7>
                            return r7;
                        default:
                            // ──────────────── Block 12 ──────────────── 
                            // CODE → addr:154 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 6>
                            r1[1] = 3
                            // CODE → addr:158 | <Mov>: <Reg8: 2, Reg8: 5>
                            r2 = 1
                            // CODE → addr:161 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
                            r1[0] = 1
                            // CODE → addr:165 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 48816>  # Object: {'value': 3, 'done': false}
                            r7 = { "value": 3, "done": false }
                            // CODE → addr:171 | <Ret>: <Reg8: 7>
                            return r7;
                    }
                    // Switch → END
                    break;
                default:
                    // Switch → START
                    switch (param1) {
                        case 1:
                            // ──────────────── Block 9 ──────────────── 
                            // CODE → addr:144 | <Throw>: <Reg8: 0>
                            throw param2;
                        case 2:
                            // ──────────────── Block 8 ──────────────── 
                            // CODE → addr:125 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:131 | <PutOwnBySlotIdx>: <Reg8: 7, Reg8: 0, UInt8: 0>
                            r7.slot_0 = param2
                            // CODE → addr:135 | <Ret>: <Reg8: 7>
                            return r7;
                        default:
                            // ──────────────── Block 7 ──────────────── 
                            // CODE → addr: 81 | <GetGlobalObject>: <Reg8: 7>
                            // USED → r7 = globalThis;
                            // CODE → addr: 83 | <TryGetById>: <Reg8: 9, Reg8: 7, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                            // USED → r9 = console;
                            // CODE → addr: 89 | <GetByIdShort>: <Reg8: 8, Reg8: 9, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                            // USED → r8 = console.log;
                            // CODE → addr: 94 | <LoadConstString>: <Reg8: 7, string_id: 4948>  # String: '__BC:Functions/GeneratorTests/simpleGeneratorTest/end' (String)
                            // USED → r7 = "__BC:Functions/GeneratorTests/simpleGeneratorTest/end";
                            // CODE → addr: 98 | <Call2>: <Reg8: 7, Reg8: 8, Reg8: 9, Reg8: 7>
                            console.log("__BC:Functions/GeneratorTests/simpleGeneratorTest/end")
                            // CODE → addr:110 | <NewObjectWithBuffer>: <Reg8: 7, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                            r7 = { "value": null, "done": true }
                            // CODE → addr:116 | <Ret>: <Reg8: 7>
                            return r7;
                    }
                    // Switch → END
                    break;
            }
            // Switch → END
        } finally {
            // ──────────────── Block 25 ──────────────── 
            // CODE → addr:338 | <Mov>: <Reg8: 2, Reg8: 6>
            r2 = 3
            // CODE → addr:341 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 6>
            r1[0] = 3
        }
    }
}