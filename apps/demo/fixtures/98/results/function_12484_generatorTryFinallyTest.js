function generatorTryFinallyTest() {
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
        // ──────────────── Block 29 ──────────────── 
        // CODE → addr:418 | <LoadConstUInt8>: <Reg8: 0, UInt8: 3>
        // USED → r0 = 3;
        // CODE → addr:421 | <Mov>: <Reg8: 2, Reg8: 0>
        r2 = 3
        // CODE → addr:424 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 0>
        r1[0] = 3
        // CODE → addr:428 | <LoadConstString>: <Reg8: 15, string_id: 3340>  # String: 'Generator functions may not be called on executing generators' (String)
        r15 = "Generator functions may not be called on executing generators"
        // CODE → addr:432 | <CallBuiltin>: <Reg8: 0, UInt8: 44, UInt8: 2>  # Built-in function: [#44 throwTypeError]
        r0 = throwTypeError(r15, r14)
    } else if (r12 === 3) {
        // Switch → START
        switch (param1) {
            case 1:
                // ──────────────── Block 28 ──────────────── 
                // CODE → addr:416 | <Throw>: <Reg8: 0>
                throw param2;
            case 2:
                // ──────────────── Block 27 ──────────────── 
                // CODE → addr:404 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:410 | <PutOwnBySlotIdx>: <Reg8: 3, Reg8: 0, UInt8: 0>
                r3.slot_0 = param2
                // CODE → addr:414 | <Ret>: <Reg8: 3>
                return r3;
            default:
                // ──────────────── Block 26 ──────────────── 
                // CODE → addr:396 | <NewObjectWithBuffer>: <Reg8: 3, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                r3 = { "value": null, "done": true }
                // CODE → addr:402 | <Ret>: <Reg8: 3>
                return r3;
        }
        // Switch → END
    } else {
        // LOOP → START (while)
        while (true) {
            try {
                // ──────────────── Block 2 ──────────────── 
                // CODE → addr: 54 | <Mov>: <Reg8: 2, Reg8: 4>
                r2 = 2
                // CODE → addr: 57 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 4>
                r1[0] = 2
                // CODE → addr: 61 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 1>
                r12 = r1[1]
                // CODE → addr: 65 | <JStrictEqualLong>: <Addr32: 213, Reg8: 11, Reg8: 12>  # Address: 00000116
                if (0 === r12) goto label_278;
            } catch (caughtException) {
                // ──────────────── Block 21 ──────────────── 
                // CODE → addr:355 | <Mov>: <Reg8: 6, Reg8: 12>
                // USED → r6 = caughtException;
                // CODE → addr:358 | <StoreToEnvironment>: <Reg8: 1, UInt8: 2, Reg8: 12>
                r1[2] = caughtException
                // CODE → addr:362 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 3>
                r12 = r1[3]
                if (0 === r12) {
                    // ──────────────── Block 23 ──────────────── 
                    // CODE → addr:379 | <Mov>: <Reg8: 2, Reg8: 7>
                    r2 = 3
                    // CODE → addr:382 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                    r1[0] = 3
                    // CODE → addr:386 | <Throw>: <Reg8: 6>
                    throw caughtException;
                }
                // ──────────────── Block 22 ──────────────── 
                // CODE → addr:370 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 5>
                r1[1] = 1
            }
        }
        // LOOP → END
        // Switch → START
        switch (r12) {
            case 1:
                // ──────────────── Block 15 ──────────────── 
                // CODE → addr:249 | <LoadFromEnvironment>: <Reg8: 12, Reg8: 1, UInt8: 2>
                // USED → r12 = r1[2];
                // CODE → addr:253 | <Mov>: <Reg8: 6, Reg8: 12>
                r6 = r1[2]
                // CODE → addr:256 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
                r1[3] = 0
                // CODE → addr:260 | <TryGetById>: <Reg8: 14, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r14 = console;
                // CODE → addr:266 | <GetByIdShort>: <Reg8: 13, Reg8: 14, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r13 = console.log;
                // CODE → addr:271 | <Call2>: <Reg8: 13, Reg8: 13, Reg8: 14, Reg8: 8>
                console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
                // CODE → addr:276 | <Throw>: <Reg8: 12>
                throw r1[2];
            case 2:
                // Switch → START
                switch (param1) {
                    case 1:
                        // ──────────────── Block 14 ──────────────── 
                        // CODE → addr:240 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:243 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                        r1[0] = 3
                        // CODE → addr:247 | <Throw>: <Reg8: 0>
                        throw param2;
                    case 2:
                        // ──────────────── Block 13 ──────────────── 
                        // CODE → addr:201 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
                        r1[3] = 0
                        // CODE → addr:205 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r13 = console;
                        // CODE → addr:211 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r12 = console.log;
                        // CODE → addr:216 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
                        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
                        // CODE → addr:221 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:224 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                        r1[0] = 3
                        // CODE → addr:228 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r12 = { "value": null, "done": true }
                        // CODE → addr:234 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
                        r12.slot_0 = param2
                        // CODE → addr:238 | <Ret>: <Reg8: 12>
                        return r12;
                    default:
                        // ──────────────── Block 12 ──────────────── 
                        // CODE → addr:182 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 7>
                        r1[1] = 3
                        // CODE → addr:186 | <Mov>: <Reg8: 2, Reg8: 5>
                        r2 = 1
                        // CODE → addr:189 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
                        r1[0] = 1
                        // CODE → addr:193 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48826>  # Object: {'value': 'b', 'done': false}
                        r12 = { "value": "b", "done": false }
                        // CODE → addr:199 | <Ret>: <Reg8: 12>
                        return r12;
                }
                // Switch → END
                break;
            default:
                // Switch → START
                switch (param1) {
                    case 1:
                        // ──────────────── Block 9 ──────────────── 
                        // CODE → addr:165 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:168 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                        r1[0] = 3
                        // CODE → addr:172 | <Throw>: <Reg8: 0>
                        throw param2;
                    case 2:
                        // ──────────────── Block 8 ──────────────── 
                        // CODE → addr:126 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
                        r1[3] = 0
                        // CODE → addr:130 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r13 = console;
                        // CODE → addr:136 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r12 = console.log;
                        // CODE → addr:141 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
                        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
                        // CODE → addr:146 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:149 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                        r1[0] = 3
                        // CODE → addr:153 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                        r12 = { "value": null, "done": true }
                        // CODE → addr:159 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
                        r12.slot_0 = param2
                        // CODE → addr:163 | <Ret>: <Reg8: 12>
                        return r12;
                    default:
                        // ──────────────── Block 7 ──────────────── 
                        // CODE → addr: 91 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 11>
                        r1[3] = 0
                        // CODE → addr: 95 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                        // USED → r13 = console;
                        // CODE → addr:101 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                        // USED → r12 = console.log;
                        // CODE → addr:106 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 8>
                        console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/cleanup")
                        // CODE → addr:111 | <Mov>: <Reg8: 2, Reg8: 7>
                        r2 = 3
                        // CODE → addr:114 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                        r1[0] = 3
                        // CODE → addr:118 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 39753>  # Object: {'value': undefined, 'done': true}
                        r12 = { "value": null, "done": true }
                        // CODE → addr:124 | <Ret>: <Reg8: 12>
                        return r12;
                }
                // Switch → END
                break;
        }
        // Switch → END
        // Switch → START
        switch (param1) {
            case 1:
                // ──────────────── Block 20 ──────────────── 
                // CODE → addr:344 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 3
                // CODE → addr:347 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                r1[0] = 3
                // CODE → addr:351 | <Throw>: <Reg8: 0>
                throw param2;
            case 2:
                // ──────────────── Block 19 ──────────────── 
                // CODE → addr:325 | <Mov>: <Reg8: 2, Reg8: 7>
                r2 = 3
                // CODE → addr:328 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 7>
                r1[0] = 3
                // CODE → addr:332 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 18047>  # Object: {'value': null, 'done': true}
                r12 = { "value": null, "done": true }
                // CODE → addr:338 | <PutOwnBySlotIdx>: <Reg8: 12, Reg8: 0, UInt8: 0>
                r12.slot_0 = param2
                // CODE → addr:342 | <Ret>: <Reg8: 12>
                return r12;
            default:
                // ──────────────── Block 18 ──────────────── 
                // CODE → addr:286 | <TryGetById>: <Reg8: 13, Reg8: 10, UInt8: 0, string_id: 108>  # String: 'console' (Identifier)
                // USED → r13 = console;
                // CODE → addr:292 | <GetByIdShort>: <Reg8: 12, Reg8: 13, UInt8: 1, string_id: 178>  # String: 'log' (Identifier)
                // USED → r12 = console.log;
                // CODE → addr:297 | <Call2>: <Reg8: 12, Reg8: 12, Reg8: 13, Reg8: 9>
                console.log("__BC:Functions/GeneratorTests/generatorTryFinallyTest/start")
                // CODE → addr:302 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 3, Reg8: 5>
                r1[3] = 1
                // CODE → addr:306 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 1, Reg8: 4>
                r1[1] = 2
                // CODE → addr:310 | <Mov>: <Reg8: 2, Reg8: 5>
                r2 = 1
                // CODE → addr:313 | <StoreNPToEnvironment>: <Reg8: 1, UInt8: 0, Reg8: 5>
                r1[0] = 1
                // CODE → addr:317 | <NewObjectWithBuffer>: <Reg8: 12, UInt16: 1047, UInt16: 48822>  # Object: {'value': 'a', 'done': false}
                r12 = { "value": "a", "done": false }
                // CODE → addr:323 | <Ret>: <Reg8: 12>
                return r12;
        }
        // Switch → END
    }
}